"""! @~russian Поставщик <I>granadvance.co.il</I>

 
 @section libs imports:
  - .login 
  - .scrapper 
  - .via_webdriver 

"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from .login import login as login
from .scrapper import scrape_product_page as scrape_product_page
from .via_webdriver import get_list_products_in_category as get_list_products_in_category
