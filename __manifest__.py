{
    'name': 'Freelance Marketplace',
    'version': '18.0.1.0',
    'category': 'custom',
    'summary': 'Manage freelance projects, bidding, and contracts',
    'depends': ['base', 'project', 'mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/freelancer_views.xml',
        'views/client_views.xml',
        'views/project_views.xml',
        'views/bid_views.xml',
        'views/contracts_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
