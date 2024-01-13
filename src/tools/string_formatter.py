"""! @~russian
@brief Модуль форматирования строки
@details Модуль предоставляet функции для форматирования строк в определенном стиле или с использованием определенного шаблона.
это могут бы быть инструменты для вставки переменных в строку, изменения регистра символов, удаления или замены подстрок и т. д.


 @section libs imports:
  - re 
  - typing 
  - urllib.parse 
  - attr 
  - src.gs 
  - src.gs 
  - .re_patterns 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from typing import Union
from urllib.parse import urlparse, parse_qs
from attr import attr, attrs
import re
import html
# --------------------------------
from src.helpers import logger,  logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads
from .re_patterns import Ptrn

# --------------------------------- 



class StringFormatter:
    """! @ru_brief StringFormatter (Форматирование строк):
    @ru_details 
    - Задача: Отформатировать строки в соответствии с определенными правилами.
    - Действия: Вставка разделителей, выравнивание, добавление форматирования даты и времени и другие манипуляции с текстом.
    - Пример использования: Форматирование номера телефона, выравнивание текста в таблице.
    """

    @staticmethod
    def remove_line_breaks(input_str: str) -> str:
        """
         Removes line breaks from the input string.

        Parameters : 
             input_str : str : input string
        Returns : 
             str : A string with line breaks removed.

        """

        s = input_str
        def _(s):
            return Ptrn.remove_line_breaks.sub(r' ', s).strip()

        if isinstance(s, list):
            for sub_s in s:
                sub_s = _(sub_s)
        else:
            s = _(s)
        return s

    @staticmethod
    def remove_htmls(input_str: str) -> str:
        """
         Removes HTML tags from the input string.

        Parameters : 
             input_str : str : input string
        Returns : 
             str : A string with HTML tags removed.

        """

        s = input_str
        def _(s):
            return Ptrn.remove_HTML.sub(r' ', str(s)).strip()

        if isinstance(s, list):
            for sub_s in s:
                sub_s = _(sub_s)
        else:
            s = _(s)
        return s

    @staticmethod
    def replace_htmls_with_escape_symbols(HTML: str) -> str:
        """
         Replaces `<` and `>` with `&lt;` and `&gt;` in the input HTML string.
        Parameters : 
             HTML : str : HTML: An input string that contains HTML tags.
        Returns : 
             str : An escaped string.

        """

        HTML = re.sub(r"<", "&lt;", HTML)
        HTML = re.sub(r">", "&gt;", HTML)
        return HTML
    
    @staticmethod
    def convert_to_html_entities(input_str):
         #return html.escape(input_str)
        return StringFormatter.escape_html_tags(input_str)
    
    @staticmethod
    def escape_html_tags(html: str) -> str:
        """@deprecated. use 
         Escapes `<...>` in the input HTML string.

        Parameters : 
             html : str : [description]

        Returns : 
             str : An escaped string.
        """

        return re.sub(r'<|>', lambda x: '\\' + x.group(), html)

    @staticmethod
    def remove_non_latin_characters(input_str: str) -> str:
        """
          Removes non-latin characters from the input string.

        Parameters : 
             input_str : str :  input string.
        Returns : 
             str : A string with non-latin characters removed.

        """

        s = input_str
        s = StringFormatter.remove_special_characters(s)

        def _(s):
            return Ptrn.remove_non_latin_characters.sub(r' ', s).strip()

        if isinstance(s, list):
            for sub_s in s:
                sub_s = _(sub_s)
        else:
            s = _(s)
        return s

    @staticmethod
    def remove_special_characters (input_str: Union [str,list]) -> str:
        """! @~russian
        @brief Удаляю символы, которые не проходят валидацию в поле `name`  `Prestashop`
        @param input_str `str` входящая строка
        @returns output_str `str` Обработанная строка
        ### Пример
        @code
        @~python
        >>> input_str = 'abc#def'
        >>> output_str = remove_special_characters(input_str)
        >>> print(output_str)
        >>> 'abc def'
        >>>
        >>> input_str = '<div>Text</div>'
        >>> output_str = remove_special_characters(input_str)
        >>> print(output_str)
        >>> 'Text'
        >>> input_str = ['a','text',45]
        >>> output_str = remove_special_characters(input_str)
        >>> print(output_str)
        >>> 'a text 45'        
        @endcode
        """
        s =  StringFormatter.convert_to_html_entities (input_str)

        if isinstance(s, list):
            out_str: str = ''
            for sub_s in s:
                sub_s = Ptrn.remove_special_characters.sub(r' ', string=s).strip
                out_str += (sub_s)
        else:
            out_str = Ptrn.remove_special_characters.sub(r' ', s).strip
        return out_str

    @staticmethod
    def convert_to_list(input: Union[list[str],list[dir],dir,str],delimiter: str = ',') -> Union[list,bool]:
        """
         [Function's description]

        Parameters : 
             input : Union[list[str],list[dir],dir,str] : [description]
             delimiter : str : [description]

        Returns : 
             Union[list,bool] : [description]
            
        TODO посмотреть результат работы этой функции
        """

        if isinstance(input, str):
            # """
            # If the argument is a string, search for supplier prefixes within the string.
            # """
            if str(input).find(delimiter) > -1:
                # """
                # If the string contains commas, it is of the form `supplier_prefix_1,supplier_prefix_2,...,supplierN`.
                # Split the string into a list using commas as separators.
                # """
                return input.split(delimiter)
            else:
                # """
                # If the string does not contain commas, it is of the form `supplier_prefix`.
                # Convert the string into a single-item list.
                # """
                return [input]
        elif isinstance(input, dict):
            # """
            # If the argument is a dictionary of the form:
            # {
            #     "2680": "aliexpress",
            #     "111": "amazon",
            # }
            # """
            return [input[k] for k in input.keys()]
            # """
            # Convert the dictionary values into a list of values.
            # """
        elif isinstance(input, list):
            return input
            # """
            # If the argument is already a list, do nothing.
            # """
        else:
            logger.error(f"Suppliers format error: {type(input)}")
            # """
            # If the argument has an unrecognized format, log an error message.
            # """


    @staticmethod
    def extract_value_from_parentheses_with_lead_dollar(input_str: str) -> str:
        """
          I use it to extract parameters within a function if it's inside a locator.
        (...)
         ^^^


        @param
            locator['attribute'] (Union[str,list]): - const f.e. 1 or 'string' or null etc
                                                    - list(const) f.e. "[1,'string,False]"
                                                    - variable: start from `_$` f.e. _$var1
                                                    - I can alternate variables and constants in any sequence: "1,_$var2,Flase ..." or "[1,_$var2,Flase]"
                                                    - hypotez objects: $d, $s, $c, $p each one mean: Driver, Supplier, Category, Product
                                                    (I can easily assign properties to object attributes if allowed.
                                                    f.e. $d.get_url )

            To avoid creating additional entities in the locator dictionary, I can transfer the values from attributes through selector.



            Here is an example of how such a locator looks like:
            -   $(scroll(5,forward',0))
            -   $(d.current_url.split(f'''/''')[-2])
            -   $(p.fields['ASIN'])


        Parameters : 
             input_str : str : [description]
        Returns : 
             Union[str,list,bool] : [description]

        """

        s = input_str
     
        match = re.search(Ptrn.extract_value_from_parentheses_with_lead_dollar, s)
        if match:
            attributes = match.group(1)
            #attributes = [attr.strip() for attr in attributes.split(',') if attr.strip()]  # Разделение атрибутов по запятым и удаление лишних пробелов
            return attributes
        else:
            return False

    @staticmethod
    def clean_url_from_protocols(url: str) -> str:
        """! 
        @brief Функция очищает `URL` от протокола `HTTP` и префикса `www`
        @details очищаю через паттерн `clean_url_from_protocols` \n
       (src.tools.re_patterns.RePtrn.clean_url_from_protocols)
        @param url `str` - raw url
        @returns url `str` - url cleaned from protocol
    
        ### Пример использования:
        @code         
        >>> url = 'https://www.example.com'
        >>> cleaned_url = clean_url_from_protocols(url)
        >>> print(cleaned_url)
        >>> 'example.com'
        @endcode
        """
       
        return Ptrn.clean_url_from_protocols.sub('', url)
    
    @staticmethod
    def clear_numbers(input_str) -> str:
        """
         Clear string from not decimal numbers or points

        Parameters : 
             input_str : input string
        Returns : 
             str : clear string
            
            @example
            > input_str = 'aaa123.456 cde'
            > output_str = clear_numbers(input_str)
            > print(output_str)
            > 123.456

        """
        return Ptrn.clear_number.sub(r' ', input_str).strip()


    
    @staticmethod
    def symbols2HTML(text: str) -> str:
        """
         заменяю все не латинкие символы и не цифры HTML-последовательностями
        словарь ASCII находится в модуле symbols2HTML_dict

        Parameters : 
             text : str : input text
        Returns : 
             str : output text
            
            @example 
            `#АБВ` : `&#35;&#1040;&#1041;&#1042;`
            Здесь `#` заменен на `&#35;`, а кириллические буквы "А", "Б" и "В" \n
            на соответствующие HTML-последовательности` &#1040;`, `&#1041;` и `&#1042;`.

        """

        text = ''.join(text) if isinstance(text,list) else text
        "list->str"
      
        html_entities = symbols2HTML_dict.html_entities
        result = ''
        for char in text:
            if char in html_entities:
                result += html_entities[char]
            else:
                result += char

        return ''.join(result)



    @staticmethod
    def symbols2UTF(text: str) -> str:
        """
         Convert to UTF

        Parameters : 
             text : str : input text
        Returns : 
             str : UTF-8 encoded text

        """
        return text.encode("utf-8")