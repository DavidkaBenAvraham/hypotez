"""! @~russian Поставщик <i>bangood.com</i>

 @section libs imports:
  - .scrapper 
  - .via_webdriver 
  - src.gs 
  - src.gs 
  - src.gs 
  - src.webdriver 
  - src.scenarios 
  

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from .scrapper import grab_product_page as grab_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator,  jprint, pprint
from src.webdriver import Driver
from src.scenarios import scenario
# ----------------------------------