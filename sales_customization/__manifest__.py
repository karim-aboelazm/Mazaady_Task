# -*- coding: utf-8 -*-
{
    'name': "Sales Customization",

    'summary': "Sales Customization",

    'description': "Sales Customization",

    'author': "Karim Mohammed Aboelazm",

    'category': 'Sales',

    'version': '1.0',

    'depends': ['base', 'sale'],

    'data': [
        'security/sales_customization_security.xml',
        'views/sales_customization_view.xml',
        'report/sales_customization_report.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,
}
