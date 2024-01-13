"""! @brief  [File's Description]


@namespace src: src
 \package src.suppliers.hb
\file login.py

 @section libs imports:
  - helpers 
Author(s):
  - Created by Davidka  on 09.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.helpers import  logger,  logs_and_errors_decorator

def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
    _l : dict = s.locators_store['login']
    _d = s.driver
    _d.window_focus()
    _d.get_url('https://amazon.com/')
    #_d.wait(.7)

    #_d.fullscreen_window()
    
    #_d.fullscreen_window()
    if not _d.click(_l['open_login_inputs']):
        _d.refresh()
        _d.window_focus()
        if not _d.click(_l['open_login_inputs']):
            ''' Тут надо искать логин кнопку в другом месте '''
            logger.debug(''' Тут надо искать логин кнопку в другом месте ''')
        pass
    #_d.wait(2)

    
    if not _d.execute_locator(_l['email_input']): 
        return False
        pass # TODO логика обработки False

    _d.wait(.7)
    if not _d.execute_locator(_l['continue_button']):
       pass # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['password_input']): 
        pass # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['keep_signed_in_checkbox']):
        pass
    _d.wait(.7)
    if not _d.execute_locator(_l['success_login_button']):
       pass # TODO логика обработки False
    if _d.current_url == "https://www.amazon.com/ap/signin":
        logger.error(f''' Неудачный логин ''')
        pass
        return False
    _d.wait(1.7)
    _d.maximize_window()
    #_d.dump_cookies_to_file()
    logger.info(f'''Залогинился .... ''')
    return True