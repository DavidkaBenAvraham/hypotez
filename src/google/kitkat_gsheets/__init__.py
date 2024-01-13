"""  [File's Description]

@namespace src: src
   \package src.google.hypotez_sheets
\file __init__.py
 
 @section libs imports:
  - httplib2 
  - apiclient.discovery 
  - pandas 
  - gspread 
  - oauth2client.service_account 
  - DBO.customers 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import httplib2 
import apiclient.discovery
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials



class spreadsheets():
    gc = None 

    def __init__(self):
        self.CREDENTIALS_FILE = 'hypotez_gsheets/e-cat-346312-d15b2f0d86d0.json'  

                    # use creds to create a client to interact with the Google Drive API
            #        
            #        https://stackoverflow.com/questions/49829002/invalid-scope-https-spreadsheets-google-com-feeds-is-not-a-valid-audience-str
            #        
            #        Scope Meaning
            #https://www.googleapis.com/auth/spreadsheets.readonly Allows read-only access to the user's sheets and their properties.
            #https://www.googleapis.com/auth/spreadsheets Allows read/write access to the user's sheets and their properties.
            #https://www.googleapis.com/auth/drive.readonly Allows read-only access to the user's file metadata and file content.
            #https://www.googleapis.com/auth/drive.file Per-file access to files created or opened by the app.
            #https://www.googleapis.com/auth/drive Full, permissive scope to access all of a user's files. Request this scope only when it is strictly necessary.
      
        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.CREDENTIALS_FILE, scope)
        self.gc = gspread.authorize(creds)
        
        #ss = gc.open(https://docs.google.com/spreadsheets/d/19QXhtuzfPccHqLPLOuvxsVchiHCdoJxTmdSfU_gtrDs)
        # https://github.com/burnash/gspread

    def get_wrksht(self, wrksh_id):
        return self.ss.get_worksheet_by_id(int(wrksh_id))

    def get_worksheets_list(self):
       return self.ss.worksheets()

    def get_listmodels_from_wrksht(self):
        return self.wsht_models.row_values(1)
    
    def build_next_order(self , data):
        self.wsht_neworder.cell()


    def update_wrksht_as_dt(self,wrkst, dt):
        wrkst.update([dt.columns.values.tolist()] + dt.values.tolist())



    def fill_wrksht_new_order(self,  last_order):    

        print(last_order)
        print(self.wsht_neworder)
        self.wsht_neworder.update_cell(3, 3, last_order[0])
        self.wsht_neworder.update_cell(4, 3, last_order[2])
        self.wsht_neworder.update_cell(5, 3, last_order[4])
        self.wsht_neworder.update_cell(10, 3, last_order[6])



        tlunotLakoah_str = str(last_order[6])

        # делю на слова
        tlunotLakoah_list = tlunotLakoah_str.split()
        # и ищу название модели компьютера
        for item in tlunotLakoah_list:
            if str(item).upper() in self.models:
                self.wsht_neworder.update_cell(7, 3, item.upper())

        if tlunotLakoah_str.find('יש אישור'):
            self.wsht_neworder.update_cell(13, 3, 'יש אישור')

        

    def fill_wrksht_customers(self):
      
        #manoa_db = manoa.DB()
        sql = str('''
        select id ,
        contactPerson,
        name ,
        cellPhone,
        fax,
        email,   
        notes,
        messages
        from DBO.customers c 
        ''')
        manoa_dt = manoa.DB().get_as_dt(sql)
        update_wrksht_as_dt(self.wsht_customers ,  manoa_dt)
    
      