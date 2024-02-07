"""! @brief   Собиратель данных со страницы HTML товара

 
 @section libs imports:
  - typing 
  - json 
  - src.gs 
  - src.gs 
  - src.tools 
  - src.product 
  
"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

""" Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
1. Заполняю поля, необходимые для создания нового товара
2. Получаю `id_product` созданного товара
3. Используя полученный `id_product` загружаю дефолтную картинку
4. итд.
"""

from typing import Union
import json
# ----------------------------
from src.settings import gs
from src.helpers import logger, logs_and_errors_decorator, jprint, pprint
from src.tools import SF, SN
from src.prestashop import Product as PrestaProduct
from src.webdriver import execute_locator
# ----------------------------




def grab(s, id_product: int = 0 , api_method: Union[str('V1'),str('V2'),str('V3')] = 'V3') -> ProductFields:
    """! @~russian  Я добавляю в базу данных престашоп товар 
    путем нескольких последовательных действий:
        1. Добавляю поля, необходимые для создания нового товара
        2. Получаю `id_product` созданного товара
        3. Используя полученный `id_product` загружаю дефолтную картинку
        4. итд.
    ПОКА ТОЛЬКО ДЛЯ НОВЫХ!!!!! СТРАНИЦ
        Собираю информацию со страницы товара. 
        Важно помнить, что драйвер уже должен быть на
        этой странице
        ---------------
    Parameters : 
         s : Supplier
         id_product : int = 0 : if `id_product` == 0  new product
         api_method : Union[str('V1'),str('V2'),str('V3')] = 'V3' : [description]
    Returns : 
         ProductFields : f (ProductFields) с заполненными полями, else False

    """

    execute_locator.reread_locators(s, 'product')
    """! @~russian _remark Если в локаторе встречается функция - она портит содержимое локатора, 
    поэтому я периодически перечитываю оригинал из файла локаторов """
    
    d = s.driver
    #_l = d.execute_locator
    """ Здесь не место для локаторов. Здесь устанавливаются поля по умолчанию """
    f: ProductFields = ProductFields(s)

    
    f = s.related_modules.product_fields.fill (s, f )

    f.id_supplier = s.supplier_id
    '''
    Тут я вытаскиваю id_supplier
    '''    
    if not f:
        return False

    """ 
    Устанавливаю defaults
    Set defaults for product of supplier 
    """
    f.active = 1
    f.on_sale = 1
    f.min_qty = 1
    f.low_stock_level = 0
    f.low_stock_threshold = ''
    f.show_price = 1
    f.show_condition = 1
    f.aviable_online_only = 0
    f.advanced_stock_management = 0
    f.state = 1

    """ Категории """

    _category_default = list (s.current_scenario ['presta_categories']['default_category'].keys() )[0]
    f.id_category_default: int = _category_default
    _category_ids: list = [ _category_default ]
    _parents = Product.get_parent_categories ( _category_default )


    if isinstance ( _parents, list ):
        #  Если `_parents` не пустой (заполненный списком иерархии категорий)
        _category_ids.extend ( _parents )
    else:
        # Если элемент не является списком, добавляем его, как есть, в общий список
        _category_ids.append (_parents)
        

    if 'additional_categories' in s.current_scenario ['presta_categories'].keys():
        ''' В сценарии может быть указано несколько категорий.
        они описаны в `additional_categories`
        '''
        
        keys_list = [list ( item.keys() )[0] for item in s.current_scenario ['presta_categories']['additional_categories']]        
        for id_category in keys_list:
            _category_ids.append (id_category)
            _parents = Product.get_parent_categories ( id_category, 2 )
            if isinstance ( _parents, list ):
                _category_ids.extend ( _parents )
            else:
                # Если элемент не является списком, добавляем его как есть в общий список
                _category_ids.append (_parents)

    f.category_ids = list (set (_category_ids ) )




    if id_product == 0: # new product

        check = Product.check_if_product_in_presta_db (f.reference)
        
        if not check  is False:
            pass
       
        product_dict = f.product_dict

        print ("---------------------NEW PRODUCT-----------------------")
        response = Product.add_2_prestashop (product_dict, api_method)
        if not response:
            return False
        if 'errors' in response.keys():
            pprint(response)
            return False

        product = response['product']
        id_product = product['id']
        print ( "---------------------NEW PRODUCT ID-----------------------" )
        print ( id_product )
        
        img = upload_image (id_product, f.images_urls)
        return product, img


    return f

def upload_image(id_product: int, image_url: str) -> ProductFields:
    """
     
    После того, как я занес новый товар в бд - я получу его id
    Далее я гружу картинку и получаю ее id
    Далее я догружаю остальные картинки
    ----------------------

    Parameters : 
         id_product : int : product id \n
        (`id_product`) - переменная в формате престасашоп. \n
        Поскольку преста оперирует разными сущностями \n
        такими как товар, категория, магазин ит.п. названия переменных начинаются с id_
         image_url : str : url картинки
    Returns : 
         ProductFields : [description]

    """

    img = Product.upload_product_default_image (
        id_product, 
        image_url)
    return img
        
  
    pass
