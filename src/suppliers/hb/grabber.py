"""! @~russian  Собиратель данных со страницы товара

@warning Алиэкспресс загружает страницу через javascript. bs и requests не работают. 
Все манипулации со страницей модуль осуществляет через селениум

 @section libs imports:
  - gs 
  - product 
  - helpers 
  - tools 
  @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import asyncio
from typing import Union

from selenium.webdriver.remote.webelement import WebElement
from src.settings import gs
from src.product import  Product, ProductFields
from src.prestashop import Product as PrestaProduct
from src.helpers import  logger, logs_and_errors_decorator
from src.tools import StringFormatter as SF, StringNormalizer as SN
from src.suppliers import Supplier
from src.webdriver import Driver

s: Supplier = None
p: Product = None
f: ProductFields = None
d: Driver = None 
l: dict = None
async_run = gs.async_run


#@logs_and_errors_decorator
def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields :
	"""! Собираю со страницы товара значения вебэлементов и привожу их к полям ProductFields
	
	@param s `Supplier` класс поставщика 
	@~russian _note - вебдрайвер должен быть установлен на странице товара. 
	- в моей учетной записи я вижу линейку "Affiliate links" - я беру из нее информацию о партнерской ссылке
	@~russian _note на али работает AJAX, это важно для сбора комбинаций! Они не передаются по URL
   
	"""
	
	global s
	s = supplier

	global p 
	p = Product (s)

	global f
	f = ProductFields (s)

	global d
	d = s.driver
	
	global l
	l = s.locators['product']
	
	d.scroll()
	"""! прокручиваю страницу товара, чтобы захватить области, которые подгружаются через AJAX """


	"""! Я получаю со страницы список из трех локаторов.
   У меня нш получается вытащить только reference. Я забираю volume, price_for_100_ml, sku """
	volume_and_price_for_100_and_sku()


	#######################################################
	"""! testing right now """
	f.reference = field_reference()
	########################################################



	#f.active = field_active() # [v] (added by default)
	#f.additional_delivery_times = field_additional_delivery_times()	# [v]  Мое поле. Нахера - не знаю
	f.additional_shipping_cost  = 0 #field_additional_shipping_cost() # [v]
	#f.advanced_stock_management = field_advanced_stock_management()
	f.affiliate_short_link = d.current_url # field_affiliate_short_link() # [v]
	#f.affiliate_summary = field_affiliate_summary()
	#f.affiliate_image_large = field_affiliate_image_large()
	#f.affiliate_image_medium = field_affiliate_image_medium()
	#f.affiliate_image_small = field_affiliate_image_small()
	#f.affiliate_summary_2 = field_affiliate_summary_2()
	#f.affiliate_text = field_affiliate_text()
	#f.affiliate_image_large = field_affiliate_image_large()
	#f.affiliate_image_medium = field_affiliate_image_medium()
	#f.affiliate_image_small = field_affiliate_image_small()
	#f.available_date = field_available_date()
	#f.available_for_order = field_available_for_order()
	#f.available_later = field_available_later()
	#f.available_now = field_available_now()
	#f.cache_default_attribute = field_cache_default_attribute()
	#f.cache_has_attachments = field_cache_has_attachments()
	#f.cache_is_pack = field_cache_is_pack()
	#f.category_ids_append = field_category_ids_append() ##<- добавочные категории. Если надо дополнить уже внесенные
	#f.condition = field_condition()
	#f.customizable = field_customizable()
	#f.date_add = field_date_add()
	#f.date_upd = field_date_upd()
	f.delivery_in_stock = 30 #field_delivery_in_stock()	 # [v]	 ##<- доставка
	#f.delivery_out_stock = field_delivery_out_stock()
	#f.depth = field_depth()
	#f.description = field_description()
	f.description_short = f.description = field_description_short()
	# f.ean13 = field_ean13()
	# f.ecotax = field_ecotax()
	# f.height = field_height()
	f.how_to_use = field_how_to_use()
	f.id_category_default = field_id_category_default()
	f.id_default_combination = field_id_default_combination()
	f.id_default_image = field_id_default_image()
	f.id_lang = field_id_lang()
	f.id_manufacturer = field_id_manufacturer()
	f.id_product = field_id_product()
	f.id_shop_default = field_id_shop_default()
	f.id_supplier = s.supplier_id	# [v]
	f.id_tax = field_id_tax() # [v]
	f.id_type_redirected = field_id_type_redirected()
	f.images_urls = field_images_urls()	# [v]
	f.indexed = field_indexed()
	f.ingridients = field_ingridients()
	#f.is_virtual = field_is_virtual()
	#f.isbn = field_isbn()
	f.link_rewrite = field_link_rewrite()
	f.location = field_location()
	#f.low_stock_alert = field_low_stock_alert()
	#f.low_stock_threshold = field_low_stock_threshold()
	f.meta_description = field_meta_description()
	f.meta_keywords = field_meta_keywords()
	f.meta_title = field_meta_title()
	f.minimal_quantity = field_minimal_quantity()
	#f.mpn = field_mpn()
	f.name = field_name()  # [v]
	f.online_only = field_online_only()
	f.on_sale = field_on_sale()
	f.out_of_stock = field_out_of_stock()
	f.pack_stock_type = field_pack_stock_type()
	f.position_in_category = field_position_in_category()
	f.price = field_price()
	f.product_type = field_product_type()
	f.quantity = field_quantity()
	f.quantity_discount = field_quantity_discount()
	f.redirect_type = field_redirect_type()
	f.reference = field_reference()	# [v]
	f.show_condition = field_show_condition()
	f.show_price = field_show_price()
	f.state = field_state()
	f.supplier_reference = field_supplier_reference()  # [v]
	f.text_fields = field_text_fields()
	f.unit_price_ratio = field_unit_price_ratio()
	f.unity = field_unity()
	f.upc = field_upc()
	f.uploadable_files = field_uploadable_files()
	f.url_default_image = field_url_default_image()
	#f.volume = field_volume()
	f.visibility = field_visibility()
	f.weight = field_weight()
	f.wholesale_price = field_wholesale_price()
	f.width = field_width()    
	pass
	return f
    


#@logs_and_errors_decorator(default_return=False)
def field_active():
	"""! @~russian 
	@brief
	@details
	"""
	return f.active
	pass
	
        

#@logs_and_errors_decorator(default_return=False)
def field_additional_delivery_times():
    """! @~russian 
    @brief
    @details
    """
    return d.execute_locator(l['additional_delivery_times'])
    pass



 
#@logs_and_errors_decorator(default_return=False)
def field_additional_shipping_cost():
    """! @~russian 
    @brief
    @details
    """
    return d.execute_locator(l['additional_shipping_cost'])
    pass
    

#@logs_and_errors_decorator(default_return=False)
def field_advanced_stock_management():
	"""! @~russian 
	@brief
	@details
	"""
	return f.advanced_stock_management
	pass
	
        
#@logs_and_errors_decorator(default_return=False)
def field_affiliate_short_link():
    """! @~russian 
    @brief
    @details
    """
    return d.execute_locator(l['affiliate_short_link'])
    pass
    


#@logs_and_errors_decorator(default_return=False)
def field_affiliate_summary():
    """! @~russian 
    @brief
    @details
    """
    return f.affiliate_summary
    pass


#@logs_and_errors_decorator(default_return=False)
def field_affiliate_summary_2():
    """! @~russian 
    @brief
    @details
    """
    return f.affiliate_summary_2
    pass
        

#@logs_and_errors_decorator(default_return=False)
def field_affiliate_text():
	"""! @~russian 
	@brief
	@details
	"""
	return f.affiliate_text
	pass
	
    

#@logs_and_errors_decorator(default_return=False)
def field_affiliate_image_large():
	"""! @~russian 
	@brief
	@details
	"""
	pass
        

#@logs_and_errors_decorator(default_return=False)
def field_affiliate_image_medium():
	"""! @~russian 
	@brief
	@details
	"""
	pass
        

#@logs_and_errors_decorator(default_return=False)
def field_affiliate_image_small():
	"""! @~russian 
	@brief
	@details
	"""
	return d.execute_locator(l['affiliate_image_small'])
        
#@logs_and_errors_decorator(default_return=False)
def field_available_date():
    """! @~russian 
    @brief
    @details
    """
    return f.available_date
    pass
        
    

#@logs_and_errors_decorator(default_return=False)
def field_available_for_order():
    """! @~russian 
    @brief
    @details
    """
    return f.available_for_order
    pass


#@logs_and_errors_decorator(default_return=False)
def field_available_later():
    """! @~russian 
    @brief
    @details
    """
    return f.available_later
    pass


#@logs_and_errors_decorator(default_return=False)
def field_available_now():
    """! @~russian 
    @brief
    @details
    """
    return f.available_now
    pass



#@logs_and_errors_decorator(default_return=False)
def field_category_ids():
	"""! @~russian 
	@brief
	@details
	"""
	return f.category_ids
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_category_ids_append():
	"""! @~russian 
	@brief
	@details
	"""
	#return f.category_ids_append
	pass
	
                

#@logs_and_errors_decorator(default_return=False)
def field_cache_default_attribute():
    """! @~russian 
    @brief
    @details
    """
    return f.cache_default_attribute
    pass


#@logs_and_errors_decorator(default_return=False)
def field_cache_has_attachments():
    """! @~russian 
    @brief
    @details
    """
    return f.cache_has_attachments
    pass	
        
                

#@logs_and_errors_decorator(default_return=False)
def field_cache_is_pack():
	"""! @~russian 
	@brief
	@details
	"""
	return f.cache_is_pack
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_condition():
	"""! @~russian 
	@brief
	@details
	"""
	pass
	return f.condition
        
#@logs_and_errors_decorator(default_return=False)
def field_customizable():
	"""! @~russian 
	@brief
	@details
	"""
	return f.customizable
	pass

#@logs_and_errors_decorator(default_return=False)
def field_date_add():
	"""! @~russian 
	@brief
	@details
	"""
	return f.date_add
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_date_upd():
	"""! @~russian 
	@brief
	@details
	"""
	return f.date_upd
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_delivery_in_stock():
	"""! @~russian 
	@brief Доставка, когда товар в наличии
	@details
	"""
	return d.execute_locator(l['delivery_in_stock'])
	pass
	
        

#@logs_and_errors_decorator(default_return=False)
def field_delivery_out_stock():
	"""! @~russian 
	@brief
	@details
	"""
	return f.delivery_out_stock
	pass
	
                

#@logs_and_errors_decorator(default_return=False)
def field_depth():
	"""! @~russian @brief
	@details
	"""
	return f.depth
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_description():
	"""! @~russian поле полного описания товара 
	@details
	"""
	return str (d.execute_locator (l['description'] ) )
	pass


#@logs_and_errors_decorator(default_return=False)
def field_description_short():
	"""! @~russian 
	@brief
	@details
	"""
	return str (d.execute_locator (l['description_short'] ) )
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_ean13():
	"""! @~russian 
	@brief
	@details
	"""
	return f.ean13
	pass


#@logs_and_errors_decorator(default_return=False)
def field_ecotax():
	"""! @~russian 
	@brief
	@details
	"""
	return f.ecotax
	pass
	
        	
                

#@logs_and_errors_decorator(default_return=False)
def field_height():
	"""! @~russian 
	@brief
	@details
	"""
	return f.height
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_how_to_use():
	"""! @~russian 
	@brief
	@details
	"""
	return d.execute_locator ( l ['how_to_use'] ) 
	pass
	
                	

#@logs_and_errors_decorator(default_return=False)
def field_id_category_default():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_category_default
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_id_default_combination():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_default_combination
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_id_default_image():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_default_image
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_lang():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_lang
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_manufacturer():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_manufacturer
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_product():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_product
	pass

#@logs_and_errors_decorator(default_return=False)
def field_id_shop_default():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_shop_default
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_supplier():
	"""! @~russian 
	@brief
	@details
	"""
	return s.supplier_id
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_tax():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_tax
	pass
	
#@logs_and_errors_decorator(default_return=False)
def field_id_type_redirected():
	"""! @~russian 
	@brief
	@details
	"""
	return f.id_type_redirected
	pass

#@logs_and_errors_decorator(default_return=False)
def field_images_urls():
	"""! @~russian 
	@brief Вначале я загружу дефолтную картинку
	@details
	"""
	return d.execute_locator(l['Image URLs (x,y,z...)'])
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_indexed():
	"""! @~russian 
	@brief
	@details
	"""
	return f.indexed
	pass
	
        
#@logs_and_errors_decorator(default_return=False)
def field_ingridients():
	"""! @~russian 
	@brief
	@details
	"""
	return f.ingridients
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_is_virtual():
	"""! @~russian 
	@brief
	@details
	"""
	return f.is_virtual
	pass


#@logs_and_errors_decorator(default_return=False)
def field_isbn():
	"""! @~russian 
	@brief
	@details
	"""
	return f.isbn
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_link_rewrite():
	"""! @~russian 
	@brief
	@details
	"""
	return f.link_rewrite
	pass
	
        

#@logs_and_errors_decorator(default_return=False)
def field_location():
	"""! @~russian 
	@brief
	@details
	"""
	return f.location
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_low_stock_alert():
	"""! @~russian 
	@brief
	@details
	"""
	return f.low_stock_alert
	pass
	
    

#@logs_and_errors_decorator(default_return=False)
def field_low_stock_threshold():
	"""! @~russian 
	@brief
	@details
	"""
	return f.low_stock_threshold
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_meta_description():
	"""! @~russian 
	@brief
	@details
	"""
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_meta_keywords():
	"""! @~russian 
	@brief
	@details
	"""
	return f.meta_keywords
	pass
	
        

#@logs_and_errors_decorator(default_return=False)
def field_meta_title():
	"""! @~russian 
	@brief
	@details
	"""
	return f.meta_title
	pass
	


#@logs_and_errors_decorator(default_return=False)
def field_minimal_quantity():
	"""! @~russian 
	@brief
	@details
	"""
	return f.minimal_quantity
	pass


#@logs_and_errors_decorator(default_return=False)
def field_mpn():
	"""! @~russian 
	@brief
	@details
	"""
	return f.mpn
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_name():
	"""! @~russian 
	@brief
	@details
	"""
	return d.execute_locator ( l['name'] )
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_online_only():
	"""! @~russian 	товар только в интернет магазине
	@brief
	@details
	"""
	return f.online_only
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_on_sale():
	"""! @~russian 	Распродажа	"""
	return f.on_sale
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_out_of_stock():
	"""! @~russian Товара нет в наличии """
	return d.execute_locator ( l['out_of_stock']) 
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_pack_stock_type():
	"""! @~russian 
	@brief
	@details
	"""
	return f.pack_stock_type
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_position_in_category():
	"""! @~russian 
	@brief
	@details
	"""
	return f.position_in_category
	pass
	
                                

#@logs_and_errors_decorator(default_return=False)
def field_price():
	"""! @~russian 
	@brief
	@details
	"""
	return d.execute_locator ( l['price'] )
	
	

#@logs_and_errors_decorator(default_return=False)
def field_product_type():
	"""! @~russian 
	@brief
	@details
	"""
	return f.product_type
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_quantity():
	"""! @~russian 
	@brief
	@details
	"""
	return f.quantity
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_quantity_discount():
	"""! @~russian 
	@brief
	@details
	"""
	return f.quantity_discount
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_redirect_type():
	"""! @~russian 
	@brief
	@details
	"""
	return f.redirect_type
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_reference():
	"""! @~russian supplier's SKU """
	return f'{s.supplier_id}-{f.supplier_reference}' 
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_show_condition():
	"""! @~russian 
	@brief
	@details
	"""
	return f.show_condition
	


