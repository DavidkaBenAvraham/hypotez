"""! @ru_brief Модуль I/O интерфейса для JSON  
Module for working with JSON and HTML data.
 
 @section libs imports:
  - json 
  - pathlib 
  - typing 
  - collections 
  - helpers 
 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import os, json
from pathlib import Path
from typing import Union
from collections import OrderedDict

from src.helpers import logger,  logs_and_errors_decorator, exceptions

#@logs_and_errors_decorator (default_return =  False)
def json_loads(jjson: Union[Path, dict, str], ordered: bool = False) -> Union[dict, OrderedDict, bool]:
    """Load JSON data from file or string.
    @details ОЧЕНЬ! Внимательно относиться к параметрам. `Path | str` Если функция получит на вход путь к файлу типа строки - она будет парсить строку
    Поэтому надо указывать тип Path в адресе файла
    @todo сделать, чтобы это не было проблемой

    @param jjson `Path` path to file
    @param jjson `dict | str` JSON data as string, or JSON object.
    @param ordered `bool` : If `True`, return an `OrderedDict` instead of a regular `dict` to preserve the order of elements.

    @returns dict  :  JSON data as a Python dict
    @returns OrderedDict `OrderedDict` словарь, который сохраняет порядок вставки элементов
    @returns False `bool`:  if an error occurred.
    """

    if isinstance(jjson, str) and not os.path.isfile(jjson):
        
        return json.loads(jjson, object_pairs_hook=OrderedDict if ordered else None)

    elif isinstance(jjson, Path) or os.path.isfile(jjson):
        try:
            with jjson.open(encoding='utf-8') as f:
                data = json.loads(f.read(), object_pairs_hook=OrderedDict if ordered else None)
            return data
        except Exception as ex:
            logger.error(f'Failed to read JSON file: {jjson}. Error: ', ex)
            return False
    else:
        logger.error(f'Не нашелся файл: {jjson}. ')
        raise exceptions.FileNotFoundError(f'Не нашелся файл: {jjson}. ')
        """! @ru_todo Реализовать обработку ошибок """
            


def json_dumps(data: dict, path: Path) -> bool:
    """Dump JSON data to file.

    @param
        data (dict): JSON data as a Python dict.
        path (Path): Path to output file.

    @returns
        bool: True if successful, False if an error occurred.

    """
    try:
        with path.absolute().open('w', encoding='utf-8') as f:
            json.dump(data, f)
        return True
    except Exception as ex:
        logger.error(f'Failed to dump file {path}. Error: ', ex)
        return False
