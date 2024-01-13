"""! @brief Постaвщик <i>wallmart</i>

@namespace src: src
 \package src.suppliers.wallmart
\file __init__.py
 
 @section libs imports:
  - logger 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python



from src.settings import gs
from .login import login as login
from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category

