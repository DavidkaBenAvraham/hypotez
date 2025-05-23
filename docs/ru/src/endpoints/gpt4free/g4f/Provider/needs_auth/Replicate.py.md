# Модуль Replicate

## Обзор

Модуль `Replicate` предоставляет асинхронный генератор для взаимодействия с платформой Replicate. Он позволяет генерировать текст на основе предоставленных сообщений, используя различные модели, размещенные на Replicate. Этот модуль поддерживает как потоковую передачу данных, так и аутентификацию через API ключ.

## Подробнее

Модуль предназначен для интеграции с платформой Replicate для выполнения задач генерации текста. Он предоставляет удобный интерфейс для взаимодействия с API Replicate, поддерживая различные параметры модели и настройки запросов. Модуль использует асинхронные запросы для эффективной работы и поддерживает потоковую передачу данных, что позволяет получать результаты в реальном времени.

## Классы

### `Replicate`

**Описание**: Класс `Replicate` является асинхронным провайдером генератора и миксином для моделей. Он отвечает за создание запросов к API Replicate и генерацию текста на основе полученных данных.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL главной страницы Replicate.
- `login_url` (str): URL страницы для получения API токенов.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для работы с провайдером.
- `default_model` (str): Модель, используемая по умолчанию, `"meta/meta-llama-3-70b-instruct"`.
- `models` (list[str]): Список поддерживаемых моделей, содержащий `default_model`.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения текста от API Replicate.

## Методы класса

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    proxy: str = None,
    timeout: int = 180,
    system_prompt: str = None,
    max_tokens: int = None,
    temperature: float = None,
    top_p: float = None,
    top_k: float = None,
    stop: list = None,
    extra_data: dict = {},
    headers: dict = {
        "accept": "application/json",
    },
    **kwargs
) -> AsyncResult:
    """ Функция создает асинхронный генератор для взаимодействия с API Replicate и получения текстовых данных.

    Args:
        cls (Type[Replicate]): Класс `Replicate`.
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в модель.
        api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
        proxy (str, optional): Прокси сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `180`.
        system_prompt (str, optional): Системный промпт для модели. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
        temperature (float, optional): Температура для генерации текста. По умолчанию `None`.
        top_p (float, optional): Top P для генерации текста. По умолчанию `None`.
        top_k (float, optional): Top K для генерации текста. По умолчанию `None`.
        stop (list, optional): Список стоп-слов для прекращения генерации. По умолчанию `None`.
        extra_data (dict, optional): Дополнительные данные для отправки в запросе. По умолчанию `{}`.
        headers (dict, optional): Дополнительные заголовки для запроса. По умолчанию `{"accept": "application/json"}`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий текстовые данные.

    Raises:
        MissingAuthError: Если `api_key` отсутствует и требуется аутентификация.
        ResponseError: Если получен невалидный ответ от API.

    
    - Извлекает модель с помощью `cls.get_model(model)`.
    - Проверяет необходимость аутентификации и наличие `api_key`. Если `api_key` отсутствует и требуется аутентификация, вызывается исключение `MissingAuthError`.
    - Формирует заголовок `Authorization` с использованием предоставленного `api_key`.
    - Определяет базовый URL API в зависимости от наличия `api_key`.
    - Создает асинхронную сессию с использованием `StreamSession` с заданными параметрами `proxy`, `headers` и `timeout`.
    - Формирует данные запроса, включая `stream`, `input` с `prompt`, отформатированным с использованием `format_prompt(messages)`, и другие параметры, такие как `system_prompt`, `max_new_tokens`, `temperature`, `top_p`, `top_k` и `stop_sequences`, отфильтрованные с помощью `filter_none`.
    - Формирует URL для запроса, объединяя `api_base`, имя модели и endpoint `/predictions`.
    - Отправляет асинхронный POST-запрос на сформированный URL с данными запроса в формате JSON.
    - Проверяет статус ответа и вызывает исключение `ResponseError` с сообщением "Model not found", если статус равен 404.
    - Преобразует ответ в формат JSON и проверяет наличие ключа "id" в результате. Если ключ отсутствует, вызывается исключение `ResponseError` с сообщением о невалидном ответе.
    - Отправляет асинхронный GET-запрос на URL потока (`result["urls"]["stream"]`) с заголовком `Accept: text/event-stream`.
    - Обрабатывает строки ответа, проверяя наличие префикса "event: ". Если событие равно "done", генерация прекращается. Если событие равно "output", извлекает данные из строки, декодирует их и выдает с помощью `yield`.

    Внутренние функции:
    - Отсутствуют

    """