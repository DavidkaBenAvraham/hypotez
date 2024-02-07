"""! @~russian @brief  <b>Kласс `ProductFields` Расписано каждое поле товара для таблиц престашоп.</b>


Наименование полей в классе соответствуют именам полей в таблицах `Prestashop`
Порядок полей в этом файле соответствует номерам полей в таблице, 
В коде программы в дальнейшем я использую алфавитный порядок

@image html ps_model.png

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
from sqlite3 import Date
from typing import Union
from pathlib import Path
from attr import attr, attrs
from enum import Enum

# --------------------------------------------
from src.settings import gs
from src.suppliers import Supplier
from src.helpers import  logger, logs_and_errors_decorator, ProductFieldException
from src.io_interface import j_loads, j_dumps
from src.tools import SF, SN
from src.suppliers import Supplier
# --------------------------------------------


"""! 
# -------------------------------------------
#
#       `ps_product`
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
#   31      `additional_delivery_times` tinyint(1) unsigned # Совершенно непонятное поле
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
"""





class ProductFields:
    """! Класс, описывающий поля товара в формате API PRESTASHOP 
    @details Поля могут быть членами разных таблиц или добавленных мной для удобства обработки.
    Названия полей (геттеров) соответствуют названиям полей в таблицах. Вначале идут поля из таблицы `ps_product`,
    а потом `ps_product_lang`. В таблицах с суффиксом `_lang` содержатся переводы на различные языки.
    @note Важно проверять ID языков. Они могут различаться в разных магазинах у клиентов
    'associations: dict = None ## <- Специальное поле, которое используется в словаре API PRESATSHOP для добавления всяких дополнительных полей
    """
    
    fields_list: list = [ 
    'associations',
    'active',
    'additional_delivery_times',
    'additional_shipping_cost',
    'advanced_stock_management',
    'affiliate_short_link',
    'affiliate_summary',
    'affiliate_summary_2',
    'affiliate_text',
    'available_date',
    'available_for_order',
    'available_later',
    'available_now',
    'cache_default_attribute',
    'cache_has_attachments',
    'cache_is_pack',
    'additional_categories_append',
    'additional_categories',
    'condition',
    'customizable',
    'date_add',
    'date_upd',
    'delivery_in_stock',
    'delivery_out_stock',
    'depth',
    'description',
    'description_short',
    'ean13',
    'ecotax',
    'height',
    'how_to_use',
    'id_category_default',
    'id_default_combination',
    'id_default_image',
    'id_lang',
    'id_manufacturer',
    'id_product',
    'id_shop_default',
    'id_shop',
    'id_product',
    'id_supplier',
    'id_tax',
    'id_type_redirected',
    'images_urls',
    'indexed',
    'ingridients',
    'is_virtual',
    'isbn',
    'link_rewrite',
    'location',
    'low_stock_alert',
    'low_stock_threshold',
    'meta_description',
    'meta_keywords',
    'meta_title',
    'minimal_quantity',
    'mpn',
    'name',
    'online_only',
    'on_sale',
    'out_of_stock',
    'pack_stock_type',
    'position_in_category',
    'price',
    'product_type',
    'quantity',
    'quantity_discount',
    'redirect_type',
    'reference',
    'show_condition',
    'show_price',
    'state',
    'supplier_reference',
    'text_fields',
    'unit_price_ratio',
    'unity',
    'upc',
    'uploadable_files',
    'default_image_url',
    'visibility',
    'weight',
    'wholesale_price',
    'width',
    ]

    fields_dict = {key: None for key in fields_list}
    

    def __init__(self, s: Supplier, *args, **kwargs):
        """! Класс работы с полями товара. Поля берутся состраницы HTML или другого источника
        и форматируются в стандарте API Prestashop. Поля можно в принципе форматировать как угодно
        
        @param s `Supplier` класс поставщика """
        
        self._payload(s, *args, **kwargs)

    def _payload(self, s: Supplier, *args, **kwargs):
        """! Загрузка дефолтных значений полей """
        
        _default = j_loads (Path (gs.dir_src, 'product', 'product_fields_default_values.json'))
        
        for attr_name, default_value in _default.items():
            setattr(self, f'field_{attr_name}', default_value)
        pass

    
    def get_fields(self):
        """! Чтобы получить список полей (атрибутов) класса, 
        я использую встроенную функцию `vars()` внутри метода класса. 
        
      

        # Пример использования
        ```python
        product_fields_instance = ProductFields(s)
        fields_list = product_fields_instance.get_fields()

        print("Список полей класса:")
        print(fields_list)
        ```

        Метод `get_fields` использует `vars(self)`, чтобы получить словарь всех атрибутов экземпляра класса, 
        а затем возвращает список ключей этого словаря, что является списком полей класса.

        Обратите внимание, что этот подход вернет все атрибуты, включая методы и свойства. 
        Если вам нужны только атрибуты, представляющие поля, вы можете дополнительно фильтровать результат. 
        Например, вы можете изменить метод `get_fields` следующим образом:

        ```python
        def get_fields(self):
            return [field for field in vars(self).keys() if not callable(getattr(self, field))]
        ```

        Этот вариант вернет только атрибуты, которые не являются callable (то есть методами).
        """
        #return list(vars(self).keys())
        #return [(key, value = None) for key, value in vars(self).items()]
        return vars(self)
        


############################################################


#   1   ID товара
    @property
    def field_associations(self):
        """! <sub>*[getter]*</sub> Возвращает словарь ключей ассоциаций.
        @details
        Конструкция `associations`:
        
        ```python
        {
         "categories": {
            "category": [
              { "id": "1" },
              { "id": "2" },
              { "id": "3" }
            ]
        },
        
        "images": {
            "image": [ { "id": "1" }  ]
        },
      
        "combinations": {
            "combination": { "id": "" }
        },
        
        "product_option_values": {
            "product_option_value": { "id": ""}
            },
            
        "product_features": {
            "product_feature": {
                "id": "",
                "id_feature_value": ""
            }
        },
        
        "tags": {
            "tag": { "id": "" }
        },
        
        "stock_availables": {
            "stock_available": [
                { "id": "1", "id_product_attribute": "1" },
                { "id": "2", "id_product_attribute": "2" },
                { "id": "3", "id_product_attribute": "3" }
            ]
        },
      
        "attachments": {
            "attachment": {
                "id": ""
            }
        },
        "accessories": {
        "product": {
            "id": ""
        }
        },
        "product_bundle": {
        "product": {
            "id": "",
            "id_product_attribute": "",
            "quantity": ""
        }
        }
            }```
        """
        return self.fields_dict['associations']
    @field_associations.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_associations(self, value = None) -> dict:
        """!  <sub>*[setter]*</sub>  Словарь ассоциаций. Список ассоциаций:
        
        `product_bundle, 
        accessories, 
        attachments, 
        stock_availables, 
        tags, 
        product_features, 
        product_option_values, 
        combinations, 
        images, 
        categories`
        """

        if not self.fields_dict['associations']:

            self.fields_dict['associations']:dict =  {
            "categories": {
            "category": {
              "id": ""
            }
          },
          "images": {
            "image": {
              "id": ""
            }
          },
          "combinations": {
            "combination": {
              "id": ""
            }
          },
          "product_option_values": {
            "product_option_value": {
              "id": ""
            }
          },
          "product_features": {
            "product_feature": {
              "id": "",
              "id_feature_value": ""
            }
          },
          "tags": {
            "tag": {
              "id": ""
            }
          },
          "stock_availables": {
            "stock_available": {
              "id": "",
              "id_product_attribute": ""
            }
          },
          "attachments": {
            "attachment": {
              "id": ""
            }
          },
          "accessories": {
            "product": {
              "id": ""
            }
          },
          "product_bundle": {
            "product": {
              "id": "",
              "id_product_attribute": "",
              "quantity": ""
            }
          }
        }

    @property
    def field_id_product(self) -> int :
        """! <sub>*[property]*</sub>  `ps_product.id: int(10) unsigned`
        @note для нового тoвара `ID` назначется в `prestashop`
        """
        return self.fields_dict['id_product']
    
    
    @field_id_product.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_product(self, value: int = None):
        """!  <sub>*[setter]*</sub>  `ID` товара. *для нового тoвара id назначется из `prestashop`*
        @details Запись нового товара в престашоп делается в два шага:
        -> в престасшоп заносятся парамеры, которые не связаны с ID, например, название товара, артикул и т.п. 
        <- От престашоп возвращается словарь, в котором установлено ID. 
        -> теперь можно грузить фото, доп парамерты, короче все, что завязано на id товара
        @param id_product `int`  :  Требуется при операциях над существующим товаром. `ps_product.id` .  
        Для нового товара ID вернется из системы при занесении товара в базу данных.
        @returns bool `True` if success, else `False`
        """
        try:
            self.fields_dict['id_product'] = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ID' данными {value}
            Ошибка:""", ex)
            return False


