"""! @ru_brief Модуль печати для просморта в удобной форме структур
@ru_details содержит 2 функции: 
- jprint - печатает json подобную структуру (например, словарь или содержимое json файла)
- pprint
 
@section libs imports:
- json 
- pprint 
  
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import json
from pprint import pprint as pretty_print

def jprint(print_data: json, indent: int = 4) -> None:
    """! @param print_data `json` струкура, которую надо распчатать как код (с опступами) 
         @param indent `int` - глубина отступов в пробелах"""
    try:
        print(json.dumps(print_data,indent))
    except:
        print(json)

def pprint(print_data):
    """! @param print_data `json` струкура, которую надо распчатать как код (с опступами) """
    try:
        pretty_print(print_data)
    except Exception as ex:
        print_data = '''
        Error on pprint:
        {ex}
        ------------
        msg :
        {print_data}
        '''
        try:
            jprint(print_data)
        except Exception as ex:
            print_data = '''
            Error on jprint:
            {ex}
            msg:
            {print_data}
            '''
            print(print_data)
        