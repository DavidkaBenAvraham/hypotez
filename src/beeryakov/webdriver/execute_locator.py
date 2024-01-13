"""!  Execute locator

 
 @section libs imports:
  - json 
  - webdriver 
  - selenium.webdriver.support.ui 
  - selenium.webdriver.support 
  - selenium.webdriver.common.by 
  - selenium.common.exceptions 
  - selenium.webdriver.common.action_chains 
  - selenium.webdriver.common.keys 
  - pprint 
  
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""
import json 
from src.webdriver import driver as d
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import pprint
pp = pprint.PrettyPrinter(indent = 4)
pprint = pp.pprint


# # Wait for the page to load
# EC.presence_of_all_elements_located
# try:
#     WebDriverWait(d, 10).until(EC.presence_of_element_located((By.ID, 'myDynamicElement')))
#     print("Page is ready!")
# except TimeoutException:
#     print("Loading took too much time!")



def execute(locator: json) -> bool:
    _by = str(locator['by']).upper()
    if _by == 'XPATH':
        _by = By.XPATH
    elif _by == 'CSS':
        _by = By.CSS_SELECTOR
    elif _by == 'CLASS_NAME':
        _by = By.CLASS_NAME
    elif _by == 'CSS_SELECTOR':
        _by = By.CSS_SELECTOR
    elif _by == 'ID':
        _by = By.ID
    elif _by == 'LINK_TEXT':
        _by = By.LINK_TEXT
    elif _by == 'PARTIAL_LINK_TEXT':
        _by = By.PARTIAL_LINK_TEXT
    elif _by == 'TAG_NAME':
        _by = By.TAG_NAME
    elif _by == 'NAME':
        _by = By.NAME
    elif _by == 'TAG_NAME':
        _by = By.TAG_NAME
    else:
        return False
    
    selector = locator['selector']
    el = None
    try:
        WebDriverWait(d, 10).until(EC.presence_of_all_elements_located((_by, selector)))
    except Exception as ex:
        #print(f'не найден элемент :(')
        #pprint(locator)
        pass
    
    if locator['action']:
        if locator['action'] == 'click()':
            try:
                WebDriverWait(d, 10).until(EC.element_to_be_clickable((_by, selector))).click()
                #e = d.find_element(_by, selector)
                #e.click()
            except Exception:
                #print(f'не найден элемент {pprint(locator)}')
                return False
                

    

    try:
        el = d.find_elements(_by, selector)
    except Exception as ex:
        el = d.find_element(_by, selector)

    res: list = []
    attribute = locator['attrs']

    if isinstance(attribute, str):    
        if isinstance(el, list):
            for e in el:
                res.append( e.get_attribute(attribute))
        elif not el is None:
            res.append(el.get_attribute(attribute))
        else:
            return False
        return res
    
    
    elif isinstance(attribute, dict):
        a: dict = attribute
        key: str = list(a.keys())[0]
        value: str = list(a.values())[0]

        if isinstance(el, list):
            for e in el:
                res.append( {e.get_attribute(key): e.get_attribute(value)})
        elif not el is None:
            res.append( {el.get_attribute(key): el.get_attribute(value)})
    else:
        return False
    return res
            
    
    