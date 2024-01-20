"""! aliexpress.com - модуль выполнения сценариев через вебдрайвер
@details Модуль делает:

- Собирает список категорий со страниц продавца . `get_list_categories_from_site()`.
@todo Сделать проверку на изменение категорий на страницах продавца. 
Продавец может добавлять новые категории, переименовывать или удалять/прятать уже существующие. 
По большому счету надо держать таблицу категории `prestashop.categories <-> aliexpress.shop.categoies`

- Собирает список товаров со страницы категории `get_list_products_in_category()`
- Обрабатывает поля товара `grab_product_page()`
 @section libs imports:
  - typing 
  - pathlib 
  - gs 
  - helpers 
  - api_aliexpress 
  @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from typing import Union
from pathlib import Path
import re
import asyncio
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
from .via_api import aliapi_to_prestashop
from .grabber import grab_product_page
from src.io_interface import j_loads, j_dumps
from src.prestashop import Product as PrestaProduct



    ##########################################################################
    #                                                                        #
    #   переменная `s` на протяжении всего кода обозначает класс `Supplier`  #
    #                                                                        #
    ##########################################################################

#@logs_and_errors_decorator(default_return=False)
def grab_product_pages(s, product_page_url_list: Union[list[str], str]) -> Union[list[dict], dict, False]:
    results = []
    for product_url in product_page_url_list if isinstance(product_page_url_list, list) else [product_page_url_list]:
        s.driver.get_url(product_url)
        results.append(grab_product_page(s))
    return results

    


#@logs_and_errors_decorator(default_return=False)
def get_list_products_in_category(s) -> Union[list[str], str]:
    """! @~russian 
    @brief Считывает URL товаров со страницы категории.

    @details Если есть несколько страниц с товарами в одной категории - листает все.
    Важно понимать, что к этому моменту вебдрайвер уже открыл страницу категорий.

    @param s `Supplier` - экземпляр поставщика
    @param run_async `bool` - устанавливает синхронность/асинхронность исполнения функции `async_get_list_products_in_category()`

    @returns list_products_in_category `list` - список собранных URL. Может быть пустым, если в исследуемой категории нет товаров.
    """
    
    return get_prod_urls_from_pagination (s)
        

#@logs_and_errors_decorator(default_return=False)
def get_prod_urls_from_pagination(s) -> list[str]:
    """! @~russian @brief Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    
    _d = s.driver
    _l: dict = s.locators['category']['product_links']
    
    list_products_in_category: list = _d.execute_locator(_l)
    
    if not list_products_in_category:
        """! В категории нет товаров. Это нормально """
        return []

    while True:
        """! @todo Опасная ситуация здесь/ Могу уйти в бесконечный цикл """
        if not _d.execute_locator (s.locators ['category']['pagination']['->'] ):
            """! @~russian _rem Если больше некуда нажимать - выходим из цикла """
            break
        list_products_in_category.extend(_d.execute_locator(_l ))
   
    return list_products_in_category if isinstance(list_products_in_category, list) else [list_products_in_category]



#@logs_and_errors_decorator(default_return=False)
def check_product_presence_in_prestashop(list_products_in_category):
    """! @~russian 
    @brief Проверяю наличие товара в базе `Prestashop`. 
    Если такой товар уже есть в бд, проверяю изменения
    @details Если есть измения в товаре - заношу в историю параметры существующего товара
    и обновляю поля товара актуальными значениями
    """
 

    # Паттерн регулярного выражения для извлечения значения между "item/" и ".html"
    pattern = re.compile(r'item/(\d+).html')

    dict_products_from_ali = {}
    """! @~russian функция создает словарь с параметрами товара.
    @details Начало подготовки товара для клиента (`Pestashop`)
    В дальнейшем словарь будет пополнятся новыми ключами """

    for url in list_products_in_category:
        match = pattern.search(url)
        if match:
            item_id = match.group(1)
            dict_products_from_ali.update ({item_id: url})
            
    dict_products_from_ali = PrestaProduct.check_prod_presence (dict_products_from_ali.keys)
    """~@~russian отдаю список `ID` товаров на проверку в `PrestaProduct` """

    
  

