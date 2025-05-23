# Модуль `PollinationsAI`

## Обзор

Модуль `PollinationsAI` предоставляет асинхронный генератор для работы с API Pollinations AI, позволяя генерировать как текст, так и изображения. Он поддерживает различные модели, включая OpenAI и другие. Модуль предназначен для интеграции с другими частями проекта `hypotez` для предоставления доступа к возможностям AI.

## Подробнее

Модуль содержит класс `PollinationsAI`, который является асинхронным провайдером и предоставляет методы для генерации текста и изображений. Он использует `aiohttp` для асинхронных HTTP-запросов и поддерживает различные параметры для настройки генерации.

## Классы

### `PollinationsAI`

**Описание**: Класс `PollinationsAI` предоставляет интерфейс для взаимодействия с API Pollinations AI.

**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:
- `label` (str): Метка провайдера ("Pollinations AI").
- `url` (str): URL сайта Pollinations AI ("https://pollinations.ai").
- `working` (bool): Флаг, указывающий, что провайдер работает (True).
- `supports_system_message` (bool): Флаг, указывающий, что провайдер поддерживает системные сообщения (True).
- `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений (True).
- `text_api_endpoint` (str): URL для текстового API ("https://text.pollinations.ai").
- `openai_endpoint` (str): URL для OpenAI API ("https://text.pollinations.ai/openai").
- `image_api_endpoint` (str): URL для API генерации изображений ("https://image.pollinations.ai/").
- `default_model` (str): Модель, используемая по умолчанию ("openai").
- `default_image_model` (str): Модель для генерации изображений по умолчанию ("flux").
- `default_vision_model` (str): Модель для vision задач по умолчанию.
- `text_models` (List[str]): Список поддерживаемых текстовых моделей.
- `image_models` (List[str]): Список поддерживаемых моделей для генерации изображений.
- `extra_image_models` (List[str]): Список дополнительных моделей для генерации изображений.
- `vision_models` (List[str]): Список моделей для vision задач.
- `extra_text_models` (List[str]): Список дополнительных текстовых моделей.
- `_models_loaded` (bool): Флаг, указывающий, загружены ли модели.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models()`: Возвращает список поддерживаемых моделей.
- `create_async_generator()`: Создает асинхронный генератор для генерации текста или изображений.
- `_generate_image()`: Асинхронно генерирует изображение.
- `_generate_text()`: Асинхронно генерирует текст.

#### Принцип работы:

Класс `PollinationsAI` предназначен для взаимодействия с API Pollinations AI с целью генерации как текстового, так и графического контента. В его основе лежит асинхронный подход, что позволяет эффективно обрабатывать запросы, не блокируя основной поток выполнения программы.

1.  **Инициализация и настройка**:
    *   При создании экземпляра класса задаются основные параметры, такие как URL-адреса API для текста и изображений, а также списки поддерживаемых моделей.
    *   Поддерживается использование системных сообщений и истории сообщений, что расширяет возможности взаимодействия с API.

2.  **Управление моделями**:
    *   Метод `get_models()` используется для получения актуального списка доступных моделей из API. Он обращается к серверам Pollinations AI для обновления списков текстовых и графических моделей.
    *   В случае возникновения ошибок при получении списка моделей используются значения по умолчанию, чтобы обеспечить работоспособность класса.
    *   Псевдонимы моделей позволяют использовать более короткие и понятные названия моделей, которые затем преобразуются в фактические идентификаторы для API.

3.  **Асинхронная генерация контента**:
    *   Метод `create_async_generator()` является центральным методом для генерации контента. Он определяет, какой тип контента (текст или изображение) необходимо сгенерировать, и вызывает соответствующие методы (`_generate_image()` или `_generate_text()`).
    *   Поддерживается передача различных параметров для настройки генерации, таких как прокси, кэширование, параметры изображения (соотношение сторон, размеры, seed), а также параметры текста (температура, штрафы за присутствие и частоту).

4.  **Генерация изображений (`_generate_image()`)**:
    *   Формирует URL-адрес запроса к API генерации изображений на основе предоставленных параметров и प्रॉम्प्ट.
    *   Использует `aiohttp.ClientSession` для асинхронного выполнения HTTP-запроса к API.
    *   Возвращает URL-адрес сгенерированного изображения или сообщение об ошибке в случае неудачи.
    *   Поддерживает генерацию нескольких изображений с использованием разных seed для каждого изображения.

