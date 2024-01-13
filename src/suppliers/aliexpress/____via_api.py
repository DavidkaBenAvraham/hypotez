"""  [File's Description]

.
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import requests
import hashlib
import time
from pathlib import Path

#from .api_aliexpress import AliexpressApi, models
#""" отсюда https://github.com/sergioteula/python-aliexpress-api/ """

from src.settings import gs
from typing import Union
from src.suppliers import Supplier
from src.io_interface import j_loads as j_loads
from src.helpers import  logger as logger
import json


#def update_scenario_file_via_api(s: Supplier, current_scenario_filename: str)->bool:
#    """ Выполнение сценария через алиэкспресс API 
#    param: s - Supplier object
#    param: current_scenario_filename - имя файла сценария
#    """
#    print(current_scenario_filename)
#    _json = j_loads(Path(gs.dir_scenarios, f'''{current_scenario_filename}'''))
#    try:
#        s.scenarios = _json['scenarios']
#    except Exception as ex:
#        logger.error(f'''Ошибка чтения сценария из файла {current_scenario_filename}. {ex.with_traceback(ex.__traceback__)} ''')
#        return False

#    _store = _json['store']
    

#    store_categories = get_store_categories(_store['store_id'])

#    for category in store_categories:
#       links = aliapi.get_affiliate_links(f'''https://aliexpress.com/item/{category['groupId']}.html''')



#    #3. сверяю полученные категории с текущим списком s.scenarios из файла current_scenario_filename
#    list_categories_id_from_file = []
#    for _key , _scenario in s.scenarios.items(): 
#        #print(_scenario['category ID on site'])
#        list_categories_id_from_file.append(_scenario['category ID on site'])
#        ''' Создаю список ID категорий из s.scenarios '''
#        _scenario['active'] = True
#        _key
#        ''' делаю все категории активными '''

#    groupId_list = []
#    updated_scenarios = []
#    ''' список ID с сайта '''
#    for group in groups_dicts:
#        ''' Обновляю категории в файле сценария '''
#        groupId_list.append(group['groupId'])
#        if group['groupId'] not in list_categories_id_from_\file 
#            ''' Добавляю в сценарий новые категории на сайте магазина '''
#            _new_scenario = {group['name']:{
#                "category ID on site":group['groupId'],
#                "brand":_store['brand'],
#                "active": True,
#                "url":group['url'],
#                "condition":"",
#                "presta_categories":None
#                }}
#            s.scenarios.update(_new_scenario)
#            updated_scenarios.append(group['groupId'])


#    if len(updated_scenarios)>0:
#        """ Если были изменения в файле ссценариев - алармирую почтой """
#        msg = f'''
#        -------------------------------------------------
#        |   Файл сценариев {current_scenario_filename}  |
#        |   был дополнен сценариями:                    |
#        |   {updated_scenarios}                         |
#        -------------------------------------------------
#        '''
#        send(msg)
#        logger.info(msg)


#    disabled_categories = list(set(list_categories_id_from_file) - set(groupId_list))
#    if len(disabled_categories)>0:
#        for _key , _scenario in s.scenarios.items(): 
#            if _scenario['category ID on site'] in disabled_categories:
#                ''' Категории отключенные в магазине '''
#                _scenario['active'] = False

#    if not s.scenarios is None and len(s.scenarios) >0:
#        _json['scenarios'].update(s.scenarios)
#        json_dump(_json,Path(gs.dir_scenarios, f'''{current_scenario_filename}'''))


#    return True

#def update_products(s: Supplier):
#    def AliexpressSolutionProductListGetRequest(app_key='', app_secret='',domain='gw.api.alibaba.com', port=80, category_ids=-1, page_no=1, page_size=10):
#        # Implementation of the function here

#        # Generate a timestamp for the request
#        timestamp = str(int(time.time() * 1000))

#        # Generate a signature for the request using the app_secret and timestamp
#        sign_str = app_secret + "aliexpress.gw.api.alibaba.com" + "/api/aliexpress/getProductList" + timestamp
#        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()

#        # Build the request headers with the required parameters
#        headers = {
#            'Content-Type': 'application/json',
#            'Authorization': f"APPCODE {app_key}",
#            'x-ca-timestamp': timestamp,
#            'x-ca-signature': sign
#        }

#        # Build the payload dictionary with the required parameters
#        payload = {
#            'categoryId': category_ids,
#            'pageNo': page_no,
#            'pageSize': page_size,
#            'app_secret': app_secret,
#            'api_key': api_key
#        }
#        #p = api_aliexpress.get_products_from_category(category_ids = str(category_ids),  page_no = page_no, page_size = page_size)
#        # Make a request to the AliExpress API to retrieve a list of products for the specified category and page
#        response = requests.get(f"http://{domain}:{port}/api/aliexpress/getProductList", headers=headers, params=payload)
#        response = requests.get(f"http://{domain}:{port}/api/aliexpress/getProductList",  params=payload)

#        # Check if the request was successful
#        if response.status_code == 200:
#            # Extract the list of products from the response
#            product_list = response.json()
#            # Do something with the list of products
#            logger.info(product_list)
#        else:
#            logger.error(f"Error: {response.status_code}")
#            return False





#    domain = 'gw.api.alibaba.com'
#    port = 80
#    category_ids = 0 # replace with the ID of the category you want to retrieve
#    page_no = 2 # replace with the page number you want to retrieve
#    page_size = 20 # replace with the number of products per page you want to retrieve
#    api_key = API_KEYS_ALIEXPRESS['key']
#    app_secret = API_KEYS_ALIEXPRESS['secret']
#    for _key, _scenario in s.scenarios.items():
        
#        # Call the function to retrieve the list of products for the specified category and page
#        if not AliexpressSolutionProductListGetRequest(api_key, app_secret, domain, port, _scenario['category ID on site'], page_no=page_no, page_size=page_size):
#            return False

def get_affiliate_links(url:list=None)->list:
    """Получаю линк на товар и возвращаю партнерскую ссылку полученную через API """
    return aliapi.get_affiliate_links(url)

def get_store_categories(store_id):

    # 1.а Устанавливаею параметры запроса
    payload = {
        'storeId': store_id
    }
    url = 'https://www.aliexpress.com/store/productGroupsAjax.htm'

    #1.б response
    response = requests.post(url, data=payload)
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
    

def get_affiliate_links(url:list=None)->list:
    """Получаю линк на товар и возвращаю партнерскую ссылку полученную через API """
    return aliapi.get_affiliate_links(url)

def get_store_categories(store_id):

    # 1.а Устанавливаею параметры запроса
    payload = {
        'storeId': store_id
    }
    url = 'https://www.aliexpress.com/store/productGroupsAjax.htm'

    #1.б response
    response = requests.post(url, data=payload)
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
    
