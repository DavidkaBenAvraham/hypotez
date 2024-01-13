# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import json
from pathlib import Path

import settings 
json_loads = settinglobal_settings.json_loads
json_dump = settinglobal_settings.json_dump

from strings_formatter import StringFormatter as SF
from src.suppliers import Supplier
from src.suppliers.Product import Product 
import suppliers.execute_scenarios as execute_scenarios
## list products from pagination
def list_products_in_category_from_pagination(s,scenario):
    ''' листалка '''
    
    _d = s.driver
        _l : dict = s.locators['category']['product_links']

    list_products_in_category : list = _d.execute_locator(_l)
    
    if not list_products_in_category: return False
    ''' В этой категории нет товаров. Это нормально '''
    
    while True:
        perv_url = _d.current_url
        _d.execute_locator(s.locators['pagination']['->'])
        if perv_url == _d.current_url:
            ''' если больше некуда нажимать - выхожу '''
            break
        list_products_in_category.append(_d.execute_locator(_l))
   
            

    if isinstance(list_products_in_category,str):
        ''' Даже если я получил всего один товар - возвращаю список '''
        _ret:list = []
        _ret.append(list_products_in_category)
        return _ret
    else:
       return list_products_in_category

def get_list_products_in_category(s, scenario):
    l = list_products_in_category_from_pagination(s,scenario)

    # Affiliate links
    try:
        # 1. Проверяю наличие товара в базе данных сайта через PRESTASHOP API

        #affiliate_links = api_aliexpress.get_affiliate_links(l)
        pass
    except Exception as ex:
        logger.error(ex)
    return l



# Сверяю файл сценария и текущее состояние списка категорий на сайте 
def update_categories_in_scenario_file(s,scenario_filename):
    scenario_json = json_loads(Path(settings.dir_scenarios, f'''{scenario_filename}'''))
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
    

  
    """
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
        json_dump(scenario_json,Path(settings.dir_scenarios, f'''{scenario_filename}'''))

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
        json_dump(scenario_json,Path(settings.dir_scenarios, f'''{scenario_filename}'''))

        post_subject = f'''Отлючены категории в файле {scenario_filename}'''
        post_message = f'''
        В файл {scenario_filename} были отключены категории:
        {removed_categories}
        '''
        send(post_subject,post_message)
    return True

def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(settings.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    pass