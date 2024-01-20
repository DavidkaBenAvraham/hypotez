"""! @~russian Поставщик <I>ebay.com</I>
 
 @section libs imports:
  - src.gs 
  - src.gs 
  - src.gs 
  - src.webdriver 
  - src.scenarios 

"""



# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator,  jprint, pprint
from src.webdriver import Driver
from src.scenarios import scenario
# ----------------------------------