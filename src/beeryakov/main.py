"""  KSP to GTables

@namespace src: src

\file main.py
 
 @section libs imports:
  - gs 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

from global_settings import \
    driver, \
    pprint, ksp, \
    GSpreadsheet, GWorksheet



def run():
    """
    Старт парсера
    """
    sh_id = '1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM'
    root: str = 'https://ksp.co.il' 
    d = driver
    d.get(root)
    worlds_dic: dict = ksp.get_worlds()

    sh = GSpreadsheet(sh_id)
    

    for url, ws_title in worlds_dic.items():
        
        ws: GWorksheet = GWorksheet(sh, ws_title)
        ws.header(ws_title, 'A1:Z1')
        
        """
          1. добавляю таблицу в книгу если ее нет,
          иначе очищаю от страых данных
          2.  и возвращаю ее  """
        
        d.get(url)
        """ ныряю в категорию """
        subs = ksp.get_subs_from_world()
        #print('\t\t CATEGORIES: ')

        for url, category_title in subs.items():
            
            d.get(url)
            
            ws.append_row (ws.category (category_title ) )
            brands = ksp.get_all_brands_list()
            print(f'\t\t\t BRANDS:')
            #_ws.append_row([f' category} - BRANDS'])
            i=0
            for brand, qty in brands.items():
                ws.append_row([brand,qty])
                i += 1
                
            print(f'added {i}')
        
        pprint(f' ********************************')

def get_all_spreadsheets():
    gspreadsheets = gsh.get_all_spreadsheets_for_current_account()
    pass

#run()