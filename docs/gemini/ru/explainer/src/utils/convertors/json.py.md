### **Системные инструкции для обработки кода проекта `hypotez`**

=========================================================================================

Описание функциональности и правил для генерации, анализа и улучшения кода. Направлено на обеспечение последовательного и читаемого стиля кодирования, соответствующего требованиям.

---

### **Основные принципы**

#### **1. Общие указания**:
- Соблюдай четкий и понятный стиль кодирования.
- Все изменения должны быть обоснованы и соответствовать установленным требованиям.

#### **2. Комментарии**:
- Используй `#` для внутренних комментариев.
- В комментариях избегай использования местоимений, таких как *«делаем»*, *«переходим»*, *«возващам»*, *«возващам»*, *«отправяем»* и т. д.. Вмсто этого используй точные термины, такие как *«извлеизвлечение»*, *«проверка»*, *«выполннение»*, *«замена»*, *«вызов»*, *«Функця выпоняет»*,*«Функця изменяет значение»*, *«Функця вызывает»*,*«отправка»*
Пример:
```python
# Неправильно:
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    # Получаем значение параметра
    ...
# Правильно:

def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    # Функция извлекает значение параметра
    ...
# Неправильно:
if not process_directory.exists():
    logger.error(f"Директория не существует: {process_directory}")
    continue  # Переходим к следующей директории, если текущая не существует

if not process_directory.is_dir():
    logger.error(f"Это не директория: {process_directory}", None, False)
    continue  # Переходим к следующей директории, если текущая не является директорией
# Правильно:

if not process_directory.exists():
    logger.error(f"Директория не существует: {process_directory}")
    continue  # Переход к следующей директории, если текущая не существует
if not process_directory.is_dir():
    logger.error(f"Это не директория: {process_directory}", None, False)
    continue  # Переходим к следующей директории, если текущая не является директорией

```
- Документация всех функций, методов и классов должна следовать такому формату: 
    ```python
        def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
            """ 
            Args:
                param (str): Описание параметра `param`.
                param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.
    
            Returns:
                dict | None: Описание возващаемого значения. Возвращает словарь или `None`.
    
            Raises:
                SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

            Ехаmple:
                >>> function('param', 'param1')
                {'param': 'param1'}
            """
    ```
- Комментарии и документация должны быть четкими, лаконичными и точными.


### **3. Заголовок файла**:
Обязательно оставляй строки 
```python
## \file path/to/file
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
```
и
```
"""
...
```rst
 .. module:: src.utils.string.html_simplification
 ```
"""
```
если они есть. Если нет - добавляй.
Пример:
## \file /src/utils/string/html_simplification.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для очистки HTML-тегов из текста и упрощения HTML-кода.
===============================================================
Модуль минимизирует HTML-код, удаляет теги и атрибуты, а также обрабатывает
специальные случаи, такие как скрипты, стили и комментарии.
Использует BeautifulSoup для надежного парсинга HTML.

Зависимости:
    - beautifulsoup4 (pip install beautifulsoup4)
    - lxml (опционально, для более быстрого парсинга: pip install lxml)

 .. module:: src.utils.string.html_simplification
