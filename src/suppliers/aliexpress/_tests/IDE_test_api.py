
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from pathlib import Path
import json
import re
# ----------------
#from hypotez import gs, Supplier, Product
from src.settings import gs
from src.suppliers.aliexpress.iop import AliexpressApi, models
from src.suppliers import Supplier
from src.product import Product
from categories import Category
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads, j_dumps

aliexpress = AliexpressApi(gs.api_aliexpress['key'], gs.api_aliexpress['secret'], models.Language.EN, models.Currency.EUR, gs.api_aliexpress['tracking_id'])

links = ['https://aliexpress.com/item/1005005626039018.html', 
         'https://aliexpress.com/item/1005004931672329.html',  
         'https://aliexpress.com/item/1005004931364762.html', 
         'https://aliexpress.com/item/1005005408655982.html', 
         'https://aliexpress.com/item/1005004931743062.html']

products = aliexpress.get_products_details(links)
