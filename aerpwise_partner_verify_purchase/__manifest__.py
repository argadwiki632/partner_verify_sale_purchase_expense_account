# -*- coding: utf-8 -*-

{
    'name': 'Partner Verify Purchase',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Purchase',
    'summary': 'Block purchase confirmation when the vendor is not verified',
    'description': """
Partner Verify Purchase
=======================

Require a verified vendor before confirming a Purchase Order.
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'aerpwise_partner_verify',
        'purchase',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
}