"""

#### **4. Форматирование кода**:
- Используй одинарные кавычки. `a:str = 'value'`, `print('Hello World!')`;
- Добавляй пробелы вокруг операторов. Например, `x = 5`;
- Все параметры должны быть аннотированы типами. `def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:`;
- Не используй `Union`. Вместо этого используй `|`.
- Не используй термин `Product`, только `товар`

#### **5. Логирование**:
- Для логгирования Всегда Используй модуль `logger` из `src.logger.logger`.
- Ошибки должны логироваться с использованием `logger.error`.
Пример:
    ```python
        try:
            ...
        except Exception as ex:
            logger.error('Error while processing data', ех, exc_info=True)
    ```
#### **6. Не используй `Union[]` в коде. Вместо него используй `|`
Например:
```python
x: str | int ...
```

#### **7. Не используй глобальные переменные. Если есть надобность - то поределяй их в классе `Config`.
Пример:

- Неправильно:
```python

state:int = 'global'

def func():
    print(state)

```
- Правильно:
```python

class Config:
    state:int = 'global'

def func():
    print(Config.state)

```

#### **8. Не используй `self` в методах класса. Вместо него используй `cls`.
#### **9. Всегда объявляй переменные вначале функции. Не объявляй их в середине функции.
Пример:
```python
def func():
    # Неправильно
    if condition:
        x = 5
        y = 10
    else:
        x = 20
        y = 30
    # Правильно
    x = None
    y = None
    if condition:
        x = 5
        y = 10
    else:
        x = 20
        y = 30
```
---

### **Основные требования**:

#### **1. Формат ответов в Markdown**:
- Все ответы должны быть выполнены в формате **Markdown**.

#### **2. Формат комментариев**:
- Используй указанный стиль для комментариев и документации в коде.
- Пример:

```python
from typing import Generator, Optional, List
from pathlib import Path


def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[List[str]] = None,
    chunk_size: int = 8192,
) -> Generator[str, None, None] | str | None:
    """
    Считывает содержимое файла (или файлов из каталога) с использованием генератора для экономии памяти.

    Args:
        file_path (str | Path): Путь к файлу или каталогу.
        as_list (bool): Если `True`, возвращает генератор строк.
        extensions (Optional[List[str]]): Список расширений файлов для чтения из каталога.
        chunk_size (int): Размер чанков для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или `None` в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при чтении файла.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
    ...
```
- Всегда делай подробные объяснения в комментариях. Избегай расплывчатых терминов, 
- таких как *«получить»* или *«делать»*
-  . Вместо этого используйте точные термины, такие как *«извлечь»*, *«проверить»*, *«выполнить»*.
- Вместо: *«получаем»*, *«возвращаем»*, *«преобразовываем»* используй имя объекта *«функция получае»*, *«переменная возвращает»*, *«код преобразовывает»* 
- Комментарии должны непосредственно предшествовать описываемому блоку кода и объяснять его назначение.

#### **3. Пробелы вокруг операторов присваивания**:
- Всегда добавляйте пробелы вокруг оператора `=`, чтобы повысить читаемость.
- Примеры:
  - **Неправильно**: `x=5`
  - **Правильно**: `x = 5`

#### **4. Использование `j_loads` или `j_loads_ns`**:
- Для чтения JSON или конфигурационных файлов замените стандартное использование `open` и `json.load` на `j_loads` или `j_loads_ns`.
- Пример:

```python
# Неправильно:
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Правильно:
data = j_loads('config.json')
```

#### **5. Сохранение комментариев**:
- Все существующие комментарии, начинающиеся с `#`, должны быть сохранены без изменений в разделе «Улучшенный код».
- Если комментарий кажется устаревшим или неясным, не изменяйте его. Вместо этого отметьте его в разделе «Изменения».

#### **6. Обработка `...` в коде**:
- Оставляйте `...` как указатели в коде без изменений.
- Не документируйте строки с `...`.
```

#### **7. Аннотации**
Для всех переменных должны быть определены аннотации типа. 
Для всех функций все входные и выходные параметры аннотириваны
Для все параметров должны быть аннотации типа.


### **8. webdriver**
В коде используется webdriver. Он импртируется из модуля `webdriver` проекта `hypotez`
```python
from src.webdirver import Driver, Chrome, Firefox, Playwright, ...
driver = Driver(Firefox)

Пoсле чего может использоваться как

close_banner = {
  "attribute": null,
  "by": "XPATH",
  "selector": "//button[@id = 'closeXButton']",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "click()",
  "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
}

result = driver.execute_locator(close_banner)

#### **9. Не используй `Union[]` в коде. Вместо него используй `|`
Например:
```python
x: str | int ...
```

#### **10. print - это моя встроенная функция.
from src.utils.printer import pprint as print


Вот она:

\file /src/utils/printer.py
-- coding: utf-8 --

#! .pyenv/bin/python3

"""
.. module::  src.utils
:platform: Windows, Unix
:synopsis: Utility functions for pretty printing and text styling.

This module provides functions to print data in a human-readable format with optional text styling, including color, background, and font styles.
"""

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print

ANSI escape codes

RESET = "\033[0m"

TEXT_COLORS = {
"red": "\033[31m",
"green": "\033[32m",
"blue": "\033[34m",
"yellow": "\033[33m",
"white": "\033[37m",
"cyan": "\033[36m",
"magenta": "\033[35m",
"light_gray": "\033[37m",
"dark_gray": "\033[90m",
"light_red": "\033[91m",
"light_green": "\033[92m",
"light_blue": "\033[94m",
"light_yellow": "\033[93m",
}

