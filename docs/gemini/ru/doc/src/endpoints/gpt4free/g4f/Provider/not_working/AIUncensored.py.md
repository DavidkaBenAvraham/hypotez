# Модуль AIUncensored

## Обзор

Этот модуль предоставляет класс `AIUncensored`, реализующий асинхронный генератор для взаимодействия с моделью AI Uncensored. 

## Подробнее

`AIUncensored` реализует интерфейс `AsyncGeneratorProvider`, позволяющий генерировать ответы модели AI Uncensored как асинхронный поток данных.

### Настройки

- `url`: Базовый URL API AI Uncensored.
- `api_key`: API-ключ для аутентификации.
- `working`: Флаг, указывающий на работоспособность провайдера (по умолчанию `False`).
- `supports_stream`: Флаг, указывающий на поддержку потоковой передачи (по умолчанию `True`).
- `supports_system_message`: Флаг, указывающий на поддержку системных сообщений (по умолчанию `True`).
- `supports_message_history`: Флаг, указывающий на поддержку истории сообщений (по умолчанию `True`).
- `default_model`: Имя модели по умолчанию (по умолчанию `"hermes3-70b"`).
- `models`: Список поддерживаемых моделей.
- `model_aliases`: Словарь для преобразования псевдонимов моделей в реальные имена.

### Функции

#### `calculate_signature`

**Назначение**: Вычисляет сигнатуру запроса к API AI Uncensored.

**Параметры**:
- `timestamp` (str): метка времени запроса в виде строки.
- `json_dict` (dict): JSON-объект с данными запроса.

**Возвращает**:
- `str`: Сигнатура запроса в виде шестнадцатеричной строки.

**Как работает функция**:
- Собирает строку сообщения, объединяя метку времени и JSON-объект запроса.
- Использует секретный ключ (`your-super-secret-key-replace-in-production`) для вычисления хеша SHA256 сообщения.
- Возвращает шестнадцатеричное представление хеша.


#### `get_server_url`

**Назначение**: Возвращает случайный URL сервера API AI Uncensored.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `str`: Случайный URL сервера.

**Как работает функция**:
- Содержит список URL серверов AI Uncensored.
- Выбирает случайный URL из списка и возвращает его.


### Классы

#### `AIUncensored`

**Описание**: Класс, реализующий асинхронный генератор для взаимодействия с AI Uncensored.
**Наследует**: 
    - `AsyncGeneratorProvider`: Интерфейс для асинхронных генераторов.
    - `ProviderModelMixin`: Класс для управления моделями.

**Атрибуты**:
- `url`: Базовый URL API.
- `api_key`: API-ключ для аутентификации.
- `working`: Флаг, указывающий на работоспособность провайдера (по умолчанию `False`).
- `supports_stream`: Флаг, указывающий на поддержку потоковой передачи (по умолчанию `True`).
- `supports_system_message`: Флаг, указывающий на поддержку системных сообщений (по умолчанию `True`).
- `supports_message_history`: Флаг, указывающий на поддержку истории сообщений (по умолчанию `True`).
- `default_model`: Имя модели по умолчанию (по умолчанию `"hermes3-70b"`).
- `models`: Список поддерживаемых моделей.
- `model_aliases`: Словарь для преобразования псевдонимов моделей в реальные имена.

**Методы**:
- `create_async_generator`: Метод для создания асинхронного генератора.

**Пример**:

```python
# Создание инстанса класса AIUncensored
ai_uncensored = AIUncensored()

# Создание асинхронного генератора
async_generator = await ai_uncensored.create_async_generator(model="hermes3-70b", messages=["Привет, как дела?"])

# Итерация по результатам генератора
async for response in async_generator:
    print(response)
```

#### `create_async_generator`

**Назначение**: Метод для создания асинхронного генератора для модели AI Uncensored.

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Сообщения для отправки в модель.
- `stream` (bool): Флаг, указывающий на поддержку потоковой передачи (по умолчанию `False`).
- `proxy` (str): Прокси-сервер для запросов (по умолчанию `None`).
- `api_key` (str): API-ключ для аутентификации (по умолчанию `None`).
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Объект с результатами генерации.

**Как работает функция**:
- Получает имя модели.
- Формирует JSON-объект с данными запроса.
- Вычисляет сигнатуру запроса.
- Отправляет POST-запрос к API AI Uncensored.
- Обрабатывает ответ, генерируя частичные результаты в виде асинхронного потока.
- Возвращает объект `AsyncResult` с результатами генерации.

**Примеры**:

```python
# Создание асинхронного генератора для модели hermes3-70b
async_generator = await AIUncensored.create_async_generator(model="hermes3-70b", messages=["Привет, как дела?"])

# Создание асинхронного генератора для модели hermes3-70b с использованием прокси-сервера
async_generator = await AIUncensored.create_async_generator(model="hermes3-70b", messages=["Привет, как дела?"], proxy="http://proxy.example.com:8080")

# Создание асинхронного генератора с потоковой передачей данных
async_generator = await AIUncensored.create_async_generator(model="hermes3-70b", messages=["Привет, как дела?"], stream=True)