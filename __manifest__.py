# -*- coding: utf-8 -*-
{
    'name': "odoo_basico",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'importarimaxes': """
        Long importarimaxes of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'accions_planificadas/accion_planificada.xml',
        'reports/report_header.xml',
        'reports/report_informacion.xml',
        'views/informacion.xml',
        'views/suceso.xml',
        'views/templates.xml',
        'views/pedido.xml',
        'views/persoa.xml',
        'views/linea_pedido.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'security/Xestion_Usuarios.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