#@logs_and_errors_decorator(default_return=False)
def field_show_price():
	"""! @~russian 
	@brief
	@details
	"""
	return f.show_price
	pass


#@logs_and_errors_decorator(default_return=False)
def field_state():
	"""! @~russian 
	@brief
	@details
	"""
	return f.state
	pass


#@logs_and_errors_decorator(default_return=False)
def field_supplier_reference():
	"""! @~russian Локатор захватит 3 объекта (по одному я устал их искать). Здесь я делаю обработку результата
	"""
	return d.execute_locator (l['supplier_reference'])
	pass
	


#@logs_and_errors_decorator(default_return=False)
def field_text_fields():
	"""! @~russian 
	@brief
	@details
	"""
	return f.text_fields
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_unit_price_ratio():
	"""! @~russian 
	@brief
	@details
	"""
	return f.unit_price_ratio
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_unity():
	"""! @~russian 
	@brief
	@details
	"""
	return f.unity
	pass
	
        

#@logs_and_errors_decorator(default_return=False)
def field_upc():
	"""! @~russian 
	@brief
	@details
	"""
	return f.upc
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_uploadable_files():
	"""! @~russian 
	@brief
	@details
	"""
	return f.uploadable_files
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_url_default_image():
	"""! @~russian 
	@brief
	@details
	"""
	return f.url_default_image
	pass
	

