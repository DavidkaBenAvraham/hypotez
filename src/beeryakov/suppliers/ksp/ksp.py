"""  [File's Description]

@namespace src: src
 \package beeryakov.suppliers.ksp 
 
\file ksp.py
 @section libs imports:
  - json 
  - webdriver 
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""
import json
from src.webdriver import execute_locator

with open('suppliers\\ksp\\locators.json', 'r',  encoding='utf-8') as f:
    locators = json.load(f)

def get_worlds():
    worlds = execute_locator(locators['worlds'])
    worlds_dic: dict = {}
    for world in worlds:
        worlds_dic.update(world)
    # with open('suppliers\\ksp\\worlds.json','w') as f:
    #     json.dump(worlds_dic, f)
    
    return worlds_dic

def get_subs_from_world():
    subs = execute_locator(locators['subs_from_worlds'])
    subs_dic: dict = {}
    for sub in subs:
        subs_dic.update(sub)
    return subs_dic

def get_all_brands_list():
    execute_locator(locators['open_full_brands_list'])
    brands_list: list = str(execute_locator(locators['get_brands_list'])[0]).split('\n')
    brands_dict: dict = dict(zip(brands_list[::2], brands_list[1::2]))
    return brands_dict


def get_product(url: str = 'https://ksp.co.il/web/item/227307') -> dict:
    pass
