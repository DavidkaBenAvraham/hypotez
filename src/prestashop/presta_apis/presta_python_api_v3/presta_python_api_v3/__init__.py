"""  [File's Description]
 @namespace src
 \package src.prestashop.presta_apis.presta_python_api_v3.presta_python_api_v3
\file __init__.py
 @section libs imports:
  - .core 
  - .exceptions 
  - .version 
Author(s):
  - Created by Davidka on 10.11.2023 .
"""
from .core import \
    Prestashop as PrestaAPIV3 , \
    Format as PrestaAPIV3Format
from .exceptions import \
    PrestaShopError as PrestaAPIV3Error ,\
    PrestaShopAuthenticationError as PrestaAPIV3AuthenticationError
from .version import __author__,__version__