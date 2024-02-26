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
                        'sort':None, 
                        'limit':None, 
                        'language':None, 
                        'io_format' : 'JSON' , 
                        'output_format' : 'JSON'}        
        pass



    
    
    #@logs_and_errors_decorator(default_return =  False)
    def get(self, 
            product_id: int = None, 
            product_reference:str = None, 
            search_filter: Union[str, dict] = None, 
            PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> dict:
        """! Тестовая функция, по сути повтор check, но работает непосредстевенно
        @details Я могу задать параметр поиска по `product_id`, `product_reference` 
        или получить готовый фильтр поиска. f.e.`{'filter[id]': product_id}` )
          
        @param  product_id `str`: id товара
        @param  product_reference `str`: reference товара
        @param filter `dict`:  фильтр поиска. f.e.`{'filter[id]': product_id}` )

        @todo  Union[str('V1'),str('V2'),str('V3')] = 'V3' переписать в Enum
        
        display=display,  sort=sort,limit=limit <- передается через  `search_filter`
       """
        #dic_product_type_PrestaAPIV1 = PrestaAPIV1.get(f'products/{id_product}')
        #dic_product_type_PrestaAPIV2 = PrestaAPIV2.get(f'products/{id_product}')
        #productsearch_filter: dict = {} if not filter else filter

        if  product_reference:
            self.params.update( {'filter[reference]': product_reference}  )
            """! Я могу прислать параметр `product_reference` """ 
        elif  product_id and isinstance(product_id, int):
            product_id = [product_id]
            self.params.update( {'filter[id]': product_id} )
            """! Я могу прислать параметр `product_id` """
        elif isinstance(search_filter, dict):
            self.params.update( search_filter )
            """! Я могу прислать готовый фильтр """
     


        if PrestaAPIV == 'V1':
            """! в версии PrestaAPIV возврщается Словарь товара если товар уже существует в базе Prestashop."""
            response = PrestaAPIV1.get('products', product_id, search_filter = search_filter)
        elif PrestaAPIV == 'V2':
            response = PrestaAPIV2.get('products', params = self.params)            
        elif  PrestaAPIV == 'V3':            
            response = PrestaAPIV3.get('products', search_filter = self.params) 
            
            # if product_reference:
            #     search_filter = f"[reference] = [{product_reference}]"
            # if product_id:
            #     search_filter = f"[id] = [{product_id}]"
            # if search_filter:  
                #response = PrestaAPIV3.get('products', search_filter = search_filter, display = 'full')
            #else:
                #response = PrestaAPIV3.get('products') # <- вываливаю  все товары из бд.

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
    def add(self, product_dict: dict, data_format = 'JSON', PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V1') -> dict:
        """ Добавление нового товара в БД PRESTASHOP через API
        -----------------
       @param
        product_dict (dict): - Заполненный словарь товара / поля класса Product
        PrestaAPIV `str`  :  Какая API будет задействована:
                'V1' - prestapyt
                'V2' - prestashop_api
       @returns
        product:dict - Заполненный словарь добавленного товара в случае успеха, иначе сообщение об ошибке
        """
        data: dict = { 'product': product_dict }
        
        if PrestaAPIV == 'V3':
            try:
                
                response = PrestaAPIV3.add('products', data)
                return response
            except Exception as ex:
                print('-------------------------V3 ERROR --------------------------------------')
                logger.error(ex)
                print('---------------------------------------------------------------')
                return False
        elif PrestaAPIV == 'V2':
            try:
                response = PrestaAPIV2.add('products', data, data_format)['product']
                return response
            except Exception as ex:
                print('--------------------------V2 ERROR -------------------------------------')
                logger.error(ex)
                print('---------------------------------------------------------------')
                return False
        else:
            try:
                response = PrestaAPIV1.add('products', data)['product']
                return response

            except Exception as ex:
                print('------------------------- V1 ERROR --------------------------------------')
                logger.error(ex)
                print('---------------------------------------------------------------')
                return False


    
    #@logs_and_errors_decorator(default_return =  False)
    def update(self, id_product: int, product_dict: dict, PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V3')-> dict:
        """ Изменение данных о существующем товаре
        @param id_product - 
        @param product:dict - Заполненный словарь товара / поля класса Product
        @PrestaAPIV - 'V1' 
        @returns product - изменненый товар в случае успеха иначе сообщение об ошибке от prestashop
        
        """
        resourse = f'products/{id_product}'
        if PrestaAPIV == 'V3':
            return   PrestaAPIV3.write(resourse, product_dict)
        elif PrestaAPIV == 'V2':
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
    #def update_categories(id_product: int, category_ids: list, PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V3')-> Union[dict, PrestaAPIError]:
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
    def get_product_schema(self, PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V1') -> Union[dict, False]:
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
    def upload_image(self, product_id: int, local_file_path: str) -> Union[int, False]:
        """
        Загружаю картинку, получаю или id_image или False
        @param
            image_url `str`  :  source url
            local_file_path `str`  :  имя файла для prestashop. Если на указано (`default.png`) - 
        Returns
            id_image `int`  :  id_image from src.prestashop db if success else False

        """
        PrestaAPIV3.create_binary('products', product_id, local_file_path)


    
    #@logs_and_errors_decorator(default_return =  False)
    def delete(self, id_product: Union[int,str], PrestaAPIV: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> dict:
        """ Удаляю товер из бд """

        #return PrestaProd.delete_product(f'products/{id_product}')
        return  PrestaAPIV1.delete(f'products/{id_product}')

        if isinstance(response, list) and len(response) > 0:
            return response[0]
        else:
            return False

