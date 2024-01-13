"""! @brief   [File's Description]


@namespace src: src
 \package src.suppliers.kualastyle
\file update_product_fields.py
 
 @section libs imports:
  - typing 
  - time 
  - gs 
  - helpers 
  - tools 
  - product 
  - suppliers 
  
Author(s):
  - Created by [Name] [Last Name] on 08.11.2023 .
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
import time
# ----------------------------
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator,  jprint, pprint
from src.tools import StringFormatter as SF, StringNormalizer as SN
from src.product import Product, ProductFields
from src.suppliers import Supplier
# ----------------------------

def set_product_fields(s:Supplier,f:ProductFields) -> Union[ProductFields, False]:
    """ добавляю поля, которые могут по разному наполняться ( в зависимости от строения локатора) """
    

    """ Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
    1. Добавляю поля, необходимые для создания нового товара
    2. Получаю `id_product` созданного товара
    3. Используя полученный `id_product` загружаю дефолтную картинку
    4. итд.
    """
    l = s.reread_locators('product')
    _ = s.driver.execute_locator
    reference = _(l['reference'])[0]
    reference = SF.clear_numbers(reference)
    f.reference = f'{s.supplier_id}-{reference}'
    f.supplier_reference = reference
    raw_price = _(l['price'])[0]
    f.price = SN.normalize_price(raw_price)
    try:
        name = _(l['name'])[0]
    except Exception as ex:
        logger.error(ex)
        return False
    #TODO: КОСТЫЛЬ!!!!!


    f.name = SF.remove_line_breaks(name)
    f.images_urls = _(l['Image URLs (x,y,z...)'])[0]
    #f.description_short = _(l['description_short'])[0]
    #f.description = _(l['description'])
        
    affiliate = _(l['affiliate_short_link'])
    #affiliate = affiliate[1][0]
    f.affiliate_short_link = affiliate

    #f.link_rewrite = d.current_url.split(f'''/''')[-4]
    #f.link_rewrite = "test-link"
    return f


    pass
