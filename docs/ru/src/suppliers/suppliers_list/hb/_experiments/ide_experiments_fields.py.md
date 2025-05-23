# src.suppliers.hb._experiments.ide_experiments_fields

## Обзор

Модуль предназначен для извлечения и обработки данных о товарах с веб-страниц поставщика HB (hbdeadsea.co.il) с целью их дальнейшей загрузки или обновления в PrestaShop. Он содержит функции для сбора информации о товаре, такой как название, описание, цена, состав, и другие характеристики, а также для нормализации и форматирования этих данных.

## Подробней

Этот модуль является частью процесса интеграции данных о товарах от поставщика HB в систему PrestaShop. Он использует Selenium WebDriver для навигации по сайту поставщика, извлечения данных о товарах и приведения этих данных к формату, совместимому с API PrestaShop.  Модуль содержит различные функции для сбора и обработки данных, специфичные для структуры веб-сайта HB. Он также включает функции для нормализации данных, такие как удаление лишних символов из цен и форматирование текста.

Модуль предназначен для автоматизации процесса сбора данных о товарах и их загрузки в PrestaShop, уменьшая необходимость ручного ввода данных и повышая точность данных.

## Классы

### `ProductFields`

**Описание**: Класс предназначен для хранения и управления полями товара.

**Наследует**: Нет

**Атрибуты**:

- `s`: Объект класса `Supplier`, представляющий поставщика товара.
- `presta_fields_dict`: Словарь, содержащий поля товара, предназначенные для PrestaShop.
- `assist_fields_dict`: Словарь, содержащий вспомогательные поля товара.

**Методы**:

- Нет явно определенных методов, но используются атрибуты для хранения полей товара.

### `Supplier`

**Описание**: Класс, представляющий поставщика товаров.

**Наследует**: Нет

**Атрибуты**:

- `supplier_prefix` (str): Префикс поставщика.
- `supplier_id` (int): ID поставщика.
- `driver`:  Драйвер для управления браузером.
- `locators`: Локаторы для поиска элементов на странице.
- `related_modules`: Связанные модули для работы с поставщиком.

**Методы**:

- Нет явно определенных методов, но используются атрибуты для хранения информации о поставщике.

### `Product`

**Описание**: Класс, представляющий товар.

**Наследует**: Нет

**Атрибуты**:

- `s`: Объект класса `Supplier`, представляющий поставщика товара.
- `presta_fields_dict`: Словарь, содержащий поля товара, предназначенные для PrestaShop.
- `assist_fields_dict`: Словарь, содержащий вспомогательные поля товара.

**Методы**:

- Нет явно определенных методов, но используются атрибуты для хранения полей товара.

## Функции

### `grab_product_page`

```python
def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields:
    """ Собираю со страницы товара значения вебэлементов и привожу их к полям ProductFields

    Args:
        supplier (Supplier): Класс поставщика. Вебдрайвер должен быть установлен на странице товара.
        async_run (bool, optional):  По умолчанию `True`.

    Returns:
        ProductFields:  Заполненный объект `ProductFields` с данными о товаре.

    """
```

**Назначение**: Извлекает данные о товаре со страницы товара и преобразует их в поля `ProductFields`.

**Параметры**:

- `supplier` (Supplier): Объект класса `Supplier`, представляющий поставщика товара. Веб-драйвер должен быть инициализирован и находиться на странице товара.
- `async_run` (bool, optional): Указывает, следует ли выполнять операции асинхронно. По умолчанию `True`.

**Возвращает**:

- `ProductFields`: Объект класса `ProductFields`, заполненный данными, извлеченными со страницы товара.

**Как работает функция**:

1.  Инициализирует глобальные переменные `s` (Supplier), `p` (Product), `f` (ProductFields), `d` (driver) и `l` (locators).
2.  Закрывает всплывающий баннер, если он отображается на странице.
3.  Прокручивает страницу товара, чтобы загрузить все элементы, подгружаемые через AJAX.
4.  Вызывает внутренние функции, специфичные для данного поставщика, для извлечения определенных полей товара:

    *   `product_reference_and_volume_and_price_for_100()`: Извлекает объем, артикул поставщика и цену за единицу товара.
    *   `set_references(f, s)`: Устанавливает идентификаторы товара, такие как `id_supplier` и `reference`.
