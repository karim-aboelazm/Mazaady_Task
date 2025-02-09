# -*- coding: utf-8 -*-
{
    'name': "Contacts Customization",

    'summary': "Contacts Customization",

    'description': "Contacts Customization",

    'author': "Karim Mohammed Aboelazm",

    'category': 'Contacts',

    'version': '1.0',

    'depends': ['base', 'mail'],

    'data': [
        'data/email_templates.xml',
        'data/contact_birth_date_cron.xml',
        'views/contacts_customization_view.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,
}
