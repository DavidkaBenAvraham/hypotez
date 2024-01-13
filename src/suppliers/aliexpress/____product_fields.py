"""! @ru_brief Интерфейс product <--> api Prestashop

@ru_details brief  Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
1. Заполняю поля, необходимые для создания нового товара
2. Получаю `id_product` созданного товара
3. Используя полученный `id_product` загружаю дефолтную картинку
4. итд.


 @section libs imports:
  - typing 
  - time 
  - gs 
  - helpers 
  - tools 
  - product 
  - suppliers 
  - api_aliexpress 
  - aliexpress 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import asyncio
from typing import Union
import time
# ----------------------------
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator, jprint, pprint
from src.tools import StringFormatter as SF, StringNormalizer as SN
from src.product import Product, ProductFields
from src.suppliers import Supplier
from src.webdriver import execute_locator

#from .iop import *

#api_aliexpress = AliexpressApi(gs.api_aliexpress['key'], gs.api_aliexpress['secret'], models.Language.EN, models.Currency.EUR, gs.api_aliexpress['tracking_id'])

#from aliexpress import iop
# ----------------------------



def fill(s:Supplier, f:ProductFields) -> ProductFields:
    """ добавляю поля в таблицу, 
    которые могут по разному наполняться ( в зависимости от строения локатора) 
   
    
    Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
    1. (->) Добавляю поля, необходимые для создания нового товара
    2. (<-) Получаю `id_product` созданного товара
    3. (->) Используя полученный `id_product` загружаю дефолтную картинку и другие элементы
            в новый товар
    4. итд.
    """

    _d = s.driver
    _l = execute_locator.reread_locators(s, 'product')



    def set_price(s, format: str = 'str') -> Union[str,float]:
        """! @ru_brief Привожу денюшку через флаг `format` 
        @ru_details к: 
        - [ ] float 
        - [v] str
        """
        #l = s.reread_locators('product')
        try:
            raw_price = _d.execute_locator ( _l ['price']['new'] )[0]
            ''' raw_price получаю в таком виде:
            ILS382.00\nILS382\n.\n00
            '''
            raw_price = str (raw_price).split ('\n')[0]
            return SN.normalize_price (raw_price)
        except Exception as ex:
            logger.error (ex)
            return False

   

    ASIN = asyncio.run ( _d.execute_locator (_l ['ASIN'] ))
    f.reference = f'{s.supplier_id}-{ASIN}'
    f.supplier_reference = ASIN
    f.price = set_price (s, format = 'str')
    f.name = _d.execute_locator (_l ['name'] )[0]
    f.images_urls = _d.execute_locator (_l ['Image URLs (x,y,z...)'] )[0]
    try:    
        #f.description_short = _d.execute_locator (_l ['description_short'] )[0]
        f.description_short = _d.execute_locator (_l ['description_short'] )[0]
    except Exception as ex:
        logger.error(ex)
        return False

    f.id_supplier = s.supplier_id
        
    affiliate = _(l['affiliate_short_link'])
    affiliate = affiliate[1][0]
    f.affiliate_short_link = affiliate

    f.link_rewrite = f.reference
    #TODO: неправильно сделано!!!!
    return f


def aliapi_to_prestashop(s, products_urls:list = None) -> bool:
    

    #iop_client = iop.IopClient()
    #iop.request

    products_obj_list = api_aliexpress.get_products_details(products_urls)
    
    for p in products_obj_list:
        f = ProductFields()
        prduct_id = p.product_id
        
        f.supplier_reference = p.shop_id
        f.reference = f'{p.shop_id}-{p.product_id}'
        f.price = p.app_sale_price
        f.name = p.product_title
        f.description_short = p.product_title
        f.id_supplier = s.supplier_id
        f.affiliate_short_link = p.promotion_link

        image_url = p.product_main_image_url


        f.id_default_image = p.product_main_image_url

        
    return f


