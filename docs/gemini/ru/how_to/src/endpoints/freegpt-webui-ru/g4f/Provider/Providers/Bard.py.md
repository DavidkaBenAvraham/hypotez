## Как использовать этот блок кода
========================================================================================

### Описание
-------------------------
Блок кода реализует функционал взаимодействия с Google Bard через API. Он предоставляет функцию `_create_completion`, которая генерирует ответ от Bard на основе заданного текста (prompt).

### Шаги выполнения
-------------------------
1. **Инициализация:** Функция получает на вход текст запроса (prompt) и другие параметры (модель, идентификаторы беседы и т.д.).
2. **Аутентификация:** 
    - Извлекает значение cookie "__Secure-1PSID" из браузера.
    - Использует его для аутентификации в API Bard.
3. **Форматирование текста:** 
    - Преобразует текст запроса в формат, ожидаемый API.
4. **Отправка запроса:**
    - Использует библиотеку `requests` для отправки HTTP-запроса к API Bard с необходимыми данными.
5. **Обработка ответа:**
    - Парсит полученный JSON-ответ от API.
    - Возвращает текст ответа Bard в виде генератора.

### Пример использования
-------------------------
```python
from g4f.Provider.Providers import Bard

messages = [
    {'role': 'user', 'content': 'Как дела?'},
]

# Инициализация провайдера Bard
bard = Bard.Bard()

# Вызов функции для получения ответа от Bard
for response in bard._create_completion(model='Palm2', messages=messages):
    print(response)
```

**Важно:**
- Перед использованием этого блока кода необходимо получить  cookie "__Secure-1PSID" из своего браузера Google.
- Google может ограничивать доступ к API Bard из некоторых стран. 
- Для стабильной работы рекомендуется использовать прокси-сервер.