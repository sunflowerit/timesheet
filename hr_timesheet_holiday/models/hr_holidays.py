# -*- coding: utf-8 -*-
# Copyright 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError


class HrHolidaysStatus(models.Model):
    """Add analytic account to holiday status"""
    _inherit = 'hr.holidays.status'

    analytic_account_id = fields.Many2one('account.analytic.account',
        'Analytic Account')


class HrHolidays(models.Model):
    """Update analytic account on status change of Leave Request"""
    _inherit = 'hr.holidays'

    @api.multi
    def holidays_validate(self):
        res = super(HrHolidays, self).holidays_validate()

        # Look for analytic account linked to Leave Type
        for leave in self:
            account = leave.holiday_status_id.analytic_account_id
            if not account:
                raise UserError("No analytic account defined for Leave Type '%s'" %
                    (leave.holiday_status_id.name,))

            # Look for company and hours per working day
            if not leave.department_id:
                raise UserError("Department not set")
            company = leave.department_id.company_id
            if not company:
                raise UserError("No company defined for Department '%s'" %
                    (leave.department_id.name,))
            hours_per_day = company.timesheet_hours_per_day
            if not hours_per_day:
                raise UserError("No hours per day defined for Company '%s'" %
                    (company.name,))

            # Add leave hours to analytic account
            # hours = abs(leave.number_of_days) * hours_per_day
            # account.write({
            #     'line_ids': [(0, False, {
            #         'name': leave.name or leave.holiday_status_id.name,
            #         'date': leave.date_from,
            #         'amount': hours,
            #         'company_id': company.id
            #     })]
            # })
            # gets error for general_acount_id
            # of naar hr.analytic.timesheet?
            # 'name': fields.char('Description', required=True),
            # 'date': fields.date('Date', required=True, select=True),
            # 'amount': fields.float('Amount', required=True, help='Calculated by multiplying the quantity and the price given in the Product\'s cost price. Always expressed in the company main currency.', digits_compute=dp.get_precision('Account')),
            # 'unit_amount': fields.float('Quantity', help='Specifies the amount of quantity to count.'),
            # 'account_id': fields.many2one('account.analytic.account', 'Analytic Account', required=True, ondelete='restrict', select=True, domain=[('type','<>','view')]),
            # 'user_id': fields.many2one('res.users', 'User'),
            # 'company_id': fields.related('account_id', 'company_id', type='many2one', relation='res.company', string='Company', store=True, readonly=True),





        return res