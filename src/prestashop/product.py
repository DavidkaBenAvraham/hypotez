"""! @brief @~russian класс товара в `Prestashop`

 @section libs imports:
  - sys 
  - os 
  - attr 
  - pathlib 
  - typing 
  - gs 
  - helpers 
  - gs 
  - prestashop.prestashop 
  - .images_exec 
  
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import sys
import os


from attr import attr, attrs
from pathlib import Path
from typing import Union

# ----------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps

from .presta_apis import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3

from .images_exec import upload_image
# --------------------------------





class PrestaProduct():
    """ Класс товара из модуля prestashop
   Непосредственно выполняет все операции через API
   ------------------------------------
   Methods:
    check(product_reference: str): Проверка наличия товара в бд
        по product_reference (SKU, MKT)
        Вернет словарь товара, если товар есть, иначе False
    search(filter: str, value: str): Расширенный поиск в БД по фильтрам
    get(id_product): Возвращает информацию о товаре по ID
    """

    #@logs_and_errors_decorator(default_return =  False)
    def __init__(self,*args,**kwards):
        self.params: dict = {'display':'full', 
                        'filter':None, 
                        'sort':None, 
                        'limit':None, 
                        'language':None, 
                        'io_format' : 'JSON' , 
                        'output_format' : 'JSON'}        
        pass


    
    #@logs_and_errors_decorator(default_return =  False)
    def get(self,  product_id: Union[int, list[int]] = None,  product_reference: str = None, params: dict = None, PrestaAPIV: str = 'PrestaAPIV3') -> bool:
        
        """! Проверка наличия товара в БД 
        -----------------
        @param product_reference `str`  - термин из престашоп = `reference` 
        @param product_id `str`   - термин из престашоп = `id`
        @param params `dict` {'display':'option'}
        example {'display':'full' | '[id, name]' | 'schema'}

        @returns `bool`   False  - if Product NOT in the DB, else True
        """
        
        product_filter: dict = {}
        if  product_reference:
            product_filter = {'filter[reference]': product_reference}
        elif  product_id and isinstance(product_id, int):
            product_filter = {'filter[id]': product_id} 
        else:
            logger.warning(f'Ситуация, когда не определен ни `product_reference` ни `product_id, в апи запросе Возвращется список всех `id` товара')
            """! Возвращется список всех `id` товара """
            pass

        params =  self.params if not params else params
        
        params['filter'] = product_filter
        
        if PrestaAPIV == 'PrestaAPIV1':
            
            response = PrestaAPIV1.get('products', product_id, params)
            """! в версии PrestaAPIV возврщается Словарь товара """
        elif  PrestaAPIV == 'PrestaAPIV2':   
            pass
        else:

            response = PrestaAPIV3.get('products', filter = params['filter'])
            """! параметры по умолчанию уже заложены в реализации функции """
            pass
        
        return response


    
    # #@logs_and_errors_decorator(default_return =  False)
    # def search(self, filter: str, value: str, PrestaAPI = PrestaAPIV3) -> Union[dict, False]:
    #     """ Расширенный поиск в БД
    #     -----------------
    #     Attrs:
    #         filter`str`  :  фильтр поиска
    #             Значения `reference` `id_category` , `id_supplier` etc
    #         value `str`  :  искомое значение
    #     @returns
    #         product - словарь товарам иначе False
    #         False - if Product NOT in the DB, else Product
    #     """
    #     product_filter = {f'filter[{filter}]': value}

    #     #return PrestaAPIV1.search('products', product_filter)

    #     response = PrestaAPIV3.search('products', product_filter)

    #     if isinstance(response, list) and len(response) > 0:
    #         return response[0]
    #     else:
    #         return False


    
    #@logs_and_errors_decorator(default_return =  False)
    def get(self, product_id: int = None, product_reference:str = None, options:dict = None, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> dict:
        """ Тестовая функция, по сути повтор check, но работает непосредстевенно 
        @param  product_id `str`: id товара
        @param  product_reference `str`: reference товара
        @param filter: dict
       Я могу задать параметр поиска по `product_id`, `product_reference` или 
       с id_product 
       
       """
        #dic_product_type_PrestaAPIV1 = PrestaAPIV1.get(f'products/{id_product}')
        #dic_product_type_PrestaAPIV2 = PrestaAPIV2.get(f'products/{id_product}')
        #product_filter: dict = {} if not filter else filter

        if  product_reference:
            self.params.update ( {'filter[reference]': product_reference} )
        elif  product_id and isinstance(product_id, int):
            self.params.update ( {'filter[id]': product_id} )
     


        #####################################################
        presta_api_version = 'V1' # <- версия АПИ обработчика
        ######################################################

        if presta_api_version == 'V1':
            
            response = PrestaAPIV1.get('products', product_id, options = options)
            """! в версии PrestaAPIV возврщается Словарь товара """
            
        elif  presta_api_version == 'V3':
            #resource:str, _id:str = None, _filter:str = None, display:str='full'
            filter = f"[reference] = [{product_reference}]"
            response = PrestaAPIV3.get('products', filter = filter, display = 'full')
       
            
        return response
    

    
    # #@logs_and_errors_decorator(default_return =  False)
    # def get_list_products_from_prestashop(self, presta_api: Union[str('V1'),str('V2'),str('V3')] = 'V3') ->dict:
    #     """
    #     Полный список товаров. Осторожно!

    #    """
    #     return   PrestaAPIV1.get('products')
    #     if isinstance(response, list) and len(response) > 0:
    #         return response[0]
    #     else:
    #         return False
        

    
    #@logs_and_errors_decorator(default_return =  False)
    def add(self, product_dict: dict, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V1') -> dict:
        """ Добавление нового товара в БД PRESTASHOP через API
        -----------------
       @param
        product_dict (dict): - Заполненный словарь товара / поля класса Product
        presta_api_version `str`  :  Какая API будет задействована:
                'V1' - prestapyt
                'V2' - prestashop_api
       @returns
        product:dict - Заполненный словарь добавленного товара в случае успеха, иначе сообщение об ошибке
        """

        if presta_api_version == 'V3':
            try:
                response = PrestaAPIV3.create('products', product_dict)
                return response
            except Exception as ex:
                print('---------------------------------------------------------------')
                pprint(ex)
                print('---------------------------------------------------------------')
                return False
        elif presta_api_version == 'V2':
            try:
                response = PrestaAPIV2.add('products', product_dict)['product']
                return response
            except Exception as ex:
                print('---------------------------------------------------------------')
                pprint(ex)
                print('---------------------------------------------------------------')
                return False
        else:
            try:
                response = PrestaAPIV1.add('products', product_dict)['product']
                return response

            except Exception as ex:
                print('---------------------------------------------------------------')
                pprint(ex)
                print('---------------------------------------------------------------')
                return False


    
    #@logs_and_errors_decorator(default_return =  False)
    def update(self, id_product: int, product_dict: dict, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V3')-> dict:
        """ Изменение данных о существующем товаре
        @param
            product:dict - Заполненный словарь товара / поля класса Product
        @returns
            product - изменненый товар в случае успеха иначе сообщение об ошибке от prestashop 
        """
        resourse = f'products/{id_product}'
        if presta_api_version == 'V3':
            return   PrestaAPIV3.write(resourse, product_dict)
        elif presta_api_version == 'V2':
            return   PrestaAPIV2.add(resourse, product_dict)['product']
        else:
            return   PrestaAPIV1.add(resourse, product_dict)

        if isinstance(response, list) and len(response) > 0:
            return response[0]
        else:
            return False

        #product = PrestaAPIV1.get('products', id_product)
        #PrestaAPIV1.edit('products', id_product, product_dict)
        pass

    #
    #def update_categories(id_product: int, category_ids: list, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V3')-> Union[dict, PrestaAPIError]:
    #    """ Изменение данных о существующем товаре
    #    @param
    #        product:dict - Заполненный словарь товара / поля класса Product
    #    @returns
    #        product - изменненый товар в случае успеха иначе сообщение об ошибке от prestashop 
    #    """
    #    product = PrestaAPIV1.get('products', id_product)
    #    product['product']['associations']['categories'] = \
    #        {'categories': [{'id': cat_id} for cat_id in category_ids]}
    #    PrestaAPIV1.edit('products', id_product, product)
    #    pass

    #@logs_and_errors_decorator(default_return =  False)
    def get_product_schema(self, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V1') -> Union[dict, False]:
        """JSON схема товара

        @returns
            Union[dict,bool]: JSON или False
        """
        params = { 'display': 'full'},  ## <- или 'basic' в зависимости от того, какую информацию я хочу получить
        
        params = 'products'
        response = PrestaAPIV1.get('products',1658)
        if response.status != 200:
            logger.error(f'Ошибка при выполнении запроса: {response}')
            return False

        return response.json


    
    #@logs_and_errors_decorator(default_return =  False)
    def upload_image(self, id_product: int, image_url: str, target_file_name: str = 'default.png') -> Union[int, bool]:
        """
        Загружаю картинку, получаю или id_image или False
        @param
            image_url `str`  :  source url
            target_file_name `str`  :  имя файла для prestashop. Если на указано (`default.png`) - 
            будет заменено на `default_<RANDOMSEQUENCE>.png`
        Returns
            id_image `int`  :  id_image from src.prestashop db if success else False

        """

        resource = fr'products/{id_product}'
        #response: dict = upload_image(resource = resource , image_url = image_url)
        #return response['prestashop']['image']['id']
        return upload_image(resource = resource , image_url = image_url)
        return response

    
    #@logs_and_errors_decorator(default_return =  False)
    def delete(self, id_product: Union[int,str], presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> dict:
        """ Удаляю товер из бд """

        #return PrestaProd.delete_product(f'products/{id_product}')
        return  PrestaAPIV1.delete(f'products/{id_product}')

        if isinstance(response, list) and len(response) > 0:
            return response[0]
        else:
            return False