Background colors mapping

BG_COLORS = {
"bg_red": "\033[41m",
"bg_green": "\033[42m",
"bg_blue": "\033[44m",
"bg_yellow": "\033[43m",
"bg_white": "\033[47m",
"bg_cyan": "\033[46m",
"bg_magenta": "\033[45m",
"bg_light_gray": "\033[47m",
"bg_dark_gray": "\033[100m",
"bg_light_red": "\033[101m",
"bg_light_green": "\033[102m",
"bg_light_blue": "\033[104m",
"bg_light_yellow": "\033[103m",
}

FONT_STYLES = {
"bold": "\033[1m",
"underline": "\033[4m",
}

def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
"""Apply color, background, and font styling to the text.

This helper function applies the provided color and font styles to the given text using ANSI escape codes.

:param text: The text to be styled.
:param text_color: The color to apply to the text. Default is an empty string, meaning no color.
:param bg_color: The background color to apply. Default is an empty string, meaning no background color.
:param font_style: The font style to apply to the text. Default is an empty string, meaning no font style.
:return: The styled text as a string.

:example:
    >>> _color_text("Hello, World!", text_color="green", font_style="bold")
    '\033[1m\033[32mHello, World!\033[0m'
"""
return f"{font_style}{text_color}{bg_color}{text}{RESET}"


def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
"""Pretty prints the given data with optional color, background, and font style.

This function formats the input data based on its type and prints it to the console. The data is printed with optional 
text color, background color, and font style based on the specified parameters. The function can handle dictionaries, 
lists, strings, and file paths.

:param print_data: The data to be printed. Can be of type ``None``, ``dict``, ``list``, ``str``, or ``Path``.
:param text_color: The color to apply to the text. Default is 'white'. See :ref:`TEXT_COLORS`.
:param bg_color: The background color to apply to the text. Default is '' (no background color). See :ref:`BG_COLORS`.
:param font_style: The font style to apply to the text. Default is '' (no font style). See :ref:`FONT_STYLES`.
:return: None

:raises: Exception if the data type is unsupported or an error occurs during printing.

:example:
    >>> pprint({"name": "Alice", "age": 30}, text_color="green")
    \033[32m{
        "name": "Alice",
        "age": 30
    }\033[0m

    >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
    \033[34m\033[1mapple\033[0m
    \033[34m\033[1mbanana\033[0m
    \033[34m\033[1mcherry\033[0m

    >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
    \033[4m\033[33m\033[41mtext example\033[0m
"""
if not print_data:
    return
if isinstance(text_color, str):
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
if isinstance(bg_color, str):
    bg_color = BG_COLORS.get(bg_color.lower(), "")
if isinstance(font_style, str):
    font_style = FONT_STYLES.get(font_style.lower(), "")


try:
    if isinstance(print_data, dict):
        print(_color_text(json.dumps(print_data, indent=4), text_color))
    elif isinstance(print_data, list):
        for item in print_data:
            print(_color_text(str(item), text_color))
    elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
        ext = Path(print_data).suffix.lower()
        if ext in ['.csv', '.xls']:
            print(_color_text("File reading supported for .csv, .xls only.", text_color))
        else:
            print(_color_text("Unsupported file type.", text_color))
    else:
        print(_color_text(str(print_data), text_color))
except Exception as ex:
    print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"]))
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

if name == 'main':
pprint({"name": "Alice", "age": 30}, text_color="green")
```

### **Анализ кода `src/utils/convertors/json.py`**

#### **1. Блок-схема**

```mermaid
graph TD
    A[Начало] --> B{Тип входных данных json_data?};
    B -- dict --> C[Преобразование в list: data = [json_data]];
    B -- str --> D[Десериализация JSON: data = json.loads(json_data)];
    B -- list --> E[data = json_data];
    B -- Path --> F[Чтение JSON из файла];
    F --> G[Десериализация JSON из файла: data = json.load(json_file)];
    B -- Другой тип --> H[Вывод ошибки ValueError];
    D --> I{save_csv_file(data, csv_file_path)};
    E --> I
    G --> I
    I --> J{Успешно?};
    J -- Да --> K[return True];
    J -- Нет --> L[Логирование ошибки];
    L --> M[return False];
    H --> M
    K --> N[Конец];
    M --> N

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style N fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ccf,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style J fill:#ccf,stroke:#333,stroke-width:2px
    style K fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#ccf,stroke:#333,stroke-width:2px
    style M fill:#ccf,stroke:#333,stroke-width:2px
