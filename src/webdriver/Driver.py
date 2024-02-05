"""! @brief   Класс <b>`Driver` </b>
класс Selenium вебдрайвера с моими дополнениями

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
import asyncio
from attr import attr, attrs
from pathlib import Path
from typing import Union
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC

# # ------------------------------
# hypotez_root_path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
# sys.path.append(hypotez_root_path)  # Добавляю корневую папку в sys.path


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, DriverException, jprint, pprint
from src.tools import StringFormatter as SF, StringNormalizer as SN
from . import execute_locator, js
# -------------------------------

    #####################################################################
    #                                                                   #
    #                   Выбор драйвера                                  #
    #                                                                   #
    #####################################################################


from .Firefox import Firefox as WebDriver
"""! @debug """

if gs.default_webdriver == 'firefox':
    from .Firefox import Firefox as WebDriver #! <- Firefox """
elif gs.default_webdriver == 'edge':
    from .Edge import Edge as WebDriver #! <- Edge 
elif gs.default_webdriver == 'chrome':
    from .Chrome import Chrome as WebDriver #! <- Chrome 
else:
    logger.error ('Не опреден ведрайвер. Запускаю `Mozilla` как дефолтный для системы ')
    from .Firefox import Firefox as WebDriver


class Driver(WebDriver):
    """! @brief Webriver `Firefox,Edge,Chrome` вебдрайвер

    Драйвер обрабатывает запросы локаторов, отдает атрибуты или целиком веб-элемент(ы)
    @param current_url `str`  :  страница, на которой находится вебдрайвер в данный момент. При первом запуске - функция get_url()
    присвает ей значение параметра `url`, полученое функцией
     
    @param EC `selenium.webdriver.support.expected_conditions.EC`  :  В Selenium `selenium.webdriver.support.expected_conditions` предоставляет ряд ожидаемых условий (`Expected Conditions`), которые можно использовать вместе с `WebDriverWait` для ожидания определенных условий, прежде чем совершить действие. В частности, `EC` содержит классы для ожидания различных событий или состояний на веб-странице.

    @note Вот несколько примеров ожидаемых условий из `selenium.webdriver.support.expected_conditions`:

    1. **`presence_of_element_located`**: Ожидание, пока элемент не станет видимым. Принимает локатор в качестве аргумента.
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myElement"))
    )
    ```

    2. **`visibility_of_element_located`**: Ожидание, пока элемент не станет видимым. Принимает локатор в качестве аргумента.
    ```python
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "myElement"))
    )
    ```

    3. **`element_to_be_clickable`**: Ожидание, пока элемент не станет кликабельным. Принимает локатор в качестве аргумента.
    ```python
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "myElement"))
    )
    ```

    4. **`title_is`**: Ожидание, пока заголовок страницы не станет заданным.
    ```python
    WebDriverWait(driver, 10).until(
        EC.title_is("Expected Page Title")
    )
    ```

    5. **`title_contains`**: Ожидание, пока заголовок страницы не содержит заданный текст.
    ```python
    WebDriverWait(driver, 10).until(
        EC.title_contains("Expected Title")
    )
    ```

    Эти условия используются в сочетании с `WebDriverWait`, который ожидает, пока условие не будет выполнено, или пока не истечет время ожидания (в данном случае, 10 секунд в приведенных выше примерах).
   
    
    @param WebDriverWait `selenium.webdriver.support.ui.WebDriverWait`  :  ожидания. 
    В Selenium `selenium.webdriver.support.expected_conditions` предоставляет ряд ожидаемых условий (`Expected Conditions`), 
    которые можно использовать вместе с `WebDriverWait` для ожидания определенных условий, 
    прежде чем совершить действие. В частности, `EC` содержит классы для ожидания различных событий или состояний на веб-странице.
    @note Вот несколько примеров ожидаемых условий из `selenium.webdriver.support.expected_conditions`:

    1. **`presence_of_element_located`**: Ожидание, пока элемент не станет видимым. Принимает локатор в качестве аргумента.
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myElement"))
    )
    ```

    2. **`visibility_of_element_located`**: Ожидание, пока элемент не станет видимым. Принимает локатор в качестве аргумента.
    ```python
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "myElement"))
    )
    ```

    3. **`element_to_be_clickable`**: Ожидание, пока элемент не станет кликабельным. Принимает локатор в качестве аргумента.
    ```python
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "myElement"))
    )
    ```

    4. **`title_is`**: Ожидание, пока заголовок страницы не станет заданным.
    ```python
    WebDriverWait(driver, 10).until(
        EC.title_is("Expected Page Title")
    )
    ```

    5. **`title_contains`**: Ожидание, пока заголовок страницы не содержит заданный текст.
    ```python
    WebDriverWait(driver, 10).until(
        EC.title_contains("Expected Title")
    )
    ```


    6. **`text_to_be_present_in_element`**: Ожидание, пока указанный текст не появится внутри элемента. Принимает локатор и ожидаемый текст.
    ```python
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "myElement"), "Expected Text")
    )
    ```

    7. **`invisibility_of_element_located`**: Ожидание, пока элемент не станет невидимым. Принимает локатор в качестве аргумента.
    ```python
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "myElement"))
    )
    ```

    8. **`presence_of_all_elements_located`**: Ожидание, пока все элементы, соответствующие заданному локатору, не станут видимыми.
    ```python
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "myClass"))
    )
    ```

    9. **`element_to_be_selected`**: Ожидание, пока элемент не будет выбран (для элементов в `<select>`).
    ```python
    WebDriverWait(driver, 10).until(
        EC.element_to_be_selected((By.ID, "mySelect"))
    )
    ```

    10. **`alert_is_present`**: Ожидание появления всплывающего окна (alert).
    ```python
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    ```

    
    Эти условия используются в сочетании с `WebDriverWait`, который ожидает, пока условие не будет выполнено, 
    или пока не истечет время ожидания (в данном случае, `10` секунд в приведенных выше примерах).
    
    @param By `selenium.webdriver.common.by.By`  :  `By` в модуле `selenium.webdriver.common.by` - класс, предоставляющий различные стратегии для поиска веб-элементов. 
    @note
    Вот несколько стратегий, предоставляемых этим классом:

    **By.ID:**
    поиск элемента по атрибуту ID.

    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.ID, 'element_id')
    ```

    **By.NAME:**
    поиск элемента по атрибуту name.

    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.NAME, 'element_name')
    ```

    **By.XPATH:**
    поиск элемента с использованием выражения XPath.

    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.XPATH, '//div[@id="example"]')
    ```

    **By.CLASS_NAME:**
    поиск элемента по имени класса.

    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.CLASS_NAME, 'example_class')
    ```

    **By.CSS_SELECTOR:**
    поиск элемента с использованием CSS-селектора.

    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.CSS_SELECTOR, 'div.example')
    ```

    **By.LINK_TEXT:**
    поиск гиперссылки по тексту.

    ```python
    from selenium.webdriver.common.by import By

    link = driver.find_element(By.LINK_TEXT, 'Example Link')
    ```

    **By.PARTIAL_LINK_TEXT:**
    поиск гиперссылки по части текста.

    ```python
    from selenium.webdriver.common.by import By

    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'partial text')
    ```

    **By.TAG_NAME**
    Поиск по имени тега
    
    ```python
    from selenium.webdriver.common.by import By

    elements = driver.find_elements(By.TAG_NAME, 'tag_name')
    ```

    **Поиск по имени класса:**
    ```python
    from selenium.webdriver.common.by import By

    elements = driver.find_elements(By.CLASS_NAME, 'class_name')
    ```

    **Поиск по имени элемента:**
    ```python
    from selenium.webdriver.common.by import By

    elements = driver.find_elements(By.NAME, 'element_name')
    ```

    **Поиск по ссылке (тексту ссылки):**
    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.LINK_TEXT, 'link_text')
    ```

    **Частичный поиск по ссылке (части текста ссылки):**
    ```python
    from selenium.webdriver.common.by import By

    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'partial_link_text')
    ```

    Эти стратегии могут использоваться в методах поиска элементов, таких как `find_element` и `find_elements`. 
    Например, `driver.find_element(By.ID, 'element_id')` находит элемент по ID.
    
    
    @param Keys `selenium.webdriver.common.keys.Keys`  :  Модуль предоставляет класс `Keys`, 
    который содержит константы для ввода клавиш в WebDriver. 
    @note
    Ниже приведен список некоторых из этих констант:
    1. **`Keys.NULL`**
    2. **`Keys.CANCEL`**
    3. **`Keys.HELP`**
    4. **`Keys.BACKSPACE`**
    5. **`Keys.TAB`**
    6. **`Keys.CLEAR`**
    7. **`Keys.RETURN`**
    8. **`Keys.ENTER`**
    9. **`Keys.SHIFT`**
    10. **`Keys.CONTROL`**
    11. **`Keys.ALT`**
    12. **`Keys.PAUSE`**
    13. **`Keys.ESCAPE`**
    14. **`Keys.SPACE`**
    15. **`Keys.PAGE_UP`**
    16. **`Keys.PAGE_DOWN`**
    17. **`Keys.END`**
    18. **`Keys.HOME`**
    19. **`Keys.LEFT`**
    20. **`Keys.UP`**
    21. **`Keys.RIGHT`**
    22. **`Keys.DOWN`**
    23. **`Keys.INSERT`**
    24. **`Keys.DELETE`**
    25. **`Keys.SEMICOLON`**
    26. **`Keys.EQUALS`**
    27. **`Keys.NUMPAD0`** through **`Keys.NUMPAD9`**
    28. **`Keys.MULTIPLY`**
    29. **`Keys.ADD`**
    30. **`Keys.SEPARATOR`**
    31. **`Keys.SUBTRACT`**
    32. **`Keys.DECIMAL`**
    33. **`Keys.DIVIDE`**
    34. **`Keys.F1`** through **`Keys.F12`**
    35. **`Keys.META`**

    Эти константы используются для моделирования нажатия клавиш в WebDriver, например, `Keys.ENTER` представляет клавишу Enter. Методы `send_keys` для веб-элементов могут использовать эти константы для отправки последовательности клавиш. Например:

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome()
    element = driver.find_element_by_name("q")
    element.send_keys("selenium" + Keys.RETURN)
    ```

    В этом примере `Keys.RETURN` используется для отправки клавиши Enter после ввода текста "selenium" в элемент ввода.
    
    
    @param ActionChains `selenium.webdriver.common.action_chains.ActionChains`  :  `ActionChains` 
    Kласс, предназначенный для выполнения цепочки взаимосвязанных действий (actions) на веб-странице. 
    Эти действия включают в себя различные взаимодействия с элементами, такие как 
    клики, ввод текста, перемещение мыши, использование клавиш клавиатуры и многие другие.

    Пример использования `ActionChains` в Selenium:

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains

    # Создаем экземпляр веб-драйвера
    driver = webdriver.Chrome()

    # Переходим на веб-страницу
    driver.get("https://example.com")

    # Находим элемент, с которым будем взаимодействовать
    element = driver.find_element_by_id("myElement")

    # Создаем объект ActionChains
    actions = ActionChains(driver)

    # Выполняем цепочку действий
    actions.move_to_element(element).click().perform()

    # Закрываем браузер
    driver.quit()
    ```

    В этом примере:

    1. Мы создаем экземпляр `ActionChains`, передавая в него веб-драйвер (`driver`).
    2. Мы используем методы `move_to_element` и `click` для перемещения к элементу и выполнения клика.
    3. Мы вызываем `perform()`, чтобы выполнить все указанные действия.

    `ActionChains` полезен в ситуациях, когда требуется выполнить сложные последовательности взаимодействий с элементами, 
    например, для эмуляции пользовательского ввода или выполнения сложных действий на веб-странице.

    @param previous_url `str`  :  URL предыдущей стрaницы
    """

    previous_url = None
    
    #@logs_and_errors_decorator(default_return=False)
    def __init__(self, *args, **kwards):
        """ @brief The constructor
        @details Старт вебрайвера. 
        Наследуется от selenium.webdriver.<webdriver>   <- Firefox, Egde, Chrome, etc 
        """
        
        logger.info(f""" 
        -----------------------------------------------------
        Старт вебдрайвера {gs.default_webdriver}. 
        Будет выбран драйвер, подключатся настройки и профиль.
        На моем компьютере это занимает около полуминуты. Ждем....
        -----------------------------------------------------""")
        
        self.delete_driver_logs()
        """! @~russian Очищаю директорию логов.
        @todo 1. Продумать очистку только логов вебдрайвера  
        2. Делать очистку по условию """

        super().__init__(*args, **kwards)
            
    # #@logs_and_errors_decorator(default_return=False)
    # @property
    # def get_ready_state(self) -> bool:
    #     """ 
    #     Опрашиваю через JS значение window.ready_state()
        
    #     @returns loading|complete `str`  
    #     """
        
    #     try:
    #         """! """
    #         return js.get_ready_state(self)
    #     except Exception as ex:
    #         logger.error(f'Ошибка {ex}')
    #         return False

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

    #@logs_and_errors_decorator(default_return=False)
    def execute_locator(self, locator: dict) -> bool:
        return execute_locator.execute_locator(self, locator)

    #@logs_and_errors_decorator(default_return=False)
    async def async_execute_locator(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.execute_locator, locator)
    

    #@logs_and_errors_decorator(default_return =  False)
    def execute_action(self, locator) -> bool:
        return execute_locator.execute_action(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_execute_action(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.execute_action, locator)
        
    
    #@logs_and_errors_decorator(default_return =  False)        
    def get_attributes_from_webelements(self, locator) -> Union[list, str]:
        return execute_locator.get_attributes_from_webelements(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_attributes_from_webelements(self, locator) -> Union [list, str]:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_attributes_from_webelements, locator)
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_attribute_from_webelement(self, locator) -> str:
        return execute_locator.get_webelements_from_page(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_attribute_from_webelement(self, locator) -> str:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_attribute_from_webelement, locator)
        
    
    #@logs_and_errors_decorator(default_return =  False)
    def get_webelements_from_page(self, locator) -> Union [list, str]:
        return execute_locator.get_webelements_from_page(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_webelments_from_page(self, locator) -> Union [list, str]:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_webelements_from_page, locator)
    
    #@logs_and_errors_decorator(default_return =  False)
    def get_webelement_as_screenshot(self, locator) -> Union[bytes, bytearray, False]:
        return execute_locator.get_webelement_as_screenshot(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_webelement_as_screenshot(self, locator) -> Union[bytes, bytearray, False]:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_webelement_as_screenshot, locator)
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_webelement_with_wait_to_be_clickable(self, locator) -> Union [WebElement, False]:
        return execute_locator.get_webelement_with_wait_to_be_clickable(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_webelement_with_wait_to_be_clickable(self, locator) ->  Union [WebElement, False]:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_webelement_with_wait_to_be_clickable, locator)
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_webelement_with_wait_to_precence_located(self, locator) -> Union [WebElement, False]:
        return execute_locator.get_webelement_with_wait_to_precence_located(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_webelement_with_wait_to_precence_located(self, locator) -> Union [WebElement, False]:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.get_webelement_with_wait_to_precence_located, locator)
        
    #@logs_and_errors_decorator(default_return =  False)
    def click(self, locator) -> bool:
        return execute_locator.click(self, locator)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_click(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, execute_locator.click, locator)
            
    #@logs_and_errors_decorator(default_return =  False)
    def scroll(self, scrolls: int = 5, frame_size: int = 1800, direction: str = 'both', delay: float = 1) -> Union [None, False]:
        """! @~english Scroll the web page.

        @param scrolls `int`  :  Number of times to scroll.
        @param frame_size `int`  :  The scroll frame in pixels.
        @param direction `str`  :  Direction of scrolling. Possible values are 'both', 'forward', 'backward', 'carousel'.
        @param delay `int`  :  Delay in seconds between each scroll.

        @returns bool  :  True if scrolling is successful, False otherwise.
        """
        """!@~russian @brief Крутилка страницы вперед, назад

        @param direction `str`  :  Направление скроллинга:  'both', 'forward', 'backward'.   
        Обычно, я кручу на 5 экранов вниз, а потом вверх """
        
 
        try:
            """! """
            if direction == 'forward':
                self.carousel ('',scrolls)
            if direction == 'backward':
                self.carousel ('-',scrolls)
            if direction == 'both':
                self.carousel ('', scrolls)
                self.carousel ('-', scrolls)
            else:
                logger.warning(f"""неправильно задано направление. Ожидается `'forward', 'backward', 'both'`. Получено {direction} '""")
                # self.carousel('')
                # self.carousel('-')
                return False
        except Exception as ex:
            logger.error(f'ошибка ', ex)
            return False
        pass

         
    def carousel (self,  direction: str = '', scrolls: int = 5, frame_size: int = 1800,  delay: float = 1) -> bool:
        """! @~russian крутилка экрана. Можно задать через scroll()
        @scrolls количество прокручиваний фреймов
        @frame_size размер фрейма
        @param direction `str`  :  'forward','backward','both' 
            в карусели для `window.scrollBy()` я передаю размер фрейма и направление: 
        'вниз': `frame_size`, 'вверх' отрицательное значение: `-frame_size`
        @param delay `int`  :   пауза между скроллингом - имитирую действия человека, чтобы ба нарвать на бан
        @returns bool  :  `True` в случае успеха, иначе `False`
        """
        for i in range(scrolls):
            self.execute_script (f'window.scrollBy({delay},{direction}{frame_size})')
            #self.wait(delay)
        pass

  
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_scroll(self, locator) -> bool:
        """! Асинхронный вызов scroll() """
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.scroll, locator)



    #@logs_and_errors_decorator(default_return =  False)
    def get_webelement_as_screenshot(webelement):
        """ 
    Возвращаю скриншот элемента
    
    @param webelement `webelement`  :  любой вебэлемент, необязательно картинка
    @returns png `binary`  :  скриншот в случае удачи, иначе False
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
            
    #@logs_and_errors_decorator(default_return=False)
    async def async_get_webelement_as_screenshot(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.get_webelement_as_screenshot, locator)    
        

    #@logs_and_errors_decorator(default_return =  False)
    def get_url(self, url: str) -> bool:
        """! Обертка для метода driver.get(): переходит по указанному URL.

        @param url `str` Адрес URL.

        @param self.previous_url `str` Адрес предыдущей страницы. сооветсвует js методу `window.back()`
        
        @param previous_url `str` в переменную запоминается URL текущей страницы  . 
        @returns bool: `True`, если переход выполнен успешно и текущий URL соответствует ожидаемому.
                Возвращает `False` в случае ошибки перехода или несоответствия текущего URL ожидаемому.
        """
                  

        _previous_url = url if not self.current_url else self.current_url
        
        try:
            _url = SN.normalize_url (url)
            
            _start_time = float(time.time())
            self.get(_url)
            while not js.get_ready_state(self) == 'complete':
                #print('Жду, пока загрузится вся страница')
                pass
            logger.debug(f'Страница загрузилась за { float (time.time()) - _start_time }')
            self.switch_to.window(self.window_handles[-1])
            """! переключаюсь на активное окно. Это если ссылка открывает новое окно 
            @todo Надо быть внимательным, 
            """

            if self.previous_url != self.current_url: 
                """! @todo А если новое окно или короткая ссылка стала полной? """
                logger.info (f''' Новый URI {self.current_url} ''')
            else: 
                logger.warning(f"""предыдущий URI {self.previous_url} совпадает с новым {self.current_url}.
                               Надо проверить""")
                # СТРОГО
                #raise DriverException (f'Ошибка перехода с URL {self.previous_url} на URL {self.current_url} ')
            

            
            """! фокус на последнeе открытое окно 
            Если ссылка открывает новое окно - я фокусируюсь на нем """

            self.previous_url = _previous_url
            """! Запомнил, откуда пришел """
            return True
            
        except DriverException as ex:
            logger.error('Ошибка драйвера', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f'Проверь URI {url}', ex)
            return False
        except Exception as ex:
            logger.error(f'Error URL {url}:', ex)
        return False
        

    #@logs_and_errors_decorator(default_return=False)
    async def async_get_url(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.get_url, locator)    
        



    #@logs_and_errors_decorator(default_return =  False)
    def page_refresh(self) -> bool:
        """ Рефреш с ожиданием полной перезагрузки страницы """
        return self.get_url(self.current_url)
    
    #@logs_and_errors_decorator(default_return=False)
    async def async_page_refresh(self, locator) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.page_refresh, locator)    
        

    #@logs_and_errors_decorator(default_return =  False)
    def unhide_dom_element(self, element) -> bool:
        """ показываю скрытые элементы """
        #_d = super()
        return js.unhide_DOM_element(self, element)
    
    async def async_unhide_dom_element(self, element) -> bool:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.unhide_dom_element, element)        
    
    def window_focus(self):
        """ Возвращаю фокус на страницу (сбрасываю фокус с элемента) """
        #_d = super()
        return js.get_ready_state(self)
    
    #@logs_and_errors_decorator(default_return =  False)
    def wait(self, wait=0, call_func=None, when='after') -> None:
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

        call_func = 'self.' + call_func
        if when == 'after':
            res = eval(call_func)
            time.sleep(wait)
            return res
        else:
            time.sleep(wait)
            return eval(call_func)
        
    #@logs_and_errors_decorator(default_return =  False)
    def close(self):
        self.delete_driver_logs()
        if not self.close(): 
            logger.error(f""" Ошибка закрытия драйвера """)
        pass
        

    #@logs_and_errors_decorator(default_return =  False)
    def delete_driver_logs(self) -> bool:
        """! Удаляю логи вебдрайвера 
        @param path `str`  :  путь к папке tmp, если None - будет построен из путей в ОС
        @todo подумать, а надо ли оно мне. пока поставил заглушку
        """
        return True
    
        logger.info("START -  удалениe временных файлов из `tmp`")
        temp_dir = Path ( gs.dir_logs, 'webdriver' )

        try:
            # Перебираем все элементы в указанной папке
            for item in os.listdir ():
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