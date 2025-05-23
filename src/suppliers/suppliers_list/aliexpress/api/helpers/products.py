## \file /src/suppliers/aliexpress/api/helpers/products.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.suppliers_list.aliexpress.api.helpers """
def parse_product(product):
    product.product_small_image_urls = product.product_small_image_urls.string
    return product


def parse_products(products):
    new_products = []

    for product in products:
        new_products.append(parse_product(product))

    return new_products

