{
    'name': 'Product Category Commission',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Calculate commission based on product categories',
    'description': """
        This module allows you to:
        - Set commission amounts on product categories
        - Automatically calculate commissions in sale orders based on product categories
        - Track commission amounts per sale order line
    """,
    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
