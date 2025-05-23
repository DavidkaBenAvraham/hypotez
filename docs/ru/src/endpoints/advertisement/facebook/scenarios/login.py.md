# Модуль `login`

## Обзор

Модуль `login` содержит сценарий для авторизации в Facebook. Он использует веб-драйвер для автоматического заполнения полей логина и пароля, а также для нажатия кнопки входа.

## Подробней

Модуль предназначен для автоматизации процесса входа в Facebook. Он загружает локаторы веб-элементов из JSON-файла и использует их для взаимодействия с элементами на странице входа. В случае успеха возвращается `True`, иначе `False`.

## Функции

### `login`

```python
def login(d: Driver) -> bool:
    """ Выполняет вход на Facebook.

    Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя
    логин и пароль, а затем нажимает кнопку входа.

    Args:
        d (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

    Returns:
        bool: `True`, если авторизация прошла успешно, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.
    """
    ...
```

**Назначение**: Выполняет вход на Facebook.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.

**Как работает функция**:
1. Функция получает учетные данные Facebook из `gs.facebook_credentials[0]`.
2. Пытается ввести логин, используя метод `d.send_key_to_webelement` с локатором `locators.email` и именем пользователя из учетных данных.
3. Если ввод логина не удался, записывает ошибку в лог и возвращает `False`.
4. Делает паузу в 1.3 секунды.
5. Пытается ввести пароль, используя метод `d.send_key_to_webelement` с локатором `locators['password']` и паролем из учетных данных.
6. Если ввод пароля не удался, записывает ошибку в лог и возвращает `False`.
7. Делает паузу в 0.5 секунды.
8. Пытается нажать кнопку входа, используя метод `d.execute_locator` с локатором `locators['button']`.
9. Если нажатие кнопки не удалось, записывает ошибку в лог и возвращает `False`.
10. Возвращает `True`, если все шаги выполнены успешно.

**Примеры**:

Пример успешного вызова функции:

```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.scenarios.login import login

driver = Driver(Chrome)
result = login(driver)
print(result)  # Выведет: True
```

Пример неуспешного вызова функции (неверные учетные данные):

```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.scenarios.login import login

driver = Driver(Chrome)
result = login(driver)
print(result)  # Может вывести: False (зависит от обработки ошибок в драйвере)