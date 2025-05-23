# Модуль Lockchat.py

## Обзор

Модуль `Lockchat.py` предоставляет интерфейс для взаимодействия с API Lockchat. Он позволяет отправлять запросы к API для получения ответов от моделей, таких как "gpt-4" и "gpt-3.5-turbo". Модуль поддерживает потоковую передачу данных и не требует аутентификации.

## Подробнее

Модуль содержит функцию `_create_completion`, которая отправляет запросы к API Lockchat и возвращает ответ в потоковом режиме.

## Классы

В данном модуле классы не определены.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    """ Функция отправляет запрос к API Lockchat и возвращает ответ в потоковом режиме.

    Args:
        model (str): Имя используемой модели.
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        temperature (float, optional): Температура для генерации текста. По умолчанию 0.7.
        **kwargs: Дополнительные аргументы.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа от API.

    Raises:
        Exception: Если возникает ошибка при отправке запроса или обработке ответа.

    """
```

**Назначение**:
Функция `_create_completion` отправляет запрос к API Lockchat для генерации текста на основе предоставленных сообщений и параметров модели. Она обрабатывает ответ от API и возвращает токены сгенерированного текста в потоковом режиме.

**Параметры**:
- `model` (str): Имя используемой модели.
- `messages` (list): Список сообщений для отправки в API.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию 0.7.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `Generator[str, None, None]`: Генератор токенов ответа от API.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при отправке запроса или обработке ответа.

**Как работает функция**:
1. Функция формирует полезную нагрузку (payload) с параметрами запроса, такими как температура, сообщения, модель и флаг потоковой передачи.
2. Устанавливает заголовки запроса, включая user-agent.
3. Отправляет POST-запрос к API Lockchat по адресу `http://super.lockchat.app/v1/chat/completions?auth=FnMNPlwZEnGFqvEc9470Vw==`.
4. Итерируется по строкам ответа, полученным из `response.iter_lines()`.
5. Проверяет наличие ошибки, связанной с отсутствием модели "gpt-4", и в случае обнаружения повторно вызывает `_create_completion`.
6. Извлекает содержимое токена из каждой строки ответа, декодирует его и извлекает поле `content` из JSON.
7. Возвращает токен, если он существует.

**Примеры**:
```python
# Пример вызова функции
messages = [{"role": "user", "content": "Hello, world!"}]
model = "gpt-3.5-turbo"
stream = True
temperature = 0.7

# result = _create_completion(model=model, messages=messages, stream=stream, temperature=temperature)
# for token in result:
#     print(token)
```

## Параметры модуля

- `url` (str): URL API Lockchat (`http://super.lockchat.app`).
- `model` (list): Список поддерживаемых моделей (`['gpt-4', 'gpt-3.5-turbo']`).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных (True).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (False).

## Дополнительная информация

`params` (str): Строка, содержащая информацию о поддерживаемых типах параметров функции `_create_completion`.