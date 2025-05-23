## Как использовать функцию `login`
=========================================================================================

### Описание
-------------------------
Функция `login` выполняет аутентификацию поставщика, передавая его объект в качестве аргумента.

### Шаги выполнения
-------------------------
1. Функция принимает объект `Supplier` в качестве аргумента.
2. **(В данный момент функция просто возвращает `True`.)** В будущем эта функция будет реализовывать логику авторизации, 
   проверяя учетные данные поставщика и возвращая `True`, если вход успешен, иначе `False`.

### Пример использования
-------------------------
```python
from src.suppliers.hb.login import login
from src.suppliers.suppliers_list.hb.hb_supplier import HBSupplier

# Создание объекта поставщика
hb_supplier = HBSupplier(login='test_login', password='test_password')

# Вызов функции login
login_result = login(hb_supplier)

# Проверка результата входа
if login_result:
    print("Вход выполнен успешно!")
else:
    print("Ошибка входа.")
```