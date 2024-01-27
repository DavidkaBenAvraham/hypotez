# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os
import header
# ----------------
from src.product import Product

presta_product = Product.check_if_product_in_db(108)