#@logs_and_errors_decorator(default_return=False)
def volume_and_price_for_100_and_sku():
    """! @~russian """
    global f
    webelements: [WebElement] = d.execute_locator(l['volume_and_price_for_100_and_sku'])
        
    for webelement in webelements:
        if ('Fl.oz' and 'מ"ל' )	in webelement.text:
            """! объем """
            f.volume = webelement.text
        elif str(r'מחיר ל100 מ"ל') in webelement.text:
            """! цена за единицу товара
            @todo придумать куда
            """
            print(f'цена за единицу товара:{webelement.text}')
        elif 'מקט' in webelement.text:
            f.supplier_reference = SN.get_numbers_only(webelement.text)
        pass
    pass
        

#@logs_and_errors_decorator(default_return=False)
def field_visibility():
	"""! @~russian 
	@brief
	@details
	"""
	return f.visibility
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_weight():
	"""! @~russian 
	@brief
	@details
	"""
	return f.weight
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_wholesale_price():
	"""! @~russian 
	@brief
	@details
	"""
	return f.wholesale_price
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_width():
	"""! @~russian 
	@brief
	@details
	"""
	return f.width
	pass
	
        
                

#@logs_and_errors_decorator
async def get_price(_d, _l) -> Union[str,float]:
	"""! @~russian Привожу денюшку через флаг `format` 
	@details к: 
	- [ ] float 
	- [v] str
	"""
	try:
		
		#raw_price = asyncio.run ( _d.execute_locator ( _l ['price']['new'] )[0])
		raw_price = asyncio.run ( _d.execute_locator ( _l ['price']['new'] )[0]) if gs.async_run else _d.execute_locator ( _l ['price']['new'] )[0]
		''' raw_price получаю в таком виде:
		ILS382.00\nILS382\n.\n00
		'''
		raw_price = str (raw_price).split ('\n')[0]
		return SN.normalize_price (raw_price)
	except Exception as ex:
		logger.error (ex)
		return False
    
    ## price
    # async def cost_price():
    #     _price = _d.execute_locator (_l['price_locator'])        
    #     if not _price or len(_price) < 1:
    #         _price = _d.execute_locator(_l['uniform-banner-box-price'])
    #         ''' цена может быть спрятана баннером. Ищу в баннере'''
    #     _price = SF.clear_price(_price)
    #     return _price
    




