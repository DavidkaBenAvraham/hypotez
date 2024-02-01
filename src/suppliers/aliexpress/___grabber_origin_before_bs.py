"""! @~russian  Собиратель данных со страницы товара

 @section libs imports:
  - gs 
  - product 
  - helpers 
  - tools 
  @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.settings import gs
from src.product import Product
from src.helpers import  logger, logs_and_errors_decorator
from src.tools import StringFormatter as SF
from .via_api import aliapi_to_prestashop
from src.suppliers import Supplier


def grab_product_page(s: Supplier) -> bool:
    """! @~russian Собираю данные со страницы товара
   @details При помощи локаторов собираю данные о товаре: название, описание, характеристики, отзывы

   @param s `Supplier` класс поставщика 
     - вебдрайвер должен быть установлен на странице товара. 
   - в моей учетной записи я вижу линейку "Affiliate links" - я беру из нее информацию о партнерской ссылке
    на али работает AJAX, это важно для сбора комбинаций! Они не передаются по URL
   
   """
    p = Product(supplier = s)
    _l : dict = s.locators['product']
    _d = s.driver
    _f = p.fields
 
    _d.scroll(3)

    ## combinations
    def combinations():
        """! @~russian У товара может быть насколько комбинаций. Функция вытаскивает все возможные
        @todo не проверена, я отложил реализацию на след версию
        """
        _l = s.locators['product']
        _comb_fs = p.combinations_fs
        _attr_position = 0

        def product_combinations():
            _type = s.current_scenario['product combinations']
            if not _type: return
            """! @~russian _rem у товара не всегда есть комбинации """

            __ = s.locators['product']['combinations']
            _comb_fs['Product ID'] = _f['id']
            _name = _d.execute_locator(__l['name'])
            _value = _d.execute_locator(__l['value'])
            
            _comb_fs['Attribute (Name:Type:Position)'] = f'''{_name}:{_type}:0'''
            _comb_fs['Value (Value:Position)'] = f'''{_value}:0'''
            _price = _d.execute_locator(_l['price_locator'])
            """! @~russian _rem получаю цену комбинации товара """
            
            _price = SF.clear_price(_price)

            _qty = _d.execute_locator(_l['qty_locator'])[0]
            _qty = SF.clear_price(_qty)



            ## форма комбинаций  в Prestashop
            # Attribute (Name:Type:Position)*
            # Value (Value:Position)*

            attr_name = _d.execute_locator(_title)
            attr_type = 'select'
            attr_position = _attr_position

            _combinations_fs['Attribute (Name:Type:Position)'] = f'''{attr_name}:{attr_type}:{attr_position}'''
        
            _vt = _d.execute_locator(_l['product_combinations_container_locator']['product_combinations_value_title'])
            _vp = _attr_position
            _combinations_fs['Value (Value:Position)'] = f'''{_vt}:{_vp}'''

                

            url_dict = _d.get_dict_from_urlstr()
            _combinations_fs['Supplier reference'] = _combina['Product reference'] = url_dict['params']['sku_id']
                
                
            _d.execute_locator(_l['product_name_locator'])

            _combinations_fs['Image URLs(x,y,z)'] = _d.execute_locator(_l['main_image_locator'])
            _combinations_fs['Quantity'] = _qty
            _combinations_fs['Wholesale price'] = _price

        try:
            _title = _l['product_combinations_container_locator']['product_combinations_title']
            _values_locator = _l['product_combinations_container_locator']['image_attribute_locator'] 
            _values = _d.execute_locator(_values_locator)
            if not _values:
                return False
            ''' нет комбинаций '''
            
            if isinstance(_values , list):
                ''' несколько вариантов товара'''
                for x in _values:
                    ''' нажимаю на каждую опцию товара '''
                    x.click()
                    product_combinations()
                    _combinot.apply(_combina)

            else:
                ''' один вариант '''
                _values.click()
                values()
                _combinot.apply(_combina)

            return True
        except Exception as ex: 
            
            logger.error(ex)
            return False

    def id():
        ''' на али работает AJAX это важно для комбинаций! Они не передаются по URL '''
        _f['id'] = _d.current_url.split('/')[-1].split('.')[0]
        _f['id'] = _d.execute_locator(_l['reference'])

    def sku_suppl():
        _f['sku suppl'] = _f['id']
        return True

    def sku_prod():
        _f['sku'] = f'''{s.settings['supplier_id']}-{_f['id']}'''
        return True

    def title():
        _f['title'] = _d.execute_locator(_l['product_name_locator'])
        _f['title'] = SF.remove_special_characters(_f['title'])
        if isinstance(_f['brand'],list):
            ''' Случай, когда у продавца все бренды слиты в одну категорию 
            В сценарии указан список брендов, а я выбираю из бенд из 'title'
            '''
            for b in _f['brand']:
                if b in _f['title']:
                    _f['brand'] = b
                    break
        return True
 
    ## price
    def cost_price():
        _price = _d.execute_locator(_l['price_locator'])
        if not _price or len(_price) ==0:
            _price = _d.execute_locator(_l['uniform-banner-box-price'])
            ''' цена может быть спрятана баннером. Ищу в баннере'''
        _price = SF.clear_price(_price)
        _f['cost price'] = _price
        return True
    
    def before_tax_price():
        _f['price tax excluded']  = _f['cost price']
    
    def description():
        '''
        многабукав
        try:
            _f['product_description'] = str(_d.execute_locator(_l['description_locator']))
            
            return True
        except Exception as ex: 
            _f['product_description'] = None
            logger.error(ex)
            return False
        '''


        #_f['product_description'] = _f['title']

        _f['product_description'] = _f['title']

    def specification():
        #_f['product_specification'] = _d.execute_locator(_l['specification_locator'])
        _f['product_specification'] = _f['product_description']
    def summary():
        _f['summary'] = _f['product_description']
    def delivery():

        #__ = _l['dynamic_shipping_block']
        #_d.execute_locator(__l['product_shippihg_locator_button'])
        #''' Открываю панель способов доставки '''
        #shipping_price = _d.execute_locator(__l['dynamic_shipping_titleLayout'])
        #dynamic_shipping_estimated = _d.execute_locator(__l['dynamic_shipping_estimated'])
        #dynamic_tracking_available = _d.execute_locator(__l['dynamic_tracking_available'])
        #close = _d.execute_locator(__l['close'])

        shipping_price = _d.execute_locator(_l['shipping_price_locator'])
        if 'Free Shipping' in shipping_price:
            _f['shipping price'] = 0
            return True
        _f['shipping price'] = SF.clear_price(shipping_price)
        return True



    def link():
        _f['link to product']= _d.current_url.split('?')[0]

    ## images
    def images():

        _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
        _img_name = f'''{_f['sku']}.png'''
        _f['img url'] =f'''{_http_server}/{_img_name}'''
        screenshot = _d.execute_locator(_l['main_image_locator'])
        s.save_and_send_via_ftp({_img_name:screenshot})

    def qty():
        try:
            _qty = _d.execute_locator(_l['qty_locator'])[0]
            _f['qty'] = SF.clear_price(_qty)
            _f['tavit im bemlay'] = _f['qty']
            return True
        except Exception as ex: 
            #field['qty'] = None
            logger.error(ex)
            return False

    def byer_protection():
        try:
            _f['product_byer_protection'] = str(_d.execute_locator(_l['byer_protection_locator']))
            return True
        except Exception as ex: 
            _f['product_byer_protection'] = None
            logger.error(ex)
            return False


    def customer_reviews():
        try:
            _f['product_customer_reviews'] = _d.execute_locator(_l['customer_reviews_locator'])
        except Exception as ex:
            _f['product_customer_reviews'] = None
            logger.error(ex)
            return False



    def rewritted_URL():
        '''
        TODO
        получается длинные
        _f['Rewritten URL'] = SF.rewritted_URL(_f['title'])
        '''
        _f['Rewritten URL'] = _f['id']
        pass
    def supplier():
        _f['supplier'] = s.settings['supplier_id']

    id()
    sku_suppl()
    sku_prod()
    title()
    description()
    summary()
    specification()
    cost_price()
    before_tax_price()
    delivery()
    images()
    combinations()
    qty()
    byer_protection()
    delivery()
    
    customer_reviews()
    link()
    #meta_keywords()
    supplier()
    rewritted_URL()
    
    return p