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
from src.settings import gs
from src.product import  Product, ProductFields
from src.prestashop import Product as PrestaProduct
from src.helpers import  logger, logs_and_errors_decorator
from src.tools import SF, SN
from src.suppliers import Supplier


s: Supplier = None
p: Product = None
f: ProductFields = ProductFields()
d = None 
l = None


#@logs_and_errors_decorator
def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields :
	"""! @~russian Собираю данные со страницы товара
	@details При помощи локаторов собираю данные о товаре: название, описание, характеристики, отзывы

	@param s `Supplier` класс поставщика 
	 - вебдрайвер должен быть установлен на странице товара. 
	- в моей учетной записи я вижу линейку "Affiliate links" - я беру из нее информацию о партнерской ссылке
	 на али работает AJAX, это важно для сбора комбинаций! Они не передаются по URL
   
	"""
	
	global s
	s = supplier

	global p 
	p = Product(supplier = s)

	global f
	f = p.productfs

	global d
	d = s.driver
	
	global l
	l = s.locators['product']
	
	d.scroll(3)
	"""! прокручиваю страницу товара, чтобы захватить области, которые подгружаются через AJAX """

	f.active = set_field_active()
	f.additional_delivery_times = set_field_additional_delivery_times()
	f.additional_shipping_cost  = set_field_additional_shipping_cost()
	f.advanced_stock_management = set_field_advanced_stock_management()
	f.affiliate_short_link = set_field_affiliate_short_link()
	f.affiliate_summary = set_field_affiliate_summary()
	f.affiliate_summary_2 = set_field_affiliate_summary_2()
	f.affiliate_text = set_field_affiliate_text()
	f.available_date = set_field_available_date()
	f.available_for_order = set_field_available_for_order()
	f.available_later = set_field_available_later()
	f.available_now = set_field_available_now()
	f.cache_default_attribute = set_field_cache_default_attribute()
	f.cache_has_attachments = set_field_cache_has_attachments()
	f.cache_is_pack = set_field_cache_is_pack()
	f.category_ids_append = set_field_category_ids_append() #<- добавочные категории. Если надо дополнить уже внесенные
	f.category_ids = set_field_category_ids() #<- доп категории
	f.condition = set_field_condition()
	f.customizable = set_field_customizable()
	f.date_add = set_field_date_add()
	f.date_upd = set_field_date_upd()
	f.delivery_in_stock = set_field_delivery_in_stock()
	f.delivery_out_stock = set_field_delivery_out_stock()
	f.depth = set_field_depth()
	f.description = set_field_description()
	f.description_short = set_field_description_short()
	f.ean13 = set_field_ean13()
	f.ecotax = set_field_ecotax()
	f.height = set_field_height()
	f.how_to_use = set_field_how_to_use()
	f.id_category_default = set_field_id_category_default()
	f.id_default_combination = set_field_id_default_combination()
	f.id_default_image = set_field_id_default_image()
	f.id_lang = set_field_id_lang()
	f.id_manufacturer = set_field_id_manufacturer()
	f.id_product = set_field_id_product()
	f.id_shop_default = set_field_id_shop_default()
	f.id_supplier = set_field_id_supplier()
	f.id_tax = set_field_id_tax()
	f.id_type_redirected = set_field_id_type_redirected()
	f.images_urls = set_field_images_urls()
	f.indexed = set_field_indexed()
	f.ingridients = set_field_ingridients()
	f.is_virtual = set_field_is_virtual()
	f.isbn = set_field_isbn()
	f.link_rewrite = set_field_link_rewrite()
	f.location = set_field_location()
	f.low_stock_alert = set_field_low_stock_alert()
	f.low_stock_threshold = set_field_low_stock_threshold()
	f.meta_description = set_field_meta_description()
	f.meta_keywords = set_field_meta_keywords()
	f.meta_title = set_field_meta_title()
	f.minimal_quantity = set_field_minimal_quantity()
	f.mpn = set_field_mpn()
	f.name = set_field_name()
	f.online_only = set_field_online_only()
	f.on_sale = set_field_on_sale()
	f.out_of_stock = set_field_out_of_stock()
	f.pack_stock_type = set_field_pack_stock_type()
	f.position_in_category = set_field_position_in_category()
	f.price = set_field_price()
	f.product_type = set_field_product_type()
	f.quantity = set_field_quantity()
	f.quantity_discount = set_field_quantity_discount()
	f.redirect_type = set_field_redirect_type()
	f.reference = set_field_reference()
	f.show_condition = set_field_show_condition()
	f.show_price = set_field_show_price()
	f.state = set_field_state()
	f.supplier_reference = set_field_supplier_reference()
	f.text_fields = set_field_text_fields()
	f.unit_price_ratio = set_field_unit_price_ratio()
	f.unity = set_field_unity()
	f.upc = set_field_upc()
	f.uploadable_files = set_field_uploadable_files()
	f.default_image_url = set_field_default_image_url()
	f.visibility = set_field_visibility()
	f.weight = set_field_weight()
	f.wholesale_price = set_field_wholesale_price()
	f.width = set_field_width()    

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
    return f.additional_delivery_times
    pass



 
#@logs_and_errors_decorator(default_return=False)
def field_additional_shipping_cost():
    """! @~russian 
    @brief
    @details
    """
    return f.additional_shipping_cost
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
    return f.affiliate_short_link
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
def field_category_ids_append(arg):
	"""! @~russian 
	@brief
	@details
	"""
	return f.category_ids_append
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
def field_condition(arg):
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
	@brief
	@details
	"""
	return f.delivery_in_stock
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
	"""! @~russian 
	@brief
	@details
	"""
	return f.depth
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_description():
	"""! @~russian 
	@brief
	@details
	"""
	return str (d.execute_locator (l['description_locator'] ) )
	pass


#@logs_and_errors_decorator(default_return=False)
def field_description_short():
	"""! @~russian 
	@brief
	@details
	"""
	return f.description_short
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
	return f.how_to_use
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
	return f.id_supplier
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
	@brief
	@details
	"""
	return f.images_urls
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
	return f.name
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_online_only():
	"""! @~russian 
	@brief
	@details
	"""
	return f.online_only
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_on_sale():
	"""! @~russian 
	@brief
	@details
	"""
	return f.on_sale
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_out_of_stock():
	"""! @~russian 
	@brief
	@details`
	"""
	return f.out_of_stock
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
	return f.price
	pass
	

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
	"""! @~russian 
	@brief
	@details
	"""
	return d.async_execute_locator(l['reference']) if async_run else d.execute_locator(l['reference'])
	pass
	

#@logs_and_errors_decorator(default_return=False)
def field_show_condition():
	"""! @~russian 
	@brief
	@details
	"""
	#return f.show_condition
	return 0
	pass


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
	"""! @~russian 
	@brief
	@details
	"""
	return f.supplier_reference
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
def field_default_image_url():
	"""! @~russian 
	@brief
	@details
	"""
	return f.default_image_url
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
	
        