# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

""" Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
1. Заполняю поля, необходимые для создания нового товара
2. Получаю `product_id` созданного товара
3. Используя полученный `product_id` загружаю дефолтную картинку
4. итд.
"""

from typing import Union
# ----------------------------
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator, jprint, pprint
from src.tools import SF, SN
from src.product import ProductFields
from src.suppliers import Supplier
# ----------------------------



#def grab_product_page(s: Supplier) -> Union[ProductFields,bool]:
#    def _set_name_brand(d,f) -> bool:

#        f.brand = d.execute_locator(l['Brand'])
#        pass

#    _set_name_brand(d,f)

#    #               """  SUMMARY,DESCRIPTION,REF DESCRIPTION,CONDITION  """
    
#    def _set_summary_description_meta(d,f) -> bool:
#        """ set the 
#        @returns
#    	"""
#        f.field_summary = d.execute_locator(l['Summary'])
#        f.field_specification = d.execute_locator(l['Specification'])
#        f.field_description = d.execute_locator(l['Description'])
#        f.field_refurbished_product_decription = d.execute_locator(
#            _l['Refirbished product description'])
#        if f.field_refurbished_product_decription is None:
#            f.field_condition = 'new'

#        pass

#    _set_summary_description_meta(d,f) 
        
        
        
#    #               SCREENSHOT                  #

#    try:
#        screenshot = d.execute_locator(l['Screenshot'])
#    except Exception as ex:
#        logger.exception(f"Ошибка", ex)

    
    
#    #           PRICE,QTY                   #
    
    
#    #try:
#    #    _price = d.execute_locator(l['Price tax excluded'])
#    #    if len(_price) == 0:
#    #        logger.error(f'''Промахнулся мимо цены.  
#    #        URL:{d.current_url}
#    #        LOCATOR: {_l['price']}''')
#    #        pass
#    #        #'''TODO: Это баг! '''
#    #    _price = SF.clear_price(_price)
#    #    if _price == 0:
#    #        logger.error(f'''Промахнулся мимо цены.  
#    #        {d.current_url}''')
#    #        #'''TODO: Это баг! '''
#    #        return False
#    #    f.field_cost_price = f.field_price_tax_exluded = f.field_price_tax_included = _price
#    #    f.field_qty = d.execute_locator(l['Quantity'])
#    #except Exception as ex:
#    #    logger.error(f"""Exception message - {ex.with_traceback()}""",ex)

    
    
#    #           AFFILIATE               #
    
#    try:
#        f.field_affiliate_short_link = d.execute_locator(l['affiliate_link'])[1]
#        f.field_affiliate_text = d.execute_locator(l['affiliate_img_HTML'])[1]
#        f.field_affiliate_summary = d.execute_locator(l['affiliate_iframe'])[1]
#    except Exception as ex:
#        logger.error(f'''  exception message ''',ex)
#    # """
#    # если локатор список, то ответ тоже будет списком
#    # """
   

#    ## set_delivery    
#    def _set_delivery():
#        _shipping = d.execute_locator(l['product_shipping_details'])
#        if 'FREE Shipping' in _shipping:
#            _field['shipping price'] = 0
#            return True
#        _field['shipping price'] = SF.clear_price(_shipping)
#        return True
   

   
#    def _set_images():
#        _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
#        _img_name = f'''{_field['sku']}.png'''
#        _field['img url'] =f'''{_http_server}/{_img_name}'''
#        screenshot = d.execute_locator(l['main_image_locator'])
#        s.save_and_send_via_ftp({_img_name:screenshot})
      
#    return f

def grab_product_page(s: Supplier):
    """ 
        Собираю информацию со страницы товара. 
        Важно помнить, что драйвер уже должен быть на
        этой странице
        ---------------
        Attrs:
            s (Supplier)
        @returns
            f (ProductFields) с заполненными полями, else False
    """


    l = s.reread_locators('product')
    d = s.driver
    f = ProductFields()
    _ = d.execute_locator
    product_dict: dict = {}
    product_dict['product']: dict = dict(f.fields)
    
    """ ID,ASIN,SKU,SUPPLIER SKU """
    

    def _set_defaults() -> bool:
        """ 
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

    def set_price(s, format: str = 'str') -> Union[str,float]:
        """ Привожу денюшку к 
        [ ] float 
        [v] str
        """

        #l = s.locators.get('product')
        #_ = s.driver.execute_locator  
          
        # ----------- Меняю значение селектора цены
        l['price']['selector'] = \
        "//div[contains(@data-csa-c-asin, '$_(driver.current_url.split(f'''/''')[-2])_$') and contains(@id, 'corePriceDisplay')]//span[1]"

        raw_price = _(l['price'])[0]
        raw_price = str(raw_price).split('\n')[0]
        return SN.normalize_price(raw_price)
    

    def fill_required_product_fields_4_new_product_in_database() -> Union[ProductFields, False]:
        """ Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
        1. Добавляю поля, необходимые для создания нового товара
        2. Получаю `product_id` созданного товара
        3. Используя полученный `product_id` загружаю дефолтную картинку
        4. итд.
        """

        _set_defaults()

        ASIN = _(l['ASIN'])
        #f.id_product = None
        f.reference = f'{s.supplier_id}-{ASIN}'
        f.supplier_reference = ASIN
        f.price = set_price(s, format = 'str')
        f.name = SN.symbols2UTF(_(l['name'])[0])
        #f.summary = _(l['summary'])[0]
        f.id_supplier = s.supplier_id
        f.id_category_default = list(s.current_scenario['presta_categories']['default_category'].keys())[0]
        f.state = 1
        affiliate = _(l['affiliate short link'])
        f.affiliate_short_link = affiliate[1][0]
        return f


    fill_required_product_fields_4_new_product_in_database()

