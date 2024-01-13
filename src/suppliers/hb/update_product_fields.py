"""! @brief  [File's Description]

@namespace src: src
 \package src.suppliers.hb
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
  - Created by Davidka  on 09.11.2023 .
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

def set_product_fields(s:Supplier, f:ProductFields) -> ProductFields:
    """! добавляю поля, которые могут по разному наполняться ( в зависимости от строения локатора) """
   
    """ Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
    1. Добавляю поля, необходимые для создания нового товара
    2. Получаю `id_product` созданного товара
    3. Используя полученный `id_product` загружаю дефолтную картинку
    4. итд.
    """

    _ = s.driver.execute_locator

    l = s.reread_locators('product')
    # ЕСЛИ НЕ ПЕРЕЧИТЫВАТЬ - ТО В ЛОКАТОРЕ ОСТАНУТСЯ УЖЕ ПЕРЕСЧИТАННЫЕ ЗНАЧЕНИЯ, А НЕ ПЕРЕМЕННЫЕ,
    # КОТОРЫЕ ВЫЧИСЛЯЮТСЯ ПО МЕСТУ
    # через этот интерфейс я перечитываю файл локатора s.reread_locators('product'), 
    # что дает мне возможность изменять локатор  в файле product.json во время тестов


    def set_price(s, format: str = 'str') -> Union[str,float]:
        """ Привожу денюшку к 
        [ ] float 
        [v] str
        """
        l = s.reread_locators('product')
        try:
            raw_price = _(l['price'])[0]
            raw_price = str(raw_price).split('\n')[0]
            return SN.normalize_price(raw_price)
        except Exception as ex:
            logger.error(ex)
            return False

   

    reference = _(l['reference'])
    f.reference = f'{s.supplier_id}-{reference}'
    f.supplier_reference = reference
    price = set_price(s, format = 'str')
    if not price: 
        return False
    f.price = price

    f.name = _(l['name'])[0]
    f.images_urls = _(l['Image URLs (x,y,z...)'])[0] if len (_(l['Image URLs (x,y,z...)'])[0])>0 else None
    f.url_default_image = _(l['url_default_image'])[0]

    try:    
        f.description_short = _(l['description_short'])[0]
    except Exception as ex:
        logger.error(ex)
        return False

    f.id_supplier = s.supplier_id
        
    affiliate = _(l['affiliate_short_link'])[0]
    f.affiliate_short_link = affiliate

    f.link_rewrite = f.reference
    #TODO: неправильно сделано!!!!

    
    return f
