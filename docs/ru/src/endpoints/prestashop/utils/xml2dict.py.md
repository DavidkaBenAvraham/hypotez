# Модуль для преобразования XML в словарь

## Обзор

Модуль предоставляет функции для преобразования XML-строк в Python-словари. Он включает в себя функции для парсинга XML-узлов, создания словарей и обработки пространств имен.

## Подробней

Этот модуль предназначен для преобразования XML-данных в структуру Python-словаря, что упрощает доступ к данным и их обработку. Он был адаптирован для использования с Prestapyt и включает в себя функции для обработки XML-узлов, атрибутов и пространств имен.

## Функции

### `_parse_node(node)`

**Назначение**: Рекурсивно разбирает XML-узел и его потомков, преобразуя их в словарь.

**Параметры**:
- `node` (xml.etree.ElementTree.Element): XML-узел для разбора.

**Возвращает**:
- `dict`: Словарь, представляющий XML-узел и его содержимое.

**Как работает функция**:
- Инициализирует пустой словарь `tree` для хранения результатов.
- Инициализирует пустой словарь `attrs` для хранения атрибутов узла.
- Перебирает атрибуты узла, вызывая `_make_dict` для каждого атрибута и добавляя результат в словарь `attrs`. Атрибуты, у которых тег `'{http://www.w3.org/1999/xlink}href'`, пропускаются.
- Извлекает текст из узла, удаляет пробельные символы в начале и конце, и сохраняет его в переменной `value`.
- Если есть атрибуты, добавляет их в словарь `tree` под ключом `'attrs'`.
- Перебирает потомков узла, устанавливает флаг `has_child` в `True` и рекурсивно вызывает `_parse_node` для каждого потомка.
- Создает словарь `cdict` с помощью функции `_make_dict` для каждого потомка.
- Если у узла есть потомки, значение `value` устанавливается в пустую строку.
- Если тег потомка еще не встречался в словаре `tree`, добавляет его.
- Если тег потомка встречается несколько раз, преобразует соответствующее значение в списке и добавляет новый элемент.
- Если у узла нет потомков, добавляет значение узла в словарь `tree` под ключом `'value'`.
- Если в словаре `tree` есть только ключ `'value'`, возвращает значение этого ключа.

**Внутренние функции**:
- Отсутствуют.

**Примеры**:

```python
import xml.etree.ElementTree as ET

xml_string = '<root><element attr1="value1">text</element></root>'
root = ET.fromstring(xml_string)
result = _parse_node(root[0])
print(result)
# {'attrs': {'attr1': 'value1'}, 'value': 'text'}
```

### `_make_dict(tag, value)`

**Назначение**: Создает словарь с тегом и значением, обрабатывая пространства имен.

**Параметры**:
- `tag` (str): Тег XML-элемента.
- `value` (str | dict): Значение XML-элемента.

**Возвращает**:
- `dict`: Словарь, содержащий тег и значение.

**Как работает функция**:

- Инициализирует `tag_values` значением `value`.
- Использует регулярное выражение для поиска пространства имен в теге.
- Если пространство имен найдено, создает словарь со значением и пространством имен.
- Возвращает словарь с тегом и значением.

**Внутренние функции**:
- Отсутствуют.

**Примеры**:

```python
result = _make_dict('tag', 'value')
print(result)
# {'tag': 'value'}

result = _make_dict('{http://example.com}tag', 'value')
print(result)
# {'tag': {'value': {'value': 'value', 'xmlns': 'http://example.com'}}}
```

### `xml2dict(xml)`

**Назначение**: Преобразует XML-строку в словарь.

**Параметры**:
- `xml` (str): XML-строка для преобразования.

**Возвращает**:
- `dict`: Словарь, представляющий XML-данные.

**Как работает функция**:

- Преобразует XML-строку в объект `ElementTree` с помощью `ET.fromstring()`.
- Вызывает функцию `ET2dict` для преобразования `ElementTree` в словарь.

**Внутренние функции**:
- Отсутствуют.

**Примеры**:

```python
xml_string = '<root><element>text</element></root>'
result = xml2dict(xml_string)
print(result)
# {'root': {'element': 'text'}}
```

### `ET2dict(element_tree)`

**Назначение**: Преобразует `ElementTree` в словарь.

**Параметры**:
- `element_tree` (xml.etree.ElementTree.Element): `ElementTree` для преобразования.

**Возвращает**:
- `dict`: Словарь, представляющий XML-данные.

**Как работает функция**:

- Вызывает функцию `_make_dict` с тегом корневого элемента и результатом функции `_parse_node`, примененной к корневому элементу.

**Внутренние функции**:
- Отсутствуют.

**Примеры**:

```python
import xml.etree.ElementTree as ET

xml_string = '<root><element>text</element></root>'
root = ET.fromstring(xml_string)
result = ET2dict(root)
print(result)
# {'root': {'element': 'text'}}
```

```