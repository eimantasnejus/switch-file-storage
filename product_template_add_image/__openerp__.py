# -*- coding: utf-8 -*-

{
    'name': 'Product Template Additional Images',
    'version': '1.0',
    'depends': ['product'],
    'author': 'Eimantas Nejus',
    'category': 'Inventory Control',
    'summary': 'product, template, images',
    'description': """
Add Images to Product Template
==============================
Allows to add up to 5 images to product.
""",
    'website': 'https://www.odoo.com',
    'data': [
        'views/product_template.xml',
    ],
    'installable': True,
    'auto-install': False,
}
