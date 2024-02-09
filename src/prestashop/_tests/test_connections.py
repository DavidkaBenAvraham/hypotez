# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os
import requests
from pathlib import Path
import json
# ----------------
import header
from src.settings import gs
from header import API_KEY, API_DOMAIN
from header import save_text_file
from header import j_dumps

from src.product import Product

p = Product()


#product_id = 1658 # <- проверка по существующему товару
product_id =None

params: dict = {'display':'full', 
                'filter':None, 
                'sort':None, 
                'limit':None, 
                'language':None, 
                'io_format' : 'JSON' , 
                'output_format' : 'JSON'}

presta_product = Product().check_prod_presence_in_prestashop(product_ud = None,product_reference = product_reference, params = params, PrestaAPIV = 'PrestaAPIV3')


j_dumps(presta_product, Path (gs.dir_log, f'{gs.get_now()}-{product_id}.json' ))
#save_text_file (presta_product, str ( Path (gs.dir_log, f'{gs.get_now()}-{product_id}.json' ) ) )

pass