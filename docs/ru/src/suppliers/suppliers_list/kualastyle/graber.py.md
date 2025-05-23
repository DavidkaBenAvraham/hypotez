# Модуль для сбора данных с сайта Kualastyle
## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `kualastyle.co.il`. Он содержит класс `Graber`, который наследуется от базового класса `Graber` (Grbr) и переопределяет некоторые методы для обработки специфичных полей данных на страницах товаров `kualastyle`.

## Подробнее

Основная цель данного модуля - автоматизировать процесс сбора информации о товарах с сайта `kualastyle.co.il`. Он использует веб-драйвер для взаимодействия с сайтом и извлечения необходимых данных. Модуль предоставляет гибкую структуру для обработки различных полей товаров, позволяя переопределять методы обработки для нестандартных случаев.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта `kualastyle.co.il`. Он наследуется от базового класса `Graber` (Grbr) и переопределяет некоторые методы для обработки специфичных полей данных на страницах товаров `kualastyle`.

**Наследует**:
- `Graber` (Grbr): Базовый класс для сбора данных о товарах.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, используется для идентификации поставщика.

**Методы**:
- `__init__(self, driver: Driver, lang_index: int)`: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.
- `close_pop_up(value: Any = None)`: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

### Методы класса

#### `__init__(self, driver: Driver, lang_index: int)`

```python
def __init__(self, driver: Driver, lang_index: int):
    """Инициализация класса сбора полей товара."""
    ...
```

**Назначение**: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка, используемый для локализации контента.

**Как работает функция**:
- Устанавливает атрибут `supplier_prefix` равным `'kualastyle'`.
- Вызывает конструктор родительского класса `Graber` (Grbr) с указанием префикса поставщика, экземпляра веб-драйвера и индекса языка.
- Устанавливает значение `Config.locator_for_decorator` равным `None`, что отключает выполнение декоратора `@close_pop_up`.

**Примеры**:
```python
driver = Driver(webdriver_type='chrome')
graber = Graber(driver=driver, lang_index=0)
print(graber.supplier_prefix)  # Вывод: kualastyle
```

#### `close_pop_up(value: Any = None)`

```python
def close_pop_up(value: Any = None):
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
    ...
```

**Назначение**: Создает декоратор для закрытия всплывающих окон.
```
"""Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
```

**Параметры**:
- `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Как работает функция**:
- Определяет внутреннюю функцию `decorator`, которая принимает функцию `func` в качестве аргумента.
- Внутри `decorator` определяется функция `wrapper`, которая выполняет попытку закрытия всплывающего окна с использованием `driver.execute_locator(Context.locator.close_pop_up)`.
- Если возникает исключение `ExecuteLocatorException`, оно логируется.
- Затем выполняется основная функция `func` и возвращается её результат.
- Декоратор возвращает функцию `wrapper`.

**Примеры**:
```python
from src.suppliers.graber import Graber as Grbr

class MyGraber(Grbr):
    supplier_prefix: str

    def __init__(self, driver: Driver, lang_index:int):
        self.supplier_prefix = 'my_supplier'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

    @Graber.close_pop_up()
    async def my_method(self):
        print("Основной метод")

# Пример использования декоратора
driver = Driver(webdriver_type='chrome')
graber = MyGraber(driver=driver, lang_index=0)
# await graber.my_method()  # Раскомментировать при необходимости
```

## Переменные класса

- `supplier_prefix` (str): Префикс поставщика, используемый для идентификации поставщика. В данном случае установлен в `'kualastyle'`.
```