```

**Примеры для каждого логического блока:**

- **Входные данные (json_data)**:
  - `dict`: `{"ключ": "значение"}`
  - `str`: `'{"ключ": "значение"}'`
  - `list`: `[{"ключ": "значение"}]`
  - `Path`: `Path("путь/к/файлу.json")`

- **Чтение JSON из файла**:
  - Открывается файл по указанному пути, данные десериализуются с использованием `json.load()`.

- **Десериализация JSON**:
  - Преобразование строки JSON в структуру данных Python (словарь или список).

- **Сохранение в CSV**:
  - Использование функции `save_csv_file()` для сохранения данных в формате CSV.

#### **2. Диаграмма**

```mermaid
graph TD
    Start[Начало] --> InputTypeCheck{Определение типа входных данных};
    InputTypeCheck -- Словарь --> ConvertToList[Преобразование в список];
    InputTypeCheck -- Строка --> DeserializeJSON[Десериализация JSON];
    InputTypeCheck -- Список --> PassToList[Передача списка];
    InputTypeCheck -- Path --> ReadJSONFile[Чтение JSON из файла];
    InputTypeCheck -- Неподдерживаемый тип --> ValueErrorHandler[Обработка ошибки ValueError];

    ConvertToList --> SaveCSVFile[Сохранение в CSV файл];
    DeserializeJSON --> SaveCSVFile;
    PassToList --> SaveCSVFile;
    ReadJSONFile --> DeserializeJSONFromFile[Десериализация JSON из файла];
    DeserializeJSONFromFile --> SaveCSVFile;
    ValueErrorHandler --> ErrorLog[Логирование ошибки];

    SaveCSVFile --> SuccessCheck{Проверка успешности сохранения};
    SuccessCheck -- Успешно --> EndSuccess[Конец: Успех];
    SuccessCheck -- Ошибка --> ErrorLog;
    ErrorLog --> EndFail[Конец: Ошибка];

    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style EndSuccess fill:#f9f,stroke:#333,stroke-width:2px
    style EndFail fill:#f9f,stroke:#333,stroke-width:2px
    style InputTypeCheck fill:#ccf,stroke:#333,stroke-width:2px
    style ConvertToList fill:#ccf,stroke:#333,stroke-width:2px
    style DeserializeJSON fill:#ccf,stroke:#333,stroke-width:2px
    style PassToList fill:#ccf,stroke:#333,stroke-width:2px
    style ReadJSONFile fill:#ccf,stroke:#333,stroke-width:2px
    style DeserializeJSONFromFile fill:#ccf,stroke:#333,stroke-width:2px
    style ValueErrorHandler fill:#ccf,stroke:#333,stroke-width:2px
    style SaveCSVFile fill:#ccf,stroke:#333,stroke-width:2px
    style SuccessCheck fill:#ccf,stroke:#333,stroke-width:2px
    style ErrorLog fill:#ccf,stroke:#333,stroke-width:2px
```

```mermaid
flowchart TD
    Start --> Header[<code>header.py</code><br> Determine Project Root]

    Header --> import[Import Global Settings: <br><code>from src import gs</code>]
