"""! @~russian Модуль взаимодействия с несколькими версиями API Prestashop
@details
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.settings import gs

"""! Все подключения происходят внутри кода, т.к. я подключаюсь к нескольким базам """

# API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
# API_KEY = gs.default_prestashop_api_credentials['API_KEY']

from src.settings import gs
from .presta_python_api_v1 import PrestaAPIV1 
from .presta_python_api_v2 import PrestaAPIV2
from .presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format

# PrestaAPIV1 = PrestaAPIV1 (API_DOMAIN, API_KEY)
# PrestaAPIV2 = PrestaAPIV2 (API_DOMAIN, API_KEY)
# PrestaAPIV3 = PrestaAPIV3 (API_DOMAIN, API_KEY, default_lang = 1, debug = True,  data_format = PrestaAPIV3Format.JSON)