#   2   Поставщик
    
    @property
    def field_id_supplier(self):
        """!  <sub>*[property]*</sub>  `ps_product.id_supplier: int(10) unsigned`
        @~russian @details: привязываю товар к id поставщика
        """
        return self.fields_dict['id_supplier']
    
    
    @field_id_supplier.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_supplier(self, value: int = None):
        """!  <sub>*[setter]*</sub> """
        
        try:
            self.fields_dict['id_supplier'] = value
            return True

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: `ps_product.id_supplier` данными {value}
            Ошибка:""", ex)
            return False


#   3   Бренд
    
    @property
    def field_id_manufacturer(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.id_manufacturer: int(10) unsigned`
        field
        @~russian @details: means BRAND. 
            Бренд может быть передан как по имени так и по ID.
            Таблица брендов:

            """

        return self.fields_dict['id_manufacturer']
    
    
    @field_id_manufacturer.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_manufacturer(self, value: int = None):
        """!  <sub>*[setter]*</sub>  Бренд может быть передан как по имени так и по ID 

         `ps_product.id_manufacturer`
        field type: int(10) unsigned
        @~russian @details: привязываю товар к бренду
        """
        try:
            self.fields_dict['id_manufacturer'] = value
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Brand' данными {value}
            Ошибка:""", ex)
            return False



#   4   Главная категория этого товара
    
    @property
    def field_id_category_default(self) -> int:
        """!  <sub>*[property]*</sub>  `ps_product.id_category_default: int(10) unsigned`
        @~russian @details: привязываю товар к главной категории для этого товара
        """
        return self.fields_dict['id_category_default']
    
    
    @field_id_category_default.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_category_default(self, value: int):
        """!  <sub>*[setter]*</sub> Сюда передается та категория, которая будет однознчно - родительская `ps_product.id_category_default: int(10) unsigned`"""
        try:
            self.fields_dict['id_category_default'] = value
            
        except ProductFieldException as ex:
            """! @todo - требуется валидатор"""
            logger.critical(f"""Ошибка заполнения поля: 'id_category_default' данными {value}
            Ошибка:""", ex)
            return False        
        

# дополнительные, которые записываются в ключе associations['categories']  
    @property
    def field_additional_categories(self) -> Union [dict, False]:
        """!  <sub>*[property]*</sub> возвращает словарь категорий товара восстановленный из файла сценария """

        return self.fields_dict['associations']['categories'] or False

    
    @field_additional_categories.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_additional_categories(self, value: Union[int,list[int]]):
        """!  <sub>*[setter]*</sub>  @~russian Дополнительные к основной категории.
        При задании доп ключей прдеыдущие значения заменяются новыми из `additional_categories`.
        Для добавления новых к уже существующим используй  функцию additional_categories_append()
        """

        try:
            if not value: return False
            
            additional_categories_list: list = [value] if isinstance ( value, str ) else value
        
            additional_categories_dict: dict = {'category': [{'id': id} for id in additional_categories_list]}

            if 'associations' not in self.fields_dict['fields'].keys():
                self.fields_dict['associations'].update('associations')
            if 'categories' not in self.fields_dict['associations'].keys():
                self.fields_dict['associations'].update('categories')
                self.fields_dict['categories']: dict = additional_categories_dict
                """! Всякие дополнения идут через ключ `associations` """
            else:
                self.fields_dict['categories']: dict = additional_categories_append(s, value = None)
                
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'additional_categories' данными {value}
            Ошибка:""", ex)  
            return False
    
    
#     def field_additional_categories_append(self,additional_categories: Union[int,list[int]]):
#         """! @~russian Дополнительные категории, кроме основной.
#         Функция расширяет additional_categories() """
        
