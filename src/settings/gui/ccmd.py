"""!  Command Line Interface 
 @section libs imports:
  - argparse 
  - asyncio 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import argparse
import asyncio
parser = argparse.ArgumentParser()
""" требуется для ассинхроннго ввода (ввода с ожиданием) """

def prompt_input(parser:argparse.PARSER)->parser:

    parser.add_argument('--suppliers', nargs='?', help=f''' префикс постащика. Например, aliexpress или mor 
       спискок поставщиков: {gs.supplier_prefix} ''')
    args = parser.parse_args()

    print(f'''Вот список поставщиков:
        {gs.supplier_prefix}
        Введи имя поставщика.
        ''')

    args.supplires = wait_for_input()
    parser.add_argument('--scenarios', nargs=None, help=f''' файл сценария. ''')
     
    return parser

async def get_input()->str:
    """_summary_

    @returns
        _type_: _description_
    """
    return input()

async def wait_for_input(print_str:str=None,N:int=1):
    """ автоввод с ожданием N секунд
    Attrs:
    print_str: будет напечатана если не пустое значение, иначе игнор
    N: интервал ожидания
    """     
    if print_str is not None:
        print(print_str)

    try:
        """_summary_

        @returns
            _type_: _description_
        """
        result = await asyncio.wait_for(get_input(), timeout=N)
        return result
    except asyncio.TimeoutError:
        print("Вы не ввели ничего в течение заданного времени.")
        return False