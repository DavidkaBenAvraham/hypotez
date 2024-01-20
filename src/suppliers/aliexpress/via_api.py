"""! @~russian  API Scenario


 @section libs imports:
  - gs (link)
  - typing (link)
  - suppliers (link)
  - io_interface (link)
  - helpers (link)
  - json (link)
  - aliexpress_api (link)
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
from pathlib import Path
from typing import Union
from src.settings import gs
import re
from requests import get, post
from typing import Union
from src.helpers import logger, logs_and_errors_decorator, beeper
from src.io_interface import jjson
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.io_interface import j_loads, j_dumps, file
from src.helpers import  logger, pprint, jprint
import json

_credentials = gs.default_aliexpress_api_credentials

from aliexpress_api import AliexpressApi, models
aliapi = AliexpressApi(_credentials['api_key'], _credentials['secret'], models.Language.EN, models.Currency.EUR, _credentials['tracking_id'])
"""! @todo переделать валюту. Там надо в код лезть 
исходник тут https://github.com/sergioteula/python-aliexpress-api
"""
pass


# def run_scenario(s: Supplier) -> bool:
#     """! @~russian запускаю сценарии на исполнение
#     @param s `Supplier` поставщик.
#     @returns bool: Возвращает True в случае успеха, иначе False.
#     """
#     for scenario_file_path in s.scenario_files:
#         scenario = j_loads(scenario_file_path)[0]
#         logger.info (jprint (scenario) )
#         #aliexpress
#     pass

#@logs_and_errors_decorator (default_return =  False)
def aliapi_get_products (products_urls: Union [list[str], str]) -> list [dict]:
    """! @~russian Функция извлекает данные о товарах 
    @details Функция получает на вход список из URL, собранных спайдером,
    вытаскивает id_product и получает детализированное инфо от aliexpress api
    """
    def extract_item_value (product_url: str) -> str:
        """! @~russian Функция для извлечения id из URL 
        @details в URL https://he.aliexpress.com/item/1005005010835970.html
        id =1005005010835970
        @param product_url `str` Первый раз приходят сырые URL, в рекурсии приходят отфильтрованные id
        """
        match = re.search (r'item/(\d+).html', product_url)
        if match:
            """! @~russian _rem Сырой URL """
            return str (match.group(1) )
        else:
            """! @~russian _rem отфильтрованный id """
            return product_url

    # Фильтрация списка URL
    product_ids : list = set ( [extract_item_value (product_url) for product_url in products_urls] )
    """! @~russian _rem Очищаю список для получения id товара """
    
    # products_details_list = [product for product in ali_api.get_products_details(product_ids)]
    # """! @~russian _bug НЕЛЬЗЯ генератором!
    # Периодически падает на таймаут коннектора """
    products_details_list: list = []
    _failed_products_list: list = []
    _count_products_details_list = len(product_ids)
    for product_id in product_ids:
        try:
            logger.info (f' -> Шлю api запрос на товар : {product_id}' )
            product_details :dict  = ali_api.get_products_details  (product_id) [0]
            products_details_list.append (product_details )
            logger.info (f' <- Товар: {product_id} получен' )
            _count_products_details_list -= 1
            if _count_products_details_list <1:
                logger.info('Собрал все. отдаю результат')
                return products_details_list
            logger.info (f' осталось : {_count_products_details_list} товаров')
            
            if len(_failed_products_list) > 0:
                if product_id in _failed_products_list:
                    """! @~russian _rem В случае успеха убираю id из списка упавших запросов """
                    _failed_products_list.remove (product_id)
                    
                logger.error(f'- Упавшие запросы: {_failed_products_list}')
            
        except Exception as ex:
            _failed_products_list.append (product_id)
            beeper.beep('long_error')
            logger.error(f'''Алиехпресс не ответил на запрос {product_id}
            Ошибка {ex}
            Все упавшие {_failed_products_list}''')
            


    if len(_failed_products_list) > 0:
        _attempts: int = 0
        while _attempts < 3:
            logger.error(f'''Поворяю для упавших запросов {_failed_products_list}''')
            aliapi_get_products(_failed_products_list)
            _attempts += 1
        
    return products_details_list

#@logs_and_errors_decorator (default_return =  False)
def aliapi_to_prestashop(s, products_urls: Union [list [str], str]) -> bool:
    """! @~russian интерфейс перевода полей api aliexpress в поля api prestashop"""
    
    aliapi_products_details = aliapi_get_products (products_urls)
    for product in aliapi_products_details:
        for key, value in product:
            print( key, value)
        file.save_text_file (str(product), Path (gs.dir_temp, f'{product.product_id}.json'))
    pass
    # for p in products_details:
    #     f = ProductFields()
    #     prduct_id = p.product_id
        
    #     f.supplier_reference = p.shop_id
    #     f.reference = f'{p.shop_id}-{p.product_id}'
    #     f.price = p.app_sale_price
    #     f.name = p.product_title
    #     f.description_short = p.product_title
    #     f.id_supplier = s.supplier_id
    #     f.affiliate_short_link = p.promotion_link

    #     image_url = p.product_main_image_url


    #     f.id_default_image = p.product_main_image_url

        
    # return f

#@logs_and_errors_decorator (default_return =  False)
def aliapi_get_affiliate_links(url:list=None)->list:
    """Получаю линк на товар и возвращаю партнерскую ссылку полученную через API """
    return aliapi.get_affiliate_links(url)

#@logs_and_errors_decorator (default_return =  False)
def get_store_categories(store_id):

    # 1.а Устанавливаею параметры запроса
    payload = {
        'storeId': store_id
    }
    url = 'https://www.aliexpress.com/store/productGroupsAjax.htm'

    #1.б response
    response = post(url, data=payload)
    """ отправляю POST-запрос с параметрами 
    успешный ответ возвращаеет 200 и словарь ответа через response.json() 
    """
    if response.status_code != 200:
        logger.error(f''' Не получил responce от aliexress.
           responce: {response} ''')
        return False

    
    def build_dict_from_json(json_data:json, result=[])->list:
        """ рекурсивная функция, которая вытаскивает из json список узлов категорий 
        в терминах полученого json категория - group
        если в категории есть подкатегории, они находятся в списке subGroupList
        Я могу передавать значения в result, в таком случае данные допишутся в конец переданных

        Attrs:
            json_data (_json_): 
            result (_list_):

        @returns
            result
        """

        for group in json_data:
            if isinstance(group,str) and str(group).lower() == 'groups':
                """ 
                Какая - то хуйня на али. Приходят разные форматы. 
                Иногда категории находятся в списке groups,
                а иногда в корне
                """
                return build_dict_from_json(json_data[group])

            elif 'subGroupList' in group and len(group['subGroupList'])>0:
                """ в узле есть подкатегории """
                build_dict_from_json(group['subGroupList'] , result)
            else:
                """ запихиваю в словарь """
                group_dict = {
                    'groupId': group['groupId'], 
                    'name': group['name'], 
                    'url': group['url']
                    }
                #print(group_dict)
                result.append(group_dict)
        return result

    return build_dict_from_json(response.json())
    
