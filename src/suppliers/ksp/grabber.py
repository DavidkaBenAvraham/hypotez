"""! @brief  [File's Description]

 
 @section libs imports:
  - pathlib 
  - requests 
  - pandas 
  - selenium.webdriver.remote.webelement 
  - selenium.webdriver.common.keys 
  - strings_formatter 
  - gs 
  - suppliers.Product 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


#Documentation for this module
#           Функции, присущие поставщику  KSP, которыми я дополняю класс supplier

#import requests

#import json as json
#from strings_formatter import StringFormatter as SF
#from src.suppliers.product import Product 
#import suppliers.ksp.banners_grabber
#from pathlib import Path
#from src.helpers import logger as logger


from pathlib import Path
import requests
import pandas as pd


from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.keys import Keys
from strings_formatter import StringFormatter as SF
import settings 
logger = settings.logger
from src.suppliers.Product import Product 


def product_attributes(self, p, delimeter, elements):
    i=0
    skip = False
    c = p.combinations 
    ''' просто сокращенная запись '''
    for e in json.build_list_from_html_elements(self, delimeter, elements):
        if i%2 == 0:

            if not p.skip_row(e):
                '''
                -----^^^^^^^^^^   
                слова в колонке, которые надо пропустить находятся в файле
                PRESTA_product_combinations_sysnonyms_<lg>.json['skip']
                '''
                i+=1
                skip = True
                continue

            attr = SF.remove_HTML_tags(e)
            ''' первое значение '''
            if c["Attribute (Name:Type: Position)"] == "": c["Attribute (Name:Type: Position)"] = f'''{attr}:select:0'''
            else: c["Attribute (Name:Type: Position)"] += f''', {attr}:select:0'''
            ''' остальные значения '''
        else:
            if skip:
                i+=1        
                skip = False
                continue

            val = e.next
            if c["value (Name:Type: Position)"] == "":c["value (Name:Type: Position)"] = f'''{e.next}:select:0'''
            else: c["value (Name:Type: Position)"] += f''',{e.next}:select:0'''
        i+=1
        pass

def grab_product_page(s):
    p = Product(supplier = s)
    _ : dict = s.locators['product']
    _s = s
    _d = s.driver
    _field = p.fields
   
    _d.scroll(4)
    
    
    ''' Вытаскиваю со страницы товара все поля по локаторам
            ------------
        p - товар
    '''
    
    def set_id():
        _id = _d.execute_locator(_['sku_locator'])
        if isinstance(_id,list):
            _d.wait(.5)
            _id = _d.execute_locator(_['sku_locator'])
            ''' повторяю запрос - должен получить строку '''
            pass
        if _id is None:
            return False
        if 'm' in str(_id) or 'M' in str(_id): 
            return False #Скидки и прочая хуйня не нужная на данном этапе
        _field['id'] = _id
        return True
    def set_sku_suppl():
        _field['sku suppl'] = _field['id']
        return True
    def set_sku_prod():
        _field['sku'] = f'''{s.settings['supplier_id']}-{_field['id']}'''
        return True
    def set_title():
        title = _d.execute_locator(_['product_name_locator'])
        _field['title'] = SF.remove_special_characters(title)
        return True

    def set_summary():
        _field['summary'] = _d.execute_locator(_['summary_locator'])
        return True

    def set_description():
        _field['description'] = _d.execute_locator(_['description_locator'])
        return True

    def set_cost_price():
        _price = _d.execute_locator(_['price_locator'])
        '''  Может прийти все, что угодно  
        Например, товара больше нет в наличии - цены не будет
        '''
        if not _price or _price is None or len(_price)==0:
            return False
        if isinstance(_price, list):
            _price = _price[0]
        _price = _price.replace(',','')
        _price = SF.clear_price(_price)
        _field['cost price'] =  _price
        return True
    def set_before_tax_price():
        _field['price tax excluded']  = _field['cost price']

        return True

    def set_delivery():
        '''TODO  перенести в комбинации '''
        product_delivery_list = _d.execute_locator(_['product_delivery_locator'])
        #for i in product_delivery_list:
        #    pass


    def set_images():

        _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
        _img_name = f'''{_field['sku']}.png'''
        _field['img url'] =f'''{_http_server}/{_img_name}'''
        screenshot = _d.execute_locator(_['main_image_locator'])
        s.save_and_send_via_ftp({_img_name:screenshot})


       

    def set_combinations():
        '''комбинации/опции товара '''
        _comb_fields = p.combinations_fields

    def set_qty():pass

    def set_specification():pass

    def set_customer_reviews():pass

 
    def set_rewritted_URL():
        #_field['Rewritten URL'] = SF.set_rewritted_URL(_field['title'])
        _field['Rewritten URL']= _field['id']
        pass

    ''' Начинаю собирать данные продукта '''
    _ret = True
    if not set_id():
        _ret = False
    set_sku_suppl()
    set_sku_prod()
    set_title()
    set_summary()
    if not set_cost_price():
        _ret = False
    set_before_tax_price()
    set_delivery()
    set_images()
    set_combinations()
    #set_qty()
    #set_byer_protection()
    set_description()
    #set_specification()
    #set_customer_reviews()
    set_rewritted_URL()
    if _ret:
        return p
    else:
        logger.error(f'''
            Товар не записался
            Проверь адрес {_d.current_url}''')
        return False
    pass


# def get_list_products_in_category(s, scenario = None):
#     _d = s.driver
#     _l: dict = s.locators['product']
#         _l : dict = s.locators['category']['product_links']

#     _d.scroll(5)

#     list_products_in_category = s.driver.execute_locator(_l)
#     if isinstance(list_products_in_category,str):
#         return [list_products_in_category]
#     return list_products_in_category

# def update_categories_in_scenario_file(supplier,current_scenario_filename):
#     return True