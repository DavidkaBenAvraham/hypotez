## \file hypotez/src/webdriver/edge/readme.ru.md
# Модуль Edge WebDriver для Selenium

Модуль предоставляет кастомную реализацию Edge WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определённые в файле `edge.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкие и автоматизированные взаимодействия с браузером.

## Ключевые особенности

- **Централизованная конфигурация**: Конфигурация управляется через файл `edge.json`.
- **Множественные профили браузера**: Поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.
- **Улучшенное логирование и обработка ошибок**: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Возможность передавать опции**: Поддерживает передачу пользовательских опций при инициализации WebDriver.

## Требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Бинарник Edge WebDriver (например, `msedgedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что бинарник `msedgedriver` доступен в `PATH` вашей системы или укажите путь к нему в конфигурации.

## Конфигурация

Конфигурация для Edge WebDriver хранится в файле `edge.json`. Ниже приведён пример структуры конфигурационного файла и его описание:

### Пример конфигурации (`edge.json`)

```json
{
  "options": [
    "--disable-dev-shm-usage",
    "--remote-debugging-port=0"
  ],
  "profiles": {
    "os": "%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default",
    "internal": "webdriver\\\\edge\\\\profiles\\\\default"
  },
  "executable_path": {
    "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
}
```

### Описание полей конфигурации

#### 1. `options`
Список аргументов командной строки, передаваемых в Edge. Примеры:
- `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в Docker-контейнерах (полезно для предотвращения ошибок в контейнеризованных средах).
- `--remote-debugging-port=0`: Устанавливает порт для удалённой отладки в Edge. Значение `0` означает, что будет назначен случайный порт.

#### 2. `profiles`
Пути к директориям с пользовательскими данными Edge для различных сред:
- **os**: Путь к стандартной директории пользовательских данных (обычно для систем Windows).
- **internal**: Внутренний путь для стандартного профиля WebDriver.

#### 3. `executable_path`
Путь к бинарнику Edge WebDriver:
- **default**: Путь к исполняемому файлу `msedgedriver.exe`.

#### 4. `headers`
Пользовательские HTTP-заголовки, используемые в запросах браузера:
- **User-Agent**: Устанавливает строку user-agent для браузера.
- **Accept**: Устанавливает типы данных, которые браузер готов принять.
- **Accept-Charset**: Устанавливает поддерживаемую браузером кодировку символов.
- **Accept-Encoding**: Устанавливает поддерживаемые методы кодирования (установлено в `none`, чтобы отключить).
- **Accept-Language**: Устанавливает предпочтительные языки.
- **Connection**: Устанавливает тип соединения, который должен использовать браузер (например, `keep-alive`).

## Использование

Чтобы использовать `Edge` WebDriver в своём проекте, просто импортируйте его и инициализируйте:

```python
from src.webdriver.edge import Edge

# Инициализация Edge WebDriver с настройками user-agent и пользовательскими опциями
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()
```

Класс `Edge` автоматически загружает настройки из файла `edge.json` и использует их для конфигурации WebDriver. Также можно указать пользовательский user-agent и передать дополнительные опции при инициализации WebDriver.

### Паттерн Singleton

WebDriver для `Edge` использует паттерн Singleton. Это означает, что будет создан только один экземпляр WebDriver. Если экземпляр уже существует, будет использован тот же экземпляр и откроется новое окно.

## Логирование и отладка

Класс WebDriver использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации. Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.

### Примеры логов

- **Ошибка при инициализации WebDriver**: `Ошибка при инициализации Edge WebDriver: <детали ошибки>`
- **Проблемы с конфигурацией**: `Ошибка в файле edge.json: <детали проблемы>`

## Лицензия

Этот проект лицензирован на условиях MIT License. Подробности см. в файле [LICENSE](../../LICENSE).

                ```

Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот раздел демонстрирует, как использовать класс `Edge` из модуля `src.webdriver.edge` для управления браузером Edge с помощью Selenium. Он описывает процесс инициализации WebDriver, открытия веб-сайта и завершения сеанса браузера.

Шаги выполнения
-------------------------
1. **Импорт класса `Edge`**:
   - Из модуля `src.webdriver.edge` импортируется класс `Edge`.
   - Это необходимо для создания экземпляра WebDriver Edge.
   
2. **Инициализация Edge WebDriver**:
   - Создаётся экземпляр класса `Edge` с передачей параметров `user_agent` и `options`.
   - `user_agent` указывает строку user-agent, которую браузер будет использовать для идентификации.
   - `options` представляет собой список опций командной строки, передаваемых в Edge, например, запуск в режиме headless и отключение GPU.

3. **Открытие веб-сайта**:
   - Используется метод `get()` экземпляра `browser` для открытия указанного URL (в данном случае, "https://www.example.com").
   - Этот шаг загружает веб-страницу в браузере Edge.

4. **Закрытие браузера**:
   - Вызывается метод `quit()` экземпляра `browser` для закрытия всех окон браузера и завершения сеанса WebDriver.
   - Это освобождает ресурсы и завершает работу WebDriver.

Пример использования
-------------------------

```python
from src.webdriver.edge import Edge

# Инициализация Edge WebDriver с настройками user-agent и пользовательскими опциями
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()