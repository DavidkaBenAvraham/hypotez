# Модуль для экспериментов с акциями из XLS-файлов AliExpress

## Обзор

Модуль предназначен для разбора XLS-таблиц, сгенерированных в личном кабинете portals.aliexpress.com, и извлечения информации об акциях.

## Подробней

Модуль `deals_from_xls.py` используется для обработки данных об акциях, представленных в формате XLS, которые экспортируются из личного кабинета AliExpress. Он использует класс `DealsFromXLS` для парсинга данных и извлечения информации о каждой акции. Полученные данные выводятся на экран с использованием функции `pprint` из модуля `src.utils.printer`.

## Импортированные модули

- `header`: Импортируется модуль `header`. Подробная информация об этом модуле недоступна.
- `src.suppliers.suppliers_list.aliexpress.DealsFromXLS`: Класс для парсинга XLS-файлов с данными об акциях AliExpress.
- `src.utils.printer.pprint`: Функция для "красивого" вывода данных в консоль.

## Переменные

- `deals_parser`: Экземпляр класса `DealsFromXLS`, используемый для парсинга данных об акциях. Инициализируется с параметрами `language='EN'` и `currency='USD'`.

## Классы

### `DealsFromXLS`

**Описание**: Класс предназначен для парсинга XLS-файлов, содержащих информацию об акциях, полученных из личного кабинета AliExpress.

**Методы**:

- `get_next_deal()`: Метод для получения следующей акции из XLS-файла.

## Функции

В данном коде напрямую не определены функции, но используется метод `get_next_deal` класса `DealsFromXLS`.

### `get_next_deal`

**Описание**: Метод `get_next_deal()` класса `DealsFromXLS` используется для итерации по строкам XLS-файла и извлечения данных о каждой акции.

**Как работает функция**:

1.  Метод извлекает данные об акции из текущей строки XLS-файла.
2.  Возвращает словарь с информацией об акции.
3.  Если достигнут конец файла, возвращает `None`.

**Примеры**:

Примеры использования метода `get_next_deal` можно найти в цикле `for deal in deals_parser.get_next_deal():`, где каждая итерация возвращает информацию о следующей акции.
```python
deals_parser = DealsFromXLS(language='EN', currency= 'USD')

for deal in deals_parser.get_next_deal():
    pprint(deal)
    ...
```
В этом примере `deals_parser` инициализируется классом `DealsFromXLS` с указанием языка (`EN`) и валюты (`USD`). Затем в цикле `for` происходит итерация по акциям, возвращаемым методом `get_next_deal()`. Каждая акция выводится на экран с использованием функции `pprint`.