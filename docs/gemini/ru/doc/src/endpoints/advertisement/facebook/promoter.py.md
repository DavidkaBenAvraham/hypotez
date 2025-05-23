# Модуль для продвижения товаров и событий в Facebook

## Обзор

Модуль `src/endpoints/advertisement/facebook/promoter.py` реализует функциональность для автоматизированного продвижения товаров и событий AliExpress в группах Facebook. Он обеспечивает обработку кампаний и событий, публикуя их в группах Facebook, избегая дублирования промо-материалов. 

## Подробнее

### **Проверка и обновление данных групп Facebook**

Модуль `src/endpoints/advertisement/facebook/promoter.py` работает с файлами, содержащими данные о группах Facebook, хранящимися в папке `google_drive/facebook/groups`. Файлы содержат информацию о каждой группе, включая URL группы, категорию, язык, валюту, а также историю опубликованных материалов (событий и товаров).

### **Промо-кампании и события**

В рамках модуля `src/endpoints/advertisement/facebook/promoter.py` реализованы функции для:

- **Обработки кампаний:** Промо-кампании AliExpress, содержащие информацию о товарах, которые необходимо продвигать в группах.
- **Обработки событий:** События AliExpress, которые также могут быть опубликованы в группах.

### **Настройка и использование**

Модуль `src/endpoints/advertisement/facebook/promoter.py` работает с объектом `Driver`, который представляет собой вебдрайвер (например, Chrome, Firefox, Playwright), используемый для автоматизации действий в браузере. 

## Классы

### `class FacebookPromoter`

**Описание**: Класс `FacebookPromoter` реализует логику продвижения товаров и событий в группах Facebook.

**Наследует**: 

**Атрибуты**:

- `d (Driver)`: Объект WebDriver, используемый для автоматизации действий в браузере.
- `group_file_paths (list[str | Path] | str | Path)`: Список путей к файлам, содержащим данные о группах.
- `no_video (bool)`: Флаг, указывающий на необходимость отключения видео в постах.
- `promoter (str)`: Имя промоутера.

**Методы**:

#### `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

**Назначение**: Инициализирует объект `FacebookPromoter`.

**Параметры**:

- `d (Driver)`: Объект WebDriver для автоматизации действий в браузере.
- `group_file_paths (list[str | Path] | str | Path)`: Список путей к файлам, содержащим данные о группах.
- `no_video (bool, optional)`: Флаг для отключения видео в постах. По умолчанию `False`.

#### `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

**Назначение**: Продвигает товар или событие в группе Facebook.

**Параметры**:

- `group (SimpleNamespace)`: Объект, содержащий информацию о группе.
- `item (SimpleNamespace)`: Объект, содержащий информацию о товаре или событии.
- `is_event (bool, optional)`: Флаг, указывающий на то, что `item` является событием. По умолчанию `False`.
- `language (str, optional)`: Язык группы. По умолчанию `None`.
- `currency (str, optional)`: Валюта группы. По умолчанию `None`.

**Возвращает**:

- `bool`: `True` если промо-материал был успешно опубликован, `False` в противном случае.

**Как работает функция**:

- Проверяет, что язык и валюта группы совпадают с языком и валютой товара или события.
- Вызывает функцию `post_message` или `post_event` для публикации товара или события в группе.
- Обновляет данные группы о последних опубликованных промо-материалах.

#### `log_promotion_error(self, is_event: bool, item_name: str)`

**Назначение**: Логирует ошибку при публикации товара или события.

**Параметры**:

- `is_event (bool)`: Флаг, указывающий на то, что `item_name` - это название события.
- `item_name (str)`: Название товара или события.

#### `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

**Назначение**: Обновляет данные о последнем опубликованном товаре или событии в группе.

**Параметры**:

- `group (SimpleNamespace)`: Объект, содержащий информацию о группе.
- `item_name (str)`: Название товара или события.
- `is_event (bool, optional)`: Флаг, указывающий на то, что `item_name` - это название события. По умолчанию `False`.

#### `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = [\'sales\'], language: str = None, currency: str = None)`

**Назначение**: Обрабатывает список групп Facebook для публикации товаров или событий.

**Параметры**:

