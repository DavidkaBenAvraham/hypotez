# """! @brief модуль коннектор `Prestashop`

# @details API хранятся в базе данных keypass.
# Я использую 3 версии prestashop api, потому, что еще не выбрал 

#  @section libs imports:
#   - sys 
#   - os 
#   - src.gs 
#   - src.helpers 
#   - src.gs 
#   - attr 
#   - pathlib 
#   - requests 
#   - xmltodict 

# """


# # -*- coding: utf-8 -*-
# #! /usr/share/projects/hypotez/venv/scripts python
# import sys
# import os


# # https://github.com/prestapyt/prestapyt


# from src.settings import gs
# from src.helpers import  logger,  logs_and_errors_decorator
# from src.io_interface import j_loads, j_dumps
# from attr import attr, attrs
# from pathlib import Path
# import requests
# import xmltodict
    

# API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
# API_KEY = gs.default_prestashop_api_credentials['API_KEY']




# # #######################################################################
# # #
# # #                      -= V1 =-
# # #
# # # https://python.hotexamples.com/examples/prestapyt/PrestaShopWebServiceDict/-/python-prestashopwebservicedict-class-examples.html
# # #

# # from .presta_apis import PrestaShopWebServiceDict_V1

# # PrestaAPIV1: PrestaShopWebServiceDict_V1 = PrestaShopWebServiceDict_V1 (API_DOMAIN, API_KEY )
# # #
# # #
# # ##############################################################################











# # ##############################################################################
# # #
# # #

# # from .presta_apis.presta_python_api_v2 import PrestashopApi_V2


# # PrestaAPIV2: PrestashopApi_V2 = PrestashopApi_V2 (API_DOMAIN, API_KEY)
# # #
# # #
# # ################################################################################




# # ################################################################################
# # #
# # #
# # #                   -= V3 =-
# # #
# # from .presta_apis.presta_python_api_v3.presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format

# # PrestaAPIV3: PrestaAPIV3 = PrestaAPIV3(
# #     API_DOMAIN,
# #     API_KEY,
# #     default_lang = 1,
# #     debug = True,
# #     data_format = PrestaAPIV3Format.JSON
# # )
# # #
# # #
# # ################################################################################







# # class PrestaAPIError():
# #     pass





#     #""" Работа с магазином на Престашоп через API 
#     #При каждом вызове класса я создаю новые JSON схемы
#     #для товара, категории, валют и т.п.
#     #Сделано для того, чтобы синхронизироваться с базой данных. 
#     #Тут над подумать над автореализацией
#     #"""


#     #def __init__(self, *args, **kwards):
#     #    """ Проверка доступности сервера и обновление схем:
#     #    product_schema,
#     #    category_schema,
#     #    languages_schema,
#     #    suppliers_schema
#     #    """
        

#     #    try:
#     #        responce = PrestaAPIV.head('products')
#     #        logger.debug(
#     #            f'''Prestashop Сервер responce:{[key for key in responce.items()]}''')

#     #    except Exception as ex:
#     #        logger.error(
#     #            f'''Ошибка при подключении к серверу: {ex.with_traceback(ex.__traceback__)}''')
#     #        pass

#     #    return self



#     #def ping():
#     #    return PrestaAPIV3.ping()

#     #def buid_schemas(self):
#     #    """
#     #    Строю json схемы, 
#     #    """
#     #    dir = gs.dir_presta_schemes

#     #    self.product_schema = self.get(
#     #        'products', options={'schema': 'blank'})
#     #    j_dumps(self.product_schema, Path(
#     #        dir, 'product_schema.json').absolute())

#     #    self.category_schema = self.get(
#     #        'categories', options={'schema': 'blank'})
#     #    j_dumps(self.category_schema, Path(
#     #        dir, 'category_schema.json').absolute())

#     #    self.languages_schema = self.get('languages', options={})
#     #    j_dumps(self.languages_schema, Path(
#     #        dir, 'languages_schema.json').absolute())

#     #    self.suppliers_dict = self.get('suppliers', options={})
#     #    j_dumps(self.suppliers_dict, Path(
#     #        dir, 'suppliers_dict.json').absolute())
        