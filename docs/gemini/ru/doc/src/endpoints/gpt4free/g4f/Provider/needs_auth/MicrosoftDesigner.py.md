# Модуль MicrosoftDesigner
## Обзор
Модуль `MicrosoftDesigner` обеспечивает доступ к модели `Microsoft Designer` для генерации изображений. 
Он использует веб-API `Microsoft Designer` для создания изображений по текстовым подсказкам.

## Классы
### `class MicrosoftDesigner`

**Описание**: Класс `MicrosoftDesigner` реализует асинхронный генератор изображений с использованием модели `Microsoft Designer`.

**Наследует**:
- `AsyncGeneratorProvider`: Базовый класс для асинхронных генераторов.
- `ProviderModelMixin`: Базовый класс для моделей провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("Microsoft Designer").
- `url` (str): Базовый URL провайдера ("https://designer.microsoft.com").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `use_nodriver` (bool): Флаг, указывающий на использование `nodriver` (True).
- `needs_auth` (bool): Флаг, указывающий на необходимость авторизации (True).
- `default_image_model` (str):  Модель изображения по умолчанию ("dall-e-3").
- `image_models` (list): Список поддерживаемых моделей изображений (`default_image_model`, "1024x1024", "1024x1792", "1792x1024").
- `models` (list): Список поддерживаемых моделей (совпадает с `image_models`).

**Методы**:
- `create_async_generator()`:  Создает асинхронный генератор изображений.
- `generate()`:  Генерирует изображения.

**Принцип работы**:
- Класс `MicrosoftDesigner`  является подклассом  `AsyncGeneratorProvider` и `ProviderModelMixin`.
- Метод `create_async_generator()` создает асинхронный генератор для  обработки запросов к модели.
- Метод `generate()`  использует веб-API  `Microsoft Designer` для генерации изображения по подсказке,  использует HAR-файлы или асинхронные запросы  для получения токена доступа. 

**Примеры**:
```python
# Создание инстанса класса MicrosoftDesigner 
designer = MicrosoftDesigner()

# Генерирование изображения с использованием модели 'dall-e-3'
image = await designer.generate(prompt='кошка в шляпе', image_size='1024x1024')
```

#### `create_async_generator()`

**Назначение**: Создает асинхронный генератор изображений.

**Параметры**:
- `model` (str): Название модели.
- `messages` (Messages): Список сообщений для контекста.
- `prompt` (str, optional): Текстовая подсказка для генерации изображения. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.

**Возвращает**:
- `AsyncResult`: Асинхронный результат с генератором изображений.

**Как работает функция**:
- Метод получает параметры, включающие модель, сообщения, подсказку и прокси.
- Определяет размер изображения в зависимости от выбранной модели.
- Вызывает метод `generate()` для генерации изображения.
- Возвращает асинхронный результат с генератором, который может быть использован для получения изображений.

**Примеры**:
```python
async_generator = await MicrosoftDesigner.create_async_generator(
    model='dall-e-3',
    messages=[
        {'role': 'user', 'content': 'Сгенерируй изображение кошки в шляпе'}
    ],
)
```

#### `generate()`

**Назначение**: Генерирует изображения.

**Параметры**:
- `prompt` (str): Текстовая подсказка.
- `image_size` (str): Размер изображения.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse` с результатом генерации.

**Как работает функция**:
- Метод получает параметры, включающие подсказку, размер изображения и прокси.
- Пытается прочитать  токен доступа и user-agent из HAR-файлов.
- Если HAR-файлов нет или они недействительны,  метод делает асинхронный запрос для получения токена доступа и user-agent.
- Вызывает функцию `create_images()` для генерации изображения.
- Возвращает `ImageResponse`,  содержащий сгенерированные изображения и исходную подсказку.

**Примеры**:
```python
image_response = await MicrosoftDesigner.generate(
    prompt='кошка в шляпе',
    image_size='1024x1024'
)

# Получение сгенерированного изображения
image_url = image_response.images[0]
```

## Функции
### `create_images()`

**Назначение**: Генерирует изображения с использованием веб-API `Microsoft Designer`.

**Параметры**:
- `prompt` (str): Текстовая подсказка.
- `access_token` (str): Токен доступа.
- `user_agent` (str): User-agent браузера.
- `image_size` (str): Размер изображения.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.
- `seed` (int, optional): Случайное число для генерации. По умолчанию `None`.

**Возвращает**:
- `list`: Список сгенерированных URL-адресов изображений.

**Как работает функция**:
- Метод формирует URL-адрес API-запроса.
- Создает объект `FormData` для отправки данных.
- Устанавливает заголовки запроса.
- Делает асинхронный POST-запрос к API `Microsoft Designer`.
- Обрабатывает ответ и извлекает URL-адреса сгенерированных изображений.

**Примеры**:
```python
images = await create_images(
    prompt='кошка в шляпе',
    access_token='your_access_token',
    user_agent='your_user_agent',
    image_size='1024x1024'
)
```


### `readHAR()`

**Назначение**:  Считывает токен доступа и user-agent из HAR-файлов.

**Параметры**:
- `url` (str): URL-адрес веб-сайта, для которого необходимо найти токены доступа.

**Возвращает**:
- `tuple[str, str]`: Кортеж, содержащий токен доступа и user-agent.

**Как работает функция**:
-  Перебирает файлы HAR,  располагающиеся в `~/.har`
-  Проверяет,  соответствует ли URL-адрес в файле HAR  заданному URL-адресу.
-  Извлекает токен доступа и user-agent из заголовков запросов,  сохраненных в файле HAR.
-  Возвращает кортеж, содержащий токен доступа и user-agent.

**Примеры**:
```python
access_token, user_agent = readHAR('https://designer.microsoft.com')
```

### `get_access_token_and_user_agent()`

**Назначение**: Получает токен доступа и user-agent с использованием `nodriver`.

**Параметры**:
- `url` (str): URL-адрес веб-сайта,  с которого необходимо получить токен доступа.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.

**Возвращает**:
- `tuple[str, str]`: Кортеж, содержащий токен доступа и user-agent.

**Как работает функция**:
-  Создает экземпляр `nodriver` с  конфигурацией для  `Microsoft Designer`.
-  Открывает страницу `Microsoft Designer`  в браузере,  используя `nodriver`.
-  Извлекает  `user-agent`  из  `navigator.userAgent`.
-  Получает токен доступа из  `localStorage`.
-  Закрывает страницу браузера.
-  Возвращает кортеж, содержащий токен доступа и  `user-agent`.

**Примеры**:
```python
access_token, user_agent = await get_access_token_and_user_agent('https://designer.microsoft.com')
```