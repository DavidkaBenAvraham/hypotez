# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! @ru_brief **Это корневая директория проекта** 
@ru_details 

---------------------------------------

- Запуск скрипта начинается в `main.py`

## Опции запуска программы

Запуск из командной строки
@code
> python main.py
@endcode 

или

@code
~powershell
> ./run
@endcode

- При запуске из командной строки все настройки будут читаться из файла `global_settings.json`


Запуск из интерпретаторa python

@code
>python
>>> import main
>>> launcher()
@endcode

---------


Для тонкой настройки запуска см комментарии к функции `main.launcher()` (`src.main.launcher()`)

--------------


## Блоксхема
- `Scenario` - JSON файл, содержащий последовательность действий для получения конечных данных
- `Supplier` - Класс поставщика. При инициализации получает список сценариев, после запуска отправляет их в исполнитель
- `Executor` - Исполнитель сценариев.
- `Connections Layer` - Подключение к источнику информации. Настраивается в классе поставщика.
- `Supplier's Data` - Информация и товаре. То, ради чего все сделано.
- `Parser` - Разбор полученных данных.
- `Product` - Сущность `товар` для экспорта.
- `Export Layer` - конечый получатель данных. У меня это фрймворк `Prestashop`.
            
@image html hypotez_flowchart.png



---------

@details Парсер всего, что парсится 
@file
"""


# Imports
import os
import sys
import datetime
from pathlib import Path


dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 
#import main





