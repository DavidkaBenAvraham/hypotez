"""! @brief  <b> Класс `Driver` </b>

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

from ast import Try
from pathlib import Path
import os
import sys
import pickle # использую для хранения / чтения кук
import time
import requests
import asyncio
from attr import attr, attrs
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
# ------------------------------------------------------------------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint, DriverException
from src.tools import StringFormatter as SF
from . import execute_locator, js
# ------------------------------------------------------------------------------------------



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
else:
    logger.error ('Не опреден ведрайвер. Запускаю `Mozilla` как дефолтный для системы ')
    from .Firefox import Firefox as WebDriver
# ----------------------------------------------------------------------------------------------------


##@logs_and_errors_decorator(default_return =  False)
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

    `ActionChains` полезен в ситуациях, когда требуется выполнить сложные последовательности взаимодействий с элементами, например, для эмуляции пользовательского ввода или выполнения сложных действий на веб-странице.
    
    
    @param previous_url `str`  :  URL предыдущей сатрницы
    """
    current_url = None

    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)

    @property
    def get_ready_state(self) -> bool:
        try:
            return js.get_ready_state(self)
        except Exception as ex:
            logger.error(f'Error: {ex}')
            return False


            #################################################################################################################
            #                                                                                                               #
            #                                               SYNC                                                            #
            #                                                                                                               #
            #################################################################################################################



    def get_url(self, url: str) -> bool:
        """! Обертка для метода driver.get(): переходит по указанному URL.
        @param url `str` Адрес URL.
        @returns bool `True`, если переход выполнен успешно и текущий URL соответствует ожидаемому.
                  `False` в случае ошибки перехода или несоответствия текущего URL ожидаемому. """
                  
        window_handles = self.window_handles
        try:
            self.get(url)
            if self.previous_url != self.current_url:
                self.previous_url = self.current_url
                self.switch_to.window(window_handles[-1])
                return True
            else: raise DriverException (f'Ошибка перехода с URL {self.previous_url} на URL {self.current_url} ')
        except DriverException as ex:
            logger.error('Ошибка драйвера', ex)
            return False
        except Exception as ex:
            logger.error(f'Error navigating to URL {url}:', ex)
            return False

    def unhide_dom_element(self, element) -> bool:
        return js.unhide_DOM_element(self, element)

    def page_refresh(self) -> bool:
        return self.get_url(self.current_url)

    def delete_driver_logs(self) -> bool:
        """! @ru_todo нет реализации """
        return True  

    def close(self):
        #self.delete_driver_logs()
        super().close() 

    def scroll(self, scroll_count: int = 5, framesize_to_scroll: int = 1800, direction: str = 'forward', delay: float = 0.8) -> bool:
        """
        Scroll the web page.

        @param
            scroll_count `int`  :  Number of times to scroll.
            framesize_to_scroll `int`  :  The scroll frame in pixels.
            direction `str`  :  Direction of scrolling. Possible values are 'both', 'forward', 'backward', 'carousel'.
            delay `int`  :  Delay in seconds between each scroll.

        @returns
            bool: True if scrolling is successful, False otherwise.
        """
        def carousel(direction):
            for i in range(scroll_count):
                self.execute_script(f'window.scrollBy({delay},{direction}{framesize_to_scroll})')
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

        def get_webelement_as_screenshot(self, webelement):
        try:
            screenshot = await webelement.screenshot_as_png
            return screenshot
        except Exception as ex:
            if "is no longer attached to the DOM" in str(ex):
                logger.error(f"Lost element in the DOM {ex}")
                return False
            else:
                logger.error(f"Lost element in some other way {ex}")
                return False
            

        def execute_locator(self, locator) -> bool:
        return await execute_locator.execute_locator(self, locator)

        def execute_action(self, locator) -> bool:
        return await execute_locator.execute_action(self, locator)

        def get_attributes_from_webelements(self, locator) -> list:
        return await execute_locator.get_attributes_from_webelements(self, locator)

        def get_attribute_from_webelement(self, locator) -> str:
        return await execute_locator.get_webelements_from_page(self, locator)

        def get_webelements_from_page(self, locator) -> list:
        return await execute_locator.get_webelements_from_page(self, locator)

        def get_webelement_as_screenshot(self, locator) -> bool:
        return await execute_locator.get_webelement_as_screenshot(self, locator)

    def get_webelement_with_wait_to_be_clickable(self, locator) -> WebElement:
        return await execute_locator.get_webelement_with_wait_to_be_clickable(self, locator)

    async def get_webelement_with_wait_to_precence_located(self, locator) -> WebElement:
        return await execute_locator.get_webelement_with_wait_to_precence_located(self, locator)

    async def click(self, locator) -> bool:
        return await execute_locator.click(self, locator)

    async def wait(self, wait=0, call_func=None, when='after') -> None:
        if call_func is None:
            await asyncio.sleep(wait)
        else:
            call_func = 'self.' + call_func
            if when == 'after':
                res = eval(call_func)
                await asyncio.sleep(wait)
                return res
            else:
                await asyncio.sleep(wait)
                return eval(call_func)

    def get_url(self, url: str) -> bool:
        """! Обертка для метода driver.get(): переходит по указанному URL.
        @param url `str` Адрес URL.
        @returns bool `True`, если переход выполнен успешно и текущий URL соответствует ожидаемому.
                  `False` в случае ошибки перехода или несоответствия текущего URL ожидаемому. """
                  
        window_handles = self.window_handles
        try:
            self.get(url)
            if self.previous_url != self.current_url:
                self.previous_url = self.current_url
                self.switch_to.window(window_handles[-1])
                return True
            else: raise DriverException (f'Ошибка перехода с URL {self.previous_url} на URL {self.current_url} ')
        except DriverException as ex:
            logger.error('Ошибка драйвера', ex)
            return False
        except Exception as ex:
            logger.error(f'Error navigating to URL {url}:', ex)
            return False

    async def unhide_dom_element(self, element) -> bool:
        return await js.unhide_DOM_element(self, element)

    def page_refresh(self) -> bool:
        return self.get_url(self.current_url)

    def delete_driver_logs(self) -> bool:
        """! @ru_todo нет реализации """
        return True  

    async def close(self):
        #self.delete_driver_logs()
        asyncio.run ( super().close() )

    async def scroll(self, scroll_count: int = 5, framesize_to_scroll: int = 1800, direction: str = 'forward', delay: float = 0.8) -> bool:
        """
        Scroll the web page.

        @param
            scroll_count `int`  :  Number of times to scroll.
            framesize_to_scroll `int`  :  The scroll frame in pixels.
            direction `str`  :  Direction of scrolling. Possible values are 'both', 'forward', 'backward', 'carousel'.
            delay `int`  :  Delay in seconds between each scroll.

        @returns
            bool: True if scrolling is successful, False otherwise.
        """
        async def carousel(direction):
            for i in range(scroll_count):
                await self.execute_script(f'window.scrollBy({delay},{direction}{framesize_to_scroll})')
                await asyncio.sleep(delay)

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

    async def get_webelement_as_screenshot(self, webelement):
        try:
            screenshot = await webelement.screenshot_as_png
            return screenshot
        except Exception as ex:
            if "is no longer attached to the DOM" in str(ex):
                logger.error(f"Lost element in the DOM {ex}")
                return False
            else:
                logger.error(f"Lost element in some other way {ex}")
                return False        

            #################################################################################################################
            #                                                                                                               #
            #                                               ASYNC                                                           #
            #                                                                                                               #
            #################################################################################################################

    async def execute_locator(self, locator) -> bool:
        return await execute_locator.execute_locator(self, locator)

    async def execute_action(self, locator) -> bool:
        return await execute_locator.execute_action(self, locator)

    async def get_attributes_from_webelements(self, locator) -> list:
        return await execute_locator.get_attributes_from_webelements(self, locator)

    async def get_attribute_from_webelement(self, locator) -> str:
        return await execute_locator.get_webelements_from_page(self, locator)

    async def get_webelements_from_page(self, locator) -> list:
        return await execute_locator.get_webelements_from_page(self, locator)

    async def get_webelement_as_screenshot(self, locator) -> bool:
        return await execute_locator.get_webelement_as_screenshot(self, locator)

    async def get_webelement_with_wait_to_be_clickable(self, locator) -> WebElement:
        return await execute_locator.get_webelement_with_wait_to_be_clickable(self, locator)

    async def get_webelement_with_wait_to_precence_located(self, locator) -> WebElement:
        return await execute_locator.get_webelement_with_wait_to_precence_located(self, locator)

    async def click(self, locator) -> bool:
        return await execute_locator.click(self, locator)

    async def wait(self, wait=0, call_func=None, when='after') -> None:
        if call_func is None:
            await asyncio.sleep(wait)
        else:
            call_func = 'self.' + call_func
            if when == 'after':
                res = eval(call_func)
                await asyncio.sleep(wait)
                return res
            else:
                await asyncio.sleep(wait)
                return eval(call_func)


