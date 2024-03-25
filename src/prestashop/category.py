"""! Class of product category in `Prestashop`
The class provides methods for adding, deleting, updating categories, 
as well as obtaining a list of parent categories from a given one.

@details `PrestaCategory` layer between client categories (Prestashop, in my case) and suppliers
 
@note Clients can each have their own unique category tree, which is only understandable to them. 
Product binding to category is described in supplier scenarios

@image html categories_tree.png 
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from attr import attr, attrs
from pathlib import Path
from typing import Union, List, Dict
import requests

# ----------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from .presta_apis import  PrestaAPIV
# --------------------------------


# # Загрузка учетных данных для PrestaShop API из настроек
# API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
# API_KEY = gs.default_prestashop_api_credentials['API_KEY']

class PrestaCategory:
    """!    
        Пример использования класса:
        ```python    
        prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacategory.add_category_prestashop('New Category', 'Parent Category')
        prestacategory.delete_category_prestashop(3)
        prestacategory.update_category_prestashop(4, 'Updated Category Name')
        print(prestacategory.get_list_parent_categories_prestashop(5))
        ```    
    """

    DOMAIN = next((domain for domain in gs.list_prestashop_api_credentials if domain.get('HAVE_FULL_CATEGORIES_TREE') == True), None)
    API_DOMAIN:str = DOMAIN ['API_DOMAIN']
    API_KEY: str = DOMAIN ['API_KEY']
    PrestaAPIV: object = PrestaAPIV(API_DOMAIN, API_KEY)

    #@logs_and_errors_decorator(default_return =  False)
    def __init__(self, *args, **kwards):
        """! Инициализация объекта PrestaCategory с учетными данными для PrestaShop API.

        @param API_DOMAIN: URL PrestaShop API
        @param API_KEY: Ключ API PrestaShop
        """

    #@logs_and_errors_decorator(default_return =  False)
    def _get_category_id_by_name(self, category_name ,PrestaAPIV):
        """
        Вспомогательный метод для получения ID категории по ее имени.

        @param category_name: Имя категории
        @returns  ID категории или None, если категория не найдена
        """
        response = requests.get(
            self.API_DOMAIN + 'categories',
            params={'filter[name]': category_name, 'display': 'full'},
            headers={'Authorization': 'Bearer ' + self.API_KEY}
        )
        category_data = response.json()['categories'][0]
        return category_data['id'] if category_data else None
    
    #@logs_and_errors_decorator(default_return =  False)
    def add_category_prestashop(self, category_name, PrestaAPIV, parent_category_name=None, parent_category_id=2):
        """
        Метод для добавления новой категории в PrestaShop.

        @param category_name: Имя новой категории
        @param parent_category_name: Имя родительской категории (по умолчанию None)
        @param parent_category_id: ID родительской категории (по умолчанию 2)
        """
        data = {'name': category_name, 'id_parent': parent_category_id}

        if parent_category_name:
            parent_id = self._get_category_id_by_name(parent_category_name)
            if parent_id:
                data['id_parent'] = parent_id
            else:
                print(f"Parent category '{parent_category_name}' not found.")
                return

        response = requests.post(
            self.API_DOMAIN + 'categories',
            json={'category': data},
            headers={'Authorization': 'Bearer ' + self.API_KEY}
        )
        print(response.json())
        
    #@logs_and_errors_decorator(default_return =  False)
    def delete_category_prestashop(self, category_id, PrestaAPIV):
        """
        Метод для удаления категории из PrestaShop по ее ID.

        @param category_id: ID категории для удаления
        """
        response = requests.delete(
            self.API_DOMAIN + f'categories/{category_id}',
            headers={'Authorization': 'Bearer ' + self.API_KEY}
        )
        print(response.json())
        
    #@logs_and_errors_decorator(default_return =  False)
    def update_category_prestashop(self, category_id,  new_name):
        """
        Метод для обновления имени категории в PrestaShop по ее ID.

        @param category_id: ID категории для обновления
        @param new_name: Новое имя категории
        """
        data = {'name': new_name}
        response = requests.put(
            self.API_DOMAIN + f'categories/{category_id}',
            json={'category': data},
            headers={'Authorization': 'Bearer ' + self.API_KEY}
        )
        print(response.json())


    #@logs_and_errors_decorator(default_return =  False)
    def get_list_parent_categories(self, id_category: int,  parent_categories_list:List[int] = []) -> list:
        """! @~russian Вытаскивет из базы данных Prestashop родительские категории от заданной 
        @details функция через API получает список категорий

        @param id_category `int`  категория для которой надо вытащить родителя
        @param dept `int = 0` : глубина рекурсии. Если 0, глубина не ограчинена
        @returns `list`  Список родительских категорий
        """

        # 1. Получение списка категорий.
        
        category_dict = self.PrestaAPIV.get('categories', id_category)
        """! возвращает словарь
        ```python
        {'category': 
                {'id': 11259, 
                'id_parent': '11248', 
                'level_depth': '5', 
                'nb_products_recursive': -1, 
                'active': '1', 
                'id_shop_default': '1', 
                'is_root_category': '0', 
                'position': '0', 
                'date_add': '2023-07-25 11:58:08', ...}
        }```"""
        _parent_category: int = int (category_dict['category']['id_parent'])
        parent_categories_list.append (_parent_category)
    
        if _parent_category <= 2: ## <- `2` корневая директория
            return parent_categories_list
            pass
        else:
            return self.get_list_parent_categories(_parent_category, parent_categories_list)
        

    