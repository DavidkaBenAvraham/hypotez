"""! @~russian 
@brief Модуль нормализации строк
@details Модуль может содержать функции для нормализации строк, то есть приведения строк к определенному стандарту или формату.
Это может включать в себя приведение всех символов к нижнему или верхнему регистру, удаление пробелов, удаление диакритических знаков и т. д.

 @section libs imports:
  - urllib.parse 
  - attr 
  - typing 
  - .string_formatter 
  - helpers 
  - gs 
  - .re_patterns 
  - . 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from urllib.parse import urlparse, parse_qs
from attr import attr, attrs
from typing import Union, List
from .string_formatter import StringFormatter as SF
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads
from .re_patterns import Ptrn
from . import symbols2HTML_dict


class StringNormalizer:
    """! @~russian StringNormalizer (Нормализатор строк):
    @details 
    - Задача: Преобразование строк в стандартный формат или нормализация.
    - Действия: Удаление лишних пробелов, преобразование регистра, обработка специальных символов и прочее.
    - Пример использования: Приведение всех букв к нижнему регистру или удаление лишних пробелов в начале и конце строки.
    """


    # #####################################################################################
    # #
    # #                               Декораторы
    # #
    # def list_to_str_decorator(func):
    #     """! @~russian Декоратор приводящий `input_str` к строке, если на входе был список """
    #     def wrapper(input_str: Union[str, List]) -> Union[str, List[str]]:
    #         if isinstance(input_str, list):
    #             input_str = ' '.join(map(str, input_str))
    #         return func(input_str)

    #     return wrapper
    
    # def list_to_str_decorator_static(method):
    #     """! @~russian Декоратор для статических методов, приводящий `input_str` к строке, если на входе был список """
    #     def wrapper(cls, input_str: Union[str, List]) -> Union[str, List[str]]:
    #         if isinstance(input_str, list):
    #             input_str = ' '.join(map(str, input_str))
    #         return method(cls, input_str)

    #     return wrapper

    # #
    # #
    # ############################################################################################


    @staticmethod
    def normalize_price(rawprice: Union[str,int,float] ) -> Union [ float, False ]:
        """! Нормализация цены
        @param rawprice `stfloat`
        """
        if len(rawprice) <1: return False 
        try:
            price = rawprice[0] if isinstance(rawprice, list) else rawprice
            price = Ptrn.clear_price.sub ('', price) .replace(',', '')
            return float (price)
        except Exception as ex:
            logger.error('Ошибка нормализации `price`',ex)
            return False


    @staticmethod
    def normalize_weight(weight: str) -> float:
        """
        Нормализация веса
        """
        if not weight:
            return None
        weight = pattern.clear_number.sub('', weight)
        weight = weight.replace(',', '.')
        try:
            weight = float(weight)
        except:
            weight = None
        return weight


    @staticmethod
    #@logs_and_errors_decorator(default_return=False)
    def get_numbers_only(input_str:str) -> Union[str,False]:
        """! @~russian Очищает строку и отдает только цифры. 
        Функция пробегает по строке и выдергивает только цифры, 
        присоединяя их одну к другой
        """
        try:
            return ''.join ( [ c for c in input_str if c.isdigit() ] )
        except Exception as ex:
            logger.error(f'Что-то не так с очисткой строки ', ех)
            return False
            
    @staticmethod
    def normalize_sku(sku: str) -> str:
        """
        Нормализация артикула ?????
        """
        sku = SF.remove_non_latin_characters(sku)
        sku = SF.remove_special_characters(sku)
        sku = SF.remove_line_breaks(sku)
        sku = sku.strip()
        return sku
    
    @staticmethod
    def normalize_product_name (input_str: Union [str,list]) -> str:
        """! @~russian поле `name` в `Prestashop` не должно содержать спецсимволов 
        Если пришел список  - декоратор конвертирует его в строку
        """
        return SF.remove_special_characters (SF.remove_line_breaks (input_str) ) 
    
    def normalize_link_rewrite(input_str: Union [str,list]) -> str:
        return str( SF.remove_special_characters (SF.remove_line_breaks (input_str) ) ).replace(" ", "_")
        
    
    @staticmethod
    def normalize_url (url: Union [str,list]) -> str:
        """! @~russian Функция старается привeсти входную строку в легитимный URL """
        return url        
        """!@todo не проверен    """

        if not url:
            return None

        url = url.strip()

        if not url.startswith('http'):
            url = 'https://' + url

        parsed_url = urlparse(url)

        if parsed_url.query:
            parsed_url = parsed_url._replace(query=parse_qs(
                parsed_url.query, keep_blank_values=True))

        return parsed_url.geturl()

        ###################################################
        #
        # Другой вариант
        #
        # protocol_pattern = re.compile(r'^https?://', re.IGNORECASE)

        # if protocol_pattern.match(url):
        #     # Если строка уже содержит протокол, считаем ее валидной
        #     return url
        # else:
        #     # Добавляем протокол, если его нет
        #     return 'http://' + url if not protocol_pattern.match('http://' + url) else 'https://' + url


        # # Пример использования
        # input_url = input("Введите URL: ")
        # result = validate_and_fix_url(input_url)

        # if result:
        #     print("Релевантный URL:", result)
        # else:
        #     print("Невалидный URL.")



    def normalize_string (input_str: Union [str,list]) -> Union [str, list[str] ]:
        if isinstance(input_str, list):
            out_str = ' '.join(input_str)
        
            
        out_str = SF.remove_line_breaks(out_str)

        # Удаление лишних пробелов
        words = out_str.split()  # Разделение строки на список слов
        clean_string = ' '.join(words)  # Соединение слов с использованием пробела в качестве разделителя


        return clean_string
    

