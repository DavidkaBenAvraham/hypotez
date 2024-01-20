"""! @brief  Реализация класса `Driver`

 @image html webdriver.png 

 @section libs imports:
  - pathlib 
  - os 
  - sys 
  - pickle 
  - time 
  - requests 
  - attr 
  - selenium.webdriver.common.action_chains 
  - selenium.webdriver.common.keys 
  - selenium.webdriver.common.by 
  - selenium.webdriver.support 
  - selenium.webdriver.support.ui 
  - selenium.webdriver.remote.webelement 
  - gs 
  - helpers 
  - tools 
  - . 
  - .Firefox 
  - .Edge 
  - .Chrome 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


###########################################################################################
#
#   вебдрайвер отвечает за http запросы и обработку элементов через селениум
#   селениум послушно работает по принципу локаторов, которые определяются для каждого
#   элемнта страницы в файлах /suppliers/<supplier>/locators/<entity>.json
#     
#
#
#
#
#import kora
#from kora.selenium import wd as KWD
#from seleniumwire import webdriver as SWWD
#''' seleniumwire работает с прокси '''
#from selenium import webdriver as SWD
#import selenium
#############################################################
#                                                           #
#       Я могу подключить один из этих модулей:             #
#       selenium: (module SWD)                              #
#       seleniumwire: (module SWWD)                         #
#       kora: (module KWD)                                  #
#                                                           #
#   -------------------------------------------------       #                                                                
#                      Выбор вебдрайвера:                   #
#                  WD = KWD | SWD | SWWD                    #                                #
#                                                           #
############################################################# 
 


#   ## Опции запуска ведрайвера(ов)
#   
#   - В разработке я использую FireFox 
#       Для работы в goggle research (collab.google) можно посмотреть на 
#       библиотеку kora, она вроде под него заточена
#
#   - в качестве вебдрайвера неплох seleniumwire
#   --  https://github.com/DavidkaBenAvraham/selenium-wire
#
#   - как работает driver_options
#   --  https://stackoverflow.com/questions/12211781/how-to-maximize-window-in-chrome-using-webdriver-python
#   
#   - как работает библиотека ast
#   -- #https://www.techiedelight.com/ru/parse-string-to-float-or-int-python/
#
#   - как загружать бинарный файл драйвера
#   -- https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
#



# 
##          Типы поддерживаемых вебдрайверов (не все!) 

# -         webdriver.Firefox</li>
# -         webdriver.Chrome</li>
# -         webdriver.Ie</li>
# -         webdriver.Edge</li>
# -         webdriver.Opera</li>
# -         webdriver.PhantomJS</li>
# -         webdriver.Remote</li>

#<h5> Умеет в </h5>

# -         webdriver.DesiredCapabilities</li>
# -         webdriver.ActionChains</li>
# -         webdriver.TouchActions</li>
# -         webdriver.Proxy</li>
# -         https://selenium-python.readthedocs.io/api.html#desired-capabilities</li>



##############################################################################################################

#                                                   Всякие кнопки для посылки вебдрайверу

#NULL = '\ue000'
#CANCEL = '\ue001'  # ^break
#HELP = '\ue002'
#BACKSPACE = '\ue003'
#BACK_SPACE = BACKSPACE  
#TAB = '\ue004'   
#CLEAR = '\ue005'  
#RETURN = '\ue006'
#ENTER = '\ue007'   
#SHIFT = '\ue008'   
#LEFT_SHIFT = SHIFT
#CONTROL = '\ue009'
#LEFT_CONTROL = CONTROL  
#ALT = '\ue00a'           
#LEFT_ALT = ALT
#PAUSE = '\ue00b'
#ESCAPE = '\ue00c'   
#SPACE = '\ue00d'    
#PAGE_UP = '\ue00e'   
#PAGE_DOWN = '\ue00f' 
#END = '\ue010'    
#HOME = '\ue011'   
#LEFT = '\ue012'  #Левая кнопка
#ARROW_LEFT = LEFT  
#UP = '\ue013'    #   ключ
#ARROW_UP = UP   
#RIGHT = '\ue014'
#ARROW_RIGHT = RIGHT  
#DOWN = '\ue015'      
#ARROW_DOWN = DOWN  
#INSERT = '\ue016'    
#DELETE = '\ue017'    #del

#SEMICOLON = '\ue018'  # ''
#EQUALS = '\ue019'     # '='
## Цифровая клавиатура
#NUMPAD0 = '\ue01a'  # number pad keys
#NUMPAD1 = '\ue01b'
#NUMPAD2 = '\ue01c'
#NUMPAD3 = '\ue01d'
#NUMPAD4 = '\ue01e'
#NUMPAD5 = '\ue01f'
#NUMPAD6 = '\ue020'
#NUMPAD7 = '\ue021'
#NUMPAD8 = '\ue022'
#NUMPAD9 = '\ue023'
#MULTIPLY = '\ue024' # '*'
#ADD = '\ue025'   # '+'
#SEPARATOR = '\ue026' # ключ '' #
#SUBTRACT = '\ue027' # клавиша # '-'
#DECIMAL = '\ue028'  # клавиша #
#DIVIDE = '\ue029'   # ключ # '/'

#F1 = '\ue031'  # function  keys
#F2 = '\ue032'
#F3 = '\ue033'
#F4 = '\ue034'
#F5 = '\ue035'
#F6 = '\ue036'
#F7 = '\ue037'
#F8 = '\ue038'
#F9 = '\ue039'
#F10 = '\ue03a'
#F11 = '\ue03b'
#F12 = '\ue03c'

#META = '\ue03d'
#COMMAND = '\ue03d'
########################################################################################

from pathlib import Path
import os
import sys
import pickle # использую для хранения / чтения кук
import time
import requests
from attr import attr, attrs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

# # ------------------------------
# hypotez_root_path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
# sys.path.append(hypotez_root_path)  # Добавляю корневую папку в sys.path


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.tools import StringFormatter as SF
from . import execute_locator, js
# -------------------------------

    #####################################################################
    #                                                                   #
    #                   Выбор драйвера                                  #
    #                                                                   #
    #####################################################################


if gs.default_webdriver == 'firefox':
    from .Firefox import Firefox as WebDriver #! <- Firefox """
