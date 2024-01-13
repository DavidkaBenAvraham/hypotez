# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! @ru_brief Модуль рекламы на фейсбук
@rem Точка входа в программу """

import os, sys
from pathlib import Path
from typing import Union

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator, jprint, pprint
from src.webdriver import Driver
from src.scenarios import executor
# ----------------------------------

class Facebook():
	"""! @ru_brief Класс общается с фейбуком через вебдрайвер 
	
	@param driver `Driver`  :   вебдрайвер (`src.webriver.Driver.Driver`) 
	"""    
	dir_facebook = Path(gs. )
	driver = Driver()
	locators = j_loads
	
	#@logs_and_errors_decorator(default_return=False)
	def __init__(self, *args, **kwards):
		"""! @~russian
		@brief Конструктор
		"""
		
		self.driver.get_url (r'https://facebook.com')
	        
	
	#@logs_and_errors_decorator(default_return=False)
	def login():
		"""! @~russian
		@brief
		@details
		"""
		pass
	    
	
	#@logs_and_errors_decorator(default_return=False)
	def click_add_images_video():
	    """! @~russian
	    @brief
	    @details
	    """
	    
	        
	        
facebook = Facebook()
pass
	
