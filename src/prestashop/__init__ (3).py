"""! @~russian  Модуль работы с Prestashop
@details Слой между сущностями престашоп: товар, поставщик, категория, язык и пр.
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


from src.settings import gs
API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
API_KEY = gs.default_prestashop_api_credentials['API_KEY']

from src.settings import gs
from .presta_apis.presta_python_api_v1 import PrestaAPIV1 
from .presta_apis.presta_python_api_v2 import PrestaAPIV2
from .presta_apis.presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format

PrestaAPIV1 = PrestaAPIV1 (API_DOMAIN, API_KEY)
PrestaAPIV2 = PrestaAPIV2 (API_DOMAIN, API_KEY)
PrestaAPIV3 = PrestaAPIV3 (API_DOMAIN, API_KEY, default_lang = 1, debug = True,  data_format = PrestaAPIV3Format.JSON)

