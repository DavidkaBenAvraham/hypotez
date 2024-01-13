"""! @~russian
@brief Модуль вебдрайвера
@details Я объединил в класс `Driver` все, что взаимодействует по протоколу `HTTP`:
- `selenium`
- `Mozilla/Chrome/Edge..` вебдрайвер 
- моя реализация работы с локаторами `execute_locator.py`


-------


@image html webdriver.png

-------


 @section libs imports:
  - .Driver 
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .Driver import Driver