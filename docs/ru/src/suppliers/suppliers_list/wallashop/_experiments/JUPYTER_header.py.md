# Документация для модуля `src.suppliers.wallashop._experiments`

## Обзор

Модуль `src.suppliers.wallashop._experiments` содержит экспериментальный код, вероятно, для тестирования и разработки новых функций, связанных с поставщиками товаров, в частности для магазина Wallashop.  Этот модуль может включать в себя прототипы, тестовые сценарии или другие временные решения, которые еще не интегрированы в основную кодовую базу.

## Подробней

Модуль включает в себя импорты необходимых библиотек и модулей, настройку путей для импорта модулей из проекта `hypotez`, а также функцию `start_supplier`. Он предназначен для экспериментов, связанных с поставщиками, и предоставляет возможность запуска поставщика с определенными параметрами.

## Переменные модуля

- `dir_root` (Path): Корневая директория проекта `hypotez`, используется для добавления корневой папки в `sys.path`.
- `dir_src` (Path): Директория `src` внутри корневой директории проекта `hypotez`, также используется для добавления в `sys.path`.

## Функции

### `start_supplier`

**Назначение**: Функция для запуска поставщика с указанными параметрами.

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params))
```

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика (например, 'aliexpress'). По умолчанию 'aliexpress'.
- `locale` (str, optional): Локаль поставщика (например, 'en'). По умолчанию 'en'.

**Возвращает**:
- Возвращает инстанс класса `Supplier` с переданными параметрами.

**Как работает функция**:

1. Функция принимает префикс поставщика и локаль в качестве аргументов, которые определяют, какого поставщика и с какой локалью следует запустить.
2. Создает словарь `params`, содержащий переданные параметры `supplier_prefix` и `locale`.
3. Создает и возвращает экземпляр класса `Supplier`, передавая словарь `params` в качестве аргументов для инициализации объекта `Supplier`.

**Примеры**:

```python
# Пример вызова функции start_supplier с параметрами по умолчанию
supplier = start_supplier()

# Пример вызова функции start_supplier с указанием префикса и локали поставщика
supplier = start_supplier(supplier_prefix='wallashop', locale='de')