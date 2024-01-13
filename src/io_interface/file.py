"""! @ru_brief Модуль импорта / экспотра файлов

 
@section libs imports:
- helpers (local)
- typing 
- pathlib 
- json (local)
  
 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import json
from typing import Union
from pathlib import Path
from src.helpers import  logger, logs_and_errors_decorator


def export_products_data_to_csv(data: str, file_name_path: str, format: Union[str, list] = 'csv') -> bool:
    """! Export data to file in the specified format.

     @param    data `Union[dict, pd.DataFrame]` : data to export
     @param    filename  `str` :  name of the file to create
     @param    format `str | list[str]` = 'csv' : format of the file ('json', 'csv', 'txt', 'xls'). Defaults to 'csv'.

    @returns     bool : `True` if the export was successful, `False` otherwise

    """
    if not file_name_path:
        raise ValueError("Filename must be specified.")

    if not isinstance(format, (str, list)):
        raise TypeError("Format must be a string or a list of strings.")

    if isinstance(format, str):
        format = [format]

    for frmt in format:
        export_file_path = Path(gs.di, f'{file_name_path}.{frmt}')

        if frmt == 'json':
            try:
                with open(export_file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)
                return True
            except Exception as ex:
                logger.error(
                    f"Error exporting to JSON file {export_file_path}: {ex}")
                return False

        elif frmt == 'csv':
            try:
                if isinstance(data, dict):
                    df = pd.DataFrame.from_dict(data)
                else:
                    df = data
                df.to_csv(export_file_path, sep=';',
                          index=False,  encoding='utf-8')
                return True
            except Exception as ex:
                logger.error(
                    f"Error exporting to CSV file {export_file_path}: {ex}")
                return False

        elif frmt == 'txt':
            try:
                with open(export_file_path, 'w', encoding='utf-8') as f:
                    f.write(str(data))
                return True
            except Exception as ex:
                logger.error(
                    f"Error exporting to TXT file {export_file_path}: {ex}")
                return False

        elif frmt == 'xls':
            # TODO: add support for XLS format
            logger.warning("XLS format is not yet supported.")
            return False

    return False

def save_text_file(data: str, file_name_path: str, mode: str = 'w') -> bool:
    """! @ru_brief Функция записывает текстовый файл 
    @param data `str` Данные на запись
    @param file_name_path `str` полный путь к файлу 
    @param mode `str` Режим записи :
    - w запись поверх данных
    - а запись в конец данных
    @returns bool `True` if successful, else `False`
    """
    try:
        with open(file_name_path, mode) as file:
            file.write(data)
        return True
    except Exception as ex:
        logger.error(f'Файл {file_name_path} не записался. Ошибка {ex} ')
        return False