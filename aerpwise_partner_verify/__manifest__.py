# -*- coding: utf-8 -*-

{
    'name': 'Partner Verify',
    'version': '18.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Verify contacts before they are used in business documents',
    'description': """
Partner Verify
==============

Review and approve customer or vendor records before they are used
in business documents.

Features
--------
* Verification workflow on contacts: Draft, To Verify, Verified, Rejected.
* Submit, verify, reject, and reset actions with chatter tracking.
* Verification is checked on the commercial partner (company / main contact).

Install the bridge modules to enforce verification on:
* Sales: aerpwise_partner_verify_sale
* Purchase: aerpwise_partner_verify_purchase
* Expenses: aerpwise_partner_verify_expense
* Accounting: aerpwise_partner_verify_account
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
    ],
    'data': [
        'security/partner_verify_security.xml',
        'security/ir.model.access.csv',
        'wizard/partner_verify_reject_wizard_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