def specification():
    #f['product_specification'] = _d.execute_locator(_l['specification_locator'])
    f['product_specification'] = f['product_description']
def summary():
    f['summary'] = f['product_description']
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
        f['shipping price'] = 0
        return True
    f['shipping price'] = SF.clear_price(shipping_price)
    return True



def link():
    f['link to product']= _d.current_url.split('?')[0]

## images
def images():

    _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
    _img_name = f'''{f['sku']}.png'''
    f['img url'] =f'''{_http_server}/{_img_name}'''
    screenshot = _d.execute_locator(_l['main_image_locator'])
    s.save_and_send_viaftp({_img_name:screenshot})

def qty():
    try:
        _qty = _d.execute_locator(_l['qty_locator'])[0]
        f['qty'] = SF.clear_price(_qty)
        f['tavit im bemlay'] = f['qty']
        return True
    except Exception as ex: 
        #field['qty'] = None
        logger.error(ex)
        return False

def byer_protection():
    try:
        f['product_byer_protection'] = str(_d.execute_locator(_l['byer_protection_locator']))
        return True
    except Exception as ex: 
        f['product_byer_protection'] = None
        logger.error(ex)
        return False


def customer_reviews():
    try:
        f['product_customer_reviews'] = _d.execute_locator(_l['customer_reviews_locator'])
    except Exception as ex:
        f['product_customer_reviews'] = None
        logger.error(ex)
        return False



