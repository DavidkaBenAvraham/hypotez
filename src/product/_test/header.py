import sys
import os
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+11])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
pass

print(dir_root)
# ----------------
from pathlib import Path
import json
import re
# ----------------

from src.settings import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.categories import Category
from src.tools import StringNormalizer as SN, StringFormatter as SF
from src.helpers import  logger,logs_and_errors_decorator, jprint, pprint
from src.prestashop import Product as PrestaProduct
from src.io_interface import j_loads, j_dumps, save_text_file
# ----------------

def start_supplier(supplier_prefix: str = 'aliexpress', scenario_language: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'scenario_language': scenario_language
    }
    
    return Supplier(**params)