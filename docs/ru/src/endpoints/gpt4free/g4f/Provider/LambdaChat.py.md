# Документация модуля LambdaChat

## Обзор

Модуль `LambdaChat` предоставляет класс для взаимодействия с чат-моделью Lambda Chat. Он наследует функциональность от класса `HuggingChat` и специализируется на работе с конкретным доменным именем `lambda.chat`. В модуле определены параметры для подключения к чат-модели, включая используемые модели, альтернативные модели и псевдонимы моделей.

## Подробней

Модуль `LambdaChat` предназначен для упрощения интеграции с чат-моделью Lambda Chat в проекте `hypotez`. Он предоставляет готовые настройки для подключения к сервису, такие как доменное имя и список поддерживаемых моделей. Класс `LambdaChat` наследует функциональность от `HuggingChat`, что позволяет повторно использовать общую логику для взаимодействия с чат-моделями.

## Классы

### `LambdaChat`

**Описание**: Класс для взаимодействия с чат-моделью Lambda Chat.

**Наследует**: `HuggingChat`

**Атрибуты**:

- `label` (str): Метка для данного провайдера чат-модели, значение `"Lambda Chat"`.
- `domain` (str): Доменное имя чат-сервиса, значение `"lambda.chat"`.
- `origin` (str): Полный URL домена, используемый для формирования URL-адресов, значение `"https://lambda.chat"`.
- `url` (str): URL чат-сервиса, значение `"https://lambda.chat"`.
- `working` (bool): Флаг, указывающий, что данный провайдер в настоящее время работает, значение `True`.
- `use_nodriver` (bool): Флаг, определяющий необходимость использования веб-драйвера, значение `False`.
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации для использования данного провайдера, значение `False`.
- `default_model` (str): Модель, используемая по умолчанию, значение `"deepseek-llama3.3-70b"`.
- `reasoning_model` (str): Модель, используемая для логических рассуждений, значение `"deepseek-r1"`.
- `image_models` (list[str]): Список моделей, поддерживающих обработку изображений (в данном случае пустой).
- `fallback_models` (list[str]): Список альтернативных моделей для использования в случае недоступности основной модели.
- `models` (list[str]): Копия списка `fallback_models`, используемая для хранения доступных моделей.
- `model_aliases` (dict[str, str]): Словарь, содержащий псевдонимы для различных моделей.

**Принцип работы**:

Класс `LambdaChat` наследует от класса `HuggingChat` и переопределяет некоторые атрибуты, чтобы настроить взаимодействие с конкретной чат-моделью Lambda Chat. Он определяет доменное имя, URL, используемые модели и другие параметры, необходимые для подключения и работы с сервисом.

## Методы класса

В данном классе не определены собственные методы, кроме переопределения атрибутов. Однако, класс наследует методы от `HuggingChat`.

## Параметры класса

- `label` (str): Метка для данного провайдера чат-модели.
- `domain` (str): Доменное имя чат-сервиса.
- `origin` (str): Полный URL домена.
- `url` (str): URL чат-сервиса.
- `working` (bool): Флаг, указывающий, что данный провайдер в настоящее время работает.
- `use_nodriver` (bool): Флаг, определяющий необходимость использования веб-драйвера.
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации для использования данного провайдера.
- `default_model` (str): Модель, используемая по умолчанию.
- `reasoning_model` (str): Модель, используемая для логических рассуждений.
- `image_models` (list[str]): Список моделей, поддерживающих обработку изображений.
- `fallback_models` (list[str]): Список альтернативных моделей.
- `models` (list[str]): Список доступных моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

## Примеры

```python
from src.endpoints.gpt4free.g4f.Provider.LambdaChat import LambdaChat

# Создание экземпляра класса LambdaChat
lambda_chat = LambdaChat()

# Вывод информации о провайдере
print(f"Провайдер: {lambda_chat.label}")
print(f"Домен: {lambda_chat.domain}")
print(f"URL: {lambda_chat.url}")
print(f"Модель по умолчанию: {lambda_chat.default_model}")
print(f"Альтернативные модели: {lambda_chat.fallback_models}")