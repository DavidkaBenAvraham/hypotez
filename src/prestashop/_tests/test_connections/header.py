# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from pathlib import Path
import json
import re
# ----------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.suppliers import Supplier
from src.product import Product, ProductFields
from categories import Category
from src.tools import StringNormalizer as SN, StringFormatter as SF, translate

from src.io_interface import j_loads, j_dumps
from src.prestashop.prestashop import PrestaAPIV1, PrestaAPIV2, PrestaAPIV3