```

#### **3. Объяснение**

- **Импорты**:
  - `json`: Используется для десериализации JSON-строк в объекты Python и наоборот.
  - `csv`: Используется для работы с CSV-файлами (чтение и запись).
  - `types.SimpleNamespace`: Класс, который используется для создания объектов, атрибутам которых можно присваивать значения.
  - `pathlib.Path`: Класс для представления путей к файлам и каталогам.
  - `typing.List`, `typing.Dict`: Используются для аннотации типов.
  - `src.utils.csv.save_csv_file`: Функция для сохранения данных в CSV-файл.
  - `src.utils.jjson.j_dumps`: Функция для сериализации данных в JSON-строку.
  - `src.utils.xls.save_xls_file`: Функция для сохранения данных в XLS-файл.
  - `src.utils.convertors.dict.dict2xml`: Функция для преобразования словаря в XML-строку.
  - `src.logger.logger.logger`: Объект логгера для записи информации о работе модуля и возникающих ошибках.

- **Функции**:
  - `json2csv(json_data, csv_file_path)`:
    - **Аргументы**:
      - `json_data` (`str | list | dict | Path`): JSON данные в виде строки, списка словарей, словаря или пути к файлу JSON.
      - `csv_file_path` (`str | Path`): Путь к CSV файлу для записи.
    - **Возвращает**:
      - `bool`: `True` в случае успеха, `False` в случае ошибки.
    - **Назначение**:
      - Преобразует JSON данные в CSV формат и сохраняет в файл.
    - **Пример**:
      ```python
      json_data = '[{"ключ1": "значение1", "ключ2": "значение2"}]'
      csv_file_path = 'output.csv'
      result = json2csv(json_data, csv_file_path)
      print(result)  # Вывод: True или False в зависимости от успеха
      ```
  - `json2ns(json_data)`:
    - **Аргументы**:
      - `json_data` (`str | dict | Path`): JSON данные в виде строки, словаря или пути к файлу JSON.
    - **Возвращает**:
      - `SimpleNamespace`: Объект `SimpleNamespace` с данными из JSON.
    - **Назначение**:
      - Преобразует JSON данные в объект `SimpleNamespace`.
    - **Пример**:
      ```python
      json_data = '{"ключ1": "значение1", "ключ2": "значение2"}'
      result = json2ns(json_data)
      print(result.ключ1)  # Вывод: значение1
      ```
  - `json2xml(json_data, root_tag="root")`:
    - **Аргументы**:
      - `json_data` (`str | dict | Path`): JSON данные в виде строки, словаря или пути к файлу JSON.
      - `root_tag` (`str`): Корневой тег для XML (по умолчанию `"root"`).
    - **Возвращает**:
      - `str`: XML строка.
    - **Назначение**:
      - Преобразует JSON данные в XML формат.
    - **Пример**:
      ```python
      json_data = '{"ключ1": "значение1", "ключ2": "значение2"}'
      result = json2xml(json_data)
      print(result)  # Вывод: XML строка
      ```
  - `json2xls(json_data, xls_file_path)`:
    - **Аргументы**:
      - `json_data` (`str | list | dict | Path`): JSON данные в виде строки, списка словарей, словаря или пути к файлу JSON.
      - `xls_file_path` (`str | Path`): Путь к XLS файлу для записи.
    - **Возвращает**:
      - `bool`: `True` в случае успеха, `False` в случае ошибки.
    - **Назначение**:
      - Преобразует JSON данные в XLS формат и сохраняет в файл.
    - **Пример**:
      ```python
      json_data = '[{"ключ1": "значение1", "ключ2": "значение2"}]'
      xls_file_path = 'output.xls'
      result = json2xls(json_data, xls_file_path)
      print(result)  # Вывод: True или False в зависимости от успеха
      ```

- **Переменные**:
  - `data`: Промежуточная переменная для хранения десериализованных JSON данных.
  - `json_file`: Файловый объект для чтения JSON данных из файла.
  - `ex`: Переменная для хранения исключения в блоке `except`.
  - `csv_file_path` (`str | Path`): Путь к CSV файлу для записи.
  - `xls_file_path` (`str | Path`): Путь к XLS файлу для записи.

- **Потенциальные ошибки и области для улучшения**:
  - В функциях `json2xls` и `json2csv` отсутствует обработка исключений, связанных с `save_xls_file` и `save_csv_file`. Необходимо добавить блоки `try...except` для обработки возможных ошибок при записи в файл.
  - В функции `json2xls` переменная `file_path` используется вместо `xls_file_path`. Это может привести к ошибкам. Необходимо исправить на `xls_file_path`.
  - Отсутствует проверка существования файла перед его чтением в функциях, где `json_data` является путем к файлу.

- **Взаимосвязи с другими частями проекта**:
  - Модуль использует функции из `src.utils.csv`, `src.utils.jjson`, `src.utils.xls` и `src.utils.convertors.dict` для выполнения преобразований и сохранения данных.
  - Для логирования ошибок используется модуль `src.logger.logger`.

Таким образом, данный модуль предоставляет набор функций для преобразования JSON данных в различные форматы, такие как CSV, SimpleNamespace, XML и XLS, и обеспечивает логирование ошибок.