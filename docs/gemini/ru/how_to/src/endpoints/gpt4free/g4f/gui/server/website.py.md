## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода реализует маршрутизацию для веб-приложения Flask, отвечая за обработку запросов к разным страницам сайта.

Шаги выполнения
-------------------------
1. **Инициализация класса Website**: Класс `Website` инициализируется с помощью объекта Flask (`app`). В конструкторе создается словарь `routes`, содержащий информацию о маршрутах и их обработчиках. 
2. **Определение маршрутов**: В словаре `routes` определены ключи, соответствующие URL-адресам, и значения, представляющие собой словари, содержащие информацию о функциях-обработчиках и методах HTTP (GET, POST).
3. **Регистрация маршрутов**: Маршруты добавляются в приложение Flask при помощи метода `add_url_rule` в методе `register_routes`.
4. **Обработка запросов**: При получении запроса Flask сравнивает URL-адрес с определенными маршрутами и вызывает соответствующую функцию-обработчик.

Пример использования
-------------------------

```python
from hypotez.src.endpoints.gpt4free.g4f.gui.server.website import Website

app = Flask(__name__) # Создаем объект приложения Flask

website = Website(app) # Инициализируем класс Website с помощью объекта Flask

website.register_routes() # Регистрируем маршруты в приложении Flask

if __name__ == "__main__":
    app.run(debug=True) # Запускаем приложение Flask
```

**Пример:**
- При запросе к URL `/chat` вызывается функция `_index`, которая возвращает страницу `index.html` с уникальным идентификатором разговора (conversation_id).
- При запросе к URL `/chat/12345` вызывается функция `_chat`, которая возвращает страницу `index.html` с conversation_id равным `12345`.
- При запросе к URL `/chat/share/12345` вызывается функция `_share_id`, которая возвращает страницу `index.html` с conversation_id равным `12345` и ссылкой на общедоступный URL (share_url) для этого разговора.

## Изменения

- Используйте `cls` вместо `self` в методах класса.
- Аннотации типов для всех входных и выходных параметров функций.
- Используйте `|` вместо `Union[]`.
- Добавлены комментарии для лучшего понимания кода.
- Добавлена документация для метода `register_routes`.
- Исправлен тип `share_id` в функции `_share_id`.
- Используется `os.environ.get` для получения значения `G4F_SHARE_URL`.
- Добавлен `redirect_home` для перенаправления на главную страницу.
- Добавлен `uuid.uuid4()` для генерации уникальных идентификаторов.
- Исправлено имя функции `_index`.
- Добавлен `debug=True` для запуска приложения Flask в режиме отладки.