#         try:
#             additional_categories = [additional_categories] if isinstance (additional_categories, str) else additional_categories
#             self.fields_dict['associations['categories']['category'].append ( [{'id': id} for id in additional_categories] )
#         except ProductFieldException as ex:
#             logger.error(f"""Ошибка заполнения поля: 'additional_categories' данными {additional_categories}
#             Ошибка:""", ex)
#             return False
   
# #   5   Магазин по умолчанию
    
    @property
    def field_id_shop_default(self) -> int:
        """!  <sub>*[property]*</sub>  `ps_product.id_shop_default: int(10) unsigned`
        field DB type: int(10) unsigned
        @~russian @details: ID магазина по умолчанию """

        return self.fields_dict['id_shop_default']
    
    
    @field_id_shop_default.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_shop_default(self, value: int = None):
        """!  <sub>*[setter]*</sub>   `ps_product.id_shop_default: int(10) unsigned`
            `ID` магазина заказчика """
        try:
            self.fields_dict['id_shop_default'] = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_shop_default' данными {value}
            Ошибка:""", ex)
            return False

#   6   НДС (Израиль - обычно 13)
    
    @property
    def field_id_tax(self) -> int:
        """!  <sub>*[property]*</sub> tax_rule `int`  :  `ID` НДС  `ps_product.id_tax: int(10) unsigned`"""

        return self.fields_dict['id_tax']

    
    @field_id_tax.setter
    #@logs_and_errors_decorator (default_return =  False)    
    def field_id_tax(self, value: int ):
        """!   <sub>*[setter]*</sub>  `ID` ндс. מע''מ = 13 """
        try:
            self.fields_dict['id_tax'] = int(value)

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Tax rule ID' данными {value}
            Ошибка:""", ex)
            return False

