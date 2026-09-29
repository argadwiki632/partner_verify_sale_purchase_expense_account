# -*- coding: utf-8 -*-

{
    'name': 'Partner Verify Sales',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Block sales confirmation when the customer is not verified',
    'description': """
Partner Verify Sales
====================

Require a verified customer before confirming a Sales Order.
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'aerpwise_partner_verify',
        'sale_management',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
}