# Сверяю файл сценария и текущее состояние списка категорий на сайте 
#@logs_and_errors_decorator(default_return =  False)
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """@~russian @brief Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен """
    
    scenario_json = j_loads(Path(gs.dir_scenarios, f'''{scenario_filename}'''))
    scenarios_in_file = scenario_json['scenarios']
    categoris_on_site = get_list_categories_from_site()

    all_ids_in_file:list=[]
    def _update_all_ids_in_file():
        for _category in scenario_json['scenarios'].items():
            if _category[1]['category ID on site'] > 0:
                # здесь может упасть, если значение 'category ID on site' не определено в файле
                all_ids_in_file.append(_category[1]['category ID on site'])
            else:
                url = _category[1]['url']
                cat = url[url.rfind('/')+1:url.rfind('.html'):].split('_')[1]
                _category[1]['category ID on site']:int = int(cat)
                all_ids_in_file.append(cat)
        #json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

    _update_all_ids_in_file()

    response = requests.get(scenario_json['store']['shop categories json file'])
    ''' получаю json категорий магазина '''
    if response.status_code == 200:
        categories_from_aliexpress_shop_json = response.json()
    else:
        logger.error(f''' Ошибка чтения JSON  {scenario_json['store']['shop categories json file']}
        response: {response}''')
        return False
    

  
    """!
    Следующий код производит сравнение списка идентификаторов категорий all_ids_in_file с current_categories_json_on_site,
    идентификаторами категорий, полученными с текущей версии сайта в формате JSON 

    В первой строке кода, из current_categories_json_on_site извлекается список групп категорий и сохраняется в переменной groups.
    Далее создаются два пустых списка all_ids_on_site и all_categories_on_site, которые будут заполняться идентификаторами и категориями в формате словаря, полученными с сайта.
    Для каждой группы в groups, если у нее нет подгрупп (т.е. длина списка subGroupList равна 0), 
    то идентификатор и сама категория добавляются в соответствующие списки all_ids_on_site и all_categories_on_site. 
    Если же у группы есть подгруппы, то для каждой подгруппы производится аналогичное добавление в списки.
    Затем код создает два списка: removed_categories и added_categories. 
    В removed_categories добавляются идентификаторы категорий из списка all_ids_in_file, которые не нашли соответствие в all_ids_on_site. 
    В added_categories добавляются идентификаторы категорий из all_ids_on_site, которых нет в all_ids_in_file.
    Итого, removed_categories и added_categories содержат различия 
    между списками идентификаторов категорий на сайте и в файле, соответственно.
    """
    
    groups = categories_from_aliexpress_shop_json['groups']
    all_ids_on_site:list=[]
    all_categories_on_site:list=[]
    for group in groups:
        if len(group['subGroupList'])==0:
            all_ids_on_site.append(str(group['groupId']))
            all_categories_on_site.append(group)
        else:
            for subgroup in group['subGroupList']:
                 all_ids_on_site.append(str(subgroup['groupId']))
                 all_categories_on_site.append(subgroup)

    removed_categories  = [x for x in all_ids_in_file if x not in set(all_ids_on_site)]
    added_categories = [x for x in all_ids_on_site if x not in set(all_ids_in_file)]



    if len(added_categories)>0:
        for category_id in added_categories: 
            category = [c for c in all_categories_on_site if c['groupId'] == int(category_id)]
            category_name = category[0]['name']
            category_url = category[0]['url']
            categories_in_file.update({category_name:{
                    "category ID on site":int(category_id),
                    "brand":"",
                    "active": True,
                    "url":category_url,
                    "condition":"",
                    "prestashop_categories":""
                    }})
        scenario_json['scenarios'] = categories_in_file
        json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

        post_subject = f'''Добавлены новые категории в файл {scenario_filename}'''
        post_message = f'''
        В файл {scenario_filename} были добавлены новые категории:
        {added_categories}
        '''
        send(post_subject,post_message)


    if len(removed_categories)>0:
        for category_id in removed_categories: 
            category = [v for k,v in categories_in_file.items() if v['category ID on site'] == int(category_id)]
            if len(category) == 0:continue
            category[0]['active'] = False
        
        scenario_json['scenarios'] = categories_in_file
        json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

        post_subject = f'''Отлючены категории в файле {scenario_filename}'''
        post_message = f'''
        В файл {scenario_filename} были отключены категории:
        {removed_categories}
        '''
        send(post_subject,post_message)
    return True

#@logs_and_errors_decorator(default_return =  False)
def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    pass