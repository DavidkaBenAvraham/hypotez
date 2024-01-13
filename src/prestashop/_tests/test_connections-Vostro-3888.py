# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from src.prestashop import Product

presta_product = Product.check_if_product_in_db(108)