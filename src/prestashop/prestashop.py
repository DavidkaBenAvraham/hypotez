"""! @brief модуль коннактор `Prestashop`

@details API хранятся в базе данных keypass.

 @section libs imports:
  - sys 
  - os 
  - src.gs 
  - src.helpers 
  - src.gs 
  - attr 
  - pathlib 
  - requests 
  - xmltodict 
  - presta_python_api_v1 
  - .presta_apis.presta_python_api_v3.presta_python_api_v3 


"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os


# https://github.com/prestapyt/prestapyt


from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads, j_dumps
from attr import attr, attrs
from pathlib import Path
import requests
import xmltodict
    

api_domain = gs.default_prestashop_api_credentials['api_domain']
api_key = gs.default_prestashop_api_credentials['api_key']

#from prestapyt import  PrestaShopWebServiceDict, PrestaShopWebServiceError
# https://python.hotexamples.com/examples/prestapyt/PrestaShopWebServiceDict/-/python-prestashopwebservicedict-class-examples.html
#
from .presta_apis.presta_python_api_v1 import PrestaShopWebServiceDict, PrestaShopWebServiceError as PrestaAPIV1Error

PrestaAPIV1: PrestaShopWebServiceDict = \
    PrestaShopWebServiceDict(
    api_domain,
    api_key
    )

#
#
##############################################################################



##############################################################################
#
#
class PrestaAPIV2Error(RuntimeError):
    pass


class PrestaAPIV2:
    STATUSES = (200, 201)

    def __init__(self, api, key):
        self.api = api
        self.key = key

    def _get_url(self, path):
        return self.api + '/' + path

    def _check_response(self, res, ret):
        if res.status_code not in self.STATUSES:
            raise PrestaAPIV2Error(f'''
            Status {res.status_code}, 
            Return {ret}
            ''')
        return ret

    def _request(self, method, path, params=None, data=None, files=None):
        if data is not None:
            data = xmltodict.unparse({'prestashop': data}).encode('utf-8')
        res = requests.request(method, self._get_url(path), auth=(self.key, ''), params=params, data=data, files=files)
        return self._check_response(res, xmltodict.parse(res.text)['prestashop'] if not files and res.text else None)

    def add(self, path, data):
        return self._request('POST', path, data=data)

    def add_image(self, path, fp, exists=False):
        with open(fp, 'rb') as fp:
            return self._request('POST', 'images/' + path, {'ps_method': 'PUT'} if exists else None,
                                 files={'image': fp})

    def get(self, path, params=None):
        return self._request('GET', path, params)

    def edit(self, path, data):
        return self._request('PUT', path, data=data)

    def delete(self, path):
        return self._request('DELETE', path)


PrestaAPIV2: PrestaAPIV2 = PrestaAPIV2 (api_domain, api_key)
#
#
################################################################################




################################################################################
#
#
from .presta_apis.presta_python_api_v3.presta_python_api_v3 import \
    PrestaAPIV3, PrestaAPIV3Format, \
    PrestaAPIV3Error, PrestaAPIV3AuthenticationError

PrestaAPIV3: PrestaAPIV3 = PrestaAPIV3(
    api_domain,
    api_key,
    default_lang = 1,
    debug = True,
    data_format = PrestaAPIV3Format.JSON
)
#
#
################################################################################







class PrestaAPIError():
    pass





    #""" Работа с магазином на Престашоп через API 
    #При каждом вызове класса я создаю новые JSON схемы
    #для товара, категории, валют и т.п.
    #Сделано для того, чтобы синхронизироваться с базой данных. 
    #Тут над подумать над автореализацией
    #"""


    #def __init__(self, *args, **kwards):
    #    """ Проверка доступности сервера и обновление схем:
    #    product_schema,
    #    category_schema,
    #    languages_schema,
    #    suppliers_schema
    #    """
        

    #    try:
    #        responce = PrestaAPIV.head('products')
    #        logger.debug(
    #            f'''Prestashop Сервер responce:{[key for key in responce.items()]}''')

    #    except Exception as ex:
    #        logger.error(
    #            f'''Ошибка при подключении к серверу: {ex.with_traceback(ex.__traceback__)}''')
    #        pass

    #    return self



    #def ping():
    #    return PrestaAPIV1V3.ping()

    #def buid_schemas(self):
    #    """
    #    Строю json схемы, 
    #    """
    #    dir = gs.dir_presta_schemes

    #    self.product_schema = self.get(
    #        'products', options={'schema': 'blank'})
    #    j_dumps(self.product_schema, Path(
    #        dir, 'product_schema.json').absolute())

    #    self.category_schema = self.get(
    #        'categories', options={'schema': 'blank'})
    #    j_dumps(self.category_schema, Path(
    #        dir, 'category_schema.json').absolute())

    #    self.languages_schema = self.get('languages', options={})
    #    j_dumps(self.languages_schema, Path(
    #        dir, 'languages_schema.json').absolute())

    #    self.suppliers_dict = self.get('suppliers', options={})
    #    j_dumps(self.suppliers_dict, Path(
    #        dir, 'suppliers_dict.json').absolute())
        