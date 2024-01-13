"""! @brief  Интерфейс авторизации. Реализация для вебдрайвера
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python



#################################################################################
#                                                                               #
#                                                                               #
#           Логин нужен для авторизации на сайт через вебдрайвер.               #
#           В данный момент я работаю через API aliexpress                      #
#                                                                               #
#################################################################################

def login(s)->bool:
    """
     execute login to aliexpress scenario

    Parameters : 
         s : Supplier
    Returns : 
         bool : True if login succes, else False

    """


    return True
    """ Сейчас доступ к сайту я делаю через API 
    Логин потерял смысл
    """
    
    _d = s.driver
    _l : dict = s.locators['login']

    _d.fullscreen_window()
    ''' полноэкранный режим '''
    _d.get_url('https://www.aliexpress.com')
    _d.execute_locator(_l['coockies_accept'])
    _d.wait(.7)


    _d.execute_locator(_l['open_login'])
    _d.wait(2)

    
    if not _d.execute_locator(_l['email_locator']): 
        pass # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['password_locator']): 
        pass # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['loginbutton_locator']): 
        pass # TODO логика обработки False
    
    #set_language_currency_shipto(s,True)
    
    #_d.dump_cookies_to_file()



# def set_language_currency_shipto(s, if_login = False) -> bool:
#     """ set the currency, country, shipto on aliexpress.com via webdriver

#     Parameters : 
#          s : [description]
#          if_login (bool) = False : Можно и без логина, обычный пользоваытель. у залогиненного пользователя меньше параметров
#     Returns : 
#          bool : True if success, else False

#     """
#     _d = s.driver
#     _l : dict = s.locators['currency_language_shipto_locators']
     
#     '''TODO: сделать механизм сохранения загрузки файлов печенек
#     '''
#     #_d.load_cookies_from_file(_d.cookies_file_path)

#     if not _d.execute_locator(_l['currency_language_shipto_block_opener_locator'],use_mouse=True):
#         logger.error(f''' Не открылся локатор выбора страны - языка- валюты ''')
#         return False
#     _d.wait(1)


#     if if_login:
#         ''' Если зарегистрировался - меняю только язык '''
#         if not _d.execute_locator(_l['language_locator'],use_mouse=True):
#             logger.error(f''' Не открылся локатор выбора языка ''')
#             return False

#     else:
#         if not _d.execute_locator(_l['shipto_locator'],use_mouse=True):
#             logger.error(f''' Не открылся shipto_locator локатор ''')
#         _d.wait(.7)

#         if not _d.execute_locator(_l['language_locator'],use_mouse=True):
#             logger.error(f''' Не открылся локатор выбора языка ''')
#         _d.wait(.7)

#         if not _d.execute_locator(_l['currency_locator'],use_mouse=True):
#             logger.error(f''' Не открылся локатор выбора валюты ''')
#         _d.wait(.7)

#     if _d.click(_l['save_button_locator']):
#         _d.wait(.7)
#         return True
    

    
