# Модуль theb.py

## Обзор

Этот модуль обеспечивает взаимодействие с API-интерфейсом Theb.ai для генерации текста. Он используется для отправки запросов к Theb.ai API, обработки ответов и вывода результатов.

## Подробней

Модуль `theb.py` предназначен для взаимодействия с Theb.ai API, который предоставляет возможности по генерации текста. Он используется для отправки запросов, обработки ответов и вывода результатов.

## Функции

### `format`

**Назначение**:  Функция форматирует части ответа от Theb.ai API, извлекая текст ответа.

**Параметры**:
- `chunk`: Часть ответа от Theb.ai API в виде байтового потока.

**Возвращает**: 
- `None`:  Если обработка завершилась успешно и текст ответа выведен.
- `None`:  Если возникла ошибка при обработке, выводится сообщение об ошибке в консоль. 

**Как работает функция**:
1. Использует регулярное выражение для поиска текста ответа в байтовом потоке `chunk`.
2. Извлекает найденный текст.
3. Выводит текст ответа в консоль с использованием `print(flush=True)`.
4. Возвращает `None`.

**Примеры**:
```python
>>> chunk = b'{"content":"Example text", "fin"'
>>> format(chunk)
Example text
```

## Основной код

**Основной код**:
1. Загружает конфигурацию из аргументов командной строки, которая содержит информацию о сообщении и параметры API.
2. Определяет заголовки запроса для Theb.ai API.
3. Создает JSON-данные для отправки запроса, включающие текст запроса и параметры.
4. Инициализирует цикл, который отправляет запрос к API и обрабатывает ответ.
5. Использует `requests.post` для отправки POST-запроса к Theb.ai API.
6. В качестве `content_callback`  использует функцию `format` для обработки ответа в реальном времени.
7. Выводит текст ответа в консоль.
8. Завершает работу после получения полного ответа от API.

**Обработка ошибок**:
1. Если возникает ошибка при обработке ответа или отправке запроса, выводится сообщение об ошибке в консоль.
2. Цикл продолжается для повторной попытки отправки запроса.

**Примеры**:
```python
>>> python theb.py '{"messages": [{"role": "user", "content": "Hello, world!"}]}'
Hello, world!
```

## Дополнительная информация

- Модуль `theb.py` использует библиотеку `curl_cffi` для отправки запросов к Theb.ai API.
- Модуль предназначен для использования в консольном режиме, для запуска скрипта из командной строки.
- Параметры API и текст запроса задаются через аргументы командной строки.
- Модуль обеспечивает простую отправку запросов к Theb.ai API и вывод ответа в консоль.