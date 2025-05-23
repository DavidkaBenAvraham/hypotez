# AliExpress API Wrapper

## Обзор

Этот модуль представляет собой обертку для API AliExpress Open Platform, которая позволяет получать информацию о продуктах и партнерские ссылки AliExpress с использованием официального API. 

## Подробнее

Модуль `api` предоставляет набор классов и функций для взаимодействия с AliExpress API. Он позволяет:

- Получать информацию о продуктах: 
    - `retrieve_product_details` - получить подробную информацию о продуктах по их ID или ссылкам.
    - `get_hotproducts` - поиск продуктов с высокими комиссионными.
- Генерировать партнерские ссылки:
    - `get_affiliate_links` - конвертировать ссылки в партнерские ссылки.
- Работать с категориями:
    - `get_categories` - получить список всех категорий.
    - `get_parent_categories` - получить список всех родительских категорий.
    - `get_child_categories` - получить список всех дочерних категорий для определенной родительской категории.

## Классы

### `AliexpressApi`

**Описание**: Класс `AliexpressApi` является основным классом для взаимодействия с API AliExpress.

**Наследует**: 
    - Не наследует

**Атрибуты**:
- `_key` (str): Ваш API-ключ.
- `_secret` (str): Ваш API-секрет.
- `_tracking_id` (str): Идентификатор отслеживания для генератора ссылок. 
- `_language` (model_Language): Языковой код. 
- `_currency` (model_Currency): Код валюты. 
- `_app_signature` (str): Подпись приложения. 
- `categories` (list): Список категорий, доступных для вашего API-ключа. 

**Методы**:

- `retrieve_product_details()`: Получает информацию о продуктах по их ID или ссылкам.
- `get_affiliate_links()`: Конвертирует ссылки в партнерские ссылки.
- `get_hotproducts()`: Поиск продуктов с высокими комиссионными.
- `get_categories()`: Получает список всех категорий.
- `get_parent_categories()`: Получает список всех родительских категорий.
- `get_child_categories()`: Получает список всех дочерних категорий для определенной родительской категории.

#### `retrieve_product_details()`

**Назначение**: Функция `retrieve_product_details()` получает информацию о продуктах по их ID или ссылкам.

**Параметры**:

- `product_ids` (`str | list[str]`): Один или несколько идентификаторов продуктов или ссылок.
- `fields` (`str | list[str]`): Поля, которые должны быть включены в результат. По умолчанию - все поля.
- `country` (`str`): Страна для фильтрации продуктов. Возвращает цену в соответствии с налоговой политикой страны.

**Возвращает**:

- `list[model_Product]`: Список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`: Если продукты с указанными параметрами не найдены.
- `InvalidArgumentException`: Если переданные аргументы неверны.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция преобразует входные данные `product_ids` в список строк, если это не список.
2. Создает объект `AliexpressAffiliateProductdetailGetRequest` с необходимыми параметрами (ключ, секрет, идентификатор отслеживания, язык, валюта, список продуктов, поля, страна).
3. Выполняет запрос к API с использованием функции `api_request` и обрабатывает ответ.
4. Если в ответе есть данные, то функция парсит их и возвращает список объектов `model_Product`.
5. Если данных нет, то функция выводит предупреждение в лог.

**Примеры**:

```python
# Получение информации о продукте по его ID
product_details = api.retrieve_product_details(product_ids='100000000000000000')

# Получение информации о продуктах по списку ID
product_details = api.retrieve_product_details(product_ids=['100000000000000000', '100000000000000001'])

# Получение информации о продукте по ссылке
product_details = api.retrieve_product_details(product_ids='https://www.aliexpress.com/item/100000000000000000.html')

# Получение информации о продуктах по списку ссылок
product_details = api.retrieve_product_details(product_ids=['https://www.aliexpress.com/item/100000000000000000.html', 'https://www.aliexpress.com/item/100000000000000001.html'])
```

#### `get_affiliate_links()`

**Назначение**: Функция `get_affiliate_links()` конвертирует ссылки в партнерские ссылки AliExpress.

**Параметры**:

- `links` (`str | list[str]`): Один или несколько идентификаторов продуктов или ссылок.
- `link_type` (`model_LinkType`): Тип партнерской ссылки. По умолчанию - `model_LinkType.NORMAL`.

**Возвращает**:

- `list[model_AffiliateLink]`: Список партнерских ссылок.

**Вызывает исключения**:

- `InvalidArgumentException`: Если переданные аргументы неверны.
- `InvalidTrackingIdException`: Если идентификатор отслеживания не задан.
- `ProductsNotFoudException`: Если продукты с указанными параметрами не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция проверяет, задан ли идентификатор отслеживания. 
2. Преобразует входные данные `links` в список строк, если это не список.
3. Создает объект `AliexpressAffiliateLinkGenerateRequest` с необходимыми параметрами (ключ, секрет, идентификатор отслеживания, язык, валюта, список ссылок, тип ссылки).
4. Выполняет запрос к API с использованием функции `api_request` и обрабатывает ответ.
5. Если в ответе есть данные, то функция возвращает список объектов `model_AffiliateLink`.
6. Если данных нет, то функция выводит предупреждение в лог.

**Примеры**:

```python
# Конвертирование ссылки в партнерскую ссылку
affiliate_links = api.get_affiliate_links(links='https://www.aliexpress.com/item/100000000000000000.html')

