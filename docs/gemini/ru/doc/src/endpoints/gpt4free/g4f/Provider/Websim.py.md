# Модуль Websim для GPT4Free

## Обзор

Модуль `Websim` предоставляет реализацию асинхронного генератора ответов (AsyncGeneratorProvider) для GPT4Free, использующего API сервиса `websim.ai`. 

## Подробней

`Websim` обеспечивает доступ к различным моделям, включая `gemini-1.5-pro`, `gemini-1.5-flash` и модели для генерации изображений. 

Этот модуль реализует асинхронный генератор, который позволяет получать ответы от сервиса `websim.ai` в виде потока, что повышает эффективность и производительность. 

## Классы

### `Websim`

**Описание**: Класс `Websim` реализует асинхронный генератор для получения ответов от модели `websim.ai`.
**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:

- `url`: Базовый URL сервиса `websim.ai`.
- `login_url`: URL для входа в систему (не используется в этом модуле).
- `chat_api_endpoint`: URL конечной точки API для текстового общения.
- `image_api_endpoint`: URL конечной точки API для генерации изображений.
- `working`: Флаг, указывающий на работоспособность сервиса (по умолчанию `True`).
- `needs_auth`: Флаг, указывающий на необходимость аутентификации (по умолчанию `False`).
- `use_nodriver`: Флаг, указывающий на использование без Selenium webdriver (по умолчанию `False`).
- `supports_stream`: Флаг, указывающий на поддержку потоковой передачи ответов (по умолчанию `False`).
- `supports_system_message`: Флаг, указывающий на поддержку системных сообщений (по умолчанию `True`).
- `supports_message_history`: Флаг, указывающий на поддержку истории сообщений (по умолчанию `True`).
- `default_model`: Модель по умолчанию (`gemini-1.5-pro`).
- `default_image_model`: Модель для генерации изображений по умолчанию (`flux`).
- `image_models`: Список доступных моделей для генерации изображений.
- `models`: Список всех доступных моделей, включая текстовые и модели для генерации изображений.

**Методы**:

- `generate_project_id(for_image=False)`:  Генерирует уникальный идентификатор проекта для API запросов.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, aspect_ratio: str = "1:1", project_id: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения ответа от модели `websim.ai`.
- `_handle_image_request(project_id: str, messages: Messages, prompt: str, aspect_ratio: str, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос для генерации изображений.
- `_handle_chat_request(project_id: str, messages: Messages, headers: dict, proxy: str = None, **kwargs) -> AsyncResult`: Обрабатывает запрос для текстового общения.


##  Функции

### `generate_project_id`

**Назначение**: Генерирует уникальный идентификатор проекта.
**Параметры**:
- `for_image` (bool, optional): Флаг, указывающий на то, генерируется ID для запроса на генерацию изображений. По умолчанию `False`.
**Возвращает**:
- `str`: Уникальный идентификатор проекта в соответствующем формате.

**Как работает функция**:
- Генерирует случайный идентификатор проекта, состоящий из строчных букв и цифр, соответствующий формату, установленному для запросов на общение или на генерацию изображений.

**Примеры**:

```python
>>> Websim.generate_project_id()
'ke3_xh5gai3gjkmruomu'

>>> Websim.generate_project_id(for_image=True)
'kx0m131_rzz66qb2xoy7'
```

### `create_async_generator`

**Назначение**: Создает асинхронный генератор для получения ответов от модели `websim.ai`.
**Параметры**:
- `model`: Модель, которую нужно использовать для генерации текста или изображений.
- `messages`: Список сообщений, которые необходимо использовать в качестве входных данных для модели.
- `prompt`: Дополнительный текст, который может быть включен в запрос.
- `proxy`: Прокси-сервер, который может быть использован для доступа к `websim.ai`.
- `aspect_ratio`: Соотношение сторон для изображений.
- `project_id`: Уникальный идентификатор проекта.
- `**kwargs`: Дополнительные ключевые слова, которые могут быть переданы в запрос.
**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который производит ответ от модели.

**Как работает функция**:
- Выполняет запрос к API `websim.ai`, используя правильный URL для запроса на генерацию текста или изображений.
- Обрабатывает ответ от модели и производит текст или изображения в формате `AsyncResult`, который может быть использован для получения ответа от модели.

**Примеры**:

```python
>>> async def main():
...     messages = [
...         {"role": "user", "content": "Привет, как дела?"}
...     ]
...     async for response in Websim.create_async_generator(model='gemini-1.5-pro', messages=messages):
...         print(response)
...
>>> asyncio.run(main())
Привет! У меня все отлично, спасибо за вопрос. Чем могу помочь?
```

## Внутренние функции

### `_handle_image_request`

**Назначение**: Обрабатывает запрос для генерации изображений.
**Параметры**:
- `project_id`: Уникальный идентификатор проекта.
- `messages`: Список сообщений, которые необходимо использовать в качестве входных данных для модели.
- `prompt`: Дополнительный текст, который может быть включен в запрос.
- `aspect_ratio`: Соотношение сторон для изображений.
- `headers`: Заголовки HTTP-запроса.
- `proxy`: Прокси-сервер, который может быть использован для доступа к `websim.ai`.
- `**kwargs`: Дополнительные ключевые слова, которые могут быть переданы в запрос.
**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который производит ответ от модели.

**Как работает функция**:
- Формирует запрос к API `websim.ai` для генерации изображений, используя предоставленные параметры.
- Отправляет запрос к API и получает ответ.
- Обрабатывает ответ и производит изображения в формате `ImageResponse`, который может быть использован для получения доступа к изображениям.

### `_handle_chat_request`

**Назначение**: Обрабатывает запрос для текстового общения.
**Параметры**:
- `project_id`: Уникальный идентификатор проекта.
- `messages`: Список сообщений, которые необходимо использовать в качестве входных данных для модели.
- `headers`: Заголовки HTTP-запроса.
- `proxy`: Прокси-сервер, который может быть использован для доступа к `websim.ai`.
- `**kwargs`: Дополнительные ключевые слова, которые могут быть переданы в запрос.
**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который производит ответ от модели.

**Как работает функция**:
- Формирует запрос к API `websim.ai` для текстового общения, используя предоставленные параметры.
- Отправляет запрос к API и получает ответ.
- Обрабатывает ответ и производит текст в формате `AsyncResult`, который может быть использован для получения доступа к тексту.

```markdown