"""! @~russian  Kласс категории товара в `Prestashop`

 @details `Categoty` слой между категориями клиента (Prestashop, в моем случае) и поставщика
 
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
import requests
# ----------------------------------


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
from src.prestashop import  PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
from .images_exec import upload_image
# --------------------------------

class PrestaCategory(): 
    """! @~russian Класс категорий товара Prestashop """

    API_DOMAIN = gs.default_prestashop_api_credentials['API_DOMAIN']
    API_KEY = gs.default_prestashop_api_credentials['API_KEY']
                                                                                                                                                      
    def __init__(self,*args,**kwards) -> None:
        """! @~russian Класс категорий товара Prestashop """
        pass
   

    def get_category_id_by_name(self, category_name):
        response = requests.get(self.API_DOMAIN + 'categories', params={'filter[name]': category_name, 'display': 'full'}, headers={'Authorization': 'Bearer ' + self.API_KEY})
        category_data = response.json()['categories'][0]
        return category_data['id'] if category_data else None

    def add_category(category_name, parent_category_name=None, parent_category_id=2):
        data = {
            'name': category_name,
            'id_parent': parent_category_id,
        }

        if parent_category_name:
            parent_id = self.get_category_id_by_name(parent_category_name)
            if parent_id:
                data['id_parent'] = parent_id
            else:
                print(f"Parent category '{parent_category_name}' not found.")
                return

        response = requests.post(self.API_DOMAIN + 'categories', json={'category': data}, headers={'Authorization': 'Bearer ' + self.API_KEY})
        print(response.json())

    def delete_category(category_id):
        response = requests.delete(self.API_DOMAIN + f'categories/{category_id}', headers={'Authorization': 'Bearer ' + self.API_KEY})
        print(response.json())

    def update_category(category_id, new_name):
        data = {'name': new_name}
        response = requests.put(self.API_DOMAIN + f'categories/{category_id}', json={'category': data}, headers={'Authorization': 'Bearer ' + self.API_KEY})
        print(response.json())

    def get_list_parent_categories(category_id, category_name=None):
        if category_name:
            category_id = get_category_id_by_name(category_name)

        response = requests.get(self.API_DOMAIN + f'categories/{category_id}', params={'display': 'full'}, headers={'Authorization': 'Bearer ' + self.API_KEY})
        category_data = response.json()['category']
    
        parents = []
        while category_data['id_parent'] != '0':
            parent_id = category_data['id_parent']
            response = requests.get(self.API_DOMAIN + f'categories/{parent_id}', params={'display': 'full'}, headers={'Authorization': 'Bearer ' + self.API_KEY})
            category_data = response.json()['category']
            parents.append(category_data['name'])

        return parents

    # Пример использования функций:
    # add_category('New Category', 'Parent Category')
    # delete_category(3)  # Удалить категорию с ID=3
    # update_category(4, 'Updated Category Name')  # Обновить категорию с ID=4
    # print(get_list_parent_categories(5))  # Получить список родительских категорий для категории с ID=5
        



    
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_list_parent_categories(id_category: int, dept: int = 0) -> list:
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
            #     Category.get_list_parent_categories(id_category)
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

    