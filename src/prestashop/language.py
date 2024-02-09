"""! @brief @~russian класс языка в `Presatshop`


 @section libs imports:
  - attr 
  - pathlib 
  - typing 
  - src.gs 
  - src.helpers 
  - src.gs 
  - src.prestashop.prestashop 
  
"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from pathlib import Path
from typing import Union

# ----------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from .presta_apis import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# --------------------------------

class PrestaLanguage(): pass