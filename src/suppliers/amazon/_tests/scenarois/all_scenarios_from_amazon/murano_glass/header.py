import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from pathlib import Path
import json
import re

# ----------------
from src.settings import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.webdriver import Driver
from src.categories import Category
from src.tools import SF, SN
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import PrestaAPIV, upload_image
# ----------------

def start_supplier(supplier_prefix: str = 'amazon' ):
    """ Старт поставщика (amazon)"""

def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params)