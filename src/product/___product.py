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
from pathlib import Path
from attr import attr, attrs
from typing import Union

# ---------------------------------
from src.settings import gs
from src.helpers import logger,  logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from .product_fields import ProductFields
from src.suppliers import Supplier
from src.prestashop import Product as PrestaProduct, Category as PrestaCategory
from src.prestashop.supplier import Supplier as PrestaSupplier
# ---------------------------------


class Product():
    """! @~russian Манипуляции с товаром.
    @details Вначале я отдаю грабберу комманду забрать данные со страницы товара,
    а потом работаю с API престашоп

    @note
    
        `supplier` (Supplier): supplier inctance
        `webelements_locators` (dict): - locators for product fields
                    Я могу читать дефолтные локаторы из файла suppliers/<supplier>/locators/product.json
                    или погонять свои для теста
                        
        `product_categories` (dict): - все категории. 
        TODO: Надо переделать!
        

        `prestashop_product_categories` (dict): словарь категорий prestashop

        `product_fields` : набор полей товара:
                    - при определении класса поставщика строится из класса suppliers.related_modules.ProductFields()
                    - иначе, из suppliers.ProductFields()
                    - сделано для тестов, чтобы менять на лету  
    """
    product_fields: ProductFields = ProductFields()
    webelements_locators : dict = None
    """ Я могу передать локаторы товара из сценария или изменить их на лету """
    
    def __init__(self , *args, **kwards):
        pass

    # ================================================================================
    #                       
    #                       Часть, взаимодействующая с вебдравейром
    @staticmethod
    def get_list_products_in_category(s) -> Union[list[str],str,bool]:
        """ Получаю список url товаров со страницы категории.
        На данный момент я подразумеваю, что уже нахожусь на странице категории
        -----------------------------------------
        Attrs:
            s (Supplier):
        @returns
            urls (str,list): one or more urlsm or False if no products in category
        """
        return s.related_modules.get_list_products_in_category(s)

    @staticmethod
    def grab_product_page(s, api_method: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> Union[dict,bool]:
        """ Запуск сценария сбора информации о товаре    
        -------------------------------------
        Attrs:
            s (Supplier): 
        @returns
            ProductFields if success, else False
        """
        # 1.    
        return s.related_modules.grab_product_page(s, api_method = api_method)
    #
    #
    # =================================================================================









    # ================================================================================
    #                       
    #                       Часть, взаимодействующая с pretstashop
    @staticmethod
    def check_if_product_in_presta_db(product_reference: str) -> Union[int,bool]:
        """ Проверяю наличие товара в БД
        -----------------------------
        Attrs:
            product_reference `str`  :  SKU, ASIN, etc.
        @returns
            id_product if present, else False
        """
        return PrestaProduct.check(product_reference)

    @staticmethod
    def get_list_products_from_presta() ->dict:
        """ Полный список товаров. Осторожно!
        ------------------------------
       """
        return PrestaProduct.get_list_products()

    @staticmethod
    def get_product_info(id_product: Union[int,str]) -> dict:
        """ Словарь товара по его ID
        ------------------------------
        """
        return PrestaProduct.get_product_info(id_product)

    @staticmethod
    def get_product_info_by_filter(filter: str, value) -> dict:
        return PrestaProduct.get_product_info_by_filter(filter,value)
        pass
    
    @staticmethod
    def add_2_prestashop(product_dict: dict, api_method: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> Union[int,bool]:
        """ Add new product to prestashop db via api
        ---------------------------------
        @param
            product_fields (ProductFields): класс полей товара
            api_method `str`  :  Какая API будет задействована:
                'V1' - prestapyt
                'V2' - prestashop_api
        @returns
            id for added product if success, else False
        """

        return PrestaProduct.add(product_dict, api_method)

    @staticmethod
    def get_parent_categories(id_category: int, dept: int = 0) -> list:
        return PrestaCategory.get_parents(id_category, dept)

    @staticmethod
    def update_product_in_prestashop(id_product: int, product_dict: dict) -> Union[int,bool]:
        """ Update product in prestashop  db via api
        --------------------------------
        @param
            product_fields (ProductFields): класс полей товара
        @returns
            id for added product if success, else False
        """
        return PrestaProduct.update(id_product, product_dict)

    @staticmethod
    def update_product_categories_in_prestashop(id_product: int, category_ids: list) -> Union[int,bool]:
        """ Update product in prestashop  db via api
        --------------------------------
        @param
            product_fields (ProductFields): класс полей товара
        @returns
            id for added product if success, else False
        """
        return PrestaProduct.update_categories(id_product, category_ids)

    @staticmethod
    def upload_product_default_image(product_id: int, image_url: str) -> Union[int,False]:
        """ Поднимаю картинку, которую я ставлю дефолтной по ёё URL """
        return PrestaProduct.upload_image(id_product = product_id, image_url = image_url)
        """ id_product = product_id <- точка смены имен переменных """
        pass

    @staticmethod
    def delete_product(id_product: Union[int,str]) -> dict:
        """ Удаляю товер из бд 
        Осторожно!
        """
        return PrestaProduct.delete(f'products/{id_product}')
    #
    #
    # =================================================================================

