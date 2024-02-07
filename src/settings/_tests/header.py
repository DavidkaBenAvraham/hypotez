""" 
  set os system path to hypotez
\file header.py
 @section libs imports:
  - sys 
  - os 
  - datetime 
  - pathlib 
Author(s):
  - Created by Davidka on 15.11.2023 .
"""

import sys
import os
import datetime
from pathlib import Path

dir_root : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (dir_root)