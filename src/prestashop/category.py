"""! @ru_brief  Kласс категории товара в `Prestashop`

 @ru_details `Categoty` слой между категориями клиента (Prestashop, в моем случае) и поставщика
 
 @note Клиенты могут быть каждый со своим уникальным деревом категорий, которые только ему и понятны. Привязка товара к категории описана в сценариях поставщиков

 @package src.prestashop.category

 @section libs imports:
  - attr 
  - pathlib 
  - typing 
  - src.gs 
  - src.helpers 
  - src.gs 
  - src.prestashop.prestashop 
  - .images_exec 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from attr import attr, attrs
from pathlib import Path
from typing import Union

# ----------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from src.prestashop.prestashop import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3, PrestaAPIError
from .images_exec import upload_image
# --------------------------------

class Category(): 
    """! @ru_brief Класс обработки категорий для предоставления товару списка связанных категорий
    """

    def __init__(self,*args,**kwards) -> None:
        pass
        

    @staticmethod
    def get_parents(id_category: int, dept: int = 0) -> list:
        """! @ru_brief Вытаскивет родительские категории от заданной 
        @ru_details функция через API получает список категорий

        @param id_category `int`  категория для которой надо вытащить родителя
        @param dept `int = 0` : глубина рекурсии. Если 0, глубина не ограчинена
        @returns `list`  Список родительских категорий
        """

        # 1. Получение списка категорий
        """! @todo Разобраться с логикой работы функции"""
        try:    
            category = PrestaAPIV1.get('categories', id_category)
        except Exception as ex:
            
            logger.error(f""" Тут иногда не отвечает .... {ex}""")
            return False

            #if 'HTTP response is empty' in e:
            #    return False

            #x=0
            #while True:
            #     Category.get_parents(id_category)
            #     if x>3: return False
            #     x+=1

        parent_categories = []
        
        step = 1
        while 'id_parent' in category['category']:
            #parent_category_id = int(category['category']['id_parent']['value'])
            parent_category_id = int(category['category']['id_parent'])
            if parent_category_id < 2:
                break
            parent_category = PrestaAPIV1.get('categories', parent_category_id)
            parent_categories.append(parent_category['category']['id'])

            if dept > 0 and step > dept:
                """если задана глубина поиска """
                return parent_categories
            else:
                step += 1

            category = parent_category

        return parent_categories

    