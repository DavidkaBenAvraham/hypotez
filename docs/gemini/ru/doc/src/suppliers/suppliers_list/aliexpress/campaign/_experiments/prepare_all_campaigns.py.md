# Модуль `prepare_all_campaigns`

## Обзор

Модуль `prepare_all_campaigns` предназначен для запуска всех рекламных кампаний для различных языков, с поиском названий категорий из директорий.

## Подробнее

Модуль `prepare_all_campaigns` запускает обработку всех рекламных кампаний для различных языков. 
Он использует функцию `process_all_campaigns` из модуля `prepare_campaigns`, которая в свою очередь использует функцию `main_process`.

## Функции

### `process_all_campaigns`

**Назначение**: Запускает обработку всех рекламных кампаний для всех языков.

**Параметры**:

- `locales` (dict): Словарь, содержащий информацию о валютах для каждого языка.

**Возвращает**: 

- `None`: Не возвращает значение.

**Как работает**:

- Функция `process_all_campaigns` принимает словарь `locales`, который содержит информацию о валютах для каждого языка.
- Она циклически перебирает языки из словаря `locales` и запускает обработку рекламных кампаний для каждого языка.
- Обработка рекламных кампаний для каждого языка выполняется функцией `main_process`.

**Примеры**:

```python
# Пример вызова функции
locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
process_all_campaigns(locales)
```

### `main_process`

**Назначение**: Запускает обработку рекламных кампаний для заданного бренда и списка категорий.

**Параметры**:

- `brand` (str): Название бренда.
- `categories` (list): Список категорий.

**Возвращает**: 

- `None`: Не возвращает значение.

**Как работает**:

- Функция `main_process` принимает название бренда и список категорий.
- Она циклически перебирает категории из списка `categories` и запускает обработку рекламных кампаний для каждой категории.
- Обработка рекламных кампаний для каждой категории выполняется функцией `process_campaigns`.

**Примеры**:

```python
# Пример вызова функции
main_process('mrgreen', ['category1', 'category2', 'category3'])
```

## Примеры

```python
# Пример использования модуля
from src.suppliers.suppliers_list.aliexpress.campaign.prepare_campaigns import process_all_campaigns, main_process

locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
campaign_name:str = 'rc'
language: str = 'EN'
currency: str = 'USD'
campaign_file:str = None

# Запуск обработки всех рекламных кампаний
process_all_campaigns(locales)

# Запуск обработки рекламных кампаний для бренда 'mrgreen'
main_process('brands', ['mrgreen'])
```