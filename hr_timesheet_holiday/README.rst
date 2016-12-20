.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Link holidays to analytic accounts
==================================

This module adds a relation between the Leave Types and the Analytic Accounts.
When a Leave Request is granted, the granted days are converted to hours and
added to the Analytic Account for that Leave Type.

When the leave is revoked, the hours are also removed from the analytic
account.

The hours added to the Analytic Account are read-only, so you cannot edit them
directly, just by granting or revoking leave requests.

The hours to input per day is configurable at company level.

Limitations:

- Consider that the work days are Monday to Friday

Contributors
------------

* Tom Blauwendraat <tom@sunflowerweb.nl>
* Terrence Nzaywa <terrence@sunflowerweb.nl>

Installation
============

Just install.

Configuration
=============

To configure this module, you need to:

#. Configure the amount of hours per workday of your company.
#. Configure Analytic accounts for each Leave Type.

Usage
=====

To use this module, you need to:

#. Approve a Leave Request
#. See the hours added to the Analytic Accounts
#. Revoke a Leave Request
#. See the hours removed from the Analytic Accounts

Known issues / Roadmap
======================

* Hours per workday should be configurable per employee, not only by company.
* hr_timesheet_sheet dependency can be changed to hr_timesheet, now only
  included because hr_timesheet_sheet adds the Timesheet configurations menu
  in Company view.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/hr-timesheet/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Therp BV
* Sunflower IT

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
