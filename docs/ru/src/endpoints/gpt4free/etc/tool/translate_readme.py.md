# Модуль для перевода README файлов

## Обзор

Этот модуль предназначен для автоматического перевода файлов `README.md` на другие языки. В частности, он ориентирован на перевод документации на немецкий язык (german) с использованием сервиса g4f (GPT4Free). Он разделяет `README.md` на части, переводит каждую часть и сохраняет результат в новом файле.

## Подробнее

Модуль использует `g4f` для перевода текста, разделяя файл `README.md` на части, чтобы эффективно обрабатывать большие объемы текста. Он также включает в себя функциональность для обработки определенных блоков текста, которые не должны быть переведены, таких как примеры кода, а также сохраняет важные элементы форматирования, такие как `[!Note]`.

## Функции

### `read_text`

```python
def read_text(text) -> str:
    """ Функция извлекает текст из markdown документа, находящегося между блоками code fence (```).

    Args:
        text (str): Исходный текст документа markdown.

    Returns:
        str: Текст, извлеченный из документа, или пустая строка, если ничего не найдено.

    
    - Функция принимает строку текста в формате markdown.
    - Разбивает текст на строки.
    - Итерируется по строкам, определяя начало и конец блоков кода, отмеченных символами '```'.
    - Извлекает текст между этими блоками, удаляет лишние пробелы в начале и конце.

    Примеры:
        >>> text = "Some text\\n```\\nCode example\\n```\\nMore text"
        >>> read_text(text)
        'Code example'
    """
```

### `translate`

```python
async def translate(text) -> str:
    """ Асинхронная функция для перевода текста с использованием сервиса g4f.Provider.OpenaiChat.

    Args:
        text (str): Текст для перевода.

    Returns:
        str: Переведенный текст.

    
    - Формирует запрос к g4f с инструкцией перевести предоставленный текст на немецкий язык.
    - Добавляет к запросу указание сохранять блоки кода без изменений.
    - Использует `g4f.Provider.OpenaiChat.create_async` для асинхронного выполнения перевода.
    - Извлекает переведенный текст из ответа, с помощью функции `read_text`.
    - Добавляет закрывающий тег "```" в конце переведенного текста, если исходный текст заканчивался на "```",
      но результат перевода – нет.

    Примеры:
        >>> text = "This is a text to translate."
        >>> translated_text = await translate(text)
        >>> print(translated_text)
        'Dies ist ein zu übersetzender Text.'
    """
```

### `translate_part`

```python
async def translate_part(part: str, i: int) -> str:
    """ Асинхронная функция для перевода части текста, исключая определенные блоки и заголовки.

    Args:
        part (str): Часть текста для перевода.
        i (int): Индекс части текста.

    Returns:
        str: Переведенная часть текста.

    
    - Проверяет, содержит ли часть текста заголовки из списка `blocklist`.
    - Если находит заблокированные заголовки, переводит только первую строку и заголовки из `allowlist`.
    - Если заблокированных заголовков нет, переводит всю часть текста целиком.
    - Выводит в консоль сообщение об успешном переводе части текста.

    Примеры:
        >>> part = "## Example text"
        >>> i = 1
        >>> translated_part = await translate_part(part, i)
        >>> print(translated_part)
        '## Beispieltext'
    """
```

### `translate_readme`

```python
async def translate_readme(readme: str) -> str:
    """ Асинхронная функция для перевода всего файла README, разделенного на части.

    Args:
        readme (str): Полный текст файла README.

    Returns:
        str: Полный переведенный текст файла README.

    
    - Разделяет текст README на части, используя разделитель '## '.
    - Асинхронно переводит каждую часть с использованием `asyncio.gather` и `translate_part`.
    - Объединяет переведенные части обратно в один текст.

    Примеры:
        >>> readme = "## Title\\nSome text"
        >>> translated_readme = await translate_readme(readme)
        >>> print(translated_readme)
        '## Titel\\nEtwas Text'
    """
```
```markdown
# Модуль для перевода README файлов

## Обзор

Этот модуль предназначен для автоматического перевода файлов `README.md` на другие языки. В частности, он ориентирован на перевод документации на немецкий язык (german) с использованием сервиса g4f (GPT4Free). Он разделяет `README.md` на части, переводит каждую часть и сохраняет результат в новом файле.

## Подробнее

Модуль использует `g4f` для перевода текста, разделяя файл `README.md` на части, чтобы эффективно обрабатывать большие объемы текста. Он также включает в себя функциональность для обработки определенных блоков текста, которые не должны быть переведены, таких как примеры кода, а также сохраняет важные элементы форматирования, такие как `[!Note]`.

## Функции

### `read_text`

**Назначение**: Извлечение текста из markdown документа, находящегося между блоками code fence (```).

**Параметры**:
- `text` (str): Исходный текст документа markdown.

**Возвращает**:
- `str`: Текст, извлеченный из документа, или пустая строка, если ничего не найдено.

**Как работает функция**:
- Функция принимает строку текста в формате markdown.
- Разбивает текст на строки.
- Итерируется по строкам, определяя начало и конец блоков кода, отмеченных символами '```'.
- Извлекает текст между этими блоками, удаляет лишние пробелы в начале и конце.

**Примеры**:
```python
>>> text = "Some text\\n```\\nCode example\\n```\\nMore text"
>>> read_text(text)
'Code example'
```

### `translate`

**Назначение**: Асинхронный перевод текста с использованием сервиса `g4f.Provider.OpenaiChat`.

**Параметры**:
- `text` (str): Текст для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
- Формирует запрос к `g4f` с инструкцией перевести предоставленный текст на немецкий язык.
- Добавляет к запросу указание сохранять блоки кода без изменений.
- Использует `g4f.Provider.OpenaiChat.create_async` для асинхронного выполнения перевода.
- Извлекает переведенный текст из ответа, с помощью функции `read_text`.
- Добавляет закрывающий тег "```" в конце переведенного текста, если исходный текст заканчивался на "```",
  но результат перевода – нет.

**Примеры**:
```python
>>> text = "This is a text to translate."
>>> translated_text = await translate(text)
>>> print(translated_text)
'Dies ist ein zu übersetzender Text.'
```

### `translate_part`

**Назначение**: Асинхронный перевод части текста, исключая определенные блоки и заголовки.

**Параметры**:
- `part` (str): Часть текста для перевода.
- `i` (int): Индекс части текста.

**Возвращает**:
- `str`: Переведенная часть текста.

**Как работает функция**:
- Проверяет, содержит ли часть текста заголовки из списка `blocklist`.
- Если находит заблокированные заголовки, переводит только первую строку и заголовки из `allowlist`.
- Если заблокированных заголовков нет, переводит всю часть текста целиком.
- Выводит в консоль сообщение об успешном переводе части текста.

**Примеры**:
```python
>>> part = "## Example text"
>>> i = 1
>>> translated_part = await translate_part(part, i)
>>> print(translated_part)
'## Beispieltext'
```

### `translate_readme`

**Назначение**: Асинхронный перевод всего файла README, разделенного на части.

**Параметры**:
- `readme` (str): Полный текст файла README.

**Возвращает**:
- `str`: Полный переведенный текст файла README.

**Как работает функция**:
- Разделяет текст README на части, используя разделитель '## '.
- Асинхронно переводит каждую часть с использованием `asyncio.gather` и `translate_part`.
- Объединяет переведенные части обратно в один текст.

**Примеры**:
```python
>>> readme = "## Title\\nSome text"
>>> translated_readme = await translate_readme(readme)
>>> print(translated_readme)
'## Titel\\nEtwas Text'
```