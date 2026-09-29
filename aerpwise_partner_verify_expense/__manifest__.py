# -*- coding: utf-8 -*-

{
    'name': 'Partner Verify Expense',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Expenses',
    'summary': 'Block expense submit and approve when related partners are not verified',
    'description': """
Partner Verify Expense
======================

Require a verified employee work contact and vendor before submitting
or approving an expense report.
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'aerpwise_partner_verify',
        'hr_expense',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
}
