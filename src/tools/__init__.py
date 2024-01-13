"""! @en_brief   A set of tools used in the code, such as string validators, randomizers, regular expression patterns
@ru_brief Внутренние утилиты
@ru_details Вспомогательные утилиты включают в себя:
- Обработчики строк: 
- - `StringValidator` Класс валидации строк `src.tools.string_validator.StringValidator`
- - `StringFormatter` Класс форматирования строк `src.tools.string_formatter.StringFormatter`
- - `StringNormalizer` Класс нормализации строк `src.tools.string_normalizer.StringNormalizer`
- Паттерны регулярных выражений `Ptrn` : `src.tools.re_patterns.RePtrn`
- Словарь ASCII символов для HTML : `src.tools.symbols2HTML_dict`


 
 @section libs imports:
  - .string_validator 
  - .string_formatter 
  - .string_normalizer 
  - .re_patterns 
  - .openai_translator 
  - .randomizer 
 @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .string_validator import StringValidator
from .string_formatter import StringFormatter
from .string_normalizer import StringNormalizer
from .re_patterns import Ptrn
from .randomizer import get_random_string
