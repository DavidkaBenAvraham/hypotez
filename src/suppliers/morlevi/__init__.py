"""! @brief  Поствщик <i>morlevi</i>
@namespace src: src
 \package src.suppliers.morlevi
\file __init__.py
 
 @section libs imports:
  - logger 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from .login import login
from .scrapper import grab_product_page
from .via_webdriver import get_list_products_in_category