#   7   Распродажа - Mivtza
    
    @property
    def field_on_sale(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.on_sale: tinyint(1)  unsigned`"""

        return self.fields_dict['on_sale']

    @field_on_sale.setter
    #@logs_and_errors_decorator (default_return =  False)    
    def field_on_sale(self, value = 0 ):
        """!  <sub>*[setter]*</sub> `1` - распродажа

        @param value (int, optional): Defaults to 0.

        @returns
            bool: _@~russian @details_
        """
        try:
            self.fields_dict['on_sale'] = value

        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'On sale (0/1)' данными {value}
            Ошибка:""", ex)
            return False

#   8 online_only: только через онлайн
    
    @property
    def field_online_only(self) -> int:
        """!   <sub>*[property]*</sub>   `ps_product.online_only: tinyint(1) unsigned`
        field DB type: tinyint(1) unsigned
        @~russian @details: товар только онлайн """

        return self.fields_dict['online_only']
    
    
    @field_online_only.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_online_only(self, value = 0) -> bool:
        """!   <sub>*[setter]*</sub> """
        try:
            self.fields_dict['online_only'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'online_only' данными {value}
            Ошибка:""", ex)
            return False

#   9   ean13
    
    @property
    def field_ean13(self) -> Union[str, None]:
        """!  <sub>*[property]*</sub>   `ps_product.ean13  varchar(13)`
        field DB type: 
        @~russian @details: __prod_desc__"""
        return self.fields_dict['ean13']

    
    @field_ean13.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_ean13(self, value = None) -> bool:
        """!   <sub>*[setter]*</sub>   `ean13`
        field DB type:  varchar(13)
        @~russian @details: __prod_desc__"""
        try:
            self.fields_dict['ean13'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ean13' данными {value}
            Ошибка:""", ex)
            return False

#   10
    
    @property
    def field_isbn(self) -> Union[str, None]:
        """!   <sub>*[property]*</sub>   `isbn`
        field DB type: varchar(32)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['isbn']
    
    
    @field_isbn.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_isbn(self, value = None) -> bool:
        """!   <sub>*[setter]*</sub>   `isbn`
        field DB type: varchar(32)
        @~russian @details: __prod_desc__"""
        try:
            self.fields_dict['isbn'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}
            Ошибка:""", ex)
            return False

#   11
    
    @property
    def field_upc(self):
        """!  <sub>*[property]*</sub>   `upc`
        field DB type: varchar(12)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['upc']
    
    
    @field_upc.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_upc(self, value = None) -> Union[str, None]:
        """!   <sub>*[setter]*</sub>   `ps_product.upc`
        field DB type: varchar(12)
        @~russian @details: __prod_desc__"""
        try:
            self.fields_dict['upc'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'isbn' данными {value}
            Ошибка:""", ex)
            return False

#   12  mpn
    
    @property
    def field_mpn(self) -> str:
        """!  <sub>*[property]*</sub>   `ps_product.mpn`
        field DB type: varchar(40)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['mpn']

    
    @field_mpn.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_mpn(self, value = None) -> bool:
        """!   <sub>*[setter]*</sub>  """
        try:
            self.fields_dict['mpn'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
                         Ошибка заполнения поля: `ps_product.mpn` данными {value}
                         -----------------
                            Ошибка:""", ex)
            return False

#   13   ecotax
    
    @property
    def field_ecotax(self):
        """!  <sub>*[property]*</sub>   `ps_product.ecotax`
        field DB type:  decimal(17,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['ecotax']

    
    @field_ecotax.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_ecotax(self, value = None) -> bool:
        """!   <sub>*[setter]*</sub>  """
        try:
            self.fields_dict['ecotax'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'ecotax' данными {value}
            Ошибка:""", ex)
            return False

# 14
    
    @property
    def field_quantity(self) -> int:
        """!  <sub>*[property]*</sub>   `ps_product.quantity`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['quantity']

    
    @field_quantity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_quantity(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   `ps_product.quantity` """
        try:
            self.fields_dict['quantity'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'quantity' данными {value}
            Ошибка:""", ex)
            return False

# 15
    
    @property
    def field_minimal_quantity(self) -> int:
        """!  <sub>*[property]*</sub>  `ps_product.minimal_quantity`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['minimal_quantity']

    
    @field_minimal_quantity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_minimal_quantity(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['minimal_quantity'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'minimal_quantity' данными {value}
            Ошибка:""", ex)
            return False

#   16
    
    @property
    def field_low_stock_threshold(self) -> int:
        """!  <sub>*[property]*</sub>  `ps_product.low_stock_threshold`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['low_stock_threshold']

    
    @field_low_stock_threshold.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_low_stock_threshold(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['low_stock_threshold'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_threshold' данными {value}
            Ошибка:""", ex)
            return False
#   17
    
    @property
    def field_low_stock_alert(self) -> int:
        """!  <sub>*[property]*</sub>  `ps_product.low_stock_alert`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['low_stock_alert']

    
    @field_low_stock_alert.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_low_stock_alert(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['low_stock_alert'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'low_stock_alert' данными {value}
            Ошибка:""", ex)
            return False
#   18
    
    @property
    def field_price(self) -> float:
        """!  <sub>*[property]*</sub>  `ps_product.price`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['price']
    
    
    @field_price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_price(self, value: Union[str,int,float]) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            if not value:
                return False
            self.fields_dict['price'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f'''
            Ошибка заполнения поля: 'price' данными {value}
            Ошибка:''', ex)
            return False
#   19
    
    @property
    def field_wholesale_price(self) -> float:
        """!  <sub>*[property]*</sub>  `ps_product.wholesale_price`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['wholesale_price']

    
    @field_wholesale_price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_wholesale_price(self, value = None) -> float:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['wholesale_price'] = str (SN.normalize_price (value) )
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'wholesale_price' данными {value}
            Ошибка:""", ex)
            return False
#   20
    
    @property
    def field_unity(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product.unity`
        field DB type: varchar(255)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['unity']
    
    @field_unity.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_unity(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['unity'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'unity' данными {value}
            Ошибка:""", ex)
            return False

#   21
    
    @property
    def field_unit_price_ratio(self) -> float:
        """!  <sub>*[property]*</sub>  `ps_product.unit_price_ratio`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['unit_price_ratio']

    
    @field_unit_price_ratio.setter
    #@logs_and_errors_decorator(default_return =  False)
    def field_unit_price_ratio(self, value: float = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['unit_price_ratio'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: `unit_price_ratio` данными {value}
            Ошибка:""", ex)
            return False
#   22
    
    @property
    def field_additional_shipping_cost(self) -> float:
        """!  <sub>*[property]*</sub> `ps_product.additional_shipping_cost`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['additional_shipping_cost']

    
    @field_additional_shipping_cost.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_additional_shipping_cost(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['additional_shipping_cost'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_shipping_cost' данными {value}
            Ошибка:""", ex)
            return False
#   23
    
    @property
    def field_reference(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product.reference`
        field DB type: `varchar(64)`
        @~russian @details: __prod_desc__
        """
        return self.fields_dict['reference']

    
    @field_reference.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_reference(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['reference'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'reference' данными {value}
            Ошибка:""", ex)
            return False
        
    
    @property
    def field_supplier_reference(self):
        """!  <sub>*[property]*</sub>  `ps_product.supplier_reference`
        field DB type: `varchar(64)`
        @~russian @details: __prod_desc__
        """
        return self.fields_dict['supplier_reference']
#   24
    
    @field_supplier_reference.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_supplier_reference(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['supplier_reference'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'supplier_reference' данными {value}
            Ошибка:""", ex)
            return False
#   25
    
    @property
    def field_location(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product.location`
        field DB type: varchar(255)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['location']

    
    @field_location.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_location(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['location'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'location' данными {value}
            Ошибка:""", ex)
            return False

#   26
    
    @property
    def field_width(self) -> float:
        """!  <sub>*[property]*</sub> `ps_product.width`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['width']

    
    @field_width.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_width(self, value: float = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['width'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'width' данными {value}
            Ошибка:""", ex)
            return False
#   27
    
    @property
    def field_height(self) -> float:
        """!  <sub>*[property]*</sub> `ps_product.height`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['height']

    
    @field_height.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_height(self, value: float = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['height'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'height' данными {value}
            Ошибка:""", ex)
            return False
#   28
    
    @property
    def field_depth(self) -> float:
        """!  <sub>*[property]*</sub> `[28] ps_product.depth  decimal(20,6)`
        field DB type:
        @~russian @details: __prod_desc__"""
        return self.fields_dict['depth']

    
    @field_depth.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_depth(self, value: float = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['depth'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'depth' данными {value}
            Ошибка:""", ex)
            return False
#   29
    
    @property
    def field_weight(self) -> float:
        """!  <sub>*[property]*</sub> `ps_product.weight`
        field DB type: decimal(20,6)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['weight']

    
    @field_weight.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_weight(self, value: float = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['weight'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'weight' данными {value}
            Ошибка:""", ex)
            return False

    #  30
    
    @property
    def field_out_of_stock(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.out_of_stock`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['out_of_stock']

    
    @field_out_of_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_out_of_stock(self, value: int = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['out_of_stock'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'out_of_stock' данными {value}
            Ошибка:""", ex)
            return False

  #  31
    
    @property
    def field_additional_delivery_times(self) -> int:
        """!!  <sub>*[property]*</sub> `ps_product.additional_delivery_times tinyint(1)`
        @~russian @details: __prod_desc__"""
        return self.fields_dict['additional_delivery_times']

    
    @field_additional_delivery_times.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_additional_delivery_times(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['additional_delivery_times'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'additional_delivery_times' данными {value}
            Ошибка:""", ex)
            return False
  #  32
    
    @property
    def field_quantity_discount(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.quantity_discount`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['quantity_discount']

    
    @field_quantity_discount.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_quantity_discount(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['quantity_discount'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'quantity_discount' данными {value}
            Ошибка:""", ex)
            return False

  #  33
    
    @property
    def field_customizable(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.customizable`
        field DB type: tinyint(2)
        @~russian @details: __prod_desc__"""
        return self.fields_dict['customizable']

    
    @field_customizable.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_customizable(self, value: int = 0) -> bool:
        try:
            self.fields_dict['customizable'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'customizable' данными {value}
            Ошибка:""", ex)
            return False

  #  34
    
    @property
    def field_uploadable_files(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.uploadable_files`
        field DB type: tinyint(4)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['uploadable_files']

    
    @field_uploadable_files.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_uploadable_files(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['uploadable_files'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'uploadable_files' данными {value}
            Ошибка:""", ex)
            return False
#  35
    
    @property
    def field_text_fields(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.text_fields`
        field DB type: tinyint(4)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['text_fields']

    
    @field_text_fields.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_text_fields(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['text_fields'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'text_fields' данными {value}
            Ошибка:""", ex)
            return False

#  36
    
    @property
    def field_active(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.active`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['active']

    
    @field_active.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_active(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['active'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'active' данными {value}
            Ошибка:""", ex)
            return False
   
        

#  37

        
    @property
    def field_redirect_type(self) -> str:
        """!  <sub>*[property]*</sub> `[37] ps_product.redirect_type enum('404','301-product','302-product','301-category','302-category')`
        
    Редиректы HTTP 301 (Moved Permanently) и 302 (Found, временное перенаправление) различаются в том, как они обрабатываются браузерами и поисковыми системами:

    301 Moved Permanently (Постоянное перенаправление):

    Этот статус указывает на то, что ресурс был окончательно перемещен на новый URL.
    Браузеры и поисковые системы обычно кэшируют этот редирект, что означает, что при следующем запросе к тому же URL клиент будет напрямую перенаправлен на новый без обращения к оригинальному местоположению.
    Этот тип редиректа обычно используется, когда страница или ресурс были перенесены на новый адрес и больше не существуют по старому.
    302 Found (Временное перенаправление):

    Этот статус указывает на то, что ресурс временно перемещен на новый URL.
    Браузеры и поисковые системы могут повторять запросы к оригинальному URL, так как это считается временным перенаправлением.
    Этот тип редиректа подходит, когда ресурс временно недоступен на оригинальном местоположении, и клиент должен использовать новый адрес, но при этом оригинальное местоположение может быть использовано в будущем.
    Выбор между 301 и 302 зависит от того, насколько постоянно изменение местоположения ресурса. Если изменение постоянное, то рекомендуется использовать 301. Если изменение временное, то следует использовать 302.
    """
        return self.fields_dict['redirect_type']


    
    class EnumRedirect(Enum):
        ERROR_404 = '404'
        REDIRECT_301_PRODUCT = '301-product'
        REDIRECT_302_PRODUCT = '302-product'
        REDIRECT_301_CATEGORY = '301-category'
        REDIRECT_302_CATEGORY = '302-category'
        
    @field_redirect_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_redirect_type(self, value: Union[EnumRedirect,str]) -> bool:
        """!  <sub>*[setter]*</sub>   Редирект. 
        Редиректы представляют собой механизм перенаправления пользователя или браузера с одного URL-адреса на другой. Они часто используются в веб-разработке для переноса посетителя с одной страницы на другую. Различные HTTP-статусы и типы редиректов сообщают браузеру или клиенту, как следует интерпретировать запрос и что делать дальше. В вашем коде вы используете строки для представления различных типов редиректов.

        ERROR_404 (404 Not Found):

        Этот редирект сообщает клиенту, что запрашиваемый ресурс не найден.
        Применяется, когда сервер не может найти запрашиваемую страницу или ресурс.
        REDIRECT_301_PRODUCT (301 Moved Permanently):

        Говорит браузеру, что ресурс был окончательно перемещен на новый URL.
        Этот тип редиректа особенно полезен для SEO, поскольку поисковые системы обычно обрабатывают его, перенося рейтинги страницы на новый адрес.
        REDIRECT_302_PRODUCT (302 Found):

        Указывает, что ресурс временно перемещен.
        Используется, когда ресурс временно недоступен, и запрос должен быть отправлен на временный адрес.
        REDIRECT_301_CATEGORY (301 Moved Permanently):

        Аналогичен REDIRECT_301_PRODUCT.
        Отправляет клиента на новый адрес с постоянным характером.
        REDIRECT_302_CATEGORY (302 Found):

        Аналогичен REDIRECT_302_PRODUCT.
        Перенаправление с временным характером для категории.

        ###пример

        ```python
            def handle_redirect(redirect_type):
                if redirect_type == EnumRedirect.ERROR_404:
                    # Обработка ошибки 404: страница не найдена
                    # Вызов функции или отображение соответствующей страницы
                    pass
                elif redirect_type in [EnumRedirect.REDIRECT_301_PRODUCT, EnumRedirect.REDIRECT_301_CATEGORY]:
                    # Обработка постоянного редиректа (301)
                    # Выполнение перенаправления на новый URL
                    pass
                elif redirect_type in [EnumRedirect.REDIRECT_302_PRODUCT, EnumRedirect.REDIRECT_302_CATEGORY]:
                    # Обработка временного редиректа (302)
                    # Выполнение временного перенаправления на новый URL
                    pass

        ```
        """
        try:
            self.fields_dict['redirect_type'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'redirect_type' данными {value}
            Ошибка:""", ex)
            return False

 #  38
    
    @property
    def field_id_type_redirected(self) -> int:
        """!  <sub>*[property]*</sub> `[38] ps_product.id_type_redirected  tinyint(10)`
        field DB type:
        @~russian @details: __prod_desc__"""

        return self.fields_dict['id_type_redirected']
    
    
    @field_id_type_redirected.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_type_redirected(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['id_type_redirected'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'id_type_redirected' данными {value}
            Ошибка:""", ex)
            return False

 #  39
    
    @property
    def field_available_for_order(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.available_for_order`
        field DB type: tinyint(10)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['available_for_order']

    
    @field_available_for_order.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_available_for_order(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['available_for_order'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_for_order' данными {value}
            Ошибка:""", ex)
            return False

 #  40
    
    @property
    def field_available_date(self) -> Date:
        """!  <sub>*[property]*</sub> `ps_product.available_date`
        field DB type: date
        @~russian @details: __prod_desc__"""

        return self.fields_dict['available_date']

    
    @field_available_date.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_available_date(self, value: Date = Date.today) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['available_date'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'available_date' данными {value}
            Ошибка:""", ex)
            return False

 #  41
    
    @property
    def field_show_condition(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.show_condition`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['show_condition']

    
    @field_show_condition.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_show_condition(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['show_condition'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_condition' данными {value}
            Ошибка:""", ex)
            return False

 #  42

    @property
    def field_condition(self) -> str:
        """!  <sub>*[property]*</sub> `[42] ps_product.condition  enum('new','used','refurbished')`
        @~russian @details: __prod_desc__"""

        return self.fields_dict['condition']
        
    class EnumCondition(Enum):
        NEW = 'new'
        USED = 'used'
        REFURBISHED = 'refurbished'
       
    @field_condition.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_condition(self, value: Union[EnumCondition, str] = EnumCondition.NEW) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['condition'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'condition' данными {value}
            Ошибка:""", ex)
            return False

 #  43
    
    @property
    def field_show_price(self) -> int:
        """!  <sub>*[property]*</sub> `[43] ps_product.show_price tinyint(1)`
        field DB type: 
        @~russian @details: __prod_desc__"""

        return self.fields_dict['show_price']
    
    
    @field_show_price.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_show_price(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['show_price'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'show_price' данными {value}
            Ошибка:""", ex)
            return False

#  44
    
    @property
    def field_indexed(self) -> int:
        """!  <sub>*[property]*</sub> `[44] ps_product.indexed  tinyint(1)`
        @~russian @details: __prod_desc__"""
        return self.fields_dict['indexed']
    
    
    @field_indexed.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_indexed(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['indexed'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'indexed' данными {value}
            Ошибка:""", ex)
            return False

#  45
    
    @property
    def field_visibility(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product.visibility`
        field DB type: enum('both','catalog','search','none')
        @~russian @details: __prod_desc__"""

        return self.fields_dict['visibility']

    class EnumVisibity(Enum):
        BOTH = 'both'
        CATALOG = 'catalog'
        SEARCH = 'search'
        NONE = 'none'

    
    @field_visibility.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_visibility(self, value: EnumVisibity = EnumVisibity.BOTH) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['visibility'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'visibility' данными {value}
            Ошибка:""", ex)
            return False


#  46

    
    @property
    def field_cache_is_pack(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.cache_is_pack`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['cache_is_pack']
    
    
    @field_cache_is_pack.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_cache_is_pack(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['cache_is_pack'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_is_pack' данными {value}
            Ошибка:""", ex)
            return False

#  47
    
    @property
    def field_cache_has_attachments(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.cache_has_attachments`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['cache_has_attachments']
    
    
    @field_cache_has_attachments.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_cache_has_attachments(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['cache_has_attachments'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_has_attachments' данными {value}
            Ошибка:""", ex)
            return False

#  48
    
    @property
    def field_is_virtual(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.is_virtual`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['is_virtual']

    
    @field_is_virtual.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_is_virtual(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['is_virtual'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'is_virtual' данными {value}
            Ошибка:""", ex)
            return False

#  49
    
    @property
    def field_cache_default_attribute(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.cache_default_attribute`
        field DB type: int(10)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['cache_default_attribute']

    
    @field_cache_default_attribute.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_cache_default_attribute(self, value: int = 1) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['cache_default_attribute'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'cache_default_attribute' данными {value}
            Ошибка:""", ex)
            return False

#  50
    
    @property
    def field_date_add(self) -> Date:
        """!  <sub>*[property]*</sub> `ps_product.date_add`
        field DB type: datetime
        @~russian @details: __prod_desc__"""

        return self.fields_dict['date_add']
    
    
    @field_date_add.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_date_add(self, value: Date = Date.today()) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['date_add'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_add' данными {value}
            Ошибка:""", ex)
            return False

#  51
    
    @property
    def field_date_upd(self) -> Date:
        """!  <sub>*[property]*</sub> `ps_product.date_upd`
        field DB type: datetime
        @~russian @details: __prod_desc__"""

        return self.fields_dict['date_upd']
    
    
    @field_date_upd.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_date_upd(self, value: Date = Date.today()) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['date_upd'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'date_upd' данными {value}
            Ошибка:""", ex)
            return False


#  52
    
    @property
    def field_advanced_stock_management(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.advanced_stock_management`
        field DB type: tinyint(1)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['advanced_stock_management']
    
    
    @field_advanced_stock_management.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_advanced_stock_management(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['advanced_stock_management'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'advanced_stock_management' данными {value}
            Ошибка:""", ex)
            return False

#  53
    
    @property
    def field_pack_stock_type(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.pack_stock_type`
        field DB type: int(11)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['pack_stock_type']
    
    
    @field_pack_stock_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_pack_stock_type(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['pack_stock_type'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'pack_stock_type' данными {value}
            Ошибка:""", ex)
            return False


#  54
    
    @property
    def field_state(self) -> int:
        """!  <sub>*[property]*</sub> `ps_product.state`
        field DB type: int(11)
        @~russian @details: __prod_desc__"""

        return self.fields_dict['state']
    
    
    @field_state.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_state(self, value: int = 0) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['state'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'state' данными {value}
            Ошибка:""", ex)
            return False


#  55
    
    @property
    def field_product_type(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product.product_type`
        field DB type: enum('standard', 'pack', 'virtual', 'combinations', '')
        @~russian @details: __prod_desc__"""

        return self.fields_dict['product_type']

    class EnumProductType(Enum):
        STANDARD = 'standard'
        PACK = 'pack'
        VIRTUAL = 'virtual'
        COMBINATIONS = 'combinations'
        EMPTY = ''
          
    @field_product_type.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_product_type(self, product_type: EnumProductType = EnumProductType.STANDARD) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['product_type'] = product_type
            return True
        except ProductFieldException as ex:
            logger.error(f"""
            Ошибка заполнения поля: 'product_type' данными {product_type}
            Ошибка:""", ex)
            return False

















####################################################################################################################################
#
#
#
#           ТАБЛИЦА `ps_product_lang` - СОДЕРЖИТ МИЛЬТИЯЗЫЧНЫЕ ПОЛЯ 
#
#
#       
#
# -----------------------------------------------------------------------------------------------------------------------------------

#
#           
#
#   |    Column Name	              |  Data Type	       | Comment
#---------------------------------------------------------------------
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
# 13	`delivery_in_stock`	            varchar(255)        Доставка, если товар н наличии
# 14	`delivery_out_stock`	        varchar(255)        (Доставка если товара нет в наличии): Текст, который будет отображаться, когда товара нет в наличии.
# 15    `delivery_additional_message`   tinytext            Мое поле. Доп для полей доставки. Например, война
# 16	`affiliate_short_link`	        tinytext
# 17	`affiliate_text`	            tinytext
# 18	`affiliate_summary`	            tinytext
# 19	`affiliate_summary_2`	        tinytext
# 20    `affiliate_image_small`         varchar(512)
# 21    `affiliate_image_medium`        varchar(512)
# 22    `affiliate_image_large`         varchar(512)
# 23	`ingridients`	                tinytext
# 24	`how_to_use`        	        tinytext


#   Поля `id_product`  берутся из верхних значениий в этом коде


########################################################################################


#   2 id_shop Я могу определить данные, ОТНОСИТЕЛЬНО магазина

    @property
    def field_id_shop(self):
        """!  <sub>*[property]*</sub> `ps_product_lang.id_shop`
        field DB type: int(10)
        description: Я могу переопределить переводы и прочее в зависимости от магазина"""
        return self.fields_dict['id_shop']

    
    @field_id_shop.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_shop(self, value: Date = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['id_shop'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_lang' данными {value}
            Ошибка:""", ex)
            return False
        
# 3 id_lang 
    """! @note  Здесь я выставляю язык перевода """
    @property
    def field_id_lang(self):
        """!  <sub>*[property]*</sub> `[3] ps_product_lang.id_lang int(10)`
        description: Я выставляю язык перевода"""
        return self.fields_dict['id_lang']

    
    @field_id_lang.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_id_lang(self, value: Date = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['id_lang'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_lang' данными {value}
            Ошибка:""", ex)
            return False
#   4
    
    @property
    def field_description(self) -> str:
        """!  <sub>*[property]*</sub> `[4] ps_product_lang.description text`
        description: Описание """
        return self.fields_dict['description']

    
    @field_description.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_description(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['description']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'description' данными {value}
            Ошибка:""", ex)
            return False
#   5
    
    @property
    def field_description_short(self) -> str:
        """!  <sub>*[property]*</sub> `[5] ps_product_lang.description_short text`
        description: __prod_desc__"""

        return self.fields_dict['description_short']
    
    @field_description_short.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_description_short(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['description_short']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'description_short' данными {value}
            Ошибка:""", ex)
            return False
#   6
    
    @property
    def field_link_rewrite(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product_lang.link_rewrite`
        field DB type: varchar(128)
        description: __prod_desc__"""
        return self.fields_dict['link_rewrite']

    
    @field_link_rewrite.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_link_rewrite(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            #self.fields_dict['link_rewrite = link_rewrite
            self.fields_dict['link_rewrite']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'link_rewrite' данными {value}
            Ошибка:""", ex)
            return False
#   7
    
    @property
    def field_meta_description(self) -> str:
        """!  <sub>*[property]*</sub> `[7] ps_product_lang.meta_description varchar(512)` 
        field DB type: 
        description: __prod_desc__"""
        return self.fields_dict['meta_description']
    
    
    @field_meta_description.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_meta_description(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['meta_description']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_description' данными {value}
            Ошибка:""", ex)
            return False

#   8
    
    @property
    def field_meta_keywords(self):
        """!  <sub>*[property]*</sub> `[8] ps_product_lang.meta_keywords varchar(255)`
        field DB type: 
        description: __prod_desc__"""
        return self.fields_dict['meta_keywords']
    
    @field_meta_keywords.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_meta_keywords(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['meta_keywords']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_keywords' данными {value}
            Ошибка:""", ex)
            return False

#   9
    
    @property
    def field_meta_title(self) -> str:
        """!  <sub>*[property]*</sub> `[9] s_product_lang.meta_title varchar(128)`
        description: __prod_desc__"""
        return self.fields_dict['meta_title']
    
    
    @field_meta_title.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_meta_title(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['meta_title']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'meta_title' данными {value}
            Ошибка:""", ex)
            return False

#   10
    
    @property
    def field_name(self):
        """!  <sub>*[property]*</sub> `[10] ps_product_lang.name  varchar(128)`
        description: __prod_desc__"""
        return self.fields_dict['name']
    
    
    @field_name.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_name(self, value: str) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['name']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'name' данными {value}
            Ошибка:""", ex)
            return False

#   11
    
    @property
    def field_available_now(self) -> str:
        """!  <sub>*[property]*</sub>  `[11] ps_product_lang.available_now varchar(255)`
        description: __prod_desc__"""
        return self.fields_dict['available_now']
    
    
    @field_available_now.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_available_now(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['available_now']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_now' данными {value}
            Ошибка:""", ex)
            return False

#   12
    
    @property
    def field_available_later(self) -> str:
        """!  <sub>*[property]*</sub>  field DB available_later: `[12] ps_product_lang.available_later varchar(255)`
        field DB type: varchar(255)
        description: __prod_desc__"""
        return self.fields_dict['available_later']
    
    @field_available_later.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_available_later(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['available_later']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'available_later' данными {value}
            Ошибка:""", ex)
            return False


#   13
    
    @property
    def field_delivery_in_stock(self):
        """!  <sub>*[property]*</sub>   `[13] ps_product_lang.delivery_in_stock varchar(255)`
        @details:  (Доставка при наличии товара): Текст, который будет отображаться, когда товар есть в наличии."""
        return self.fields_dict['delivery_in_stock']
    
    @field_delivery_in_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_delivery_in_stock(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['delivery_in_stock']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_in_stock' данными {value}
            Ошибка:""", ex)
            return False


#   14
    
    @property
    def field_delivery_out_stock(self) -> str:
        """!  <sub>*[property]*</sub>   `[14] ps_product_lang.delivery_out_stock varchar(256)` 
        description: __prod_desc__"""
        return self.fields_dict['delivery_out_stock']
    
    @field_delivery_out_stock.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_delivery_out_stock(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['delivery_out_stock']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_out_stock' данными {value}
            Ошибка:""", ex)
            return False
        
#   15

    @property
    def field_delivery_additional_message(self) -> str:
        """!  <sub>*[property]*</sub>   `[15] ps_product_lang.delivery_out_stock`
        field DB type: 
        description: __prod_desc__"""
        return self.fields_dict['delivery_additional_message']
    
    @field_delivery_additional_message.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_delivery_additional_message(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub> Заметки по доставке. Например: война, хз когда доставим  
        Мультиязычное поле. Формирует словарь:
        ```python
            {
            "language":[
            {'attrs':{'id':'1'}, 'value':delivery_additional_message},
            {'attrs':{'id':'2'}, 'value':delivery_additional_message},
            {'attrs':{'id':'3'}, 'value':delivery_additional_message},
            ]}
        ```
        """
        try:
            self.fields_dict['delivery_additional_message']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'delivery_out_stock' данными {value}
            Ошибка:""", ex)
            return False

#   16

    
    @property
    def field_affiliate_short_link(self) -> dict:
        """!  <sub>*[property]*</sub>   `[15] ps_product_lang.affiliate_short_link  varchar(255)`
        description: __prod_desc__"""
        return self.fields_dict['affiliate_short_link']
    
    @field_affiliate_short_link.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_short_link(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub> Короткие линки не партнерские преогаммы. Мультиязычное поле.
        Формирует словарь:
        ```python
         {
            "language":[
            {'attrs':{'id':'1'}, 'value':affiliate_short_link},
            {'attrs':{'id':'2'}, 'value':affiliate_short_link},
            {'attrs':{'id':'3'}, 'value':affiliate_short_link},
            ]}
            ```
        """
        try:
            self.fields_dict['affiliate_short_link']: dict = {
                "language":[
                {'attrs':{'id':'1'}, 'value':value},
                {'attrs':{'id':'2'}, 'value':value},
                {'attrs':{'id':'3'}, 'value':value},
            ]}

            
            # self.fields_dict['affiliate_short_link']: dict = {
            #     "language":[
            #     {'#text': affiliate_short_link, '@id':'1'},
            #     {'#text': affiliate_short_link, '@id':'2'},
            #     {'#text': affiliate_short_link, '@id':'3'},
            # ]}
            
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_short_link' данными {value}
            Ошибка:""", ex)
            return False

#   17
    
    @property
    def field_affiliate_text(self) -> str:
        """!  <sub>*[property]*</sub>   `[17] ps_product_lang.affiliate_text varchar(256)`"""
        return self.fields_dict['affiliate_text']
    
    @field_affiliate_text.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_text(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            #self.fields_dict['affiliate_text = affiliate_text
            self.fields_dict['affiliate_text']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
        ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_text' данными {value}
            Ошибка:""", ex)
            return False


#   18
    
    @property
    def field_affiliate_summary(self) -> str:
        """!  <sub>*[property]*</sub>  `[18] ps_product_lang.affiliate_summary varchar(256)`"""
        return self.fields_dict['affiliate_summary']
    
    
    @field_affiliate_summary.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_summary(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['affiliate_summary']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
        ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary' данными {value}
            Ошибка:""", ex)
            return False


#   18

    
    @property
    def field_affiliate_summary_2(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.fields_dict['affiliate_summary_2']

    
    @field_affiliate_summary_2.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_summary_2(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['affiliate_summary_2']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка:""", ex)
            return False

#   20

    
    @property
    def field_affiliate_image_small(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.fields_dict['affiliate_image_small']

    
    @field_affiliate_image_small.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_image_small(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['affiliate_image_small']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка:""", ex)
            return False

 #   21

    
    @property
    def field_affiliate_image_medium(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.fields_dict['affiliate_image_medium']

    
    @field_affiliate_image_medium.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_image_medium(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['affiliate_image_medium']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {affiliate_image_medium}
            Ошибка:""", ex)
            return False

    
 #   22

    
    @property
    def field_affiliate_image_large(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product_lang.affiliate_summary_2`"""
        return self.fields_dict['affiliate_image_medium']

    
    @field_affiliate_image_large.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_affiliate_image_large(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['affiliate_image_medium']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'affiliate_summary_2' данными {value}
            Ошибка:""", ex)
            return False

    
# 23
    
    @property
    def field_ingridients(self) -> str:
        """!  <sub>*[property]*</sub>  `ps_product_lang.ingridients`"""
        return self.fields_dict['ingridients']

    
    @field_ingridients.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_ingridients(self, value: str = None) -> bool:
        """!  <sub>*[setter]*</sub>  Ингридиенты. Текстовое поле - можно хранить фрагменты кода 
        формирует список словарей:
        ```python
        {
        "language":[
            {'attrs':{'id':'1'}, 'value':ingridients},
            {'attrs':{'id':'2'}, 'value':ingridients},
            {'attrs':{'id':'3'}, 'value':ingridients},
        ]}
        ```
        значение `ingridients` может быть блоком HTML
        """
        try:
            self.fields_dict['ingridients']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f'Ошибка заполнения `ingridients` данными {value} Ошибка:', ex)
            return False

    
    @property
    def field_how_to_use(self) -> str:
        """!  <sub>*[property]*</sub> `ps_product_lang.how_to_use` """
        return self.fields_dict['how_to_use']

    
    @field_how_to_use.setter
    #@logs_and_errors_decorator (default_return =  False)
    def field_how_to_use(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>  `ps_product_lang.how_to_use` """
        try:
            self.fields_dict['how_to_use']: dict = {
            "language":[
            {'attrs':{'id':'1'}, 'value':value},
            {'attrs':{'id':'2'}, 'value':value},
            {'attrs':{'id':'3'}, 'value':value},
            ]}
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'how_to_use' данными {value}
            Ошибка:""", ex)
            return False

    
    @property
    def default_image_url(self) -> str:
        """!  <sub>*[property]*</sub>   `_???????.id_default_image` """
        return self.fields_dict['id_default_image']
    
    
    @default_image_url.setter
    #@logs_and_errors_decorator (default_return =  False)
    def default_image_url(self, value = '' ) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['default_image_url'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_image' данными {value}
            Ошибка:""", ex)
            return False
        
    
    @property
    def id_default_image(self) -> str:
        """!  <sub>*[property]*</sub>  field DB affiliate_summary_2: `_???????.id_default_image`"""
        return self.fields_dict['id_default_image']
    
    
    @id_default_image.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_default_image(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['id_default_image'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_image' данными {value}
            Ошибка:""", ex)
            return False


    
    @property
    def images_urls(self):
        """!  <sub>*[property]*</sub>   __prod_name__
        field DB type: __prod_type__
        description: __prod_desc__"""
        return self.fields_dict['images_urls']
    
    
    @images_urls.setter
    #@logs_and_errors_decorator (default_return =  False)
    def images_urls(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['images_urls'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'Image URLs (x,y,z...)' данными {value}
            Ошибка:""", ex)
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
        """!  <sub>*[property]*</sub>  field DB affiliate_summary_2: `_?????????.id_default_combination`"""
        return self.fields_dict['id_default_combination']
    
    
    @id_default_combination.setter
    #@logs_and_errors_decorator (default_return =  False)
    def id_default_combination(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['id_default_combination'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'id_default_combination' данными {value}
            Ошибка:""", ex)
            return False

#  ---------

    
    @property
    def position_in_category(self) -> str:
        """!  <sub>*[property]*</sub>   field DB affiliate_summary_2: `_?????????.position_in_category`"""
        return self.fields_dict['position_in_category']

    
    @position_in_category.setter
    #@logs_and_errors_decorator (default_return =  False)
    def position_in_category(self, value = None) -> bool:
        """!  <sub>*[setter]*</sub>   """
        try:
            self.fields_dict['position_in_category'] = value
            return True
        except ProductFieldException as ex:
            logger.error(f"""Ошибка заполнения поля: 'position_in_category' данными {value}
            Ошибка:""", ex)
            return False





#####################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
