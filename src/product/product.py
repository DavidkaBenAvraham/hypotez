"""! @~russian Класс `Product`. Взаимодействие  сайт <--> товар <--> престашоп
@details Определяет поведение товара в проекте. 
@todo Переосмыслить модуль. Здесь выполняется несколько действий: 
- обращение к грабберу для получения данных о товаре
- обращение к API Prestashop.
это ненормальная логика

 @section libs imports:
  - sqlite3 
  - pathlib 
  - attr 
  - typing 
  - src.gs (local)
  - src.gs (local)
  - src.gs (local)
  - src.prestashop (local)
  
  @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from sqlite3 import Date
#from pathlib import Path
from typing import Union

# ---------------------------------
from src.settings import gs
from src.helpers import logger,  logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import PrestaProduct, PrestaCategory, PrestaSupplier
from src.categories import Category
# ---------------------------------


class Product(PrestaProduct):
    """! @~russian Манипуляции с товаром.
    @details Вначале я отдаю грабберу комманду забрать данные со страницы товара,
    а потом работаю с API престашоп


        `product_categories` (dict): - все категории. 
        TODO: Надо переделать!
        

    """
    """ Я могу передать локаторы товара из сценария или изменить их на лету """
    #c = Category()    
    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        pass

    # #@logs_and_errors_decorator(default_return =  False)
    # def check_if_product_in_presta_db(self, product_reference: str) -> Union[int,bool]:
    #     """ Проверяю наличие товара в БД
    #     -----------------------------
    #     Attrs:
    #         product_reference `str`  :  SKU, ASIN, etc.
    #     @returns
    #         id_product if present, else False
    #     """
        
    #     return PrestaProduct.check(self, product_reference)

    # #@logs_and_errors_decorator(default_return =  False)
    # def get_list_products_from_presta() ->dict:
    #     """ Полный список товаров. Осторожно!
    #     ------------------------------
    #    """
       
    #     return PrestaProduct.get_list_products()

    #@logs_and_errors_decorator(default_return =  False)
    # def get_product_info(id_product: Union[int,str]) -> dict:
    #     """ Словарь товара по его ID
    #     ------------------------------
    #     """
    #     return PrestaProduct.get_product_info(id_product)

    #@logs_and_errors_decorator(default_return =  False)
    # def get_product_info_by_filter(filter: str, value) -> dict:
    #     return PrestaProduct.get_product_info_by_filter(filter,value)
    #     pass
    
    #@logs_and_errors_decorator(default_return =  False)
    # def add_2_prestashop(product_dict: dict, presta_api_version: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> Union[int,bool]:
    #     """ Add new product to prestashop db via api
    #     ---------------------------------
    #     @param
    #         product_fields (ProductFields): класс полей товара
    #         presta_api_version `str`  :  Какая API будет задействована:
    #             'V1' - prestapyt
    #             'V2' - prestashop_api
    #     @returns
    #         id for added product if success, else False
    #     """

    #     return PrestaProduct.add(product_dict, presta_api_version)

    #@logs_and_errors_decorator(default_return =  False)
    def get_parent_categories(id_category: int, dept: int = 0) -> list:
        return Category.get_parents(id_category, dept)

    # #@logs_and_errors_decorator(default_return =  False)
    # def update_product_in_prestashop(id_product: int, product_dict: dict) -> Union[int,bool]:
    #     """ Update product in prestashop  db via api
    #     --------------------------------
    #     @param
    #         product_fields (ProductFields): класс полей товара
    #     @returns
    #         id for added product if success, else False
    #     """
    #     return PrestaProduct.update(id_product, product_dict)

    #@logs_and_errors_decorator(default_return =  False)
    # def update_product_categories_in_prestashop(id_product: int, category_ids: list) -> Union[int,bool]:
    #     """ Update product in prestashop  db via api
    #     --------------------------------
    #     @param
    #         product_fields (ProductFields): класс полей товара
    #     @returns
    #         id for added product if success, else False
    #     """
    #     return PrestaProduct.update_categories(id_product, category_ids)

    # #@logs_and_errors_decorator(default_return =  False)
    # def upload_product_default_image(product_id: int, image_url: str) -> Union[int,False]:
    #     """ Поднимаю картинку, которую я ставлю дефолтной по ёё URL """
    #     return PrestaProduct.upload_image(id_product = product_id, image_url = image_url)
    #     """ id_product = product_id <- точка смены имен переменных """
    #     pass

    #@logs_and_errors_decorator(default_return =  False)
    # def delete_product(id_product: Union[int,str]) -> dict:
    #     """ Удаляю товер из бд 
    #     Осторожно!
    #     """
    #     return PrestaProduct.delete(f'products/{id_product}')
    #
    #
    # =================================================================================