5.  **Генерация текста (`_generate_text()`)**:
    *   Формирует данные запроса к API генерации текста на основе предоставленных параметров, включая сообщения, модель, температуру и другие параметры.
    *   Использует `aiohttp.ClientSession` для асинхронного выполнения HTTP-запроса к API.
    *   Обрабатывает потоковые и не потоковые ответы от API, а также поддерживает различные форматы ответов, включая JSON.
    *   Извлекает сгенерированный текст из ответа API и возвращает его.

6.  **Обработка аудио**:
    *   Определяет, содержит ли запрос аудиоданные, и выбирает соответствующую модель для обработки аудио.

В целом, класс `PollinationsAI` предоставляет гибкий и мощный интерфейс для взаимодействия с API Pollinations AI, позволяя генерировать разнообразный контент с использованием различных моделей и параметров.

## Методы класса

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Обновляет и возвращает список доступных моделей.

        Args:
            **kwargs: Дополнительные аргументы.

        Returns:
            List[str]: Список доступных текстовых и графических моделей.
        """
```

**Назначение**: Обновляет и возвращает список доступных моделей из API Pollinations AI.

**Как работает функция**:
- Функция пытается получить списки моделей для генерации текста и изображений из API Pollinations AI.
- Если запрос успешен, функция объединяет списки моделей, удаляя дубликаты.
- Если запрос не удачен, функция использует модели по умолчанию, чтобы обеспечить работоспособность.

**Примеры**:
```python
PollinationsAI.get_models()
# ['openai', 'flux', 'flux-pro', 'flux-dev', 'flux-schnell', 'midjourney', 'dall-e-3', 'turbo']
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        proxy: str = None,
        cache: bool = False,
        # Image generation parameters
        prompt: str = None,
        aspect_ratio: str = "1:1",
        width: int = None,
        height: int = None,
        seed: Optional[int] = None,
        nologo: bool = True,
        private: bool = False,
        enhance: bool = False,
        safe: bool = False,
        n: int = 1,
        # Text generation parameters
        media: MediaListType = None,
        temperature: float = None,
        presence_penalty: float = None,
        top_p: float = None,
        frequency_penalty: float = None,
        response_format: Optional[dict] = None,
        extra_parameters: list[str] = ["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "voice", "modalities", "audio"],
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для генерации текста или изображений.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для генерации текста.
            stream (bool): Флаг, указывающий, использовать ли потоковую генерацию.
            proxy (str): Прокси-сервер для использования.
            cache (bool): Флаг, указывающий, использовать ли кэширование.
            prompt (str): Текст запроса для генерации изображения.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            nologo (bool): Флаг, указывающий, удалять ли логотип.
            private (bool): Флаг, указывающий, является ли изображение приватным.
            enhance (bool): Флаг, указывающий, улучшать ли изображение.
            safe (bool): Флаг, указывающий, использовать ли безопасный режим.
            n (int): Количество изображений для генерации.
            media (MediaListType): Список медиафайлов для генерации текста.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие для генерации текста.
            top_p (float): Top-p для генерации текста.
            frequency_penalty (float): Штраф за частоту для генерации текста.
            response_format (Optional[dict]): Формат ответа.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные параметры.

        Yields:
            AsyncResult: Часть сгенерированного текста или URL изображения.
        
        Raises:
            ModelNotFoundError: Если указанная модель не найдена.
        """
```

**Назначение**: Создает асинхронный генератор для генерации текста или изображений в зависимости от указанной модели.

**Как работает функция**:
1.  **Загрузка моделей**:
    *   Вызывает метод `cls.get_models()` для обновления списка доступных моделей.
2.  **Определение модели**:
    *   Определяет, какая модель должна использоваться для генерации. Если модель не указана, проверяет, есть ли аудиоданные в запросе, и выбирает соответствующую модель.
    *   Если указанная модель не найдена, вызывает исключение `ModelNotFoundError`.
3.  **Генерация контента**:
    *   Если модель входит в список моделей для генерации изображений (`cls.image_models`), вызывает метод `cls._generate_image()` для генерации изображения.
    *   В противном случае вызывает метод `cls._generate_text()` для генерации текста.
4.  **Асинхронная генерация**:
    *   Использует `async for` для итерации по результатам, возвращаемым методами `_generate_image()` и `_generate_text()`.
    *   Каждый полученный чанк возвращается как часть асинхронного генератора.

**Примеры**:
```python
async for chunk in PollinationsAI.create_async_generator(model='openai', messages=[{'role': 'user', 'content': 'Hello'}]):
    print(chunk)

async for chunk in PollinationsAI.create_async_generator(model='flux', prompt='A cat', aspect_ratio='16:9'):
    print(chunk)
