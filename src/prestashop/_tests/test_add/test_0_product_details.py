from typing import Union
import header
from header import gs, jprint, pprint, Product, ProductFields
response = Product.get_product_info(103)
product = response['products'][0]

category_ids = Product.get_parent_categories(product['id_category_default'])
category_ids: list = [category_ids] if isinstance(category_ids,str) else category_ids
category_ids: list = [{'id': id} for id in category_ids]


product['associations']['categories']: list = category_ids
edited_product: dict = {'product':
    {
    'id': product['id'],
    'associations':{
        'categories': category_ids
        },
    'price': product['price']
    }
}

response = Product.update_product_in_prestashop( product['id'], edited_product)
pass