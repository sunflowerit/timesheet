# Copyright 2018-2020 Brainbean Apps (https://brainbeanapps.com)
# Copyright 2020 CorporateHub (https://corporatehub.eu)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime, time, timedelta

import pytz

from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import ValidationError


class HrUtilizationAnalysis(models.TransientModel):
    _inherit = "hr.utilization.analysis"

    def _get_entry_values(self, employees, dates):
        entries = super(HrUtilizationAnalysis, self)._get_entry_values(employees, dates)

        data = {}
        for employee in employees:
            tz = pytz.timezone(employee.resource_calendar_id.tz)
            from_datetime = datetime.combine(min(dates), time.min).replace(tzinfo=tz)
            to_datetime = datetime.combine(max(dates), time.max).replace(tzinfo=tz)
            leaves = employee.list_leaves(from_datetime, to_datetime)
            data[employee.id] = {leave[0]: leave[1] for leave in leaves}

        for entry in entries:
            employee_id = entry["employee_id"]
            date = entry["date"]
            difference = leaves_by_date.get(employee_id, {}).get(date, 0)
            if difference:
                entry["amount"] -= difference

        return entries
