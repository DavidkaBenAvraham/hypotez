"""! @brief Модуль сбора товаров со страницы категорий поставщика hb.co.il через вебдрайвер

 @section libs imports:
  - typing 
  - pathlib 
  - gs 

"""
from typing import Union
from pathlib import Path

from src.settings import gs
from src.helpers import logger

def get_list_products_in_category (s) -> Union [list[str], str, None]:    
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
    """ Собирал ссылки на товары.  """
    
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        return False
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    

    return list_products_in_category

def get_list_categories_from_site(s):
    pass