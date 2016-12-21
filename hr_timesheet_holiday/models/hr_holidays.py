# -*- coding: utf-8 -*-
# Copyright 2016 Sunflower IT <http://sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrHolidays(models.Model):
    """Update analytic account on status change of Leave Request"""
    _inherit = 'hr.holidays'

    # Add hr.analytic.timesheet to a leave request
    holiday_analytic_timesheet_id = fields.Many2one(
        comodel_name='hr.analytic.timesheet', string="Analytic Timesheet")

    @api.multi
    def holidays_validate(self):
        res = super(HrHolidays, self).holidays_validate()

        # Postprocess Leave Types that have an analytic account configured
        for leave in self:
            account = leave.holiday_status_id.analytic_account_id

            if account:

                # Assert hours per working day
                company = leave.employee_id.company_id
                hours_per_day = company.timesheet_hours_per_day
                if not hours_per_day:
                    raise UserError(
                        _("No hours per day defined for Company '%s'") %
                        (company.name,))

                # Assert user connected to employee
                user = leave.employee_id.user_id
                if not user:
                    raise UserError(
                        _("No user defined for Employee '%s'") %
                        (leave.employee_id.name,))

                # Add analytic line for the leave hours
                hours = abs(leave.number_of_days) * hours_per_day
                timesheet = self.env['hr.analytic.timesheet'].create({
                    'name': leave.name or leave.holiday_status_id.name,
                    'date': leave.date_from,
                    'unit_amount': hours,
                    'company_id': company.id,
                    'account_id': account.id,
                    'user_id': user.id,
                    'journal_id': leave.employee_id.journal_id.id
                })
                leave.write({'holiday_analytic_timesheet_id': timesheet.id})

        return res

    @api.multi
    def holidays_refuse(self):
        res = super(HrHolidays, self).holidays_refuse()

        for leave in self:
            leave.holiday_analytic_timesheet_id.unlink()

        return res
