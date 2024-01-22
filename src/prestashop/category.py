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
from typing import Union
import requests
# ----------------------------------


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from src.prestashop.prestashop import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
from .images_exec import upload_image
# --------------------------------


# Загрузка учетных данных для PrestaShop API из настроек
api_domain = gs.default_prestashop_api_credentials['api_domain']
api_key = gs.default_prestashop_api_credentials['api_key']

class PrestaCategory:
    """!    
        Пример использования класса:
        ```python    
        prestacategory = PrestaCategory(api_domain=api_domain, api_key=api_key)
        prestacategory.add_category_prestashop('New Category', 'Parent Category')
        prestacategory.delete_category_prestashop(3)
        prestacategory.update_category_prestashop(4, 'Updated Category Name')
        print(prestacategory.get_list_parent_categories_prestashop(5))
        ```    
        """
    api_domain = api_domain
    api_key = api_key
    
    def __init__(self, *args, **kwards):
        """! Инициализация объекта PrestaCategory с учетными данными для PrestaShop API.

        @param api_domain: URL PrestaShop API
        @param api_key: Ключ API PrestaShop
        """


    def _get_category_id_by_name(self, category_name):
        """
        Вспомогательный метод для получения ID категории по ее имени.

        @param category_name: Имя категории
        :return: ID категории или None, если категория не найдена
        """
        response = requests.get(
            self.api_domain + 'categories',
            params={'filter[name]': category_name, 'display': 'full'},
            headers={'Authorization': 'Bearer ' + self.api_key}
        )
        category_data = response.json()['categories'][0]
        return category_data['id'] if category_data else None

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
            self.api_domain + 'categories',
            json={'category': data},
            headers={'Authorization': 'Bearer ' + self.api_key}
        )
        print(response.json())

    def delete_category_prestashop(self, category_id):
        """
        Метод для удаления категории из PrestaShop по ее ID.

        @param category_id: ID категории для удаления
        """
        response = requests.delete(
            self.api_domain + f'categories/{category_id}',
            headers={'Authorization': 'Bearer ' + self.api_key}
        )
        print(response.json())

    def update_category_prestashop(self, category_id, new_name):
        """
        Метод для обновления имени категории в PrestaShop по ее ID.

        @param category_id: ID категории для обновления
        @param new_name: Новое имя категории
        """
        data = {'name': new_name}
        response = requests.put(
            self.api_domain + f'categories/{category_id}',
            json={'category': data},
            headers={'Authorization': 'Bearer ' + self.api_key}
        )
        print(response.json())

    # def get_list_parent_categories_prestashop(self, category_id, category_name=None):
    #     """
    #     Метод для получения списка родительских категорий от заданной категории в PrestaShop.

    #     @param category_id: ID категории, от которой нужно получить родительские категории
    #     @param category_name: Имя категории, от которой нужно получить родительские категории (по умолчанию None)
    #     :return: Список родительских категорий
    #     """
    #     if category_name:
    #         category_id = self._get_category_id_by_name(category_name)

    #     response = requests.get(
    #         self.api_domain + f'/categories/{category_id}',
    #         params={'display': 'full'},
    #         headers={'Authorization': 'Bearer ' + self.api_key}
    #     )
    #     response_json = response.json()
    #     category_data = response.json()['category']
        
    #     parents = []
    #     while category_data['id_parent'] != '0':
    #         parent_id = category_data['id_parent']
    #         response = requests.get(
    #             self.api_domain + f'categories/{parent_id}',
    #             params={'display': 'full'},
    #             headers={'Authorization': 'Bearer ' + self.api_key}
    #         )
    #         category_data = response.json()['category']
    #         parents.append(category_data['name'])

    #     return parents


   
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_list_parent_categories_from_prestashop(id_category: int, dept: int = 0) -> list:
        """! @~russian Вытаскивет из базы данных Prestashop родительские категории от заданной 
        @details функция через API получает список категорий

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
            #     Category.get_list_parent_categories_from_prestashop(id_category)
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

    