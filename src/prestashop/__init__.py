"""! @~russian  Модуль работы с Prestashop
@details Слой между сущностями престашоп: товар, поставщик, категория, язык и пр и сущностями программы.
        <code>  
            {    
                "API_DOMAIN": "https://domain.com",  
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
from .product import PrestaProduct
from .supplier import PrestaSupplier
from .category import PrestaCategory
from .language import PrestaLanguage
from .shop import PrestaShop
from .images_exec import upload_image
from .presta_apis import PrestaAPIV1, PrestaAPIV2, PrestaAPIV3

