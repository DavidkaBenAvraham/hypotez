"""! @brief Класс поставщика в `Prestashop`

 @section libs imports:
  - sys 
  - os 
  - attr 
  - pathlib 
  - typing 
  - gs 
  - helpers 
  - gs 
  - prestashop.prestashop 
  - .images_exec 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os
# path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
# sys.path.append(path)  # Добавляю корневую папку в sys.path

from attr import attr, attrs
from pathlib import Path
from typing import Union

# ----------------------------------
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from .presta_apis import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# --------------------------------

class PrestaSupplier (): pass
