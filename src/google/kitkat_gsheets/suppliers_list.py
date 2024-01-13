"""  google.kikat_gshets

@namespace src: src
   \package src.google.hypotez_sheets
 
\file supplier_prefix.py
 
 @section libs imports:
  - asyncio.log 
  - hypotez_gsheets 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from asyncio.log import logger
from hypotez_gsheets import spreadsheets as spreadsheets

class supplier_prefix(spreadsheets):
    s = spreadsheets()
    SS_SUPPLIERS = '14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ'
    WRKSHT_EXPORT_SUPPLIERS = '931130305'
    ss = False
    def __init__(self):
        #super().__init__()
        self.ss = self.s.gc.open_by_key(self.SS_SUPPLIERS)
        pass
    
    def get(self):
        try:
            wksht = self.ss.get_worksheet_by_id(int(self.WRKSHT_EXPORT_SUPPLIERS))
            return wksht
        except Exception as ex:
            logger.error(f''' не удалось прочитать гугль лист ''')
    
    