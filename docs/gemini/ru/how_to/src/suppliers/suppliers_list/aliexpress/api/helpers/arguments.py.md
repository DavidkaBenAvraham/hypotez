## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет две функции для обработки аргументов, которые используются при работе с AliExpress API. 

**`get_list_as_string`**  преобразует входной аргумент в строку, если он является списком.

**`get_product_ids`**  преобразует входной аргумент в список идентификаторов продуктов (product_ids), если он является строкой или списком.

Шаги выполнения
-------------------------
### `get_list_as_string`
1. **Проверка на None**: Если входной аргумент `value` равен None, функция ничего не возвращает.
2. **Проверка на строку**: Если `value` является строкой, функция возвращает ее без изменений.
3. **Проверка на список**: Если `value` является списком, функция объединяет его элементы в строку, используя запятую как разделитель, и возвращает полученную строку.
4. **Ошибка**: Если `value` не является ни строкой, ни списком, функция вызывает исключение `InvalidArgumentException`, сообщая о том, что аргумент должен быть списком или строкой.

### `get_product_ids`
1. **Проверка на строку**: Если `values` является строкой, она разделяется по запятой, и полученный список записывается в переменную `values`.
2. **Проверка на список**: Если `values` не является ни строкой, ни списком, функция вызывает исключение `InvalidArgumentException`, сообщая о том, что аргумент `product_ids` должен быть списком или строкой.
3. **Извлечение product_ids**: Из входного списка `values` извлекаются идентификаторы продуктов (product_ids) с использованием функции `get_product_id`. Каждый product_id добавляется в список `product_ids`.
4. **Возвращение списка**: Функция возвращает полученный список `product_ids`.

Пример использования
-------------------------

```python
from src.suppliers.aliexpress.api.helpers.arguments import get_list_as_string, get_product_ids

# Пример использования get_list_as_string
product_ids = [123456789, 987654321]
product_ids_str = get_list_as_string(product_ids)
print(product_ids_str)  # Вывод: 123456789,987654321

# Пример использования get_product_ids
product_ids_str = '123456789,987654321'
product_ids = get_product_ids(product_ids_str)
print(product_ids)  # Вывод: [123456789, 987654321] 

product_ids_list = [123456789, 987654321]
product_ids = get_product_ids(product_ids_list)
print(product_ids)  # Вывод: [123456789, 987654321]
```

**Важно:** В данном примере `get_product_id` - это  функция, которая должна быть определена в другом модуле и преобразовать строку в product_id.