def rewritted_URL():
    '''
    TODO
    получается длинные
    f['Rewritten URL'] = SF.rewritted_URL(f['title'])
    '''
    f['Rewritten URL'] = f['id']
    pass

## combinations
def combinations():
    """! @~russian У товара может быть насколько комбинаций. Функция вытаскивает все возможные
    @todo не проверена, я отложил реализацию на след версию
    """
    _l = s.locators['product']
    _combfs = p.combinationsfs
    _attr_position = 0

    def product_combinations():
        _type = s.current_scenario['product combinations']
        if not _type: return
        """! @~russian _rem у товара не всегда есть комбинации """

        __ = s.locators['product']['combinations']
        _combfs['Product ID'] = f['id']
        _name = _d.execute_locator(__l['name'])
        _value = _d.execute_locator(__l['value'])
            
        _combfs['Attribute (Name:Type:Position)'] = f'''{_name}:{_type}:0'''
        _combfs['Value (Value:Position)'] = f'''{_value}:0'''
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

        _combinationsfs['Attribute (Name:Type:Position)'] = f'''{attr_name}:{attr_type}:{attr_position}'''
        
        _vt = _d.execute_locator(_l['product_combinations_container_locator']['product_combinations_value_title'])
        _vp = _attr_position
        _combinationsfs['Value (Value:Position)'] = f'''{_vt}:{_vp}'''

                

        url_dict = _d.get_dictfrom_urlstr()
        _combinationsfs['Supplier reference'] = _combina['Product reference'] = url_dict['params']['sku_id']
                
                
        _d.execute_locator(_l['product_name_locator'])

        _combinationsfs['Image URLs(x,y,z)'] = _d.execute_locator(_l['main_image_locator'])
        _combinationsfs['Quantity'] = _qty
        _combinationsfs['Wholesale price'] = _price

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
