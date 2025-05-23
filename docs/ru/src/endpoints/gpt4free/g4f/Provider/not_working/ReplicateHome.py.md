# Модуль `ReplicateHome`

## Обзор

Модуль `ReplicateHome` предоставляет асинхронный генератор для взаимодействия с API Replicate.com. Он позволяет генерировать текст и изображения с использованием различных моделей, поддерживаемых Replicate. Модуль поддерживает потоковую передачу данных и предоставляет удобные средства для обработки запросов и ответов API.

## Подробней

Модуль предназначен для использования в асинхронных приложениях, где требуется взаимодействие с API Replicate для генерации контента. Он включает в себя поддержку различных моделей, как текстовых, так и для генерации изображений. Модуль автоматически форматирует запросы и обрабатывает ответы, предоставляя результаты в удобном формате.

## Классы

### `ReplicateHome`

**Описание**: Класс `ReplicateHome` является поставщиком асинхронных генераторов для API Replicate.com.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL главной страницы Replicate.com.
- `api_endpoint` (str): URL API для создания предсказаний.
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `default_model` (str): Модель по умолчанию для генерации текста (`'google-deepmind/gemma-2b-it'`).
- `default_image_model` (str): Модель по умолчанию для генерации изображений (`'stability-ai/stable-diffusion-3'`).
- `image_models` (list): Список моделей для генерации изображений.
- `text_models` (list): Список моделей для генерации текста.
- `models` (list): Объединенный список моделей для текста и изображений.
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.
- `model_versions` (dict): Словарь версий моделей, используемых в API.

**Принцип работы**:
Класс использует `aiohttp` для выполнения асинхронных HTTP-запросов к API Replicate. Он поддерживает как текстовые, так и графические модели, автоматически выбирая соответствующие параметры запроса. Класс обрабатывает ответы API, проверяет статус предсказания и возвращает результаты в виде асинхронного генератора.

## Методы класса

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    prompt: str = None,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Replicate.

    Args:
        cls (ReplicateHome): Класс `ReplicateHome`.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для формирования запроса.
        prompt (str, optional): Текст запроса. Если `None`, формируется автоматически. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий результаты предсказания.

    Raises:
        Exception: Если предсказание не удалось или истекло время ожидания.
        ValueError: Если получен неожиданный формат ответа от API.

    """
    ...
```

**Назначение**: Создает и возвращает асинхронный генератор для выполнения запросов к API Replicate.

**Параметры**:
- `cls` (ReplicateHome): Ссылка на класс `ReplicateHome`.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Текст запроса. Если `None`, формируется автоматически. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий результаты предсказания.

**Вызывает исключения**:
- `Exception`: Если предсказание не удалось или истекло время ожидания.
- `ValueError`: Если получен неожиданный формат ответа от API.

**Как работает функция**:
1. **Извлекает модель**: Функция извлекает название модели, используя `cls.get_model(model)`, что позволяет использовать псевдонимы моделей.
2. **Формирует заголовки**: Определяет необходимые заголовки для HTTP-запроса, включая `accept`, `content-type`, `origin` и `user-agent`.
3. **Создает сессию**: Создает асинхронную сессию `ClientSession` с заданными заголовками и прокси (если указан).
4. **Формирует запрос**: Если `prompt` не указан, формирует его на основе `messages`.  Для моделей изображений `prompt` берется из последнего сообщения.
5. **Отправляет запрос**: Отправляет POST-запрос к `cls.api_endpoint` с данными, включающими модель, версию модели и входные параметры.
6. **Обрабатывает ответ**: Получает `prediction_id` из ответа.
7. **Опрашивает API**: Опрашивает API по URL `poll_url` для получения статуса предсказания.
8. **Проверяет статус**: В цикле проверяет статус предсказания. Если статус `succeeded`, возвращает результаты. Если `failed`, вызывает исключение.
9. **Возвращает результаты**: Для моделей изображений возвращает `ImageResponse` с URL изображения. Для текстовых моделей возвращает чанки текста через генератор.
10. **Обрабатывает ошибки**: Если время ожидания истекло или произошла ошибка при обработке ответа, вызывает исключение.

**Примеры**:

```python
# Пример использования для текстовой модели
model = "gemma-2b"
messages = [{"role": "user", "content": "Hello, how are you?"}]
async for chunk in ReplicateHome.create_async_generator(model=model, messages=messages):
    print(chunk)

# Пример использования для модели генерации изображений
model = "sd-3"
messages = [{"role": "user", "content": "A beautiful landscape"}]
async for image_response in ReplicateHome.create_async_generator(model=model, messages=messages):
    print(image_response.image_url)