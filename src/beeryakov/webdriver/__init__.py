"""  [File's Description]

@namespace src: src
 \package beeryakov.webdriver
\file __init__.py
 
 @section libs imports:
  - webdriver.edge 
  - webdriver.execute_locator 
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""

from src.webdriver.edge import driver
#from src.webdriver.mozilla import driver
from src.webdriver.execute_locator import execute as execute_locator