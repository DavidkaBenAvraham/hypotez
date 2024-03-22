# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! @~russian Модуль рекламы на фейсбук
@rem Точка входа в программу """

import os, sys
from pathlib import Path
from typing import Union, Dict, List

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator, DefaultSettingsException, jprint, pprint
from src.webdriver import Driver

# ----------------------------------


class Facebook():
	"""! @~russian Класс общается с фейбуком через вебдрайвер 
	
	@param driver `Driver`  :   вебдрайвер (`src.webriver.Driver.Driver`) 
	"""    
	#dir_facebook_ads = Path(gs. )
	d = driver = Driver()
	locators = j_loads
	
	#@logs_and_errors_decorator(default_return=False)
	def __init__(self, *args, **kwards):
		"""! @~russian 
		@brief Конструктор
		"""
		
		self.driver.get_url (r'https://facebook.com')
	        
	
	#@logs_and_errors_decorator(default_return=False)
	def login(self, d):
		pass
	    
	
	#@logs_and_errors_decorator(default_return=False)
	def click_add_images_video():
	    """! @~russian 
	    @brief
	    @details
	    """
	    
	        
	        
facebook = Facebook()
pass
	
