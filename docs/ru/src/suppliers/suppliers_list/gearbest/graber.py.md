# Модуль для сбора данных о товарах с Gearbest
## Обзор

Модуль содержит класс `Graber`, предназначенный для сбора информации о товарах с веб-сайта `gearbest.com`. Он наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки различных полей товара на странице. В случае необходимости нестандартной обработки поля, метод может быть переопределен.

## Подробнее

Модуль предназначен для извлечения структурированных данных о товарах с сайта `gearbest.com`. Он использует веб-драйвер для навигации по сайту и извлечения необходимой информации. Класс `Graber` предоставляет методы для обработки различных полей товара на странице. Если требуется нестандартная обработка поля, метод может быть переопределен. Перед отправкой запроса к веб-драйверу можно совершить предварительные действия через декоратор.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора и обработки данных о товарах с веб-сайта `gearbest.com`. Он наследуется от базового класса `src.suppliers.graber.Graber`.

**Наследует**:
- `src.suppliers.graber.Graber`: Базовый класс, предоставляющий общую функциональность для сбора данных о товарах с веб-сайтов.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, используемый для идентификации поставщика в системе.

**Методы**:
- `__init__(driver: Optional['Driver'] = None, lang_index: Optional[int] = None)`: Инициализирует экземпляр класса `Graber`.

### `__init__`

```python
def __init__(self, driver: Optional['Driver'] = None, lang_index:Optional[int] = None):
    """Инициализация класса сбора полей товара.

    Args:
        driver (Optional['Driver'], optional): Экземпляр веб-драйвера для управления браузером. По умолчанию `None`.
        lang_index (Optional[int], optional): Индекс языка. По умолчанию `None`.

    """
```

**Назначение**: Инициализация класса `Graber` для сбора данных о товарах с веб-сайта `gearbest.com`.

**Параметры**:
- `driver` (Optional['Driver'], optional): Экземпляр веб-драйвера для управления браузером. По умолчанию `None`.
- `lang_index` (Optional[int], optional): Индекс языка, используемый при сборе данных. По умолчанию `None`.

**Как работает функция**:
- Устанавливает префикс поставщика (`supplier_prefix`) как `etzmaleh`.
- Вызывает конструктор родительского класса `Grbr` с указанием префикса поставщика, экземпляра веб-драйвера и индекса языка.
- Устанавливает значение `Config.locator_for_decorator` в `None`, что указывает на отсутствие необходимости выполнения каких-либо действий в декораторе `@close_pop_up`.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome
# Пример создания экземпляра класса Graber с использованием веб-драйвера Chrome
driver = Driver(Chrome)
graber = Graber(driver=driver)
```
```python
# Пример создания экземпляра класса Graber без указания веб-драйвера и индекса языка
graber = Graber()