```

### `_generate_image`

```python
    @classmethod
    async def _generate_image(
        cls,
        model: str,
        prompt: str,
        proxy: str,
        aspect_ratio: str,
        width: int,
        height: int,
        seed: Optional[int],
        cache: bool,
        nologo: bool,
        private: bool,
        enhance: bool,
        safe: bool,
        n: int
    ) -> AsyncResult:
        """Асинхронно генерирует изображение.

        Args:
            model (str): Модель для использования.
            prompt (str): Текст запроса для генерации изображения.
            proxy (str): Прокси-сервер для использования.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг, указывающий, использовать ли кэширование.
            nologo (bool): Флаг, указывающий, удалять ли логотип.
            private (bool): Флаг, указывающий, является ли изображение приватным.
            enhance (bool): Флаг, указывающий, улучшать ли изображение.
            safe (bool): Флаг, указывающий, использовать ли безопасный режим.
            n (int): Количество изображений для генерации.

        Yields:
            ImageResponse: URL сгенерированного изображения.
        """
```

**Назначение**: Асинхронно генерирует изображение, используя API Pollinations AI.

**Как работает функция**:
1.  **Формирование параметров запроса**:
    *   Использует функцию `use_aspect_ratio` для формирования параметров запроса на основе предоставленных аргументов и соотношения сторон изображения.
    *   Кодирует параметры и текст запроса в URL-совместимый формат.
2.  **Формирование URL запроса**:
    *   Создает URL для запроса к API генерации изображений, включая закодированный текст запроса и параметры.
3.  **Асинхронный запрос к API**:
    *   Использует `aiohttp.ClientSession` для выполнения асинхронного GET-запроса к API.
    *   В случае ошибки при выполнении запроса логирует ошибку и возвращает URL ответа.
4.  **Возврат результата**:
    *   Возвращает URL сгенерированного изображения в объекте `ImageResponse`.

**Примеры**:
```python
async for chunk in PollinationsAI._generate_image(model='flux', prompt='A cat', aspect_ratio='16:9', proxy=None, width=512, height=512, seed=None, cache=False, nologo=True, private=False, enhance=False, safe=True, n=1):
    print(chunk)
```

### `_generate_text`

```python
    @classmethod
    async def _generate_text(
        cls,
        model: str,
        messages: Messages,
        media: MediaListType,
        proxy: str,
        temperature: float,
        presence_penalty: float,
        top_p: float,
        frequency_penalty: float,
        response_format: Optional[dict],\
        seed: Optional[int],\
        cache: bool,\
        stream: bool,\
        extra_parameters: list[str],\
        **kwargs\
    ) -> AsyncResult:\
        """Асинхронно генерирует текст.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для генерации текста.
            media (MediaListType): Список медиафайлов для генерации текста.
            proxy (str): Прокси-сервер для использования.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие для генерации текста.
            top_p (float): Top-p для генерации текста.
            frequency_penalty (float): Штраф за частоту для генерации текста.
            response_format (Optional[dict]): Формат ответа.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг, указывающий, использовать ли кэширование.
            stream (bool): Флаг, указывающий, использовать ли потоковую генерацию.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные параметры.

        Yields:
            str: Часть сгенерированного текста.
            Usage: Информация об использовании модели.
            FinishReason: Причина завершения генерации.
            ToolCalls: Вызовы инструментов, если есть.
        """
```

**Назначение**: Асинхронно генерирует текст, используя API Pollinations AI.

**Как работает функция**:
1.  **Подготовка параметров**:
    *   Устанавливает случайное зерно, если оно не указано и кэширование не используется.
    *   Определяет, используется ли формат JSON.
2.  **Асинхронный запрос к API**:
    *   Использует `aiohttp.ClientSession` для выполнения асинхронного POST-запроса к API.
    *   Формирует данные запроса, включая сообщения, модель, параметры генерации и дополнительные параметры.
3.  **Обработка ответа**:
    *   Обрабатывает различные типы ответов:
        *   `text/plain`: Возвращает текст ответа.
        *   `text/event-stream`: Обрабатывает потоковый ответ, извлекая контент, информацию об использовании и причину завершения.
        *   `application/json`: Извлекает контент, информацию об использовании, причину завершения и вызовы инструментов из JSON-ответа.
4.  **Возврат результата**:
    *   Возвращает части сгенерированного текста, информацию об использовании и причину завершения генерации.

**Примеры**:
```python
async for chunk in PollinationsAI._generate_text(model='openai', messages=[{'role': 'user', 'content': 'Hello'}], media=None, proxy=None, temperature=0.7, presence_penalty=0, top_p=1, frequency_penalty=0, response_format=None, seed=None, cache=False, stream=True, extra_parameters=[]):
    print(chunk)