# Конвертирование списка ссылок в партнерские ссылки
affiliate_links = api.get_affiliate_links(links=['https://www.aliexpress.com/item/100000000000000000.html', 'https://www.aliexpress.com/item/100000000000000001.html'])

# Конвертирование ссылок в партнерские ссылки с использованием горячей комиссии
affiliate_links = api.get_affiliate_links(links='https://www.aliexpress.com/item/100000000000000000.html', link_type=model_LinkType.HOTLINK)
```

#### `get_hotproducts()`

**Назначение**: Функция `get_hotproducts()` позволяет получить список продуктов с высокими комиссионными.

**Параметры**:

- `category_ids` (`str | list[str]`): Один или несколько идентификаторов категорий.
- `delivery_days` (`int`): Предполагаемое время доставки.
- `fields` (`str | list[str]`): Поля, которые должны быть включены в результат. По умолчанию - все поля.
- `keywords` (`str`): Ключевые слова для поиска продуктов.
- `max_sale_price` (`int`): Максимальная цена для фильтрации продуктов.
- `min_sale_price` (`int`): Минимальная цена для фильтрации продуктов.
- `page_no` (`int`): Номер страницы.
- `page_size` (`int`): Количество продуктов на странице.
- `platform_product_type` (`model_ProductType`): Тип продукта на платформе.
- `ship_to_country` (`str`): Страна для фильтрации продуктов. 
- `sort` (`model_SortBy`): Метод сортировки.

**Возвращает**:

- `model_HotProductsResponse`: Объект, содержащий информацию об ответе и список продуктов.

**Вызывает исключения**:

- `ProductsNotFoudException`: Если продукты с указанными параметрами не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция создает объект `AliexpressAffiliateHotproductQueryRequest` с необходимыми параметрами.
2. Выполняет запрос к API с использованием функции `api_request` и обрабатывает ответ.
3. Если в ответе есть данные, то функция возвращает объект `model_HotProductsResponse`, который содержит информацию об ответе и список продуктов.
4. Если данных нет, то функция выводит предупреждение в лог.

**Примеры**:

```python
# Получение горячих продуктов по категории
hot_products = api.get_hotproducts(category_ids='100000000000000000')

# Получение горячих продуктов по ключевым словам
hot_products = api.get_hotproducts(keywords='dress')

# Получение горячих продуктов по категории и цене
hot_products = api.get_hotproducts(category_ids='100000000000000000', min_sale_price=1000, max_sale_price=10000)
```

#### `get_categories()`

**Назначение**: Функция `get_categories()` получает список всех категорий.

**Параметры**:

- `**kwargs` (dict): Дополнительные параметры запроса.

**Возвращает**:

- `list[model_Category | model_ChildCategory]`: Список категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция создает объект `AliexpressAffiliateCategoryGetRequest` с необходимыми параметрами (ключ, секрет, идентификатор отслеживания, язык, валюта).
2. Выполняет запрос к API с использованием функции `api_request` и обрабатывает ответ.
3. Если в ответе есть данные, то функция возвращает список объектов `model_Category | model_ChildCategory`.
4. Если данных нет, то функция выводит предупреждение в лог.

**Примеры**:

```python
# Получение списка всех категорий
categories = api.get_categories()
```

#### `get_parent_categories()`

**Назначение**: Функция `get_parent_categories()` получает список всех родительских категорий.

**Параметры**:

- `use_cache` (`bool`): Использовать кэшированные категории для сокращения количества запросов к API. 

**Возвращает**:

- `list[model_Category]`: Список родительских категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция проверяет, есть ли в кэше список категорий. Если нет, то вызывает функцию `get_categories()`, чтобы получить их.
2. Фильтрует список категорий, оставляя только родительские категории.
3. Возвращает отфильтрованный список категорий.

**Примеры**:

```python
# Получение списка всех родительских категорий
parent_categories = api.get_parent_categories()
```

#### `get_child_categories()`

**Назначение**: Функция `get_child_categories()` получает список всех дочерних категорий для определенной родительской категории.

**Параметры**:

- `parent_category_id` (`int`): Идентификатор родительской категории.
- `use_cache` (`bool`): Использовать кэшированные категории для сокращения количества запросов к API. 

**Возвращает**:

- `list[model_ChildCategory]`: Список дочерних категорий.

**Вызывает исключения**:

- `CategoriesNotFoudException`: Если категории не найдены.
- `ApiRequestException`: Если произошла ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если ответ от API некорректный.

**Как работает**:

1. Функция проверяет, есть ли в кэше список категорий. Если нет, то вызывает функцию `get_categories()`, чтобы получить их.
2. Фильтрует список категорий, оставляя только дочерние категории для заданного `parent_category_id`.
3. Возвращает отфильтрованный список категорий.

**Примеры**:

```python
# Получение списка дочерних категорий для родительской категории с ID 100000000000000000
child_categories = api.get_child_categories(parent_category_id=100000000000000000)