"""! @brief  [File's Description]

@namespace src: src
 \package src.suppliers.etzmaleh
\file login.py
 
 @section libs imports:
  - helpers 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.helpers import  logger,  logs_and_errors_decorator
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
  
    logger.info(f'''Залогинился .... ''')
    return True