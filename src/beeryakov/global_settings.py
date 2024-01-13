"""!  global settings for module

 
 @section libs imports:
  - os 
  - sys 
  - webdriver.edge 
  - suppliers.ksp 
  - goog 
  - pprint 
  - os 
  
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""

import os
# Current working directory
cwd = os.getcwd()

import sys
sys.path.append(cwd)


from src.webdriver.edge import driver
from src.suppliers.ksp import ksp
from goog import GSpreadsheet, GWorksheet, GSRender

import pprint
pp = pprint.PrettyPrinter(indent = 4)
pprint = pp.pprint


import os

file_path = "../example.txt"

cwd = os.getcwd()