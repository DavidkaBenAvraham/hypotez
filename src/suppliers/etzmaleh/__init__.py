"""! @~russian Поставщик <I>etzmaleh.co.il</I>

 
 @section libs imports:
  - .update_product_fields 
  - .via_webdriver 
  - gs 
  - gs 
  - gs 
  - webdriver 
  - scenarios 
  
"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .update_product_fields import set_product_fields
from .via_webdriver import get_list_products_in_category

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator,  jprint, pprint
from src.webdriver import Driver
from src.scenarios import scenario
# ----------------------------------