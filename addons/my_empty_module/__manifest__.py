{
    'name': 'My Empty Module',
    'version': '1.0.0',
    'category': 'Custom',
    'summary': 'A simple empty module for Odoo',
    'description': """This is a bare minimum Odoo module with no models or views.""",
    'author': 'Your Name',
    'website': 'https://example.com',
    'depends': ['base'],  # base is required for every module
    'data': [
        # put XML files here (views, security, etc.)
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

