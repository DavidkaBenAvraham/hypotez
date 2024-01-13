"""!  Edge webdriver


 
 @section libs imports:
  - selenium 

"""
from selenium import webdriver

options = webdriver.EdgeOptions()
#options.use_chromium = True
#options.add_argument("headless")
#options.add_argument("disable-gpu")

driver = webdriver.Edge(options = options)
