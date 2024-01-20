"""! @~russian Поставщик <I>aliexpress.com</I>

@details У поставщика есть деление на категории общие для всего портала и внутренние категории 
отдельных продавцов и магазинов

@section libs imports:
- .grabber (local)
- .via_webdriver (local)
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

# from .login import login as login
# # from .update_product_fields import fill
# import via_api
# import sdk.iop as iop
from .via_webdriver import get_list_products_in_category, get_list_categories_from_site
#from . import product_fields, via_api
from .grabber import grab_product_page
#from src.suppliers import Supplier


