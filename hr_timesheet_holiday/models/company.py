# -*- coding: utf-8 -*-
# Copyright 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields

class ResCompany(models.Model):
    """Add hours per day to company"""
    _inherit = 'res.company'

    timesheet_hours_per_day = fields.Float(
        'Timesheet Hours Per Day',
        digits=(2, 2), default=8.0)
