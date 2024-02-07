"""! @~russian Модуль взаимодействия с несколькими версиями API Prestashop
@details
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

API_KEY = gs.default_prestashop_api_credentials['API_KEY']
API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
from src.settings import gs
from .presta_python_api_v1 import PrestaAPIV1
from .presta_python_api_v2 import PrestaAPIV2
from .presta_python_api_v3 import PrestaAPIV3
PrestaAPIV1(API_KEY,API_DOMAIN)
PrestaAPIV2(API_KEY,API_DOMAIN)
PrestaAPIV3(API_KEY,API_DOMAIN)

