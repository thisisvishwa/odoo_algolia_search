{
    'name': 'Advanced Algolia Search Integration',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Integrates Algolia Search with Odoo eCommerce v16',
    'author': 'Bard (AI Assistant)',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['website_sale'],
    'data': [
        'views/algolia_backend_views.xml',
        'views/algolia_search_templates.xml',
        'controllers/main.py',
        'data/algolia_data.xml',
        'security/ir.model.access.csv',
        'security/algolia_security.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/src/img/algolia_logo.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'static/src/js/algolia_autocomplete.js',
            'static/src/css/algolia_styles.css',
        ],
    },
    'test': [
        'tests/test_algolia_integration.py',
    ],
    'external_dependencies': {
        'python': [],
    },
    'description': """
Advanced Algolia Search Integration for Odoo eCommerce v16
==========================================================

This module integrates Algolia Search with Odoo eCommerce to enhance the search experience.
    """,
}