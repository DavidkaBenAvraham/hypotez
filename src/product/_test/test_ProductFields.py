import sys
import os
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+11])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) )  # Добавляю рабочую папку в sys.path 


from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.tools import SF, SN, StringValidator as SV
from src.helpers import logger,  logs_and_errors_decorator

def start_supplier(supplier_prefix: str = 'aliexpress', scenario_language: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'scenario_language': scenario_language
    }
    
    return Supplier(**params)

s = start_supplier('aliexpress')
p = Product(supplier = s)
_l : dict = s.locators['product']
_d = s.driver
_f = p.product_fields


test_scenario: dict = {
  "category ID on site": 40000002781737,
  "brand": "APPLE",
  "url": "https://hi5group.aliexpress.com/store/group/iPhone-13-13-mini/1053035_40000002781737.html",
  "active": True,
  "condition": "new",
  "presta_categories": {
    "template": {
      "apple": "iPhone 13"
    }
  },
  "product combinations": [
    "bundle",
    "color"
  ]
}

test_products_list: list = ['https://s.click.aliexpress.com/e/_oFLpkfz', 
                            'https://s.click.aliexpress.com/e/_oE5V3d9', 
                            'https://s.click.aliexpress.com/e/_oDnvttN', 
                            'https://s.click.aliexpress.com/e/_olWWQCP', 
                            'https://s.click.aliexpress.com/e/_ok0xeMn']

_d.get_url(test_products_list[0])

_f.supplier_reference = _d.current_url.split('/')[-1].split('.')[0]
_f.reference = f'''{s.supplier_id}-{_f.supplier_reference}'''
_f.name = SF.convert_to_html_entities (_d.execute_locator (_l['name']) )