5.  Вызывает ряд функций `field_*()` для извлечения других полей товара, таких как `additional_shipping_cost`, `affiliate_short_link`, `available_for_order`, `condition`, `description`, `how_to_use`, `id_category_default`, `id_manufacturer`, `ingredients`, `name`, `link_rewrite`, `on_sale`, `price` и `visibility`.
6.  Извлекает URL изображений товара.
7.  Возвращает объект `ProductFields`, заполненный извлеченными данными.

**Внутренние функции**:

### `product_reference_and_volume_and_price_for_100`

```python
def product_reference_and_volume_and_price_for_100():
    """ Функция вытаскивает 3 поля:
       - volume,
       - supplier_reference,
       - цена за единицу товара
       @todo Реализовать поле `цена за единицу товара`"""
    global f, s
    webelements: List[WebElement] = d.execute_locator(l["product_reference_and_volume_and_price_for_100"])
    for webelement in webelements:
        if ('Fl.oz' and 'מ"ל') in webelement.text:
            """ объем """
            f.volume = webelement.text
        elif str(r'מחיר ל100 מ"ל') in webelement.text:
            """ цена за единицу товара
            @todo придумать куда
            """
            print(f'цена за единицу товара:{webelement.text}')
        elif 'מקט' in webelement.text:
            f.supplier_reference = StringNormalizer.get_numbers_only(webelement.text)
        ...
    ...
```

**Назначение**: Извлекает информацию об объеме, артикуле поставщика и цене за единицу товара из веб-элементов на странице товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `f` (ProductFields), `s` (Supplier) и `d` (driver).

**Возвращает**:

- Нет явного возвращаемого значения. Обновляет поля объекта `f` (ProductFields) напрямую.

**Как работает функция**:

1.  Получает список веб-элементов, соответствующих локатору `l["product_reference_and_volume_and_price_for_100"]`.
2.  Перебирает веб-элементы и извлекает информацию в зависимости от содержимого текста веб-элемента:

    *   Если текст содержит `'Fl.oz'` и `'מ"ל'`, извлекает объем товара.
    *   Если текст содержит `str(r'מחיר ל100 מ"ל')`, извлекает цену за единицу товара (TODO: определить, куда сохранять это значение).
    *   Если текст содержит `'מקט'`, извлекает артикул поставщика, используя `StringNormalizer.get_numbers_only()` для получения только числовых значений.

### `set_references`

```python
def set_references(f, s):
    """ все, что касается id товара """
    # f.supplier_reference = field_supplier_reference()
    f.id_supplier = int(s.supplier_id)
    f.reference = f'{s.supplier_id}-{f.supplier_reference}'
```

**Назначение**: Устанавливает значения для полей, связанных с идентификацией товара, таких как `id_supplier` и `reference`.

**Параметры**:

- `f` (ProductFields): Объект класса `ProductFields`, который необходимо обновить.
- `s` (Supplier): Объект класса `Supplier`, содержащий информацию о поставщике.

**Возвращает**:

- Нет явного возвращаемого значения. Обновляет поля объекта `f` (ProductFields) напрямую.

**Как работает функция**:

1.  Устанавливает значение поля `id_supplier` равным `s.supplier_id` (ID поставщика).
2.  Формирует значение поля `reference` как комбинацию `s.supplier_id` и `f.supplier_reference` (артикул поставщика) в формате `'{s.supplier_id}-{f.supplier_reference}'`.

### `field_additional_shipping_cost`

```python
def field_additional_shipping_cost():
    """

    стоимость доставки
    @details
    """
    return d.execute_locator(l["additional_shipping_cost"])
    ...
```

**Назначение**: Извлекает стоимость доставки товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["additional_shipping_cost"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["additional_shipping_cost"])` для получения стоимости доставки с веб-страницы.

### `field_delivery_in_stock`

```python
def field_delivery_in_stock():
    """

    Доставка, когда товар в наличии
    @details
    """
    return str(d.execute_locator(l["delivery_in_stock"]))
    ...
```

**Назначение**: Извлекает информацию о доставке, когда товар есть в наличии.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["delivery_in_stock"]`, преобразованное в строку.

