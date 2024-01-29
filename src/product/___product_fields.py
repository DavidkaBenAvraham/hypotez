"""! @~russian 
@brief  Kласс `ProductFields` и функции сортировки в категориях
Наименование полей в классе соответствуют именам полей в таблицах `Prestashop`
Порядок полей в этом файле соответствует номерам полей в таблице, В коде программы в дальнейшем я использую алфавитный порядок

 @section libs imports:
  - src.prestashop 
  - sqlite3 
  - typing 
  - pathlib 
  - attr 
  - enum 
  - src.gs 
  - src.helpers 
  - src.gs 
  - src.tools 

"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import json
from src.prestashop import Product as PrestashopProduct
from sqlite3 import Date
from typing import Union
from pathlib import Path
from attr import attr, attrs
from enum import Enum

# --------------------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, ProductFieldException
from src.io_interface import j_loads, j_dumps
from src.tools import StringFormatter as SF, StringNormalizer as SN
# --------------------------------------------



# -------------------------------------------
#
#       `table_product`
#
#           Column Name                 Data Type	            Allowed NULL
#   1	    `id_product`                int(10) unsigned	    [V]
#   2       `id_supplier`               int(10) unsigned	    [V]
#   3       `id_manufacturer`           int(10) unsigned	    [v]
#   4       `id_category_default`       int(10) unsigned	    [v]
#   5       `id_shop_default`           int(10) unsigned        [v]
#   6       `id_tax`	    int(11) unsigned        [v]
#   7       `on_sale`                   tinyint(1) unsigned     [v]
#   8       `online_only`               tinyint(1) unsigned     [v]
#   9       `ean13`                     varchar(13)             [v]
#   10      `isbn`                      varchar(32)
#   11      `upc`                       varchar(12)
#   12      `mpn`                       varchar(40)
# 	13	    `ecotax`                    decimal(17,6)
#   14      `quantity`                  int(10)
#   15      `minimal_quantity`          int(10) unsigned
#   16      `low_stock_threshold`       int(10)
#   17      `low_stock_alert`           tinyint(1)
#   18      `price`                     decimal(20,6)
#   19      `wholesale_price`           decimal(20,6)
#   20      `unity`                     varchar(255)
#   21      `unit_price_ratio`          decimal(20,6)
#   22      `additional_shipping_cost`  decimal(20,6)
#   23      `reference`                 varchar(64)
#   24      `supplier_reference`        varchar(64)
#   25      `location`                  varchar(255)
#   26      `width`                     decimal(20,6)
#   27      `height`                    decimal(20,6)
#   28      `depth`                     decimal(20,6)
#   29      `weight`                    decimal(20,6)
#   30      `out_of_stock`              int(10) unsigned
#   31      `additional_delivery_times` tinyint(1) unsigned
#   32      `quantity_discount`         tinyint(1)
#   33      `customizable`              tinyint(2)
#   34      `uploadable_files`          tinyint(4)
#   35      `text_fields`               tinyint(4)
#   36      `active`                    tinyint(1) unsigned
#   37      `redirect_type`             enum('404','301-product','302-product','301-category','302-category')
#   38      `id_type_redirected`        int(10) unsigned
#   39      `available_for_order`       tinyint(1)
#   40      `available_date`            date
#   41      `show_condition`            tinyint(1)
#   42      `condition`                 enum('new','used','refurbished')
#   43      `show_price`                tinyint(1)
#   44      `indexed`                   tinyint(1)
#   45      `visibility`                enum('both','catalog','search','none')
#   46      `cache_is_pack`             tinyint(1)
#   47      `cache_has_attachments`     tinyint(1)
#   48      `is_virtual`                tinyint(1)
#   49      `cache_default_attribute`   int(10) unsigned
#   50      `date_add`                  datetime
#   51      `date_upd`                  datetime
#   52      `advanced_stock_management` tinyint(1)
#   53      `pack_stock_type`           int(11) unsigned
#   54      `state`                     int(11) unsigned
#   55      `product_type`              enum('standard','pack','virtual','combinations','')



class ProductFields():
    """
    @class ProductFields
     Обработчик полей товара


    """

    product_dict: dict = {}
    fields: dict = {}

    def __init__(self, *args, **kwards):
        self.product_dict['product']: dict = self.fields
        """! @todo странная и непонятная конструкция """
        self._payload(*args, **kwards)
        pass

    def _payload(self, *args, **kwards):
        """! @~russian Установки полей товара по умолчанию """
        
        default_value = j_loads (Path (gs.dir_src, 'product', 'product_fields_default_values.json'))
        
        self.active = default_value['active']
        self.additional_delivery_times = default_value['additional_delivery_times']
        self.additional_shipping_cost  = default_value['additional_shipping_cost']
        self.advanced_stock_management = default_value['advanced_stock_management']
        self.affiliate_short_link = default_value['affiliate_short_link']
        self.affiliate_summary = default_value['affiliate_summary']
        self.affiliate_summary_2 = default_value['affiliate_summary_2']
        self.affiliate_text = default_value['affiliate_text']
        self.available_date = default_value['available_date']
        self.available_for_order = default_value['available_for_order']
        self.available_later = default_value['available_later']
        self.available_now = default_value['available_now']
        self.cache_default_attribute = default_value['cache_default_attribute']
        self.cache_has_attachments = default_value['cache_has_attachments']
        self.cache_is_pack = default_value['cache_is_pack']
        self.category_ids_append = None #default_value[''] #<- добавочные категории.
        self.category_ids = None #default_value['category_ids'] #<- 
        self.condition = default_value['condition']
        self.customizable = default_value['customizable']
        self.date_add = default_value['date_add']
        self.date_upd = default_value['date_upd']
        self.delivery_in_stock = default_value['delivery_in_stock']
        self.delivery_out_stock = default_value['delivery_out_stock']
        self.depth = default_value['depth']
        self.description = default_value['description']
        self.description_short = default_value['description_short']
        self.ean13 = default_value['ean13']
        self.ecotax = default_value['ecotax']
        self.height = default_value['height']
        self.how_to_use = default_value['how_to_use']
        self.id_category_default = default_value['id_category_default']
        self.id_default_combination = default_value['id_default_combination']
        self.id_default_image = default_value['id_default_image']
        self.id_lang = default_value['id_lang']
        self.id_manufacturer = default_value['id_manufacturer']
        self.id_product = default_value['id_product']
        self.id_shop_default = default_value['id_shop_default']
        self.id_product = default_value['id_product']
        self.id_supplier = default_value['id_supplier']
        self.id_tax = default_value['id_tax']
        self.id_type_redirected = default_value['id_type_redirected']
        self.images_urls = None #default_value['images_urls'] нет такого поля в престашоп
        self.indexed = default_value['indexed']
        self.ingridients = default_value['ingridients']
        self.is_virtual = default_value['is_virtual']
        self.isbn = default_value['isbn']
        self.link_rewrite = default_value['link_rewrite']
        self.location = default_value['location']
        self.low_stock_alert = default_value['low_stock_alert']
        self.low_stock_threshold = default_value['low_stock_threshold']
        self.meta_description = default_value['meta_description']
        self.meta_keywords = default_value['meta_keywords']
        self.meta_title = default_value['meta_title']
        self.minimal_quantity = default_value['minimal_quantity']
        self.mpn = default_value['mpn']
        self.name = default_value['name']
        self.online_only = default_value['online_only']
        self.on_sale = default_value['on_sale']
        self.out_of_stock = default_value['out_of_stock']
        self.pack_stock_type = default_value['pack_stock_type']
        self.position_in_category = default_value['position_in_category']
        self.price = default_value['price']
        self.product_type = default_value['product_type']
        self.quantity = default_value['quantity']
        self.quantity_discount = default_value['quantity_discount']
        self.redirect_type = default_value['redirect_type']
        self.reference = default_value['reference']
        self.show_condition = default_value['show_condition']
        self.show_price = default_value['show_price']
        self.state = default_value['state']
        self.supplier_reference = default_value['supplier_reference']
        self.text_fields = default_value['text_fields']
        self.unit_price_ratio = default_value['unit_price_ratio']
        self.unity = default_value['unity']
        self.upc = default_value['upc']
        self.uploadable_files = default_value['uploadable_files']
        self.default_image_url = None # default_value['default_image_url']
        self.visibility = default_value['visibility']
        self.weight = default_value['weight']
        self.wholesale_price = default_value['wholesale_price']
        self.width = default_value['width']            

        
    def get_product_dict(self):
        return self.product_dict




    

############################################################

#   1   ID товара
    @property
    def id_product(self) -> int :
        """! *[getter]*  field: `table_product.id: int(10) unsigned`
        @note для нового тoвара `ID` назначется в `prestashop`
        """

        return self.fields.get('id', None)
    
    
    @id_product.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_product(self, id_product: int = None) -> bool:
        """! *[setter]*  `ID` товара. *для нового тoвара id назначется из `prestashop`*
        @details Запись нового товара в престашоп делается в два шага:
        -> в престасшоп заносятся парамеры, которые не связаны с ID, например, название товара, артикул и т.п. 
        <- От престашоп возвращается словарь, в котором установлено ID. 
        -> теперь можно грузить фото, доп парамерты, короче все, что завязано на id товара
        @param id_product `int`  :  Требуется при операциях над существующим товаром. `table_product.id` .  
        Для нового товара ID вернется из системы при занесении товара в базу данных.
        @returns bool `True` if success, else `False`
        """
        try:
            self.fields['id'] = id_product
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ID' данными {id_product}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   2   Поставщик
    
    @property
    def id_supplier(self):
        """! *[getter]*  field: `table_product.id_supplier: int(10) unsigned`
        @~russian @details: привязываю товар к id поставщика
        """
        return self.fields.get('id_supplier', None)
    
    
    @id_supplier.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_supplier(self, id_supplier: int = None) -> bool:
        """! *[setter]* """
        try:
            self.fields['id_supplier'] = id_supplier
            return True

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: `table_product.id_supplier` данными {id_supplier}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   3   Бренд
    
    @property
    def id_manufacturer(self) -> int:
        """! *[getter]* field: `table_product.id_manufacturer: int(10) unsigned`
        field
        @~russian @details: means BRAND. 
            Бренд может быть передан как по имени так и по ID.
            Таблица брендов:

            """

        return self.fields.get('id_manufacturer', None)
    
    
    @id_manufacturer.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_manufacturer(self, id_manufacturer: int = None) -> bool:
        """! *[setter]*  Бренд может быть передан как по имени так и по ID 

        field: `table_product.id_manufacturer`
        field type: int(10) unsigned
        @~russian @details: привязываю товар к бренду
        """
        try:
            self.fields['id_manufacturer'] = id_manufacturer
            # self.fields_psapi['id_manufacturer']=self.fields.get('Brand']=brand
            # TODO - получить словарь поставщиков и ловить id_manufacturer
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Brand' данными {id_manufacturer}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False



#   4   Главная категория этого товара
    
    @property
    def id_category_default(self) -> int:
        """! *[getter]* field: `table_product.id_category_default: int(10) unsigned`
        @~russian @details: привязываю товар к главной категории для этого товара
        """
        return self.fields.get('id_category_default', None)
    
    
    @id_category_default.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_category_default(self, id_category_default: int) -> bool:
        """! *[setter]* Сюда передается та категория, которая будет однознчно - родительская `table_product.id_category_default: int(10) unsigned`"""
        try:
            self.fields['id_category_default'] = id_category_default
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_category_default' данными {id_category_default}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False        
        
     
    @property
    def category_ids(self) -> dict:
        """! *[getter]* возвращает словарь категорий товара восстановленный из файла сценария """
        return self.fields.get('associations')['categories']

    
    @category_ids.setter
    #@logs_and_errors_decorator (default_return =  False)
    def category_ids(self, category_ids: Union[int,list[int]] ) -> bool :
        """! *[setter]*  @~russian Дополнительные к основной категории.
        При задании доп ключей прдеыдущие значения заменяются новыми из `category_ids`.
        Для добавления новых к уже существующим используй  функцию category_ids_append()
        """
        try:
            if not category_ids: return
            category_ids = [category_ids] if isinstance ( category_ids, str ) else category_ids
        
            category_ids: dict = {'category': [{'id': id} for id in category_ids]}

            if 'associations' in self.fields.keys():
                """! Всякие дополнения идут через ключ `associations` """
                self.fields ['associations']['categories']: dict = category_ids
            else:
                self.fields ['associations']: dict = {}
                self.fields ['associations']['categories']: dict = category_ids
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'category_ids' данными {category_ids}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False            
    
    
    def category_ids_append(self,category_ids: Union[int,list[int]]):
        """! @~russian Дополнительные категории, кроме основной.
        Функция расширяет category_ids() """
        
        try:
            category_ids = [category_ids] if isinstance (category_ids, str) else category_ids
            self.fields ['associations']['categories']['category'].append ( [{'id': id} for id in category_ids] )
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'category_ids' данными {category_ids}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
   
#   5   Магазин по умолчанию
    
    @property
    def id_shop_default(self) -> int:
        """! *[getter]* field: `table_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
        @~russian @details: ID магазина по умолчанию """

        return self.fields.get('id_shop_default')
    
    
    @id_shop_default.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_shop_default(self, id_shop_default: int = None) -> bool:
        """! *[setter]*  field: `table_product.id_shop_default: int(10) unsigned`
            `ID` магазина заказчика """
        try:
            self.fields['id_shop_default'] = id_shop_default
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop_default' данными {id_shop_default}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   6   НДС (Израиль - обычно 13)
    
    @property
    def id_tax(self) -> int:
        """! *[getter]* tax_rule `int`  :  `ID` НДС  `table_product.id_tax: int(10) unsigned`"""

        return self.fields.get('id_tax')

    
    @id_tax.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_tax(self, tax_rule_id: int = 1) -> bool:
        """!  *[setter]*  `ID` ндс. מע''מ = 13 """
        try:
            self.fields['id_tax'] = int(tax_rule_id)
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Tax rule ID' данными {tax_rule_id}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   7   Распродажа - Mivtza
    
    @property
    def on_sale(self) -> int:
        """! *[getter]*  field: `table_product.on_sale: tinyint(1)  unsigned`"""

        return self.fields.get('on_sale')

    @on_sale.setter
    #@logs_and_errors_decorator (default_return =  False)    
    def on_sale(self, on_sale: int = 0) -> bool:
        """! *[setter]*  Indicates whether there is a sale on the item.

        @param
            on_sale (int, optional): Defaults to 0.

        @returns
            bool: _@~russian @details_
        """
        try:
            self.fields['on_sale'] = on_sale
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'On sale (0/1)' данными {on_sale}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   8 online_only: только через онлайн
    
    @property
    def online_only(self) -> int:
        """!  *[getter]*  field: `table_product.online_only: tinyint(1) unsigned`
        field DB type: tinyint(1) unsigned
        @~russian @details: товар только онлайн """

        return self.fields.get('online_only')
    
    
    @online_only.setter
    #@logs_and_errors_decorator (default_return =  False)
    def online_only(self, online_only: int = 0) -> bool:
        """!  *[setter]* """
        try:
            self.fields['online_only'] = online_only
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'online_only' данными {online_only}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   9   ean13
    
    @property
    def ean13(self: str = None) -> Union[str, None]:
        """! *[getter]*  field: `ean13`
        field DB type:  varchar(13)
        @~russian @details: __prod_desc__"""
        return self.fields.get('ean13')

    
    @ean13.setter
    #@logs_and_errors_decorator (default_return =  False)
    def ean13(self, ean13=None) -> bool:
        """!  *[setter]*  field: `ean13`
        field DB type:  varchar(13)
        @~russian @details: __prod_desc__"""
        try:
            self.fields['ean13'] = ean13
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ean13' данными {ean13}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   10
    
    @property
    def isbn(self) -> Union[str, None]:
        """!  *[setter]*  field: `isbn`
        field DB type: varchar(32)
        @~russian @details: __prod_desc__"""
        return self.fields.get('isbn')
    
    
    @isbn.setter
    #@logs_and_errors_decorator (default_return =  False)
    def isbn(self, isbn: str = None) -> bool:
        """!  *[setter]*  field: `isbn`
        field DB type: varchar(32)
        @~russian @details: __prod_desc__"""
        try:
            self.fields['isbn'] = isbn
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {isbn}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   11
    
    @property
    def upc(self):
        """! *[getter]*  field: `upc`
        field DB type: varchar(12)
        @~russian @details: __prod_desc__"""
        return self.fields.get('upc')
    
    
    @upc.setter
    #@logs_and_errors_decorator (default_return =  False)
    def upc(self, upc: str = None) -> Union[str, None]:
        """!  *[setter]*  field: `table_product.upc`
        field DB type: varchar(12)
        @~russian @details: __prod_desc__"""
        try:
            self.fields['isbn'] = upc
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {upc}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   12  mpn
    
    @property
    def mpn(self) -> str:
        """! *[getter]*  field: `table_product.mpn`
        field DB type: varchar(40)
        @~russian @details: __prod_desc__"""
        return self.fields.get('mpn')

    
    @mpn.setter
    #@logs_and_errors_decorator (default_return =  False)
    def mpn(self, mpn: str = None) -> bool:
        """!  *[setter]*  """
        try:
            self.fields['mpn'] = mpn
            return True
        except ProductFieldException as ex:
            logger.error(f"""
                         Ошибка заполнения поля: `table_product.mpn` данными {mpn}
                         -----------------
                            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   13   ecotax
    
    @property
    def ecotax(self):
        """! *[getter]*  field: `table_product.ecotax`
        field DB type:  decimal(17,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('ecotax')

    
    @ecotax.setter
    #@logs_and_errors_decorator (default_return =  False)
    def ecotax(self, ecotax=None) -> bool:
        """!  *[setter]*  """
        try:
            self.fields['ecotax'] = ecotax
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ecotax' данными {ecotax}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

# 14
    
    @property
    def quantity(self) -> int:
        """! *[getter]*  field: `table_product.quantity`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""

        return self.fields.get('quantity')

    
    @quantity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def quantity(self, quantity: int = 0) -> bool:
        """! *[setter]*  field: `table_product.quantity` """
        try:
            self.fields['quantity'] = quantity
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'quantity' данными {quantity}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

# 15
    
    @property
    def minimal_quantity(self) -> int:
        """! *[getter]* field: `table_product.minimal_quantity`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields.get('minimal_quantity')

    
    @minimal_quantity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def minimal_quantity(self, minimal_quantity: int = 0) -> bool:
        try:
            self.fields['minimal_quantity'] = minimal_quantity
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'minimal_quantity' данными {minimal_quantity}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   16
    
    @property
    def low_stock_threshold(self) -> int:
        """! *[getter]* field: `table_product.low_stock_threshold`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields.get('low_stock_threshold')

    
    @low_stock_threshold.setter
    #@logs_and_errors_decorator (default_return =  False)
    def low_stock_threshold(self, low_stock_threshold: int = 0) -> bool:
        try:
            self.fields['low_stock_threshold'] = low_stock_threshold
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_threshold' данными {low_stock_threshold}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   17
    
    @property
    def low_stock_alert(self) -> int:
        """! *[getter]* field: `table_product.low_stock_alert`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""
        return self.fields.get('low_stock_alert')

    
    @low_stock_alert.setter
    #@logs_and_errors_decorator (default_return =  False)
    def low_stock_alert(self, low_stock_alert: int = 0) -> bool:
        try:
            self.fields['low_stock_alert'] = low_stock_alert
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_alert' данными {low_stock_alert}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   18
    
    @property
    def price(self) -> float:
        """! *[getter]* field: `table_product.price`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('price')
    
    
    @price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def price(self, price: Union[str,int,float]) -> bool:
        try:
            if not price:
                return False
            self.fields['price'] = price
            return True
        except ProductFieldException as ex:
            logger.error(f'''
            Ошибка заполнения поля: 'price' данными {price}
            Ошибка: {ex.with_traceback(ex.__traceback__)}''', ex)
            return False
#   19
    
    @property
    def wholesale_price(self) -> float:
        """! *[getter]* field: `table_product.wholesale_price`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('wholesale_price')

    
    @wholesale_price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def wholesale_price(self, wholesale_price: str = None) -> float:
        try:
            self.fields['wholesale_price'] = str(SN.normalize_price(
                wholesale_price))
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'wholesale_price' данными {wholesale_price}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   20
    
    @property
    def unity(self) -> str:
        """! *[getter]* field: `table_product.unity`
        field DB type: varchar(255)
        @~russian @details: __prod_desc__"""

    
    @unity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def unity(self, unity: str = None) -> bool:
        try:
            self.fields['unity'] = unity
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'unity' данными {unity}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   21
    
    @property
    def unit_price_ratio(self) -> float:
        """! *[getter]* field: `table_product.unit_price_ratio`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('unit_price_ratio')

    
    @unit_price_ratio.setter
    def unit_price_ratio(self, unit_price_ratio: float = 0) -> bool:
        try:
            self.fields['unit_price_ratio'] = unit_price_ratio
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: `unit_price_ratio` данными {unit_price_ratio}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   22
    
    @property
    def additional_shipping_cost(self) -> float:
        """! *[getter]* field: `table_product.additional_shipping_cost`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('additional_shipping_cost')

    
    @additional_shipping_cost.setter
    #@logs_and_errors_decorator (default_return =  False)
    def additional_shipping_cost(self, additional_shipping_cost: int = 1) -> bool:
        try:
            self.fields['additional_shipping_cost'] = additional_shipping_cost
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_shipping_cost' данными {additional_shipping_cost}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   23
    
    @property
    def reference(self) -> str:
        """ 
       ! *[getter]* field: `table_product.reference`
        field DB type: `varchar(64)`
        @~russian @details: __prod_desc__
        """
        return self.fields.get('reference')

    
    @reference.setter
    #@logs_and_errors_decorator (default_return =  False)
    def reference(self, reference: str) -> bool:
        try:
            self.fields['reference'] = str(reference)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'reference' данными {reference}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
        
    
    @property
    def supplier_reference(self):
        """
       ! *[getter]* field: `table_product.supplier_reference`
        field DB type: `varchar(64)`
        @~russian @details: __prod_desc__
        """
        return self.fields.get('supplier_reference')
#   24
    
    @supplier_reference.setter
    #@logs_and_errors_decorator (default_return =  False)
    def supplier_reference(self, supplier_reference: str = None) -> bool:
        try:
            self.fields['supplier_reference'] = str(supplier_reference)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'supplier_reference' данными {supplier_reference}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   25
    
    @property
    def location(self) -> str:
        """! *[getter]* field: `table_product.location`
        field DB type: varchar(255)
        @~russian @details: __prod_desc__"""
        return self.fields.get('location')

    
    @location.setter
    #@logs_and_errors_decorator (default_return =  False)
    def location(self, location: str = None) -> bool:
        try:
            self.fields['location'] = str(location)
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'location' данными {location}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   26
    
    @property
    def width(self) -> float:
        """! *[getter]* field: `table_product.width`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('width')

    
    @width.setter
    #@logs_and_errors_decorator (default_return =  False)
    def width(self, width: float = None) -> bool:
        try:
            self.fields['width'] = width
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'width' данными {width}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   27
    
    @property
    def height(self) -> float:
        """! *[getter]* field: `table_product`..`height`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('height')

    
    @height.setter
    #@logs_and_errors_decorator (default_return =  False)
    def height(self, height: float = None) -> bool:
        try:
            self.fields['height'] = height
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'height' данными {height}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   28
    
    @property
    def depth(self) -> float:
        """! *[getter]* field: `table_product`..`depth`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('depth')

    
    @depth.setter
    #@logs_and_errors_decorator (default_return =  False)
    def depth(self, depth: float = None) -> bool:
        try:
            self.fields['depth'] = depth
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'depth' данными {depth}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   29
    
    @property
    def weight(self) -> float:
        """! *[getter]* field: `table_product.weight`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields.get('weight')

    
    @weight.setter
    #@logs_and_errors_decorator (default_return =  False)
    def weight(self, weight: float = None) -> bool:
        try:
            self.fields['weight'] = weight
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'weight' данными {weight}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

    #  30
    
    @property
    def out_of_stock(self) -> int:
        """! *[getter]* field: `table_product.out_of_stock`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields.get('out_of_stock')

    
    @out_of_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def out_of_stock(self, out_of_stock: int = None) -> bool:
        try:
            self.fields['out_of_stock'] = out_of_stock
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'out_of_stock' данными {out_of_stock}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

  #  31
    
    @property
    def additional_delivery_times(self) -> int:
        """!! *[getter]* field: `table_product.additional_delivery_times`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields.get('additional_delivery_times')

    
    @additional_delivery_times.setter
    #@logs_and_errors_decorator (default_return =  False)
    def additional_delivery_times(self, additional_delivery_times: int = 0) -> bool:
        try:
            self.fields['additional_delivery_times'] = additional_delivery_times
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_delivery_times' данными {additional_delivery_times}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
  #  32
    
    @property
    def quantity_discount(self) -> int:
        """! *[getter]* field: `table_product.quantity_discount`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""
        return self.fields.get('quantity_discount')

    
    @quantity_discount.setter
    #@logs_and_errors_decorator (default_return =  False)
    def quantity_discount(self, quantity_discount: int = 0) -> bool:
        try:
            self.fields['quantity_discount'] = quantity_discount
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'quantity_discount' данными {quantity_discount}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

  #  33
    
    @property
    def customizable(self) -> int:
        """! *[getter]* field: `table_product.customizable`
        field DB type: tinyint(2)
        @~russian @details: __prod_desc__"""
        return self.fields.get('customizable')

    
    @customizable.setter
    #@logs_and_errors_decorator (default_return =  False)
    def customizable(self, customizable: int = 0) -> bool:
        try:
            self.fields['customizable'] = customizable
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'customizable' данными {customizable}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

  #  34
    
    @property
    def uploadable_files(self) -> int:
        """! *[getter]* field: `table_product.uploadable_files`
        field DB type: tinyint(4)
        @~russian @details: __prod_desc__"""

        return self.fields.get('uploadable_files')

    
    @uploadable_files.setter
    #@logs_and_errors_decorator (default_return =  False)
    def uploadable_files(self, uploadable_files: int = 0) -> bool:
        try:
            self.fields['uploadable_files'] = uploadable_files
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'uploadable_files' данными {uploadable_files}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#  35
    
    @property
    def text_fields(self) -> int:
        """! *[getter]* field: `table_product.text_fields`
        field DB type: tinyint(4)
        @~russian @details: __prod_desc__"""

        return self.fields.get('text_fields')

    
    @text_fields.setter
    #@logs_and_errors_decorator (default_return =  False)
    def text_fields(self, text_fields: int = 0) -> bool:
        try:
            self.fields['text_fields'] = text_fields
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'text_fields' данными {text_fields}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  36
    
    @property
    def active(self) -> int:
        """! *[getter]* field: `table_product.active`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('active')

    
    @active.setter
    #@logs_and_errors_decorator (default_return =  False)
    def active(self, active: int = 0) -> bool:
        try:
            self.fields['active'] = active
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'active' данными {active}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
   
        

#  37
    
    @property
    def redirect_type(self) -> str:
        """! *[getter]* field: `table_product.redirect_type`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('redirect_type')

    class EnumRedirect(Enum):
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'

    
    @redirect_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def redirect_type(self, redirect_type: EnumRedirect = None) -> bool:
        try:
            self.fields['redirect_type'] = redirect_type
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'redirect_type' данными {redirect_type}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  38
    
    @property
    def id_type_redirected(self) -> int:
        """! *[getter]* field: `table_product.id_type_redirected`
        field DB type: tinyint(10)
        @~russian @details: __prod_desc__"""

        return self.fields.get('id_type_redirected')
    
    
    @id_type_redirected.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_type_redirected(self, id_type_redirected: int = 0) -> bool:
        try:
            self.fields['id_type_redirected'] = id_type_redirected
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'id_type_redirected' данными {id_type_redirected}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  39
    
    @property
    def available_for_order(self) -> int:
        """! *[getter]* field: `table_product.available_for_order`
        field DB type: tinyint(10)
        @~russian @details: __prod_desc__"""

        return self.fields.get('available_for_order')

    
    @available_for_order.setter
    #@logs_and_errors_decorator (default_return =  False)
    def available_for_order(self, available_for_order: int = 0) -> bool:
        try:
            self.fields['available_for_order'] = available_for_order
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_for_order' данными {available_for_order}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  40
    
    @property
    def available_date(self) -> Date:
        """! *[getter]* field: `table_product.available_date`
        field DB type: date
        @~russian @details: __prod_desc__"""

        return self.fields.get('available_date')

    
    @available_date.setter
    #@logs_and_errors_decorator (default_return =  False)
    def available_date(self, available_date: Date = Date.today) -> bool:
        try:
            self.fields['available_date'] = available_date
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_date' данными {available_date}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  41
    
    @property
    def show_condition(self) -> int:
        """! *[getter]* field: `table_product.show_condition`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('show_condition')

    
    @show_condition.setter
    #@logs_and_errors_decorator (default_return =  False)
    def show_condition(self, show_condition: int = 1) -> bool:
        try:
            self.fields['show_condition'] = show_condition
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_condition' данными {show_condition}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  42
    
    @property
    def condition(self) -> str:
        """! *[getter]* field: `table_product.condition`
        field DB type: enum('new','used','refurbished')
        @~russian @details: __prod_desc__"""

        return self.fields.get('condition')

    class EnumCondition(Enum):
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'
        
    
    @condition.setter
    #@logs_and_errors_decorator (default_return =  False)
    def condition(self, condition: EnumCondition = EnumCondition.NEW) -> bool:
        try:
            self.fields['condition'] = condition
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'condition' данными {condition}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

 #  43
    
    @property
    def show_price(self) -> int:
        """! *[getter]* field: `table_product.show_price`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('show_price')
    
    
    @show_price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def show_price(self, show_price: int = 1) -> bool:
        try:
            self.fields['show_price'] = show_price
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_price' данными {show_price}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  44
    
    @property
    def indexed(self) -> int:
        """! *[getter]* field: `table_product.indexed`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('indexed')
    
    
    @indexed.setter
    #@logs_and_errors_decorator (default_return =  False)
    def indexed(self, indexed: int = 1) -> bool:
        try:
            self.fields['indexed'] = indexed
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'indexed' данными {indexed}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  45
    
    @property
    def visibility(self) -> str:
        """! *[getter]* field: `table_product.visibility`
        field DB type: enum('both','catalog','search','none')
        @~russian @details: __prod_desc__"""

        return self.fields.get('visibility')

    class EnumVisibity(Enum):
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'

    
    @visibility.setter
    #@logs_and_errors_decorator (default_return =  False)
    def visibility(self, visibility: EnumVisibity = EnumVisibity.BOTH) -> bool:
        try:
            self.fields['visibility'] = visibility
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'visibility' данными {visibility}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#  46

    
    @property
    def cache_is_pack(self) -> int:
        """! *[getter]* field: `table_product.cache_is_pack`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('cache_is_pack')
    
    
    @cache_is_pack.setter
    #@logs_and_errors_decorator (default_return =  False)
    def cache_is_pack(self, cache_is_pack: int = 1) -> bool:
        try:
            self.fields['cache_is_pack'] = cache_is_pack
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_is_pack' данными {cache_is_pack}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  47
    
    @property
    def cache_has_attachments(self) -> int:
        """! *[getter]* field: `table_product.cache_has_attachments`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('cache_has_attachments')
    
    
    @cache_has_attachments.setter
    #@logs_and_errors_decorator (default_return =  False)
    def cache_has_attachments(self, cache_has_attachments: int = 1) -> bool:
        try:
            self.fields['cache_has_attachments'] = cache_has_attachments
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_has_attachments' данными {cache_has_attachments}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  48
    
    @property
    def is_virtual(self) -> int:
        """! *[getter]* field: `table_product.is_virtual`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('is_virtual')

    
    @is_virtual.setter
    #@logs_and_errors_decorator (default_return =  False)
    def is_virtual(self, is_virtual: int = 1) -> bool:
        try:
            self.fields['is_virtual'] = is_virtual
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'is_virtual' данными {is_virtual}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  49
    
    @property
    def cache_default_attribute(self) -> int:
        """! *[getter]* field: `table_product.cache_default_attribute`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""

        return self.fields.get('cache_default_attribute')

    
    @cache_default_attribute.setter
    #@logs_and_errors_decorator (default_return =  False)
    def cache_default_attribute(self, cache_default_attribute: int = 1) -> bool:
        try:
            self.fields['cache_default_attribute'] = cache_default_attribute
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_default_attribute' данными {cache_default_attribute}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  50
    
    @property
    def date_add(self) -> Date:
        """! *[getter]* field: `table_product.date_add`
        field DB type: datetime
        @~russian @details: __prod_desc__"""

        return self.fields.get('date_add')
    
    
    @date_add.setter
    #@logs_and_errors_decorator (default_return =  False)
    def date_add(self, date_add: Date = Date.today()) -> bool:
        try:
            self.fields['date_add'] = date_add
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_add' данными {date_add}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  51
    
    @property
    def date_upd(self) -> Date:
        """! *[getter]* field: `table_product.date_upd`
        field DB type: datetime
        @~russian @details: __prod_desc__"""

        return self.fields.get('date_upd')
    
    
    @date_upd.setter
    #@logs_and_errors_decorator (default_return =  False)
    def date_upd(self, date_upd: Date = Date.today()) -> bool:
        try:
            self.fields['date_upd'] = date_upd
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_upd' данными {date_upd}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#  52
    
    @property
    def advanced_stock_management(self) -> int:
        """! *[getter]* field: `table_product.advanced_stock_management`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields.get('advanced_stock_management')
    
    
    @advanced_stock_management.setter
    #@logs_and_errors_decorator (default_return =  False)
    def advanced_stock_management(self, advanced_stock_management: int = 0) -> bool:
        try:
            self.fields['advanced_stock_management'] = advanced_stock_management
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'advanced_stock_management' данными {advanced_stock_management}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  53
    
    @property
    def pack_stock_type(self) -> int:
        """! *[getter]* field: `table_product.pack_stock_type`
        field DB type: int(11)
        @~russian @details: __prod_desc__"""

        return self.fields.get('pack_stock_type')
    
    
    @pack_stock_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def pack_stock_type(self, pack_stock_type: int = 0) -> bool:
        try:
            self.fields['pack_stock_type'] = pack_stock_type
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'pack_stock_type' данными {pack_stock_type}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#  54
    
    @property
    def state(self) -> int:
        """! *[getter]* field: `table_product.state`
        field DB type: int(11)
        @~russian @details: __prod_desc__"""

        return self.fields.get('state')
    
    
    @state.setter
    #@logs_and_errors_decorator (default_return =  False)
    def state(self, state: int = 0) -> bool:
        try:
            self.fields['state'] = state
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'state' данными {state}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#  55
    
    @property
    def product_type(self) -> str:
        """! *[getter]* field: `table_product.product_type`
        field DB type: enum('standard', 'pack', 'virtual', 'combinations', '')
        @~russian @details: __prod_desc__"""

        return self.fields.get('product_type')

    class EnumProductType(Enum):
        STANDARD = 'standard'
        PACK = 'pack'
        VIRTUAL = 'virtual'
        COMBINATIONS = 'combinations'
        EMPTY = ''
          
    @product_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def product_type(self, product_type: EnumProductType = EnumProductType.STANDARD) -> bool:
        try:
            self.fields['product_type'] = product_type
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'product_type' данными {product_type}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

















####################################################################################################################################
#
#
#
#           ТАБЛИЦА `_product_lang` - СОДЕРЖИТ МИЛЬТИЯЗЫЧНЫЕ ПОЛЯ 
#
#
#               в таблице `_product_lang` находятся поля специфичные для языка 
#
#
#
# -------------------------------------------------------
#
#           _product_lang
#
#       Column Name	                    Data Type	        Comment
# 1	    `id_product`                    int(10) unsigned
# 2	    `id_shop`	                    int(11) unsigned
# 3	    `id_lang`	                    int(10) unsigned
# 4	    `description`	                text
# 5	    `description_short`	            text
# 6	    `link_rewrite`	                varchar(128)
# 7	    `meta_description`	            varchar(512)
# 8	    `meta_keywords`	                varchar(255)
# 9	    `meta_title`	                varchar(128)
# 10	`name`	                        varchar(128)
# 11	`available_now`	                varchar(255)
# 12	`available_later`	            varchar(255)
# 13	`delivery_in_stock`	            varchar(255)
# 14	`delivery_out_stock`	        varchar(255)
# 15    `delivery_additional_message`   tinytext
# 16	`affiliate_short_link`	        tinytext
# 17	`affiliate_text`	            tinytext
# 18	`affiliate_summary`	            tinytext
# 19	`affiliate_summary_2`	        tinytext
# 20	`ingridients`	                tinytext
# 21	`how_to_use`        	        tinytext


#   Поля `id_product` и `id_shop` берутся из верхних значениий в этом коде



#   3
    
    @property
    def id_lang(self):
        """! *[getter]* field: `_product_lang.`
        field DB type: int(10)
        description: __prod_desc__"""
        return self.fields.get('Discount from (yyyy-mm-dd)')

    
    @id_lang.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_lang(self, id_lang: Date = None) -> bool:
        try:
            self.fields['id_lang'] = id_lang
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_lang' данными {id_lang}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   4
    
    @property
    def description(self) -> str:
        """! *[getter]* field: `_product_lang.description`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('description')

    
    @description.setter
    #@logs_and_errors_decorator (default_return =  False)
    def description(self, description: str = None) -> bool:
        try:
            self.fields['description']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':description},
                {'attrs':{'id':'2'}, 'value':description},
                {'attrs':{'id':'3'}, 'value':description},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'description' данными {description}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   5
    
    @property
    def description_short(self) -> str:
        """! *[getter]* field: `_product_lang.description_short`
        field DB type: text
        description: __prod_desc__"""

        return self.fields.get('description_short')
    
    @description_short.setter
    #@logs_and_errors_decorator (default_return =  False)
    def description_short(self, description_short: str = None) -> bool:
        try:
            self.fields['description_short']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':description_short},
                {'attrs':{'id':'2'}, 'value':description_short},
                {'attrs':{'id':'3'}, 'value':description_short},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'description_short' данными {description_short}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   6
    
    @property
    def link_rewrite(self) -> str:
        """! *[getter]* field: `_product_lang.link_rewrite`
        field DB type: varchar(128)
        description: __prod_desc__"""
        return self.fields.get('link_rewrite')

    
    @link_rewrite.setter
    #@logs_and_errors_decorator (default_return =  False)
    def link_rewrite(self, link_rewrite: str = None) -> bool:
        try:
            #self.fields['link_rewrite'] = link_rewrite
            self.fields['link_rewrite']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':link_rewrite},
                {'attrs':{'id':'2'}, 'value':link_rewrite},
                {'attrs':{'id':'3'}, 'value':link_rewrite},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'link_rewrite' данными {link_rewrite}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
#   7
    
    @property
    def meta_description(self) -> str:
        """! *[getter]* field: `_product_lang.meta_description`
        field DB type: varchar(512)
        description: __prod_desc__"""
        return self.fields.get('meta_description')
    
    
    @meta_description.setter
    #@logs_and_errors_decorator (default_return =  False)
    def meta_description(self, meta_description=None) -> bool:
        try:
            self.fields['meta_description']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':meta_description},
                {'attrs':{'id':'2'}, 'value':meta_description},
                {'attrs':{'id':'3'}, 'value':meta_description},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_description' данными {meta_description}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   8
    
    @property
    def meta_keywords(self):
        """! *[getter]* field: `_product_lang.meta_keywords`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('meta_keywords')
    
    @meta_keywords.setter
    #@logs_and_errors_decorator (default_return =  False)
    def meta_keywords(self, meta_keywords=None) -> bool:
        try:
            self.fields['meta_keywords']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':meta_keywords},
                {'attrs':{'id':'2'}, 'value':meta_keywords},
                {'attrs':{'id':'3'}, 'value':meta_keywords},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_keywords' данными {meta_keywords}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   9
    
    @property
    def meta_title(self) -> str:
        """! *[getter]* field: `_product_lang.meta_title`
        field DB type: varchar(128)
        description: __prod_desc__"""
        return self.fields.get('meta_title')
    
    
    @meta_title.setter
    #@logs_and_errors_decorator (default_return =  False)
    def meta_title(self, meta_title=None) -> bool:
        try:
            self.fields['meta_title']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':meta_title},
                {'attrs':{'id':'2'}, 'value':meta_title},
                {'attrs':{'id':'3'}, 'value':meta_title},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_title' данными {meta_title}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   10
    
    @property
    def name(self):
        """! *[getter]* field: `_product_lang.name`
        field DB type: varchar(128)
        description: __prod_desc__"""
        return self.fields.get('name')
    
    
    @name.setter
    #@logs_and_errors_decorator (default_return =  False)
    def name(self, name: str) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':name},
                {'attrs':{'id':'2'}, 'value':name},
                {'attrs':{'id':'3'}, 'value':name},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'name' данными {name}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   11
    
    @property
    def available_now(self) -> str:
        """ field DB available_now: `_product_lang.available_now`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('available_now')
    
    
    @available_now.setter
    #@logs_and_errors_decorator (default_return =  False)
    def available_now(self, available_now=None) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':available_now},
                {'attrs':{'id':'2'}, 'value':available_now},
                {'attrs':{'id':'3'}, 'value':available_now},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_now' данными {available_now}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   12
    
    @property
    def available_later(self) -> str:
        """ field DB available_later: `_product_lang.available_later`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('available_later')
    
    @available_later.setter
    #@logs_and_errors_decorator (default_return =  False)
    def available_later(self, available_later=None) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':available_later},
                {'attrs':{'id':'2'}, 'value':available_later},
                {'attrs':{'id':'3'}, 'value':available_later},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_later' данными {available_later}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   13
    
    @property
    def delivery_in_stock(self):
        """ field DB delivery_in_stock: `_product_lang.delivery_in_stock`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('delivery_in_stock')
    
    @delivery_in_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def delivery_in_stock(self, delivery_in_stock=None) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':delivery_in_stock},
                {'attrs':{'id':'2'}, 'value':delivery_in_stock},
                {'attrs':{'id':'3'}, 'value':delivery_in_stock},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_in_stock' данными {delivery_in_stock}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   14
    
    @property
    def delivery_out_stock(self) -> str:
        """ field DB delivery_out_stock: `_product_lang.delivery_out_stock`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('delivery_out_stock')
    
    @delivery_out_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def delivery_out_stock(self, delivery_out_stock=None) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':delivery_out_stock},
                {'attrs':{'id':'2'}, 'value':delivery_out_stock},
                {'attrs':{'id':'3'}, 'value':delivery_out_stock},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_out_stock' данными {delivery_out_stock}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
        
#   15

    @property
    def delivery_additional_message(self) -> str:
        """ field DB delivery_out_stock: `_product_lang.delivery_out_stock`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('delivery_out_stock')
    
    @delivery_out_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def delivery_additional_message(self, delivery_additional_message=None) -> bool:
        try:
            self.fields['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':delivery_additional_message},
                {'attrs':{'id':'2'}, 'value':delivery_additional_message},
                {'attrs':{'id':'3'}, 'value':delivery_additional_message},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_out_stock' данными {delivery_out_stock}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   15

    
    @property
    def affiliate_short_link(self) -> str:
        """ field DB affiliate_short_link: `_product_lang.affiliate_short_link`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields.get('affiliate_short_link')
    
    @affiliate_short_link.setter
    #@logs_and_errors_decorator (default_return =  False)
    def affiliate_short_link(self, affiliate_short_link:str) -> bool:
        try:
            self.fields['affiliate_short_link']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':affiliate_short_link},
                {'attrs':{'id':'2'}, 'value':affiliate_short_link},
                {'attrs':{'id':'3'}, 'value':affiliate_short_link},
            ]}

            
            # self.fields['affiliate_short_link']: dict = {
            #     "language":[
            #     {'#text': affiliate_short_link, '@id':'1'},
            #     {'#text': affiliate_short_link, '@id':'2'},
            #     {'#text': affiliate_short_link, '@id':'3'},
            # ]}
            
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_short_link' данными {affiliate_short_link}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#   16
    
    @property
    def affiliate_text(self) -> str:
        """ field DB affiliate_text: `_product_lang.affiliate_text`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('affiliate_text')
    
    @affiliate_text.setter
    #@logs_and_errors_decorator (default_return =  False)
    def affiliate_text(self, affiliate_text=None) -> bool:
        try:
            #self.fields['affiliate_text'] = affiliate_text
            self.fields['affiliate_text']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':affiliate_text},
            {'attrs':{'id':'2'}, 'value':affiliate_text},
            {'attrs':{'id':'3'}, 'value':affiliate_text},
        ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_text' данными {affiliate_text}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   17
    
    @property
    def affiliate_summary(self) -> str:
        """ field DB affiliate_summary: `_product_lang.affiliate_summary`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('affiliate_summary')
    
    
    @affiliate_summary.setter
    #@logs_and_errors_decorator (default_return =  False)
    def affiliate_summary(self, affiliate_summary=None) -> bool:
        try:
            #self.fields['affiliate_summary'] = affiliate_summary
            self.fields['affiliate_short_link']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':affiliate_summary},
            {'attrs':{'id':'2'}, 'value':affiliate_summary},
            {'attrs':{'id':'3'}, 'value':affiliate_summary},
        ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary' данными {affiliate_summary}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


#   18

    
    @property
    def affiliate_summary_2(self) -> str:
        """ field DB affiliate_summary_2: `_product_lang.affiliate_summary_2`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('affiliate_summary_2', None)

    
    @affiliate_summary_2.setter
    #@logs_and_errors_decorator (default_return =  False)
    def affiliate_summary_2(self, affiliate_summary_2: str = None) -> bool:
        try:
            self.fields['affiliate_summary_2']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':affiliate_summary_2},
            {'attrs':{'id':'2'}, 'value':affiliate_summary_2},
            {'attrs':{'id':'3'}, 'value':affiliate_summary_2},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {affiliate_summary_2}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

    
    @property
    def ingridients(self) -> str:
        """ field DB ingridients: `_product_lang.affiliate_summary_2`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('ingridients', None)

    
    @ingridients.setter
    #@logs_and_errors_decorator (default_return =  False)
    def ingridients(self, ingridients: str = None) -> bool:
        try:
            self.fields['ingridients']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':ingridients},
            {'attrs':{'id':'2'}, 'value':ingridients},
            {'attrs':{'id':'3'}, 'value':ingridients},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {affiliate_summary_2}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

    
    @property
    def how_to_use(self) -> str:
        """ field DB affiliate_summary_2: `_product_lang.affiliate_summary_2`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('how_to_use', None)

    
    @ingridients.setter
    #@logs_and_errors_decorator (default_return =  False)
    def how_to_use(self, how_to_use: str = None) -> bool:
        try:
            self.fields['how_to_use']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':how_to_use},
            {'attrs':{'id':'2'}, 'value':how_to_use},
            {'attrs':{'id':'3'}, 'value':how_to_use},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'how_to_use' данными {how_to_use}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

    
    @property
    def default_image_url(self) -> str:
        """ field DB affiliate_summary_2: `_???????.id_default_image`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('id_default_image')
    
    
    @default_image_url.setter
    #@logs_and_errors_decorator (default_return =  False)
    def default_image_url(self, default_image_url: int) -> bool:
        try:
            self.fields['default_image_url'] = default_image_url
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_image' данными {id_default_image}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False
        
    
    @property
    def id_default_image(self) -> str:
        """ field DB affiliate_summary_2: `_???????.id_default_image`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('id_default_image')
    
    
    @id_default_image.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_default_image(self, id_default_image: int) -> bool:
        try:
            self.fields['id_default_image'] = id_default_image
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_image' данными {id_default_image}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False


    
    @property
    def images_urls(self):
        """ field: __prod_name__
        field DB type: __prod_type__
        description: __prod_desc__"""
        return self.fields.get('Image URLs (x,y,z...)')
    
    
    @images_urls.setter
    #@logs_and_errors_decorator (default_return =  False)
    def images_urls(self, images_urls: str = '') -> bool:
        try:
            self.fields['Image URLs (x,y,z...)'] = images_urls
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Image URLs (x,y,z...)' данными {images_urls}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False



#####################################################################################################################################
##
##
##
##           Всякие пока не найденные поля в таблицах
##
##


#  ---------



#  ---------
    
    @property
    def id_default_combination(self) -> str:
        """ field DB affiliate_summary_2: `_?????????.id_default_combination`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('id_default_combination')
    
    
    @id_default_combination.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_default_combination(self, id_default_combination=None) -> bool:
        try:
            self.fields['id_default_combination'] = id_default_combination
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_combination' данными {id_default_combination}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False

#  ---------

    
    @property
    def position_in_category(self) -> str:
        """ field DB affiliate_summary_2: `_?????????.position_in_category`
        field DB type: text
        description: __prod_desc__"""
        return self.fields.get('position_in_category')

    
    @position_in_category.setter
    #@logs_and_errors_decorator (default_return =  False)
    def position_in_category(self, position_in_category=None) -> bool:
        try:
            self.fields['position_in_category'] = position_in_category
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'position_in_category' данными {position_in_category}
            Ошибка: {ex.with_traceback(ex.__traceback__)}""", ex)
            return False





#####################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
