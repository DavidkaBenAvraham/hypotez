"""! @~russian Поставщик <I>amazon.com</I>

 
 @section libs imports:
  - .login 
  - .update_product_fields 
  - .via_webdriver 
  - src.gs 
  - src.gs 
  - src.gs 
  - webdriver 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .via_webdriver import get_list_products_in_category
from .grabber import grab_product_page