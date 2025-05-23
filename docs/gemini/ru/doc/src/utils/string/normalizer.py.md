# Модуль нормализации строк и числовых данных

## Обзор

Модуль предоставляет функции для нормализации строк, булевых значений, целых и чисел с плавающей точкой. 
Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

## Подробнее

Модуль `src/utils/string/normalizer.py` используется для преобразования входных данных в унифицированный формат. 
Он содержит набор функций, которые позволяют нормализовать строки, булевы значения, целые числа и числа с плавающей точкой. 
Эти функции используются для обработки данных, поступающих из различных источников, и приведения их к формату, 
подходящему для использования в других частях проекта.

## Классы

### `class StringNormalizer` 

**Описание**: Класс для нормализации строк. Не используется в проекте. 

**Атрибуты**: 
- `input_str` (str): Исходная строка для нормализации.

**Методы**: 
- `simplify_string()`: Упрощает строку, оставляя только буквы, цифры и заменяя пробелы подчеркиваниями. 
- `remove_line_breaks()`: Удаляет переносы строк из строки. 
- `remove_html_tags()`: Удаляет HTML-теги из строки. 
- `remove_special_characters()`: Удаляет указанные специальные символы из строки.

## Функции

### `normalize_boolean`

**Назначение**: Преобразует данные в булево значение.

**Параметры**:
- `input_data` (Any): Данные, которые могут представлять булево значение (например, bool, строка, целое число).

**Возвращает**:
- `bool`: Булевое представление входных данных.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время преобразования.

**Как работает функция**:
- Функция проверяет тип входных данных. 
- Если данные уже являются булевым значением, функция возвращает их. 
- В противном случае функция преобразует входные данные в строку, удаляет пробелы и приводит ее к нижнему регистру. 
- Затем функция проверяет, соответствует ли строка одному из предопределенных значений, представляющих `True` или `False`. 
- Если строка соответствует одному из этих значений, функция возвращает соответствующее булево значение. 
- В противном случае функция возвращает исходное значение.

**Примеры**:

```python
>>> normalize_boolean('yes')
True
>>> normalize_boolean(True)
True
>>> normalize_boolean(0)
False
>>> normalize_boolean('no')
False
>>> normalize_boolean('abc')
'abc'  # Возвращается исходное значение, если преобразование не удалось
```

### `normalize_string`

**Назначение**: Нормализует строку или список строк.

**Параметры**:
- `input_data` (str | list): Входные данные, которые могут быть либо строкой, либо списком строк.

**Возвращает**:
- `str`: Очищенная и нормализованная строка в кодировке UTF-8.

**Вызывает исключения**:
- `TypeError`: Если `input_data` не является строкой или списком строк.

**Как работает функция**:
- Функция проверяет тип входных данных. 
- Если данные являются списком, функция объединяет все элементы списка в одну строку, разделяя их пробелами. 
- Затем функция последовательно выполняет следующие операции:
    - Удаление HTML-тегов.
    - Удаление переносов строк.
    - Удаление специальных символов.
    - Удаление лишних пробелов.
- После выполнения всех операций функция возвращает нормализованную строку в кодировке UTF-8.

**Примеры**:

```python
>>> normalize_string('  Hello  World!  ')
'Hello World!'
>>> normalize_string(['Hello', '  World!  '])
'Hello World!'
>>> normalize_string('<b>Пример</b> строки с HTML')
'Пример строки с HTML'
```

### `normalize_int`

**Назначение**: Преобразует данные в целое число.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть числом или его строковым представлением.

**Возвращает**:
- `int`: Целочисленное представление входных данных.

**Вызывает исключения**:
- `ValueError`: Если входные данные не могут быть преобразованы в целое число.
- `TypeError`: Если входные данные имеют недопустимый тип.
- `InvalidOperation`: Если входные данные представляют собой десятичное число, которое не может быть преобразовано в целое число.

**Как работает функция**:
- Функция проверяет тип входных данных. 
- Если данные уже являются целым числом, функция возвращает их. 
- В противном случае функция пытается преобразовать входные данные в целое число.
- Если преобразование успешно, функция возвращает полученное целое число. 
- В противном случае функция возвращает исходное значение.

**Примеры**:

```python
>>> normalize_int('42')
42
>>> normalize_int(42)
42
>>> normalize_int(42.5)
42
>>> normalize_int('42.5')
42
>>> normalize_int('abc')
'abc'  # Возвращается исходное значение, если преобразование не удалось
```

### `normalize_float`

**Назначение**: Безопасно конвертирует входное значение в float или возвращает None, если конвертация не удалась. Удаляет распространенные символы валют и разделители тысяч перед конвертацией.

**Параметры**:
- `value` (Any): Входное значение (int, float, str и т.д.).

**Возвращает**:
- `Optional[float]`: Число float или None, если конвертация не удалась.

**Как работает функция**:
- Функция проверяет, не является ли входное значение None. 
- Если значение None, функция возвращает None.
- Если значение уже является числом, функция преобразует его в float.
- Если значение является строкой, функция пытается преобразовать его в float.
- Если преобразование успешно, функция возвращает полученное float значение.
- В противном случае функция возвращает None.

**Примеры**:

