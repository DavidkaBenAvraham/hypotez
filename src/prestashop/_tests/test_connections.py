# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os
import header
# ----------------
from src.product import Product

p = Product()
presta_product = Product().check_prod_presence_in_prestashop(product_id = 1658)

pass