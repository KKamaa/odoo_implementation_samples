# Copyright 2019 Kevin Kamau
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Website Test Form',
    'version': '12.0.1.0.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'website': "www.odoo-kenya.co.ke",
    'author': "Kevin Kamau",
    'summary': "This modules tests recaptcha v2 features in a website form",
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_recaptcha_v2'
    ],
    'data': [
        'templates/website_frontend_assets.xml',
        'templates/website_form_templates.xml'
    ],
    'installable': True,
}
