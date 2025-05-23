# Модуль для сбора данных с сайта Wallashop
## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с сайта `wallashop.co.il`. Он наследует базовый класс `Graber` и переопределяет его методы для специфичной обработки данных, характерной для данного поставщика. Модуль использует веб-драйвер для взаимодействия с сайтом и извлечения необходимых данных.

## Подробнее

Этот модуль является частью системы для сбора данных о товарах с различных онлайн-платформ. Он содержит класс `Graber`, который специализируется на извлечении и обработке данных с сайта `wallashop.co.il`.  Перед отправкой запроса к веб-драйверу можно совершить предварительные действия через декоратор. Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение в `Context.locator`. Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта `wallashop.co.il`. Он наследует функциональность от базового класса `Graber` (`Grbr`) и переопределяет некоторые методы для адаптации к структуре и особенностям сайта `wallashop.co.il`.

**Наследует**:
- `src.suppliers.graber.Graber` (`Grbr`)

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, устанавливается как `'wallashop'`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """Инициализация класса сбора полей товара."""
    self.supplier_prefix = 'wallashop'
    super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

    # Закрыватель поп ап `@close_pop_up`
    Config.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка.

**Как работает функция**:
- Устанавливает атрибут `supplier_prefix` в значение `'wallashop'`.
- Вызывает конструктор родительского класса `Graber` (`Grbr`) с указанием префикса поставщика, экземпляра веб-драйвера и индекса языка.
- Устанавливает `Config.locator_for_decorator` в `None`, что указывает на отсутствие необходимости использовать декоратор `@close_pop_up`.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver import Firefox
driver = Driver(Firefox)
graber = Graber(driver, 0)