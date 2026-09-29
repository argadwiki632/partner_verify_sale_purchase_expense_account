# -*- coding: utf-8 -*-

{
    'name': 'Partner Verify Accounting',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Block invoice and bill posting when the partner is not verified',
    'description': """
Partner Verify Accounting
=========================

Require a verified customer or vendor before posting invoices and bills.
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'aerpwise_partner_verify',
        'account',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
}
