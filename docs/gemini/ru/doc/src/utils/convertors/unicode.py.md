# Модуль `unicode`

## Обзор

Модуль `unicode` содержит функцию `decode_unicode_escape` для декодирования строк, списков или словарей, содержащих юникодные escape-последовательности. 

## Функции

### `decode_unicode_escape`

**Назначение**: 
Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

**Параметры**:

- `input_data` (Dict[str, Any] | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

**Возвращает**:

- Dict[str, Any] | list | str: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

**Вызывает исключения**:

- `UnicodeDecodeError`: Если при декодировании строки возникает ошибка.

**Пример**:
```python
input_dict = {
    'product_name': r'\u05de\u05e7\"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
    'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
    'price': 123.45
}

input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

input_string = r'\u05de\u05e7\"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

# Применяем функцию
decoded_dict = decode_unicode_escape(input_dict)
decoded_list = decode_unicode_escape(input_list)
decoded_string = decode_unicode_escape(input_string)

print(decoded_dict)
print(decoded_list)
print(decoded_string)
```

**Как работает функция**:

- Функция проверяет тип входных данных: словарь, список или строка.
- Если `input_data` - словарь, функция рекурсивно обрабатывает все значения словаря с помощью себя же.
- Если `input_data` - список, функция рекурсивно обрабатывает все элементы списка с помощью себя же.
- Если `input_data` - строка, функция выполняет следующие действия:
    - Декодирует строку с escape-последовательностями с помощью `input_data.encode('utf-8').decode('unicode_escape')`.
    - Если декодирование не удается, функция возвращает исходную строку.
    - Преобразует все найденные последовательности \\uXXXX с помощью регулярного выражения `r'\\\\u[0-9a-fA-F]{4}'`.
- В случае, если тип входных данных не поддерживается, функция возвращает данные без изменений.

```python
def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    Args:
        input_data (dict | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.

    Returns:
        dict | list | str: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

    Пример использования:
    .. code-block:: python
        input_dict = {
            'product_name': r'\u05de\u05e7\"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
            'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
            'price': 123.45
        }

        input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

        input_string = r'\u05de\u05e7\"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

        # Применяем функцию
        decoded_dict = decode_unicode_escape(input_dict)
        decoded_list = decode_unicode_escape(input_list)
        decoded_string = decode_unicode_escape(input_string)

        print(decoded_dict)
        print(decoded_list)
        print(decoded_string)

    """
    
    if isinstance(input_data, dict):
        # Рекурсивная обработка значений словаря
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    
    elif isinstance(input_data, list):
        # Рекурсивная обработка элементов списка
        return [decode_unicode_escape(item) for item in input_data]
    
    elif isinstance(input_data, str):
        # Функция декодирует строку, если она содержит escape-последовательности
        try:
            # Шаг 1: Декодирование строки с escape-последовательностями
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError:
            decoded_string = input_data
        
        # Шаг 2: Преобразование всех найденных последовательностей \\uXXXX
        unicode_escape_pattern = r'\\\\u[0-9a-fA-F]{4}'
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        
        return decoded_string
    
    else:
        # Если тип данных не поддерживается, функция вернет данные без изменений
        return input_data