**Как работает функция**:

1.  Использует `d.execute_locator(l["delivery_in_stock"])` для получения информации о доставке с веб-страницы.
2.  Преобразует полученное значение в строку с помощью `str()`.

### `field_active`

```python
def field_active():
    """

    @details
    """
    return f.active  # <-  поставить в зависимость от delivery_out_stock
    ...
```

**Назначение**: Определяет, активен ли товар.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.active`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.active`.

### `field_additional_delivery_times`

```python
def field_additional_delivery_times():
    """

    @details
    """
    return d.execute_locator(l["additional_delivery_times"])
    ...
```

**Назначение**: Извлекает информацию о дополнительном времени доставки.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["additional_delivery_times"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["additional_delivery_times"])` для получения информации о дополнительном времени доставки с веб-страницы.

### `field_advanced_stock_management`

```python
def field_advanced_stock_management():
    """

    @details
    """
    return f.advanced_stock_management
    ...
```

**Назначение**: Возвращает значение расширенного управления запасами.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.advanced_stock_management`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.advanced_stock_management`.

### `field_affiliate_short_link`

```python
def field_affiliate_short_link():
    """

    @details
    """
    return d.current_url
    ...
```

**Назначение**: Возвращает текущий URL страницы в качестве короткой партнерской ссылки.

**Параметры**:

- Нет параметров. Использует глобальную переменную `d` (driver).

**Возвращает**:

- Текущий URL страницы, полученный с помощью `d.current_url`.

**Как работает функция**:

1.  Возвращает текущий URL страницы.

### `field_affiliate_summary`

```python
def field_affiliate_summary():
    """

    @details
    """
    return f.affiliate_summary
    ...
```

**Назначение**: Возвращает краткое описание партнерской программы.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.affiliate_summary`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.affiliate_summary`.

### `field_affiliate_summary_2`

```python
def field_affiliate_summary_2():
    """

    @details
    """
    return f.affiliate_summary_2
    ...
```

**Назначение**: Возвращает второе краткое описание партнерской программы.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.affiliate_summary_2`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.affiliate_summary_2`.

### `field_affiliate_text`

```python
def field_affiliate_text():
    """

    @details
    """
    return f.affiliate_text
    ...
```

**Назначение**: Возвращает текст партнерской программы.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.affiliate_text`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.affiliate_text`.

### `field_affiliate_image_large`

```python
def field_affiliate_image_large():
    """

    @details
    """
    ...
```

**Назначение**: Предназначена для возвращения большого изображения партнерской программы.

**Параметры**:

- Нет параметров.

**Возвращает**:

- Нет возврата.

**Как работает функция**:

1.  Внутри тела функции отсутствует какая-либо логика.

### `field_affiliate_image_medium`

```python
def field_affiliate_image_medium():
    """

    @details
    """
    ...
```

**Назначение**: Предназначена для возвращения среднего изображения партнерской программы.

**Параметры**:

- Нет параметров.

**Возвращает**:

- Нет возврата.

**Как работает функция**:

1.  Внутри тела функции отсутствует какая-либо логика.

### `field_affiliate_image_small`

```python
def field_affiliate_image_small():
    """

    @details
    """
    return d.execute_locator(l["affiliate_image_small"])
```

**Назначение**: Извлекает малое изображение партнерской программы.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["affiliate_image_small"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["affiliate_image_small"])` для получения малого изображения партнерской программы с веб-страницы.

### `field_available_date`

```python
def field_available_date():
    """

    @details
    """
    return f.available_date
    ...
```

**Назначение**: Возвращает дату доступности товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.available_date`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.available_date`.

### `field_available_for_order`

```python
def field_available_for_order():
    """ Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
   """
    available_for_order = d.execute_locator(l["available_for_order"])
    ...
    if available_for_order is None:
        f.available_for_order = 1
    else:
        f.available_for_order = 0
        f.active = 0
    ...
```

**Назначение**: Определяет, доступен ли товар для заказа.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver), `l` (locators) и `f` (ProductFields).

**Возвращает**:

- Нет явного возвращаемого значения. Обновляет поля объекта `f` (ProductFields) напрямую.

**Как работает функция**:

