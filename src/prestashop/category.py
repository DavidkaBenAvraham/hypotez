"""!  Kласс категории товара в `Prestashop`
Класс предоставляет методы для добавления, удаления, обновления категорий, 
а также получения списка родительских категорий от заданной.


 @details `PrestaCategory` слой между категориями клиента (Prestashop, в моем случае) и поставщика
 
 @note Клиенты могут быть каждый со своим уникальным деревом категорий, которые только ему и понятны. 
 Привязка товара к категории описана в сценариях поставщиков

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
from typing import Union, List, Dict
import requests
# ----------------------------------


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from .presta_apis import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# --------------------------------


# Загрузка учетных данных для PrestaShop API из настроек
API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
API_KEY = gs.default_prestashop_api_credentials['API_KEY']

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
    API_DOMAIN = API_DOMAIN
    API_KEY = API_KEY
    
    def __init__(self, *args, **kwards):
        """! Инициализация объекта PrestaCategory с учетными данными для PrestaShop API.

        @param API_DOMAIN: URL PrestaShop API
        @param API_KEY: Ключ API PrestaShop
        """


    def _get_category_id_by_name(self, category_name):
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
    def add_category_prestashop(self, category_name, parent_category_name=None, parent_category_id=2):
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
    def delete_category_prestashop(self, category_id):
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
    def update_category_prestashop(self, category_id, new_name):
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
    def get_list_parent_categories(self, id_category: int, parent_categories_list:List[int] = []) -> list:
        """! @~russian Вытаскивет из базы данных Prestashop родительские категории от заданной 
        @details функция через API получает список категорий

        @param id_category `int`  категория для которой надо вытащить родителя
        @param dept `int = 0` : глубина рекурсии. Если 0, глубина не ограчинена
        @returns `list`  Список родительских категорий
        """

        # 1. Получение списка категорий.
        
        category_dict = PrestaAPIV3.get('categories', id_category)
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
        

    