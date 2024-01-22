"""! @~russian Модуль взаимодействия с несколькими версиями API Prestashop
@details
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .presta_python_api_v1 import PrestaShopWebServiceDict_V1   as PrestaAPIV1
from .presta_python_api_v2 import PrestashopApi_V2 as PrestaAPIV2
from .presta_python_api_v3 import Prestashop_V3 as PrestaAPIV3