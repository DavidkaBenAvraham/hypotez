"""! @russin Модуль рамещения рекламы
@param dir_root `Path`  :  корневая директория (hypotez)
@param dir_src `Path`  :  директория кода (hypotez)
"""
import os
import sys
import datetime
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 


from facebook import Facebook