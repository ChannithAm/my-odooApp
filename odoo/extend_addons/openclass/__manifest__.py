# -*- coding: utf-8 -*-
{
    'name': "OpenClass",

    'summary': """
        Test""",

    'description': """
        To test my memory!! ^-^
    """,

    'author': "Digital Token",
    'website': "http://www.digitaltoken.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/openclass_view.xml',
        'views/teacher_view.xml',
        'views/session_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}