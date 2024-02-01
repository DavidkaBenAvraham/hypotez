"""! @~russian 

@brief  исполнитель (экзекьютор) сценария через вебдрайвер.
@details экзекьютор:
- выполняет алогритм по переходам на страницы, прописанный в <b>файлах сценария</b>.
- исполняет алгоритм взаимодйствия со страницей, прописанный в <b>файлах локатора</b>.

@image html diagrams-execute_locator.png

### Примеры локаторов
``` python
{
  "product_links": {
    "attribute": "href",
    
    "by": "XPATH",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    
    "use_mouse": false, "mandatory": true,
    "action": nul
  },


  "pagination": {
    "ul": {
      
      "attribute": nul,
      "by": "XPATH",
      "selector": "//ul[@class='pagination']",
      "action": "click()"
    },
    "->": {
      "attribute": nul,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "action": "click()",
      "use_mouse": false
    }
  }

}
```

@todo сделать вариант, когда в списке передается аттрибут по `VALUE`, но формулой, например $_(get_user_name())_$, $_(get_user_password())_$

 @section libs imports:
  - logging 
  - sys 
  - os 
  - typing 
  - re 
  - selenium.webdriver.common.keys 
  - selenium.webdriver.common.by 
  - selenium.webdriver.support.ui 
  - selenium.webdriver.support 
  - webdriver 
  - gs 
  - gs 
  - gs 
  - tools.string_formatter 
  - product 
  - locator: 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


#from logging import raiseExceptions
import asyncio
import sys
import os
from pathlib import Path
from typing import List, Union, Dict
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------
from src.webdriver import Driver
from src.settings import gs
from src.helpers import logger, logs_and_errors_decorator, jprint, pprint
from src.helpers.exceptions import DefaultSettingsException, DriverException, ExecuteLocatorException
from src.io_interface import j_loads, j_dumps
from src.tools.string_formatter import StringFormatter as SF
#from src.suppliers import Supplier
#from src.product import Product
# ------------------------------

#@logs_and_errors_decorator (default_return =  False)
def execute_locator(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union [str, list, dict, None, False]:
    """! Исполняет локаторы. В зависимости от сореджимого локатора функция выбирает логику исполнения
    If the `action` and `attribute` values in the locator are `None`, return the entire web element. \n
    If the locator contains `send_keys()` in the `action` section , there are two ways to obtain `keys`:
       - 1. From the locator itself, if a key is specified there. For example: `send_keys(Key.F5)`, `send_keys(12345)`.
       - 2. From an external source, passed as an argument `keys` to this function.
     Event handling is processed first, folowed by attribute colection.
    
    @param driver `Driver` The selenium webdriver object.
    @param keys  The `Keys` object used to send keys to the web element (f.e. `Key.Enter`) . Defaults to `None`.
    ### list of keys:
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
    
    @param locator `dict` The locator json dict.
    ## Example
     <pre>   
     "shipto_locator": {
      
      "attribute": [ nul, nul, nul ],
      "by": [ "XPATH", "XPATH", "xpath" ],
      "selector": [
        "//a[contains(@class,'address-select-trigger') and contains(@data-role,'country')]",
        "//div[@class = 'filter-list-container']",
        "//li[contains(@data-code,'il')]"
      ],
      "action": [ "click()", "click()", "click()" ],
      "use_mouse": false
    }
    </pre>
    
    

    @returns
        If `action` and `attribute` are both `None`, return the entire web element.  
        If `action` is `None`, but `attribute` is specified in `locator`, return the attribute(s) of the web element.  
        If `action` is a string, execute the corresponding action and return the result.  
        If `action` is a list, iterate through the list and execute each action. Recursively process each locator in the list and append the result to the `attrs` list. Finaly, return `attrs`.  
        If `action` is a dictionary, execute the specified feature. (Currently not implemented)  
        
     @image html execute_locator.png
     
     ## Действия (actions) Всегда выполняются ДО получения атрибута. Если надо получить действие по значению атрибута -
     сделай формулу в конструкции "$_(...)_$ 
    """

    
    ###################################################################################################
    #
    #               Парсер локатора
    #
    #
    def parse_locator(l):
        
        ret = None

        _saved_locator = l 
        """! если в локаторах есть функция - я ее исполняю до обработки локатора.
        @note Функция из локатора обычно замещает себя результатом исполнения.
        @todo проверить как веддет себя `l`, если это локальная в функции тогда `_saved_locator = l` не нужен, т.к. глобальный `l` не меняется"""     
        
        l['attribute'] = evaluate_locator(l.get('attribute'),driver)
        l['selector'] = evaluate_locator(l.get('selector'),driver) 
   
        # 1.
        if all ( [ l['action'], l['attribute'] ] ) is None:
            """! @~russian если нет действий на элементов и нет конкретных аттрибутов для получения от вебэлемента - то я возвращаю ВЕСЬ элемент """
            """! @~english Return the entire web element if `action` and `attribute` are None."""

            ret = get_webelements_from_page (driver, l)
    
        # 1.1 

        if str(l['by']).upper() == 'VALUE':
            """! Я могу передать свое значение (формулу) через ключ `attribute` 
        
            Например:
            ```python
              "delivery_in_stock": {
                "attribute": "Israel Post",
                "by": "VALUE",
                "selector": nul,
                "use_mouse": false, 
                "mandatory": true,
                "action": null
              }
            ```
        
            @todo проверить на формулу в `attribute`
            """
            ret = l['attribute']
    
        # 1.2.
        elif l['action'] is None:
            """! действия над элементом не требуются. Будет возвращен аттрибут 
             Return the attribute(s) of the web element if 'action' is None but 'attribute' 
             is specified in the locator.
             Например:
             ```python
            "product_reference_and_volume_and_price_for_100": {
                "attribute": "InnerText",
                "by": "XPATH",
                "selector": "//div[@data-widget_type='shortcode.default']",
                "use_mouse": false, "mandatory": true,
                "action": null,
                "@note": ""
              },
                     """
            ret = get_attributes_from_webelements ( driver, l )

        # 1.3
        else:
            """! @~russian если задан параметр 'action' -> бегу выполнять его  """
            """! @en_rem Execute the one action and return the result."""        
            ret = execute_action (driver, l, keys)
        
   
        l = _saved_locator
        """! возвращаю локатор в изначальное состояние """
        return ret
    #
    #
    #
    ###########################################################################################






    if isinstance(locator['attribute'], list):
        """! локаторы могут содержать списки. 
        Например:
        ```python
          l: {
            "attribute": [ nul, nul ],
            "by": [ "XPATH", "XPATH" ],
            "selector": [ "//a[contains(@href, 'אופן-השימוש')]", "//div[contains(@id ,'אופן-השימוש')]//p" ],
            "use_mouse": [ false, false ],
            "mandatory": [ true, true ],
            "action": [ "click()", nul ],
            "@note": [ nul, nul ]
          }
          
        "affiliate_short_link": {
            "attribute": "$_(driver.current_url)_$",
            "by": "VALUE",
            "selector": null,
            "use_mouse": false,
            "mandatory": true,
            "action": null,
            "@note": "Исполняю формулу и отдаю результат через `value`"
          }
          ```
          """
          
        ret = []
        for i in range(len(locator['attribute'])):
            l = {key: locator[key][i] for key in locator}
            if ret is None or len(ret) == 0:
                """! код может вернуть `None` """
                ret = parse_locator(l) 
            else:    
                ret.append ( parse_locator(l) )
                
            ret = ret if ret is None else list(filter(lambda x: x is not None, ret))
            pass
                
    else:
        ret = parse_locator(locator)
        
    
    return ret

                
    


#@logs_and_errors_decorator (default_return =  False)
def execute_action(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> bool:
    """! @~en Executes the specified action on the element identified by the given locator.
    @~russian Исполняет действие над вебэлементом/страницей (click, send.KEY, scrol, refersh,  etc)
    
    @param driver `Driver` инстанс вебдрайвера подключенного к исполняемому поставщику
    @param locator `dict` a dictionary containing the folowing keys:
        - "attribute": the attribute to search for
        - "by": the search method to use
        - "selector": the value to search for
        - "action": the action to perform
    @param keys: optional argument to pass to the "send_keys" action (f.e. Key.ENTER)

    @returns bool `True` if the action is successful; `False` otherwise
    
    @image html execute_action.png
    """

    _d = driver

    # 1.
    # if the action is a "loop" action
    if locator['action'] == 'loop':
        if not _d.execute_locator(locator):
                    pass
        # if len(locator['variables in selector']) > 0:
        #     # evaluate the range specified in the formula
        #     _range = locator['formula for locator']
        #     for x in eval(_range):
        #         # replace the "{x}" placeholder in the selector with the current value of x
        #         selector = str(locator['selector']).replace('{x}', str(x))
        #         _l = {
        #             "attribute": locator['attribute'],
        #             "by": locator['by'],
        #             "selector": selector,
        #             "action": None
        #         }
        #         # execute the locator
        #         if not _d.execute_locator(_l):
        #             pass

    # 2.
    # if the action is a "click" action
    if locator['action'] == 'click()':
        """! реализация простого клика.  click() 
        Если надо заполнить поле и потом кликнуть - 
        используй click( send_keys(KEY.VALUE) ) внутри локатора"""
        
        if not driver.click(locator):
           if locator['mandatory']:
               logger.error(f'Не нашел на что кликать {locator.keys} => {locator}')  
           
           return False
           

    # 3.
    # if the action is a "send_keys" action
    elif 'send_keys(' in locator['action']:
        # """  send_keys() """
        webelement = get_webelements_from_page(driver, locator)
        if not webelement:
            logger.error(f""" Не на что кликать
            Элемент не найден: {pprint(locator)}""")
            return False


        # if keys are not specified, extract them from the locator
        if keys is None:
            key_from_locator = locator['action']
            key_from_locator = f"""{key_from_locator[key_from_locator.rfind("('")+2:key_from_locator.rfind("')"):]}"""
            # keys are enclosed in single quotes, so we extract them here
            keys = key_from_locator
            try:
                webelement.send_keys(keys)
                return True
            except Exception as ex:
                logger.error(
                    f"""
                Failed to execute action {locator['action']}
                Ошибка: {ex}""", exc_info=True)
                return False
        # if keys are specified, use them
        else:
            try:
                webelement.send_keys(keys)
                return True
            except Exception as ex:
                logger.error(f"""
                Error in send_keys({keys}):
                {ex}
                """, exc_info=True)
                return False

    # 4.
    # if the action is a "screenshot" action
    elif str(locator['action']).find('screenshot(') > -1:
        #"""  screenshot() """
        webelements = get_webelements_from_page(driver, locator)
        if webelements == False:
            logger.error(f'''Image not found :( ''')
            return False
        # take a screenshot of the element
        return get_webelement_as_screenshot(webelements[0]) if isinstance(webelements, list) else get_webelement_as_screenshot(webelements)

    # 5.
    # if the action is a "scrol" action
        # 4. scrol
    elif str(locator['action']).find('scrol(') > -1:
        return eval(locator['action'])

    # 6. wait
    elif str(locator['action']).find('wait(') > -1:
        """! 
        @todo Стам, выебнулся. Надо упростить. 
        @~en @note
        Explanation of the regular expression:
        wait\( matches the literal "wait(" in the string
        ([^,]+) matches any non-empty sequence of characters that are not commas, and captures them in the first capturing group
        ,\s* matches a comma, optionaly folowed by some whitespace
        ([^,]+) matches any non-empty sequence of characters that are not commas, and captures them in the second capturing group
        ,\s* matches a comma, optionaly folowed by some whitespace
        (after|before) matches either the string "after" or the string "before", and captures it in the third capturing group.
        \) matches the literal ")" in the string.
        """
        """! @~russian Объяснение регулярного выражения: 
        @note
        - `wait\(` соответствует буквальной подстроке "wait(" в строке.
        - `([^,]+)` соответствует любой непустой последовательности символов, кроме запятых, и запоминает их в первой группе захвата.
        - `,\s*` соответствует запятой, возможно, с последующими пробелами.
        - `([^,]+)` соответствует любой непустой последовательности символов, кроме запятых, и запоминает их во второй группе захвата.
        - `,\s*` соответствует запятой, возможно, с последующими пробелами.
        - `(after|before)` соответствует либо строке "after", либо строке "before" и запоминает это в третьей группе захвата.
        - `\)` соответствует буквальной подстроке ")" в строке.
        """
        pattern = r"wait\(([^,]+),\s*([^,]+),\s*(after|before)\)"
        
        match = re.match(pattern, locator['action'])
        
        if match:
            cal_func = match.group(1)
            if cal_func == 'click()':
                cal_func = cal_func.replace('()', f'({locator})')
                """ Insert the locator into click() """
            inteval = int(match.group(2))
            when = match.group(3)
            driver.wait(cal_func=cal_func, wait=inteval, when=when)

#@logs_and_errors_decorator (default_return =  False)
def get_webelements_from_page(driver: Driver, locator: dict) -> Union[list, False]:
    """! This function takes a WebDriver instance and a locator dictionary and returns web elements found on the page by that locator.
    @param driver `Driver` : A WebDriver instance.
    @param locator `dict` : A dictionary containing the locator information. It must contain 'by' and 'selector' keys.
    
    @returns
        A list of web elements if there are multiple elements found, a web element if there is only one element found, or False if no elements are found.
    """
    if str ( locator['by'] ).upper() == 'XPATH':
        by = By.XPATH
        
    elif str ( locator['by'] ).upper() == 'ID':
        by = By.ID
        
    elif str ( locator['by'] ).upper() == 'TAG_NAME':
        by = By.TAG_NAME
        
    elif str ( locator['by'] ).upper() == 'CSS_SELECTOR':
        by = By.CSS_SELECTOR
        
    elif str ( locator['by'] ).upper() == 'NAME':
        by = By.NAME
        
    elif str ( locator['by'] ).upper() == 'LINK_TEXT':
        by = By.LINK_TEXT
        
    elif str ( locator['by'] ).upper() == 'PARTIAL_LINK_TEXT':
        by = By.PARTIAL_LINK_TEXT
        
    elif str ( locator['by'] ).upper() == 'TAG_NAME':
        by = By.TAG_NAME
        
    elif str ( locator['by'] ).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
        
    elif str ( locator['by'] ).upper() == 'VALUE':
        return locator ['attribute']
    
    
    elif str( locator['by'] ).upper() == 'ACTION':
        ''' Я могу подключить ислопнение комманд
        если locator['by'].upper() == 'ACTION'.
        См. `еxecute_action` метод
        '''        
        return execute_action(driver, locator)

    else:
        logger.error(f""" Не определен метод захвата элемента! 
        Локатор {locator} """)
        return False

    

    """!  Я решил всегда возвращать список даже если нашелся один элемент
    Алогритм поиска
    - Вначале пытаюсь выловить через driver.find_elements, (множество)
    - в случае неудачи через driver.find_element, (один)
    - если не поймал - делаю те же манипуляции через явное ожидание появления элемента на странице
    (при медленном коннекте такое помогает при долгой загрузке элемента)
    """
    _d = driver
    el: WebElement = None
    try:
        el =  _d.find_elements ( by, locator['selector'] )
    except Exception as ex:
        logger.warning(f'не найден СПИСОК элементов')
        try:
            el = [ _d.find_element(by, locator['selector']) ]
        except Exception as ex:
            logger.warning(f'не найден ОДИН элемент')    
            try:
                el = WebDriverWait (_d,10).until (EC.visibility_of_al_elements_located ((by, locator['selector'])) )
            except Exception as ex:
                logger.warning(f'не найден СПИСОК элементов с ожиданием')
                try:    
                    el = [ WebDriverWait(_d,5).until (EC.visibility_of_element_located ((by, locator['selector'])) )]
                except Exception as ex:
                    logger.warning(f'не найден ОДИН элемент с ожиданием')

    return el
  

#@logs_and_errors_decorator (default_return =  False)
def get_attributes_from_webelements(driver: Driver, locator: dict) -> Union[List[Dict[str, str]], Dict[str, str]]:
    """! @~russian Если локатор сложный (составной, с формулами итп) эта функция обрабатывает локатор и
    вызывает `get_attribute_by_locator()`  для получения значения аттрибута вебэлемента. 
    В простом случае вполне можно использовать `get_attribute_by_locator()`

     @param driver `Driver` WebDriver instance.
        
     @param locator `dict` containing information to locate the web element(s) and get the attribute(s).
                    Keys:
                        - 'by': the type of locator strategy to use (e.g., 'id', 'xpath', 'class name', etc.).
                        - 'selector': the selector string to use with the chosen locator strategy.
                        - 'action': the action to perform on the web element(s) (e.g., 'click', 'scrol', etc.).
                        - 'attribute': the attribute(s) to retrieve from the web element(s).
                                      It can be a single string or a dictionary with keys as attribute names and values
                                      as the desired attribute value for that attribute name.

    @returns
        Dictionary or List of dictionaries with the attribute-value pairs if multiple attributes are requested or
             a dictionary with a single attribute-value pair if a single attribute is requested.
    """
    ret = []
    
    # 1.1
    if locator['attribute'] is None:
        # If attribute is not specified, return the web element(s)
        #TODO: Странная ситуация. она уже оговорена в execute_locator
        return get_webelements_from_page ( driver, locator )

    # 1.2
    if isinstance(locator['attribute'], dict):
        # If attribute is a dictionary, get the attribute-value pairs as specified in the dictionary.
        # e.g., attribute:{"innerText":"href"}

        for key, value in locator['attribute'].items():
            # I build a temporary locator based on a dictionary defined in the passed locator to a function
            #   {"key":"value"}
            # A.
            # Get the attribute key
            key_locator: dict = dict.copy(locator)
            key_locator['attribute'] = key
            #key_locator = {
            #    "attribute": key,
            #    "by": locator["by"],
            #    "selector": locator['selector'],
            #    "action": locator['action']
            #}
            key_attributes = get_attribute_by_locator(driver, key_locator)
            
            # B.
            # Get the attribute value
            value_locator: dict = dict.copy(locator)
            value_locator['attribute'] = value
            #value_locator = {
            #    "attribute": value,
            #    "by": locator["by"],
            #    "selector": locator['selector'],
            #    "action": locator['action']
            #}
            value_attributes = get_attribute_by_locator(driver, value_locator)

            if isinstance(key_attributes, list):
                # If multiple web elements match the locator, return a list of attribute-value pairs
                for i in range(len(key_attributes)):
                    ret.append({key_attributes[i]: value_attributes[i]})
            elif isinstance(key_attributes, str):
                # If only one web element matches the locator, return a dictionary with a single attribute-value pair
                ret.append({key_attributes: value_attributes})
            else:
                # This should not happen, but just in case, log an error and return False
                logger.error(
                    f"Unknown type returned: {key_attributes, value_attributes}")
                return False

    # 1.3
    elif isinstance (locator['attribute'], list):
        # If attribute is a list, replace  the locator['attribute'] values for each element in the list.
        locator_attrs: list = locator['attribute']
        for _locator in locator_attrs:
            locator['attribute'] = _locator
            ret.append ( get_attribute_by_locator (driver, locator) )

    # 1.4
    else:
        """! Отдать аттрибут вебэлемента (списка веэлементов)"""
        # If attribute is a string, get the attribute value for the web element.
        ret = get_attribute_by_locator(driver, locator)
    return ret

#@logs_and_errors_decorator (default_return =  False)
def get_attribute_by_locator(driver: Driver, locator: dict) -> str:
    """! @~russian При простом локаторе - простое решение, чтобы получить атрибут элемента/ов .

    @param driver: an instance of WebDriver class, which controls the browser
    @param locator: a dictionary that contains the folowing keys:
        - "by": a string that specifies the way to locate the element (e.g. "id", "name", "xpath")
        - "selector": a string that specifies the value to locate the element
        - "attribute": a string that specifies the name of the attribute to retrieve from the element
    
    @returns a string representing the value of the attribute
    
    Raises: 
    - NoSuchElementException: if the web element cannot be found by the locator
    - WebDriverException: if some unexpected error occurs while retrieving the attribute
    
    """


    # -------------------- Поиск вебелемента --------------------------

    ret = None

    webelements = get_webelements_from_page(driver, locator)
    """! Вначале получаю вебэлемент целиком, а потом забираю нужный аттрибут """

    
    # ------------------------------------------------------------------

    if not webelements:
        # If no web elements are found by the locator, log an error message and return an empty list:
        if 'mandatory' in locator and locator['mandatory'] is False:
            """! необязательный элемент """
            logger.warning(f"""Не вернулся НЕОБЯЗАТЕЛЬНЫЙ элемент по локатору: 
                           {pprint(locator)}  """)
            return None
        
        logger.debug(f"""Не вернулся ОБЯЗАТЕЛЬНЫЙ элемент по локатору: 
                {pprint(locator)}  """)
        return False
        
    elif isinstance(webelements, list):
        """! @~russian итерируюсь по списку  полученных вебэлементов и собираю аттрибуты """
        # If multiple web elements are found by the locator, get the attribute value of each web element
        attributes = []
        for webelement in webelements:
            try:
                attributes.append (webelement.get_attribute ( locator['attribute']) )
                
            except Exception as ex:
                logger.debug(F"Error: {ex}", exc_info=True)
                # -- аттрибут не найден. Не строго. Пропускаю и ищу в следующем
                continue

                # --- СТРОГО. Заканчиваю поиск после первого фейла и возвращаю, что нашел
                #return attributes

                # ---- ОЧ СТРОГО
                #raise ExecuteLocatorException(ex)
        ret =  attributes
    else:
        """! получил один вебэлемент. Все равно возваращаю список аттрибутов """
        try:
            """! """
            ret =[ webelements.get_attribute ( locator['attribute'] ) ]
            #attributes = webelements.get_attribute(locator['attribute']) 
        except Exception as ex:
            logger.error(f'ошибка ', ex)
            ret = False 

   
    return ret

          

#@logs_and_errors_decorator (default_return =  False)
def evaluate_locator(expression_as_str, driver):
    """ Проверяю строку на наличие внутренней функции обрамленной в `$_(...)_$`
        если нашел - выплоняю эту/эти функцию/функции
        @param expression_as_str `str`  :  string to check evluatable blocks
        @param driver `Driver` [optional]: driver for execute
        @retruns функция возвращает строку с просчитанным значением, если в строке была формула, иначе функция возвращает
        строку без изменений. 
        @warning Пересчитанная строка остается в памяти локатора. Чтобы вернуть исходное состояние надо заново перечитать
        локатор из файла `JSON`. Файлы локаторов есть для трех страниц поставщика: 
        - category (категория), 
        - product (товар)
        - story (магазин)
        Функция, которая перечитывает локаторы из исходных файлов - `reread_locators(s: Supplier, entity: str)`,
        где entity - имя исходного файла `product` , `category` , `shop`
    """
    
    if not isinstance (expression_as_str, str): return expression_as_str
    if expression_as_str is None: return None
    if not '$_(' in expression_as_str: return expression_as_str

        

    def evaluate_expression(expression, driver):
        try:
            res = eval(expression)
            return str(res)
        except Exception as ex:
            logger.error(f""" Ошибка {ex} """, exc_info=True)
            return False

    start_marker = "$_("
    end_marker = ")_$"
    parts = expression_as_str.split(start_marker)
    prefix = parts[0]
    #result = prefix
    for part in parts[1:]:
        expression, suffix = part.split(end_marker, 1)
        evaluated_expression = evaluate_expression(expression,driver)
        res =  prefix + evaluated_expression + suffix
        return res
        pass


        ## @todo: Надо доделать часть, когда функций > 1.
        # сейчас я выполнаю только первую и то при условии, что она единственная 
        # в смысле, кроме нее ничего нет
    #    result += evaluated_expression + rest
    #return result

#@logs_and_errors_decorator (default_return =  False)
def get_webelement_as_screenshot(webelement) -> bool:
    """! @~russian Беру скиншот элемента в формате `.png`.
    @todo добавить возможность делать скриншот всего экрана, его части, всплывающих окон
    Takes a screenshot of a given WebElement object and returns it as a PNG image.

    @param webelement: вебэлемент. 
    @note Вначале по локатору достается вебэлемент, а потом прогоняю его через функцию
    и получаю массив байтов, по сути, картинку

    @returns Бинарный код изображения
        A binary PNG image if successful, False if the element is no longer attached to the DOM or an error occurs.
    """
    try:
        screenshot = webelement.screenshot_as_png
        return screenshot
    except Exception as ex:
        logger.error ( f"Error:{ex}" )
        return False

#@logs_and_errors_decorator (default_return =  False)
def click(driver, locator) -> bool:
    """!
    Clicks the WebElement identified by the provided locator.

    @param driver `Driver`: The Driver instance.
    @param locator `dict`: A dictionary containing the details of the locator.

    @returns `True` if the click was successful, `False` otherwise.

    """

    # Get the WebElement
    webelement = get_webelements_from_page (driver, locator)

    if not webelement and locator['mandatory'] is False:
        return False
    elif not webelement and locator['mandatory'] is True:
        logger.error(f"Could not find element to click. Locator: {locator}")
        return False
    
    # Click the FIRST  element
    try:
        _prev_url = driver.current_url
        webelement[0].click()
        if  _prev_url != driver.current_url:
            driver.previous_url = _prev_url
            """! Запомнил, откуда пришел, если клик увел на другой адрес """
        
        driver.switch_to.window(driver.window_handles[-1])
        """! фокус на последннeе открытое окно 
        Если ссылка открывает новое окно - я фокусируюсь на нем """
        
    except Exception as ex:
        logger.error(f"Failed to click element. Locator: {locator}. Error: {ex}")
        return False

    return True


#@logs_and_errors_decorator (default_return =  False)
def reread_locators(s, entity: str ) -> Union[dict, False]:
    """! @~russian  Заново перечитываю файлы локаторов вебэлементов
    @details
    Иногда, чтобы построить локатор требуется провести предварительные вычисления
    После исполнения вычисления в памяти остается изменное значение локатора. 
    @param entity `str` : Какой из локаторов обновить: `product, category, login, shop`
    @example 
        "price": {

            "new": {
            "attribute": "innerText",
            
            "by": "XPATH",
            "selector": "//div[contains(@data-csa-c-asin, '$_(driver.current_url.split(f'''/''')[-2])_$') and contains(@id, 'corePriceDisplay')]//span[1]",
            
            "use_mouse": false, 
            "mandatory": true,
            "action": nul
            }
        }

    """
    
    try:
        """! """
        locators_file = Path (s.supplier_abs_path, 'locators', f'{entity}.json')
        s.locators [ entity ] = j_loads (locators_file) 
        return s.locators [ entity ]
    except Exception as ex:
        logger.error(f'ошибка ', ex)
        return False
            






####################################################################################################
#            
#
#                                   Старый код
#
#
#def return_value_from_locator(driver, locator):
#    """
#    @param
#        locator['attribute'] (Union[str,list]): - const f.e. 1 or 'string' or nul etc
#                                                - list(const) f.e. "[1,'string,False]"
#                                                - variable: start from `_$` f.e. _$var1
#                                                - I can alternate variables and constants in any sequence: "1,_$var2,Flase ..." or "[1,_$var2,Flase]"
#                                                - hypotez objects: $d, $s, $c, $p each one mean: Driver, Supplier, Category, Product
#                                                (I can easily assign properties to object attributes if alowed.
#                                                f.e. $d.get_url )



#        To avoid creating additional entities in the locator dictionary, I can transfer the values from attributes through selector.
#        я могу передать данные (константы, переменные, классы) через ключ `attribute` 
#        здесь строится логика, основанная на синтаксисе $_()_

#        Here is an example of how such a locator looks like:

#        {
#            "attribute": "$_(d.current_url.split(f'''/''')[-2])_$",
#            "logic for attribue[AND|OR|XOR|VALUE|nul]": None,
#            "by": "VALUE",
#            "selector": "",
#            "logic for action[AND|OR|XOR|VALUE|nul]": None,
#            "use_mouse": False,
#            "action": None
#        }
#        OR
#          "price": {
#                "attribute": "innerText",
#                
#                "by": "XPATH",
#                "selector": "//div[contains(@data-csa-c-asin, '$_(d.current_url.split(f'''/''')[-2])_$') and contains(@id, 'corePrice_desktop')]// span[contains(@class, 'apexPriceToPay')]",
#                
#                "use_mouse": false, "mandatory": true,
#                "action": nul
#              }

#    @returns from the example shown above, the folowing wil be returned: [5,forward',0]
#        """
#    pass


#def get_imgs_links(driver, url):
#    """
#    Extracts image URLs from the specified URL.

#    @param
#        driver: An instance of the Selenium webdriver.
#        url `str`  :  The URL of the page to extract images from.

#    @returns
#        A dictionary of image names and URLs. Returns None if no images were found.
#    """


#    locator = {
#        "attribute": {"innerText": "src"},
#        "by": "XPATH",
#        "selector": "//img",
#        "action": None
#    }

#    _ = driver.scrol(5)
    
#    imgs = driver.execute_locator(locator)
#    f"""возвращает словарь {"img name":"img url"} """
    
#    if not imgs or len(imgs) == 0:
#        return None
#    else:
#        return imgs

#def calculate_formulae_in_locators(driver, locator) -> list[str]:
#    formulae = SF.extract_value_from_parentheses_with_lead_dolar(locator['attribute'])
#    res: list = list()
#    for formula in formulae:
#         res.append(eval(formula))    
#    return res


# def execute_action(driver,locator,keys=None)->bool:
#     _d = driver
#     # Проверяю наличие формулы для локатора
#     if locator['action'] == 'loop':
#         if len(locator['variables in selector'])>0 :
#             #x = eval(locator['variables in selector'])
#             _range = locator['formula for locator']
#             for x in eval(_range):
#                 selector = str(locator['selector']).replace('{x}',str(x))
#                 _l:dict = {
#                 "attribute" : locator['attribute'],
#                 "by": locator['by'],
#                 "selector" : selector,
#                 "action":None}

#                 if not _d.execute_locator(_l):
#                     pass               
#         pass
    
#     #1. click
#     if locator['action'] == 'click()':
#         """ 1. click() """
#         driver.click(locator)
        
#     #2. send_keys([key])
#     elif str(locator['action']).find('send_keys(')>-1:
#         """ 2. send_keys() """
#         #if not driver.click(driver, locator):pass
#         """ не нажался элемент. Пока не страшно. 
#         нам важно ему передать значение. Нажималка для подстраховки"""

#         webelement = get_webelements_from_page(driver,locator)
#         if not webelement:
#             logger.error(f"""Не найден {locator}""")
#             return False
                     
#         """ ключ может передаваться самим локатором или извне 
#         TODO сделать внешний приоритетным
#         """
#         if keys is None:
#             key_from_locator = locator['action']
#             key_from_locator = f"""{key_from_locator[key_from_locator.rfind("('")+2:key_from_locator.rfind("')"):]}"""
#             """ ключи передаются в ОДИНОЧНЫХ скобках парамертрами функции. Я их вытаскиваю """
#             keys = key_from_locator
#             try:
#                 webelement.send_keys(keys)
#                 return True
#             except Exception as ex:
#                 logger.error(f""" не выполнилось действие {locator['action']}""")
#                 return False

#         else:
#             try:
#                 webelement.send_keys(keys)
#                 return True
#             except Exception as ex:
#                 logger.error(f"""Ошибка в send_keys({keys}):
#                 {ex.with_traceback(ex.__traceback__)}""") 

#                 return False

#     #3. screenshot
#     elif str(locator['action']).find('screenshot(')>-1:
#         """ 3. screenshot() """
#         webelements = get_webelements_from_page(driver,locator)
#         if webelements == False: 
#             logger.error(f''' Не нашел картинку :( ''')
#             return False
#         return get_webelement_as_screenshot(webelements[0]) if isinstance(webelements, list) else get_webelement_as_screenshot(webelements)

#     #4. scrol
#     elif str(locator['action']).find('scrol(')>-1:
#         """ 4. scrol() """
#         return eval(locator['action'])
#     #5. wait
#     elif str(locator['action']).find('wait(')>-1:
#         pattern = r"wait\(([^,]+),\s*([^,]+),\s*(after|before)\)"

#         """ Объяснение:
#             wait\( соответствует литералу "wait(" в строке
#             ([^,]+) соответствует любой непустой последовательности символов, не являющихся запятой, 
#                 и сохраняет их в первую группу захвата
#             ,\s* соответствует запятой, за которой могут следовать некоторые пробелы
#             ([^,]+) соответствует любой непустой последовательности символов, не являющихся запятой, 
#                 и сохраняет их во вторую группу захвата
#             ,\s* соответствует запятой, за которой могут следовать некоторые пробелы
#             (after|before) соответствует либо строке "after", либо строке "before", 
#                 и сохраняет ее в третью группу захвата.
#             \) соответствует литералу ")" в строке.

#         """
#         match = re.match(pattern, locator['action'])
#         if match:
#             cal_func = match.group(1)
#             if cal_func == 'click()':
#                 cal_func = cal_func.replace('()',f'''({locator})''')
#                 """ вставляю локатор в click() """
#             inteval = int(match.group(2))
#             when =  match.group(3)
#             driver.wait(cal_func = cal_func, wait=inteval, when=when)

    
# def get_attributes_from_webelements(driver,locator)->list:
       
#     _ret:list=[]                          
#     if locator['attribute'] is None:
#         """TODO ЗАЧЕМ Я ВОЗВРАЩАЮ разные ТИПы ??? 
#         Здесь я возвращаю весь вебэлемент """
#         return get_webelements_from_page(driver,locator)

#     if isinstance(locator['attribute'],dict):
#         # Я могу получить аттрибут в виде словаря.
#         # Например, attribute:{"innerText":"href"}
#         # пример использования есть в файле gsmarena_com.py
            
        
#         for key,value in locator['attribute'].items():

#             #а) ключи
#             _k : dict = {"attribute":key,
#                         "by":locator["by"],
#                         "selector":locator['selector'],
#                         "action":locator['action']}

#             k = get_attribute_by_locator(driver,_k)
#             # получаю в ответ список ключей

#             #б) значения
#             _l : dict = {"attribute":value,
#                         "by":locator["by"],
#                         "selector":locator['selector'],
#                         "action":locator['action']}

#             v = get_attribute_from_web_element(driver,_l)  
#             # получаю в ответ список значений
                             

#             if isinstance(k,list):
#                 """ Может вернуться список [{ключ:значение},{...|...}]"""
#                 for i in range(len(k)):
#                     _ret.append({k[i]:v[i]})
#                 return _ret

#             elif isinstance(k,str):
#                 """ или одна пара {ключ:значение}"""
#                 return {k:v}
#             else: 
#                 """ не знаю, что за ситуация """
#                 logger.error(f"""А ты кто такое?
#                 {k,v}""")
#                 return False

#     elif isinstance(locator['attribute'],list):
#         # я могу получить список требуемых аттрибутов веб эемента/ов

#         while len(locator['attribute'])>0:
#             _ret.append(get_attribute_by_locator(driver,locator).pop(0))
                
#     else:
#         _ret = get_attribute_by_locator(driver, locator)
#     return _ret
     

# def get_attribute_by_locator(driver,  locator)->str: 
#     webelements = get_webelements_from_page(driver,locator)

#     if not webelements:
#         logger.error(f'''  Не вытащил атрибут по локатору 
#         {locator}
#         ''')
#         return []

#     elif isinstance(webelements,list):
#         attributes:list = []
#         for webelement in webelements:
#             try:
#                 _attr = webelement.get_attribute(locator['attribute'])
#                 attributes.append(_attr)
#             except Exception as ex: 
#                 logger.error(ex)
#                 return attributes
#         return attributes
                

#     else:
#         """ пришел один элемент """
#         attributes = webelements.get_attribute(locator['attribute'])
#         return attributes
    

# def get_webelements_from_page(driver, locator)->list:

#     if locator['by'].upper() == 'XPATH':
#         by = By.XPATH
#     if locator['by'].upper() == 'ID':
#         by = By.ID
#     if locator['by'].upper() == 'TAG_NAME':
#         by = By.TAG_NAME
#     if locator['by'].upper() == 'CSS_SELECTOR':
#         by = By.CSS_SELECTOR
#     if locator['by'].upper() == 'NAME':
#         by = By.NAME

#     try: 
#         """ может быть несколько элементов на странице """
#         #elements = webdriverWait(driver,3).until(EC.visibility_of_al_elements_located((locator['by'], locator['selector'])))
#         #WITH WAIT (GOOD FOR AJAX)

#         elements = driver.find_elements(by, locator['selector'])
#     except Exception as ex: 
#         """ а может быть один """
#         try:
#             #elements = webdriverWait(driver,3).until(EC.visibility_of_element_located((locator['by'], locator['selector'])))
#             #WITH WAIT (GOOD FOR AJAX)

#             element = driver.find_element(by, locator['selector'])
#         except Exception as ex:    
#             logger.error(f""" Не найден элемент по локатору 
#             {locator}
#             """)
#             return False

#     ##if isinstance(elements, WebElement):
#     #    return elements
#     if len(elements)<1: 
#         return False

#     elif len(elements)==1:
#         return elements[0]
#     else: 
#         return elements 

# def get_webelement_as_screenshot(webelement)->bool:
#     """ Возвращает png любого элемента DOM
#     @param
#         webelement (_WebElement_): релевантный DOM элемент
#     @returns
#         png image
#     """
#     try:
#         screenshot = webelement.screenshot_as_png
#         return screenshot
#     except Exception as ex:
#         if ex.with_traceback().find("is no longer attached to the DOM"):
#             logger.error(f"""Потерял элемент в DOMе {ex.with_traceback(ex.__traceback__)}""" )
#             return False
#         else:
#             logger.error(f"""Потерял элемент кяк то по - другому {ex.with_traceback(ex.__traceback__)}""")
#             return False

# def save_webelement_as_screenshot(driver, webelement, file_path, send=True)->bool:
#     """Сохраняю вебэлемент в скриншот """
#     ''' https://stackoverflow.com/questions/17361742/download-image-with-selenium-python '''
#     #TODO: send to ftp
    
#     try:
#         with open(file_path , 'wb') as\file
#             file.write(webelement.screenshot_as_png)
#             return True
#     except Exception as ex:
#         logger.error(f''' не записался скриншот элемента {dir(webelement)} 
#         в путь: {file_path}''')

