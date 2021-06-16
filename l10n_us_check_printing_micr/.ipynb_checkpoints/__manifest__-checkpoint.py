# -*- coding: utf-8 -*-
{
    'name': "USA Check Printing MICR Format",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Avalantec",
    'website': "https://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account_accountant',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'account_accountant','l10n_us_check_printing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_journal_form.xml',
        'views/report_check_top.xml',
        'views/ckus_stub_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
