"""! @ru_brief  Модуль работы с Prestashop
@ru_details Слой между сущностями престашоп: товар, поставщик, категория, язык и пр и сущностями программы.
        <code>  
            {    
                "api_domain": "https://domain.com",  
                "product_manipulations_key": "xxxxxxxxxxxxxxxxxx"  
            }
        </code>

 
 @section libs imports:
  - sys 
  - os 
  - src.gs 
  - .product 
  - .supplier 
  - .category 
  - .language 
  - .shop 
  - .images_exec 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import sys
import os

from src.settings import gs
from .product import Product
from .supplier import Supplier
from .category import Category
from .language import Language
from .shop import Shop
from .images_exec import upload_image
from .presta_apis import presta_python_api_v1, presta_python_api_v2, presta_python_api_v3
