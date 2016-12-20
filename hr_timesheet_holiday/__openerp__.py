# -*- coding: utf-8 -*-
# Copyright 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Import holidays in timesheets',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'summary': "Link holidays to analytic accounts",
    'author': "Therp BV, Odoo Community Association (OCA)",
    'website': 'http://therp.nl',
    'license': 'AGPL-3',
    'depends': [
        'hr',
        'account',
        'hr_holidays',
        'hr_timesheet_sheet'
    ],
    'data': [
        'views/hr_holidays_view.xml',
        'views/company_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
