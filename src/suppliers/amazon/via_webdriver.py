"""! @brief  [File's Description]

@namespace src: src
 \package src.suppliers.amazon
\file via_webdriver.py
 
 @section libs imports:
  - typing 
  - pathlib 
  - gs 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
from typing import Union
from pathlib import Path

from src.settings import gs, logger


def get_list_products_in_category(s) -> Union[list[str],str,None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    d = s.driver
    l: dict = s.locators['category']
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return False
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собираю ссылки на товары.  """
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары')
        return False
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category


    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    
    #""" Проверяю наличие товара в базе данных магазина """
    #for asin in list_products_in_category:
    #    _asin = asin.split(f'''/''')[-2]
    #    _sku = f'''{s.supplier_id}_{_asin}''' 
    #    if PrestashopProduct.check(_sku) == False:
    #        """ Синтаксис для того, чтобы помнить,
    #        что я проверяю ОТСУТСТВИЕ товара в базе данных
    #        """
    #        continue
    #    else:
    #        """ Товар в базе данных """
    #        continue
            #TODO: Логику 


    return list_products_in_category

    