# Модуль для определения типов данных в `g4f`
## Обзор

Этот модуль предоставляет типы данных, используемые в `g4f` для типизации данных, передаваемых в функции и методы.

## Детали

Модуль `typing.py` определяет типы данных, которые используются для типизации параметров, возвращаемых значений и атрибутов в `g4f`. 

Типы данных:

- **`sha256`**:  Тип данных для представления хеша SHA-256.

## Типы данных

### `sha256`

**Описание**: Тип данных для представления хеша SHA-256.
**Тип**: `NewType('sha_256_hash', str)`

**Пример**:

```python
from g4f.typing import sha256

hash_value: sha256 = '0000000000000000000000000000000000000000000000000000000000000000'

```