1.  Пытается получить веб-элемент, соответствующий локатору `l["available_for_order"]`.
2.  Если веб-элемент не найден (возвращается `None`), устанавливает `f.available_for_order = 1`, что означает, что товар доступен для заказа.
3.  Если веб-элемент найден, устанавливает `f.available_for_order = 0` и `f.active = 0`, что означает, что товар недоступен для заказа и неактивен.

### `field_available_later`

```python
def field_available_later():
    """

    @details
    """
    return f.available_later
    ...
```

**Назначение**: Возвращает текст о доступности товара позже.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.available_later`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.available_later`.

### `field_available_now`

```python
def field_available_now():
    """

    @details
    """
    return f.available_now
    ...
```

**Назначение**: Возвращает текст о доступности товара сейчас.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.available_now`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.available_now`.

### `field_category_ids`

```python
def field_category_ids():
    """

    @details
    """
    return f.category_ids
    ...
```

**Назначение**: Возвращает идентификаторы категорий товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.category_ids`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.category_ids`.

### `field_category_ids_append`

```python
def field_category_ids_append():
    """

    @details
    """
    # return f.category_ids_append
    ...
```

**Назначение**: Предназначена для добавления идентификаторов категорий товара.

**Параметры**:

- Нет параметров.

**Возвращает**:

- Нет возврата.

**Как работает функция**:

1.  Внутри тела функции отсутствует какая-либо логика.

### `field_cache_default_attribute`

```python
def field_cache_default_attribute():
    """

    @details
    """
    return f.cache_default_attribute
    ...
```

**Назначение**: Возвращает атрибут кэширования по умолчанию.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.cache_default_attribute`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.cache_default_attribute`.

### `field_cache_has_attachments`

```python
def field_cache_has_attachments():
    """

    @details
    """
    return f.cache_has_attachments
    ...
```

**Назначение**: Возвращает информацию о наличии вложений в кэше.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.cache_has_attachments`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.cache_has_attachments`.

### `field_cache_is_pack`

```python
def field_cache_is_pack():
    """

    @details
    """
    return f.cache_is_pack
    ...
```

**Назначение**: Возвращает информацию о том, является ли товар комплектом в кэше.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.cache_is_pack`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.cache_is_pack`.

### `field_condition`

```python
def field_condition():
    """

    @details
    """
    return d.execute_locator(l.condition)
```

**Назначение**: Извлекает условие (состояние) товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l.condition`.

**Как работает функция**:

1.  Использует `d.execute_locator(l.condition)` для получения условия товара с веб-страницы.

### `field_customizable`

```python
def field_customizable():
    """

    @details
    """
    return f.customizable
    ...
```

**Назначение**: Возвращает информацию о возможности настройки товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.customizable`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.customizable`.

### `field_date_add`

```python
def field_date_add():
    """

    @details
    """
    return f.date_add
    ...
```

**Назначение**: Возвращает дату добавления товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.date_add`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.date_add`.

### `field_date_upd`

```python
def field_date_upd():
    """

    @details
    """
    return f.date_upd
    ...
```

**Назначение**: Возвращает дату обновления товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.date_upd`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.date_upd`.

### `field_depth`

```python
def field_depth():
    """
    @details
    """
    return d.execute_locator ( l ["depth"] )
    ...
```

**Назначение**: Извлекает глубину товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["depth"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["depth"])` для получения глубины товара с веб-страницы.

### `field_description`

```python
def field_description():
    """ поле полного описания товара
   @details
   """
    return d.execute_locator (l["description"] )[0].text
    ...
```

**Назначение**: Извлекает полное описание товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Текст, полученный с помощью локатора `l["description"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["description"])[0].text` для получения полного описания товара с веб-страницы.

### `field_id_category_default`

```python
def field_id_category_default():
    """ Главная категория товара. Берется из сценария """
    return s.current_scenario["presta_categories"]["default_category"]
    ...
```

**Назначение**: Возвращает идентификатор главной категории товара из сценария.

**Параметры**:

- Нет параметров. Использует глобальную переменную `s` (Supplier).

**Возвращает**:

- Идентификатор главной категории товара, полученный из `s.current_scenario["presta_categories"]["default_category"]`.

**Как работает функция**:

