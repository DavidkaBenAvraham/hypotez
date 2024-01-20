"""! @~russian  функции и методы JavaScript 


 @section libs imports:
  - gs 
  - helpers 

"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


# -------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator
# ------------------------------

#@logs_and_errors_decorator (default_return =  False)
def unhide_DOM_element(driver, element):
    '''! @~russian Если DOM элемент invisible, необходимо сделать его видимым.  '''
    script :str = f''' 
    arguments[0].style.opacity=1;
    arguments[0].style['transform']='translate(0px, 0px) scale(1)';
    arguments[0].style['MozTransform']='translate(0px, 0px) scale(1)';
    arguments[0].style['WebkitTransform']='translate(0px, 0px) scale(1)';
    arguments[0].style['msTransform']='translate(0px, 0px) scale(1)';
    arguments[0].style['OTransform']='translate(0px, 0px) scale(1)';
    arguments[0].scrollIntoView(true);
    return true; 
    '''
    try:
        driver.execute_script(script, element)
        return True
    except Exception as ex:
        logger.error(f''' ошибка JS в unhide_DOM_element() {ex.with_traceback(ex.__traceback__)}''')
        return False
       
#@logs_and_errors_decorator (default_return =  False)
def get_ready_state(driver) -> str:
    '''! Проверка полной загрузки объекта document
    пока идет загрузка DOM дерева возвращает "loading", 
    а когда загрузка закончилась - "complete"  '''

    script = 'return document.readyState;'
    
    try:
        return driver.execute_script(script)
    except Exception as ex: 
        logger.error(f''' ошибка JS в return document.readyState; {ex.with_traceback(ex.__traceback__)}''')
        return False
        
#@logs_and_errors_decorator (default_return =  False)
def window_focus(driver):
    script = 'return window.focus();'
    try:
        return driver.execute_script(script)
    except Exception as ex: 
        logger.error(f''' ошибка JS в window.focus() {ex.with_traceback(ex.__traceback__)}''')
        return False

def get_referrer(driver):
# Исполнение JavaScript для получения значения document.referrer
    referrer_url = driver.execute_script("return document.referrer;")
    return referrer_url