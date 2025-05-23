## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода определяет модели данных (классы `BaseModel`) для работы с API gpt4free. 

Шаги выполнения
-------------------------
1. **Определение модели данных:** Код определяет несколько классов для представления данных, передаваемых через API gpt4free.
2. **Использование моделей данных:** Модели данных могут использоваться для валидации входных и выходных данных API.
3. **Заполнение полей:**  В модели данных можно задать значения полей с помощью  `Field`. 
4. **Пример использования:** 
```python
from g4f.api.stubs import ChatCompletionsConfig

config = ChatCompletionsConfig(
    messages=[{"role": "system", "content": "Ты - помощник по программированию."}, {"role": "user", "content": "Напиши функцию, которая складывает два числа."}],
    model="gpt-3.5-turbo",
    temperature=0.7
)

# использование config для вызова функции ChatCompletions 
```


Пример использования
-------------------------
```python
from g4f.api.stubs import ChatCompletionsConfig

config = ChatCompletionsConfig(
    messages=[{"role": "system", "content": "Ты - помощник по программированию."}, {"role": "user", "content": "Напиши функцию, которая складывает два числа."}],
    model="gpt-3.5-turbo",
    temperature=0.7
)

# использование config для вызова функции ChatCompletions 
```