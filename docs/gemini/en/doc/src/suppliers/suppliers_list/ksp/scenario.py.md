# Модуль сбора товаров со страницы категорий поставщика hb.co.il

## Обзор

Этот модуль предназначен для сбора товаров со страниц категорий поставщика `hb.co.il` с помощью вебдрайвера. Он содержит функции для получения списка категорий, товаров в категориях и обработки страниц товаров.

## Подробности

Модуль реализует следующие функции:

- `get_list_categories_from_site(s)`: Собирает актуальные категории с сайта,  затем возвращает список категорий.
- `get_list_products_in_category(s)`: Собирает список URL-адресов товаров со страницы категории. Если на странице есть пагинация, функция пролистывает все страницы и собирает товары со всех страниц.
- `paginator(d, locator, list_products_in_category)`: Функция пагинации, реализующая переключение на следующую страницу категории.
- `grab_product_page()`: Функция обработки страницы товара. Эта функция извлекает данные о товаре, передает их в класс `Product`, а затем возвращает объект `Product` с собранными данными.

## Классы

### `Supplier`

**Описание**: Класс `Supplier` представляет поставщика.

**Атрибуты**:

- `driver`: Экземпляр `Driver` для взаимодействия с веб-браузером.
- `locators`: Словарь, содержащий локаторы для элементов на странице поставщика.
- `current_scenario`: Текущий сценарий, который выполняется.

## Функции

### `get_list_products_in_category(s)`

**Цель**: Возвращает список URL-адресов товаров со страницы категории.

**Параметры**:

- `s` (`Supplier`): Экземпляр класса `Supplier`, содержащий информацию о поставщике и драйвере.

**Возвращает**:

- `list[str, str, None]`: Список URL-адресов товаров или `None`, если товары не найдены.

**Описание**:

- Эта функция получает список товаров со страницы категории, используя вебдрайвер и локаторы.
- Она использует `d.execute_locator(l['product_links'])`, чтобы получить список ссылок на товары.
- Функция также реализует пагинацию, если на странице категории есть пагинация.
- Если товаров на странице нет, возвращает `None`.

### `paginator(d, locator, list_products_in_category)`

**Цель**: Функция пагинации, реализующая переключение на следующую страницу категории.

**Параметры**:

- `d` (`Driver`): Экземпляр класса `Driver`, отвечающий за работу с веб-браузером.
- `locator` (`dict`): Словарь, содержащий локаторы для элементов на странице.
- `list_products_in_category` (`list`): Список URL-адресов товаров.

**Возвращает**:

- `bool`: `True`, если пагинация выполнена успешно, и `False`, если пагинация невозможна.

**Описание**:

- Эта функция проверяет наличие кнопки пагинации на странице и, если она есть, переходит на следующую страницу.
- Она использует `d.execute_locator(locator['pagination']['<-\'])`, чтобы проверить наличие кнопки пагинации и перейти на следующую страницу.
- Если пагинация невозможна, функция возвращает `False`.

### `get_list_categories_from_site(s)`

**Цель**: Собирает актуальные категории с сайта,  затем возвращает список категорий.

**Параметры**:

- `s` (`Supplier`): Экземпляр класса `Supplier`, содержащий информацию о поставщике и драйвере.

**Возвращает**:

- `list`: Список категорий с сайта.

**Описание**:

- Функция использует вебдрайвер для сбора списка категорий с сайта поставщика.
- Внутри функции используется метод `d.execute_locator()`, чтобы получить список категорий с сайта.
-  Функция обрабатывает ошибки, которые могут возникнуть при сборе категорий.
-  В конце функция возвращает собранный список категорий.

## Примеры

```python
# Создание экземпляра класса Supplier
supplier = Supplier(driver=Driver(Chrome), locators={'category': {'product_links': {'by': 'XPATH', 'selector': '//a[@class="product-name"]', 'if_list': 'all', 'timeout': 10}}, 'pagination': {'<-\': {'by': 'XPATH', 'selector': '//button[@class="button"]', 'if_list': 'first', 'timeout': 10}}}, current_scenario={'name': 'some_category_name'})

# Получение списка товаров
list_products = get_list_products_in_category(supplier)
# Проверка, найдены ли товары
if list_products:
    print(f'Найдено {len(list_products)} товаров')
    for product_url in list_products:
        print(f'URL товара: {product_url}')

# Получение списка категорий
list_categories = get_list_categories_from_site(supplier)
# Проверка, найдены ли категории
if list_categories:
    print(f'Найдено {len(list_categories)} категорий')
    for category_name in list_categories:
        print(f'Название категории: {category_name}')

# Проверка пагинации
paginator(supplier.driver, supplier.locators['category'], list_products_in_category)
```