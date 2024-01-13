"""! @ru_brief Поставщик <I>amazon.com</I>

@namespace src: src
 \package src.suppliers.amazon
\file __init__.py
 
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

from .login import login as login
from .update_product_fields import set_product_fields
from .via_webdriver import get_list_products_in_category

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator,  jprint, pprint
from src.webdriver import Driver
# ----------------------------------