```python
>>> normalize_float(5)
5.0
>>> normalize_float("5")
5.0
>>> normalize_float("3.14")
3.14
>>> normalize_float("abc")
None
>>> normalize_float("₪0.00")
0.0
>>> normalize_float("$1,234.56")
1234.56
>>> normalize_float("  - 7.5 € ")
-7.5
>>> normalize_float(None)
None
>>> normalize_float(['1'])
None
>>> normalize_float('')
None
```

**Важно!** Проверять после вызова этой функции, что она не вернула None.

### `normalize_sql_date`

**Назначение**: Преобразует данные в формат даты SQL (YYYY-MM-DD).

**Параметры**:
- `input_data` (str): Данные, которые могут представлять дату (например, строка, объект datetime).

**Возвращает**:
- `str`: Нормализованная дата в формате SQL (YYYY-MM-DD) или исходное значение, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время преобразования.

**Как работает функция**:
- Функция проверяет тип входных данных. 
- Если данные являются строкой, функция пытается распарсить дату из строки, используя различные форматы. 
- Если данные уже являются объектом datetime, функция преобразует его в формат даты SQL (YYYY-MM-DD).
- Если преобразование успешно, функция возвращает полученную дату. 
- В противном случае функция возвращает исходное значение.

**Примеры**:

```python
>>> normalize_sql_date('2024-12-06')
'2024-12-06'
>>> normalize_sql_date('12/06/2024')
'2024-12-06'
>>> normalize_sql_date('abc')
'abc'  # Возвращается исходное значение, если преобразование не удалось
```

### `simplify_string`

**Назначение**: Упрощает входную строку, оставляя только буквы, цифры и заменяя пробелы подчеркиваниями.

**Параметры**:
- `input_str` (str): Строка, которую необходимо упростить.

**Возвращает**:
- `str`: Упрощенная строка.

**Как работает функция**:
- Функция удаляет все символы, кроме букв, цифр и пробелов.
- Затем она заменяет пробелы подчеркиваниями.
- После этого функция удаляет повторяющиеся подчеркивания.

**Примеры**:

```python
>>> simplify_string("It's a test string with 'single quotes', numbers 123 and symbols!")
'Its_a_test_string_with_single_quotes_numbers_123_and_symbols'
```

### `remove_line_breaks`

**Назначение**: Удаляет переносы строк из входной строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без переносов строк.

**Как работает функция**:
- Функция заменяет все символы перевода строки (`\n`) и возврата каретки (`\r`) пробелами.
- Затем она удаляет начальные и конечные пробелы.

**Примеры**:

```python
>>> remove_line_breaks("This is a\nstring with\rline breaks.")
'This is a string with line breaks.'
```

### `remove_html_tags`

**Назначение**: Удаляет HTML-теги из входной строки.

**Параметры**:
- `input_html` (str): Входная строка HTML.

**Возвращает**:
- `str`: Строка без HTML-тегов.

**Как работает функция**:
- Функция использует регулярное выражение для удаления всех HTML-тегов из входной строки.

**Примеры**:

```python
>>> remove_html_tags("<b>This is a</b> string with <i>HTML tags</i>.")
'This is a string with HTML tags.'
```

### `remove_special_characters`

**Назначение**: Удаляет указанные специальные символы из строки или списка строк.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.
- `chars` (list[str], optional): Список символов для удаления. По умолчанию `None`.

**Возвращает**:
- `str | list`: Обработанная строка или список с удаленными указанными символами.

**Как работает функция**:
- Функция создает шаблон регулярного выражения для удаления указанных символов. 
- Если входные данные являются строкой, функция применяет шаблон к строке.
- Если входные данные являются списком, функция применяет шаблон ко всем элементам списка.

**Примеры**:

```python
>>> remove_special_characters("This is a string with # special characters.")
'This is a string with  special characters.'
>>> remove_special_characters(["This is string #1", "This is string #2"], chars=['#', '1', '2'])
['This is string ', 'This is string ']
```

### `normalize_sku`

**Назначение**: Нормализует SKU, удаляя специфические ивритские ключевые слова и все небуквенно-цифровые символы, за исключением дефисов.

**Параметры**:
- `input_str` (str): Входная строка, содержащая SKU.

**Возвращает**:
- `str`: Нормализованная строка SKU.

**Как работает функция**:
- Функция удаляет ивритские ключевые слова, такие как "מקט" и "מק'''ט", используя регулярное выражение с флагом `re.IGNORECASE` для учета регистра.
- Затем она удаляет все небуквенно-цифровые символы, за исключением дефисов, используя регулярное выражение `[^\\w-]`.

**Примеры**:

```python
>>> normalize_sku("מקט: 303235-A")
'303235-A'
>>> normalize_sku("מק\'\'ט: 12345-B")
'12345-B'
>>> normalize_sku("Some text מקט: 123-456-789 other text")
'Some text 123-456-789 other text'  # Важно: теперь дефисы и пробелы между текстами сохраняются
```

**Важно!** Обратите внимание, что функция `normalize_sku` удаляет только специфические ивритские ключевые слова. 
Если в строке SKU есть другие небуквенно-цифровые символы, кроме дефисов, они останутся в строке.