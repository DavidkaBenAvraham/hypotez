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
#from hypotez import gs, Supplier, Product
from src.settings import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from categories import Category

import helpers
from src.helpers import  logger,logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps


