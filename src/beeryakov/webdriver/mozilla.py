"""  Mozilla webdriver

@namespace src: src
 \package beeryakov.webdriver.mozilla
\file mozilla.py
 
 @section libs imports:
  - selenium 
  - time 
  
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""
from selenium import webdriver

import time


options = webdriver.FirefoxOptions()
#options.use_chromium = True
#options.add_argument("headless")
#options.add_argument("disable-gpu")

driver = webdriver.Firefox()
