"""! @brief   close popup on kualastyle homepage


@namespace src: src
 \package src.suppliers.kualastyle
\file login.py
 
 @section libs imports:
  - gs 
  - gs 
Author(s):
  - Created by [Name] [Last Name] on 08.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""
EN:
    
RU:
    закрываю все поп ап окна
"""
from src.settings import *
import settings
logger = settings.logger


def login(s) -> bool:
    """ Функция логин
   @param
        s - Supplier
    @returns
        True if login else False

   """
    _d = s.driver
    _l : dict = s.locators['close_popup_locator']
    
    _d.get_url('https://www.kualastyle.com')
    _d.window_focus(_d)
    _d.wait(5)
    #_d.page_refresh()
    return _d.execute_locator(_l)
    
    pass