1.  Возвращает идентификатор главной категории товара, который берется из сценария поставщика.

### `field_ean13`

```python
def field_ean13():
    """

    @details
    """
    return d.execute_locator ( l ["ean13"] )
    ...
```

**Назначение**: Извлекает код EAN13 товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["ean13"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["ean13"])` для получения кода EAN13 товара с веб-страницы.

### `field_ecotax`

```python
def field_ecotax():
    """

    @details
    """
    return f.ecotax
    ...
```

**Назначение**: Возвращает значение налога ecotax.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.ecotax`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.ecotax`.

### `field_height`

```python
def field_height():
    """

    @details
    """
    return d.execute_locator ( l ["height"] )
    ...
```

**Назначение**: Извлекает высоту товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["height"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["height"])` для получения высоты товара с веб-страницы.

### `field_how_to_use`

```python
def field_how_to_use():
    """

    @details
    """
    return d.execute_locator ( l ["how_to_use"] ) [0].text
    ...
```

**Назначение**: Извлекает инструкцию по использованию товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Текст, полученный с помощью локатора `l["how_to_use"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["how_to_use"])[0].text` для получения инструкции по использованию товара с веб-страницы.

### `field_id_default_combination`

```python
def field_id_default_combination():
    """

    @details
    """
    return f.id_default_combination
    ...
```

**Назначение**: Возвращает идентификатор комбинации по умолчанию.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_default_combination`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_default_combination`.

### `field_id_default_image`

```python
def field_id_default_image():
    """

    @details
    """
    return f.id_default_image
    ...
```

**Назначение**: Возвращает идентификатор изображения по умолчанию.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_default_image`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_default_image`.

### `field_id_lang`

```python
def field_id_lang():
    """

    @details
    """
    return f.id_lang
    ...
```

**Назначение**: Возвращает идентификатор языка.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_lang`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_lang`.

### `field_id_manufacturer`

```python
def field_id_manufacturer():
    """ ID бренда. Может быть и названием бренда - престашоп сам разберется """

    return d.execute_locator(l["id_manufacturer"])
    ...
```

**Назначение**: Извлекает идентификатор производителя товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["id_manufacturer"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["id_manufacturer"])` для получения идентификатора производителя товара с веб-страницы.

### `field_id_product`

```python
def field_id_product():
    """

    @details
    """
    return f.id_product
    ...
```

**Назначение**: Возвращает идентификатор товара.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_product`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_product`.

### `field_id_shop_default`

```python
def field_id_shop_default():
    """

    @details
    """
    return f.id_shop_default
    ...
```

**Назначение**: Возвращает идентификатор магазина по умолчанию.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_shop_default`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_shop_default`.

### `field_id_supplier`

```python
def field_id_supplier():
    """

    @details
    """
    return d.execute_locator(l["id_supplier"])
    ...
```

**Назначение**: Извлекает идентификатор поставщика товара.

**Параметры**:

- Нет параметров. Использует глобальные переменные `d` (driver) и `l` (locators).

**Возвращает**:

- Значение, полученное с помощью локатора `l["id_supplier"]`.

**Как работает функция**:

1.  Использует `d.execute_locator(l["id_supplier"])` для получения идентификатора поставщика товара с веб-страницы.

### `field_id_tax`

```python
def field_id_tax():
    """

    @details
    """
    return f.id_tax
    ...
```

**Назначение**: Возвращает идентификатор налога.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_tax`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_tax`.

### `field_id_type_redirected`

```python
def field_id_type_redirected():
    """

    @details
    """
    return f.id_type_redirected
    ...
```

**Назначение**: Возвращает идентификатор типа переадресации.

**Параметры**:

- Нет параметров. Использует глобальную переменную `f` (ProductFields).

**Возвращает**:

- Значение атрибута `f.id_type_redirected`.

**Как работает функция**:

1.  Возвращает текущее значение атрибута `f.id_type_redirected`.

### `field_images_urls`

```python
def field_images_urls():
    """
    Вначале я загружу дефолтную картинку
   @details
   """
    return d.execute_locator(l["additional_images_urls"])
    ...
```

**Назначение**: Извлекает URL дополнительных изображений товара.

**Параметры**:

- Нет параметров. Использует глобальные