# Provider.py

## Обзор

Этот файл содержит базовый класс `Provider`, который используется для взаимодействия с различными моделями AI, такими как Google Gemini и OpenAI. 
Он предоставляет абстрактные методы для создания запросов и обработки ответов.

## Подробнее

Этот файл содержит базовый класс для всех провайдеров, которые будут использоваться в `g4f`.  

## Классы

### `class Provider`

**Описание**: Базовый класс для провайдеров, которые будут использоваться в `g4f`. 

**Атрибуты**:

- `url` (str): Базовый URL для провайдера.
- `model` (str): Имя модели AI.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую обработку.
- `needs_auth` (bool): Флаг, указывающий, требуется ли авторизация для доступа к API провайдера.

**Методы**:

- `_create_completion(model: str, messages: list, stream: bool, **kwargs)`: Абстрактный метод для создания запросов к модели AI.
    - **Параметры**:
        - `model` (str): Имя модели AI.
        - `messages` (list): Список сообщений для модели.
        - `stream` (bool): Флаг, указывающий, нужно ли использовать потоковую обработку.
        - `**kwargs`: Дополнительные параметры для запроса.
    - **Возвращает**:
        - Ответ модели AI.

## Функции

### `_create_completion`

**Назначение**: Создает запрос к модели AI.

**Параметры**:

- `model` (str): Имя модели AI.
- `messages` (list): Список сообщений для модели.
- `stream` (bool): Флаг, указывающий, нужно ли использовать потоковую обработку.
- `**kwargs`: Дополнительные параметры для запроса.

**Возвращает**:

- Ответ модели AI.

**Пример**:

```python
from g4f.Provider.Provider import _create_completion

model = 'gpt-3.5-turbo'
messages = [{'role': 'user', 'content': 'Привет'}]
stream = False
kwargs = {}

response = _create_completion(model, messages, stream, **kwargs)

print(response)
```

**Как работает функция**:

Эта функция использует глобальные переменные `url` и `model` для создания URL-адреса для запроса к модели AI. Она затем формирует запрос, используя предоставленные сообщения и параметры, и отправляет его на сервер модели. 

**Примеры**:

-  Пример создания запроса с потоковой обработкой:
    ```python
    response = _create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Привет'}], stream=True)
    ```
-  Пример создания запроса без потоковой обработки:
    ```python
    response = _create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Привет'}], stream=False)
    ```
-  Пример создания запроса с дополнительными параметрами:
    ```python
    response = _create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Привет'}], stream=False, temperature=0.5)
    ```

## Параметры

- `url` (str): Базовый URL для провайдера.
- `model` (str): Имя модели AI.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую обработку.
- `needs_auth` (bool): Флаг, указывающий, требуется ли авторизация для доступа к API провайдера.

## Внутренние функции 

### `get_type_hints`

**Назначение**: Получает типы параметров функции.

**Параметры**:

- `func`: Функция.

**Возвращает**:

- Словарь, где ключи — имена параметров, а значения — типы параметров.

**Как работает функция**:

Эта функция использует стандартную библиотеку Python `typing` для получения типов параметров функции.

## Примеры

-  Пример создания экземпляра класса Provider:
    ```python
    from g4f.Provider.Provider import Provider

    provider = Provider()
    ```
-  Пример вызова метода `_create_completion`:
    ```python
    response = provider._create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Привет'}], stream=False)
    ```