elif gs.default_webdriver == 'edge':
    from .Edge import Edge as WebDriver #! <- Edge 
elif gs.default_webdriver == 'chrome':
    from .Chrome import Chrome as WebDriver #! <- Chrome 




class Driver(WebDriver):
    """! @brief в зависимости от насторек в settinglobal_settings.json Может быть выбран один из Firefox, Egde, Chrome, etc.

    Драйвер обрабатывает запросы локаторов, отдает аттрибуты или целиком вебэлемнт(ы)
   """
   
    #@logs_and_errors_decorator (default_return =  False)
    def __init__(self, *args, **kwards):
        """ @brief The constructor
        @details Старт вебрайвера. 
        Наследуется от selenium.webdriver.<webdirver>   <- Firefox, Egde, Chrome, etc 
        
        ---
        
        
        """
        
        logger.info(f""" 
        ----------------------
        Старт вебдрайвера {gs.default_webdriver}. 
        Будет выбран драйвер, подключатся настройки и профиль.
        На моем компьютере это занимает около полуминуты
        Ждем....
        ----------------------
        """)
        
        self.delete_driver_logs
        """! @~russian Очищаю директорию логов.
        @todo 1. Продумать очистку только логов вебдрайвера  
        2. Делать очистку по условию """

        super().__init__(*args, **kwards)

        self.WebDriverWait = WebDriverWait
        self.EC = expected_conditions
        self.By = By
        self.Keys = Keys
        self.ActionChains = ActionChains
        self.previous_url:str = None
        

    #@logs_and_errors_decorator (default_return =  False)
    @property
    def get_ready_state(self) -> bool:
        """ 
        Опрашиваю через JS значение window.ready_state()
        
        @returns 
            str: loading | complete 
        """
        
        try:
            """! """
            return js.get_ready_state (self)
        except Exception as ex:
            logger.error (f'ошибка ', ex)
            return False
                
        




        #####################################################################################
        #                                                                                   #
        #                 Полный/F11 экран                                                  #
        #       Когда я запускаю окно в режиме F11   совпадают коордианты  мышки            #
        #       и элементов на странице                                                     #
        #                                                                                   #
        #       self.fullscreen_window()                                                    #
        #       или                                                                         #
        #       self.maximize_window()                                                      #
        #                                                                                   #
        #####################################################################################

        
        # Set the interceptor on the driver
        #https://stackoverflow.com/questions/15645093/setting-request-headers-in-selenium
        #self.request_interceptor = interceptor




    #####################################################################
    #                                                                   #
    #       Логика локаторов находится в файле execute_locator.py       #
    #                                                                   #
    #####################################################################

    def execute_locator (self, locator )->bool:
        return execute_locator.execute_locator ( self, locator )

    def execute_action (self, locator )->bool:
        return execute_locator.execute_action ( self, locator )
        
    def get_attributes_from_webelements ( self ,locator) -> list:
        return execute_locator.get_attributes_from_webelements ( self, locator )


    def get_attribute_from_webelement ( self, locator ) -> str:
        return execute_locator.get_webelements_from_page ( self, locator )

    def get_webelements_from_page ( self, locator )->list:
        return execute_locator.get_webelements_from_page ( self, locator )

    def get_webelement_as_screenshot ( self, locator )->bool:
        return execute_locator.get_webelement_as_screenshot ( self, locator )

    def get_webelement_with_wait_to_be_clickable ( self, locator ) -> WebElement:
        return execute_locator.get_webelement_with_wait_to_be_clickable ( self, locator )

    def get_webelement_with_wait_to_precence_located ( self, locator ) -> WebElement:
        return execute_locator.get_webelement_with_wait_to_precence_located(self,locator)

    def click ( self, locator ) -> bool:
        return execute_locator.click ( self, locator )

    def wait (self, wait=0, call_func=None,  when='after' ) -> None:
        """
        Ожидание с необязательным вызовом функции
        @param
            call_func - вызываемая функция
            wait:int - пауза
            when:str after|before - пауза может быть до вызова функции или после
        @returns
            результат вызова call_func 
        """
        if call_func is None: 
            return time.sleep(wait)

        call_func = 'self.'+call_func
        if when == 'after':
            res = eval(call_func)
            time.sleep(wait)
            return res
        else:
            time.sleep(wait)
            return eval(call_func)

    def get_url ( self, url: str ) -> bool:
        """
        Обертка для метода driver.get(): переходит по указанному URL.

        @param url `str` Адрес URL.

        @returns bool: `True`, если переход выполнен успешно и текущий URL соответствует ожидаемому.
                Возвращает `False` в случае ошибки перехода или несоответствия текущего URL ожидаемому.

        """
        try:
            #previous_url = SF.clean_url_from_protocols(url)
            # Очищенный адрес страницы, откуда планируется переход            
            previous_url = url
            self.get(url)
            
            if self.current_url != url:
                # проверка попал - не попал на страницу
                logger.error("Не попал на запрашиваемую страницу!")
                return False

            self.previous_url = self.current_url
            return True

        except Exception as ex:
            logger.error(f"Ошибка при переходе на URL {url}: {ex}")
            return False

    def window_focus(self):
        """ Возвращаю фокус на страницу """
        #_d = super()
        return js.get_ready_state (self)
    

    async def scroll(self, scroll_count: int = 5, framesize_to_scroll: int = 1800, direction: str = 'forward', delay: float = 1) -> bool:
        """! Scroll frame on the web page.

        @param scroll_count `int`  :  Number of times to scroll.
        @param framesize_to_scroll `int`  :  The scroll frame in pixels.
        @param direction `str`  :  Direction of scrolling. Possible values are 'both', 'forward', 'backward', 'carousel'.
        @param delay `int`  :  Delay in seconds between each scroll.

        @returns bool: `True` if scrolling is successful, `False` otherwise.
        """
        async def carousel(direction):
            for i in range(scroll_count):
                await self.execute_script(f'window.scrollBy({delay},{direction}{framesize_to_scroll})')
                await self.wait(delay)

        try:
            if direction == 'forward':
                await carousel('')
            if direction == 'backward':
                await carousel('-')
            if direction == 'both':
                await carousel('')
                await carousel('-')
                
        except Exception as ex:
            logger.error(f"""Ошибка {ex} """, ex)
            return False
        return True
        
   
    def get_webelement_as_screenshot(webelement):
        """ 
    Возвращаю скриншот элемента
    
    Attrs:
        webelement (_webelement_): любой вебэлемент, необязательно картинка
    @returns
        png (_binary_): скриншот в случае удачи, иначе False
        """
        try:
            screenshot = webelement.screenshot_as_png
            return screenshot
        except Exception as ex:
            if ex.with_traceback().find("is no longer attached to the DOM"):
                logger.error(f"""Потерял элемент в DOMе {ex.with_traceback(ex.__traceback__)}""")
                return False
            else:
                logger.error(f"""Потерял элемент кяк то по - другому {ex.with_traceback(ex.__traceback__)}""")
                return False

    def page_refresh(self)->bool:
        """ Рефреш с ожиданием полной перезагрузки страницы """
        return self.get_url(self.current_url)
       
    def unhide_dom_element(self, element)->bool:
        """ показываю скрытые элементы """
        #_d = super()
        return js.unhide_DOM_element(self, element)
        

    def close(self):
        self.delete_driver_logs()
        if not self.close(): 
            logger.error(f""" Ошибка закрытия драйвера """)
        pass



    def delete_driver_logs(self, path: str = None) -> bool:
        """ Очищаю %APPDATA% 
        @param path `str`: путь к папке tmp, если None - будет построен из путей в ОС
        @todo подумать, а надо ли оно мне. пока поставил заглушку
        """
        return True
    
        logger.info("START -  удалениe временных файлов из `tmp`")
        app_data_temp_dir = Path(os.environ.get('TEMP')) if path is None else path

        try:
            # Перебираем все элементы в указанной папке
            for item in os.listdir(app_data_temp_dir):
                item_path = os.path.join(app_data_temp_dir, item)
                # Проверяем, является ли элемент файлом или директорией
                if os.path.isfile(item_path):
                    # Если это файл, удаляем его
                    try:
                        os.remove(item_path)
                    except Exception as ex:
                        print(f"Ошибка при удалении содержимого папки: {ex}")
                        continue
                elif os.path.isdir(item_path):
                    # Если это директория, удаляем ее рекурсивно
                    try:
                        self.clear_temp_directory(item_path)
                    except Exception as ex:
                        print(f"Ошибка при удалении содержимого папки: {ex}")
                        continue
                    # Затем удаляем саму директорию
                    try:
                        os.rmdir(item_path)
                    except Exception as ex:
                        print(f"Ошибка при удалении содержимого папки: {ex}")
                        continue

        finally:
            logger.info("STOP -  удаления временных файлов из `tmp`")

    
   


  
