"""! @~russian Запуск теста сценариев из IDE Visual Studio """
"""!@~russian @details """


from math import prod
import os, sys
from pathlib import Path

################# добавление корневой директории позволяет мне плясать от печки ###################
dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind('hypotez') + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))
from src.webdriver import execute_locator
"""! @~russian добавление корневой директории позволяет мне плясать от печки. """
####################################################################################################


from src.settings import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.io_interface import j_loads, j_dumps
from src.helpers import ExecuteLocatorException
from src.webdriver import Driver
from src.tools import StringFormatter as SF, StringNormalizer as SN


s: Supplier = Supplier(supplier_prefix = 'aliexpress')
p: Product = Product(s)
l: dict = s.locators['product']
d: Driver = s.driver
f: ProductFields = ProductFields(s)

def reread_locators(s:Supplier = s, entity: str = 'product'):
    s.locators [entity] = execute_locator.reread_locators (s, entity)
    global l
    return s.locators [entity]

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
pass
"""! @debug Тестовый сценарий. Нужен для правильного распределиня категорий """



d.get_url (test_scenario['url'])
"""! перехожу по URL сценария (обычно, категория)"""

list_products_in_category: list = s.related_modules.get_list_products_in_category(s)
"""! собрал список товаров в категории """

d.get_url(list_products_in_category[0])
"""! перешел по первому url из списка """

pass


def set_default_values():
    global f
    f.active = 1
    f.supplier_reference = s.supplier_id

set_default_values()



def field_additional_shipping_cost():
    """! @russian
    @brief стоимость доставки
    @details
    """
    _result = SN.normalize_price (d.execute_locator(l['additional_shipping_cost']) )
    if not _result:
        raise ExecuteLocatorException(f"Не получил значения {d.execute_locator(l['additional_shipping_cost'])}'")

    return _result
    

f.additional_shipping_cost = field_additional_shipping_cost() 


#get_attributes_from_webelements (driver, _l)[0].text

def field_affiliate_short_link():
    """! @russian
    @brief Короткая ссылка на партнрскую программу
    @details
    """
    return d.execute_locator (l['affiliate_short_link'])[0]
    pass
  
f.affiliate_short_link = field_affiliate_short_link()



def field_affiliate_summary():
    """! @russian Описание к партнерской программе """
    
    return d.execute_locator(l['field_affiliate_summary'])[0]
    

pass


#f.additional_shipping_cost = field_additional_shipping_cost()
#f.affiliate_short_link = field_affiliate_short_link()
field_affiliate_short_link()

pass

