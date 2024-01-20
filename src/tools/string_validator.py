"""! @~russian 
@brief Модуль валидации строк
@details Модуль может предоставлять функции для проверки строк на соответствие определенным критериям или форматам.
Валидация может включать в себя проверку наличия определенных символов, длины строки, формата электронной почты, URL и т. д.
 
 @section libs imports:
  - re 
  - .re_patterns 
  - urllib.parse 
  - attr 
  - .string_formatter 
  - helpers 
  - gs 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import re
from .re_patterns import *
from urllib.parse import urlparse, parse_qs
from attr import attr, attrs
from .string_formatter import StringFormatter as SF
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads, j_dumps


class StringValidator:
    """!
    @~russian StringValidator (Валидатор строк):
    @details 
    - Задача: Проверка строки на соответствие определенным критериям или шаблонам.
    - Действия: Проверка наличия определенных символов, длины строки, соответствие регулярным выражениям и другие проверки.
    - Пример использования: Проверка корректности электронной почты, пароля или номера кредитной карты.
    """

    @staticmethod
    def validate_price(price: str) -> bool:
        """!
        @brief [Function's description]

        Parameters : 
            @param price : str  :  [description]
        Returns : 
            @return bool  :  [description]

        """
        """
        Валидация цены
        """
        if not price:
            return False
        price = pattern.clear_price.sub('', price)
        price = price.replace(',', '.')
        try:
            float(price)
        except:
            return False
        return True


    @staticmethod
    def validate_weight(weight: str) -> bool:
        """!
        @brief [Function's description]

        Parameters : 
            @param weight : str  :  [description]
        Returns : 
            @return bool  :  [description]

        """
        """
        Валидация веса
        """
        if not weight:
            return False
        weight = pattern.clear_number.sub('', weight)
        weight = weight.replace(',', '.')
        try:
            float(weight)
        except:
            return False
        return True


    @staticmethod
    def validate_sku(sku: str) -> bool:
        """!
        @brief [Function's description]

        Parameters : 
            @param sku : str  :  [description]
        Returns : 
            @return bool  :  [description]

        """
        """
        Валидация артикула
        """
        if not sku:
            return False
        sku = StringFormatter.remove_special_characters(sku)
        sku = StringFormatter.remove_line_breaks(sku)
        sku = sku.strip()
        if len(sku) < 3:
            return False
        return True


    @staticmethod
    def validate_url(url: str) -> bool:
        """!
        @brief [Function's description]

        Parameters : 
            @param url : str  :  [description]
        Returns : 
            @return bool  :  [description]

        """
        """
        Валидация URL
        """
        if not url:
            return False

        url = url.strip()

        if not url.startswith('http'):
            url = 'http://' + url

        parsed_url = urlparse(url)

        if not parsed_url.netloc or not parsed_url.scheme:
            return False

        return True

    @staticmethod
    def isint(s: str) -> bool:
        """!
        @brief [Function's description]

        Parameters : 
            @param s : str  :  [description]
        Returns : 
            @return bool  :  [description]

        """
        try:
            s = int(s)
            return True
        except Exception as ex:
            return False