- `campaign_name (str, optional)`: Название кампании. По умолчанию `None`.
- `events (list[SimpleNamespace], optional)`: Список событий для публикации. По умолчанию `None`.
- `is_event (bool, optional)`: Флаг, указывающий на то, что необходимо публиковать события. По умолчанию `False`.
- `group_file_paths (list[str], optional)`: Список путей к файлам с данными о группах. По умолчанию `None`.
- `group_categories_to_adv (list[str], optional)`: Список категорий, которые необходимо продвигать. По умолчанию `['sales']`.
- `language (str, optional)`: Язык группы. По умолчанию `None`.
- `currency (str, optional)`: Валюта группы. По умолчанию `None`.

**Как работает функция**:

- Проверяет, что есть данные для публикации (название кампании или список событий).
- Перебирает файлы с данными о группах.
- Для каждой группы проверяет соответствие категории, языка и валюты.
- Если группа подходит, то вызывает функцию `promote` для публикации товара или события.
- Обновляет данные группы о последних опубликованных промо-материалах.
- Выполняет паузу между публикациями.

#### `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

**Назначение**: Возвращает объект товара для публикации в группе.

**Параметры**:

- `campaign_name (str)`: Название кампании.
- `group (SimpleNamespace)`: Объект, содержащий информацию о группе.
- `language (str)`: Язык группы.
- `currency (str)`: Валюта группы.

**Возвращает**:

- `SimpleNamespace`: Объект, содержащий информацию о товаре.

**Как работает функция**:

- В зависимости от промоутера (aliexpress или другой) получает информацию о товарах из соответствующего источника данных.
- Выбирает случайный товар из списка доступных товаров.
- Возвращает объект, содержащий информацию о товаре.

#### `check_interval(self, group: SimpleNamespace) -> bool`

**Назначение**: Проверяет, достаточно ли времени прошло с момента последней публикации в группе.

**Параметры**:

- `group (SimpleNamespace)`: Объект, содержащий информацию о группе.

**Возвращает**:

- `bool`: `True` если достаточно времени прошло, `False` в противном случае.

#### `validate_group(self, group: SimpleNamespace) -> bool`

**Назначение**: Проверяет правильность данных о группе.

**Параметры**:

- `group (SimpleNamespace)`: Объект, содержащий информацию о группе.

**Возвращает**:

- `bool`: `True` если данные о группе правильные, `False` в противном случае.

## Функции

### `get_event_url(group_url: str) -> str`

**Назначение**: Формирует URL для создания события в группе Facebook.

**Параметры**:

- `group_url (str)`: URL группы Facebook.

**Возвращает**:

- `str`: URL для создания события.

**Как работает функция**:

- Извлекает идентификатор группы из URL.
- Формирует URL для создания события, используя идентификатор группы и другие необходимые параметры.
- Возвращает сформированный URL.

## Примеры

```python
# Создание объекта промоутера
promoter = FacebookPromoter(d=Driver(Chrome), promoter='aliexpress')

# Промоутер для событий
events = [
    {
        'name': 'Событие 1',
        'language': {
            'ru': 'Событие 1'
        },
        'start': datetime.now(),
        'end': datetime.now() + timedelta(days=7),
        'promotional_link': 'https://aliexpress.com/event1'
    },
    {
        'name': 'Событие 2',
        'language': {
            'ru': 'Событие 2'
        },
        'start': datetime.now(),
        'end': datetime.now() + timedelta(days=14),
        'promotional_link': 'https://aliexpress.com/event2'
    }
]
promoter.process_groups(events=events, is_event=True)

# Промоутер для товаров
promoter.process_groups(campaign_name='Winter Sale', language='ru', currency='RUB')
```

## Твое поведение при анализе кода:

- Внутри кода ты можешь встретить выражение между `<` `>`. Например: <инструкция для модели gemini:Загрузка описаний продуктов в PrestaShop.>, <далее, если есть>. Это заготовки, куда ты вставляешь релевантное значение
- Всегда смотри системную инструкцию для обработки кода проекта `hypotez`;
- Анализируй расположение файла в проекте. Это поможет понять его назначение и взаимосвязь с другими файлами. Расположение файла ты найдешь в самой превой строке кода, начинающейся с `## \\file /...`;
- Запоминай предоставленный код и анализируй его связь с другими частями проекта;
- В этой инструкции не надо предлагать улучшение кода. Четко следуй пункту 5. **Пример файла** при составлении ответа