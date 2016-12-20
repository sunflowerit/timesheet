# -*- coding: utf-8 -*-
# Copyright 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

class AnalyticAccount(models.Model):
    """Add 'is leave account' flag to Analytic Account"""
    _inherit = 'account.analytic.account'

    is_leave_account = fields.Boolean('Leaves',
        help="Check this field if this account manages leaves",
        default=False)
