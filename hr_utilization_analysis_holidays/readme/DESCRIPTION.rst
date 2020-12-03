This module adds support for leaves to `hr_utilization_analysis`

Without this module installed, leaves are not taken into account:
for a single 4-hour entry on specific day with 8 working hours and
4 hours of leaves, capacity would be calculated as 8 hours and utilization
would be calculated as 100%.

With this module installed, leaves are taken into account:
for a single 4-hour entry on specific day with 8 working hours and
4 hours of leaves, capacity would be calculated as 4 hours and utilization
would be calculated as 100%.

