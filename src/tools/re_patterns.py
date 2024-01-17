"""! @brief   regex patterns

@namespace src: src
 \package src.tools
\file re_patterns.py
 
 @section libs imports:
  - re 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""


# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import re

class RePtrn:
    """! @ru_brief Реалиация паттернов регулярных выражений """

    _instance = None

    def __new__ (cls, *args, **kwargs):
        """! @ru_brief Создаю инстанс  """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance (cls) -> _instance:
        """! @ru_brief Проверяю, а есть ли инстанс?
       @ru_details Если инстанса класса еще нет - создаю, иначе возвращаю сам инстанс"""
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    remove_HTML: re = None
    remove_non_latin_characters: re = None
    remove_line_breaks: re = None
    clear_price: re = None
    remove_special_characters: re = None
    remove_supplier_name: re = None
    replace_doubles: re = None
    clean_url_from_protocols: re = None

    def __init__(self, *attrs, **kwards):
        self.remove_HTML: re = re.compile('<[^<]+?>')
        self.remove_non_latin_characters: re = re.compile('[^A-Za-z0-9-]')
        self.remove_line_breaks: re = re.compile('^\s+|\n|\r|\s+$')
        self.clear_price: re = re.compile('[^0-9.,]')
        self.clear_number: re = re.compile('[^0-9.]')
        self.remove_special_characters: re = re.compile('[<>;=#{}]')
        self.remove_supplier_name: re = re.compile('[KSP,ksp]')
        self.replace_doubles: re = re.compile(r'(\w+)(\s+\1)+')
        #self.extract_value_from_parentheses_with_lead_dollar: re = re.compile('\$_\((.*?)\)_')
        self.clean_url_from_protocols: re = re.compile(r'^(https?://|www\.)')

Ptrn: RePtrn = RePtrn().get_instance()
    #@property
    #def remove_line_breaks(self):
    #    """ Регулярное выражение re.compile('^\s+|\n|\r|\s+$') используется для поиска и удаления начальных и конечных пробелов, 
    #    а также символов новой строки (\n) и возврата каретки (\r) в строке.

    #    Вот объяснение того, что делает каждая часть выражения:

    #    ^\s+ - соответствует одному или более пробельным символам в начале строки (^). 
    #    Пробельный символ может быть пробелом, 
    #    табуляцией или другим символом пробела.
    #    | - используется как оператор "или", разделяющий два варианта выражения.
    #    \n - соответствует символу новой строки.
    #    \r - соответствует символу возврата каретки.
    #    \s+ - соответствует одному или более пробельным символам в конце строки ($).
    #    Таким образом, это регулярное выражение позволяет найти и удалить начальные и конечные пробелы, 
    #    а также символы новой строки и возврата каретки в строке. """
    #    return self.remove_line_breaks
    #@remove_line_breaks.setter
    #def remove_line_breaks(self, re_pattern: str) -> bool:
    #    self.remove_line_breaks = re.compile(re_pattern)


    #@property
    #def clear_price(self):
    #    """ [^0-9.,] - набор символов, 
    #    указанных внутри квадратных скобок [], 
    #    с префиксом ^, который означает отрицание. 
    #    Таким образом, выражение соответствует любому символу, 
    #    который не является цифрой (0-9), точкой (.) или запятой (,). """
    #    return self.clear_price
    #@clear_price.setter
    #def clear_price(self, re_pattern: str) -> bool:
    #    self.clear_price = re.compile(re_pattern)

    #@property
    #def clear_number(self):
    #    """ [^0-9.] - набор символов, 
    #    указанных внутри квадратных скобок [], 
    #    с префиксом ^, который означает отрицание. 
    #    Таким образом, выражение соответствует любому символу, 
    #    который не является цифрой (0-9) или точкой (.). """
    #    return self.clear_number
    #@clear_number.setter
    #def clear_number(self, re_pattern: str) -> bool:
    #    self.clear_number = re.compile(re_pattern)

    #@property
    #def remove_special_characters(self):
    #    """ Регулярное выражение re.compile('[#|]') используется для поиска символов # или | в строке.

    #    Вот объяснение того, что делает каждая часть выражения:

    #    [#|] - набор символов, указанных внутри квадратных скобок [], без префикса ^. 
    #    Такое выражение соответствует любому символу, который является либо символом #, либо символом |. """
    #    return self.remove_special_characters

    #@remove_special_characters.setter
    #def remove_special_characters(self, re_pattern: str) -> bool:
    #    self.remove_special_characters = re.compile(re_pattern)

    #@property
    #def replace_doubles(self):
    #    """ Регулярное выражение re.compile(r'(\w+)(\s+\1)+') используется для поиска повторяющихся слов в строке, 
    #    разделенных одним или несколькими пробельными символами.

    #    Вот объяснение того, что делает каждая часть выражения:

    #    (\w+) - это группа захвата, которая соответствует одному или более словам. 
    #    Символ \w соответствует любому буквенно-цифровому символу или символу подчеркивания.
    #    (\s+\1)+ - это группа захвата, которая соответствует одному или нескольким повторяющимся последовательностям 
    #    пробельных символов и слов из первой группы захвата. 
    #    Символ \s соответствует любому пробельному символу (пробел, табуляция и т.д.). 
    #    Символ \1 обозначает обратную ссылку на первую группу захвата. """
    #    return self.replace_doubles

    #@replace_doubles.setter
    #def replace_doubles(self, re_pattern: str) -> bool:
    #    self.replace_doubles = re.compile(re_pattern)


    #@property
    #def extract_value_from_parentheses_with_lead_dollar(self):
    #    """ Регулярное выражение re.compile('\$\((.*?)\)') используется для поиска паттерна $(...) 
    #    в строке и захвата значения, находящегося между скобками.

    #    Вот объяснение того, что делает каждая часть выражения:

    #    \$\( - символ $ и открывающая скобка \(. 
    #    Символ $ в регулярном выражении должен быть экранирован с помощью \, чтобы представлять сам символ $, а не его специальное значение.
    #    (.*?) - это некоторое выражение, которое соответствует нулю или более символов, используя ленивый квантификатор *?. 
    #    Ленивый квантификатор говорит регулярному выражению быть настолько ленивым, насколько возможно, 
    #    чтобы соответствовать минимальному количеству символов.
    #    \) - закрывающая скобка \). """
    #    return self.extract_value_from_parentheses_with_lead_dollar

    #@extract_value_from_parentheses_with_lead_dollar.setter
    #def extract_value_from_parentheses_with_lead_dollar(self, re_pattern: str) -> bool:
    #    self.extract_value_from_parentheses_with_lead_dollar = re.compile(re_pattern)


    #@property
    #def clean_url_from_protocols(self):
    #    """  """
    #    return self.clean_url_from_protocols

    #@clean_url_from_protocols.setter
    #def clean_url_from_protocols(self, re_pattern: str) -> bool:
    #    self.clean_url_from_protocols = re.compile(re_pattern)

