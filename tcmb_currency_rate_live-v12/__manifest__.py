# -*- coding: utf-8 -*-
{
    'name': 'TCMB Live Currency Exchange Rate',
    'version': '2.3',
    'author': "MechSoft",
    'category': 'Accounting',
    'description': """Import exchange rates from the Turkey TCMB Bank.
""",
    'depends': [
        'crm',
        'sale_management',
        'account_accountant',
        'currency_rate_live'
    ],
    'data': [
        'views/views.xml',
        'data/data.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
