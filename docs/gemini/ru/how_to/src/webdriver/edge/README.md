## \file hypotez/src/webdriver/edge/README.MD
# Модуль Edge WebDriver для Selenium

Этот модуль предоставляет пользовательскую реализацию Edge WebDriver с использованием Selenium. Он интегрирует параметры конфигурации, определенные в файле `edge.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкое и автоматизированное взаимодействие с браузером.

## Ключевые особенности

- **Централизованная конфигурация**: Конфигурация управляется через файл `edge.json`.
- **Поддержка нескольких профилей браузера**: Поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.
- **Расширенное ведение журнала и обработка ошибок**: Предоставляет подробные журналы для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Возможность передачи пользовательских параметров**: Поддерживает передачу пользовательских параметров во время инициализации WebDriver.

## Требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Двоичный файл Edge WebDriver (например, `msedgedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что двоичный файл `msedgedriver` доступен в системном `PATH` или укажите его путь в конфигурации.

## Конфигурация

Конфигурация для Edge WebDriver хранится в файле `edge.json`. Ниже приведена примерная структура файла конфигурации и ее описание:

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

- `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker (полезно для предотвращения ошибок в контейнерных средах).
- `--remote-debugging-port=0`: Устанавливает порт для удаленной отладки в Edge. Значение `0` означает, что будет назначен случайный порт.

#### 2. `profiles`

Пути к каталогам пользовательских данных Edge для различных сред:

- **os**: Путь к каталогу пользовательских данных по умолчанию (обычно для систем Windows).
- **internal**: Внутренний путь для профиля WebDriver по умолчанию.

#### 3. `executable_path`

Путь к двоичному файлу Edge WebDriver:

- **default**: Путь к двоичному файлу `msedgedriver.exe`.

#### 4. `headers`

Пользовательские HTTP-заголовки, используемые в запросах браузера:

- **User-Agent**: Устанавливает строку user-agent для браузера.
- **Accept**: Устанавливает типы данных, которые браузер готов принимать.
- **Accept-Charset**: Устанавливает кодировку символов, поддерживаемую браузером.
- **Accept-Encoding**: Устанавливает поддерживаемые методы кодирования (установите значение `none`, чтобы отключить).
- **Accept-Language**: Устанавливает предпочтительные языки.
- **Connection**: Устанавливает тип соединения, который должен использовать браузер (например, `keep-alive`).

## Использование

Чтобы использовать `Edge` WebDriver в своем проекте, просто импортируйте и инициализируйте его:

```python
from src.webdriver.edge import Edge

# Инициализация Edge WebDriver с настройками user-agent и пользовательскими параметрами
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()
```

Класс `Edge` автоматически загружает настройки из файла `edge.json` и использует их для настройки WebDriver. Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

### Паттерн Singleton

`Edge` WebDriver использует паттерн Singleton. Это означает, что будет создан только один экземпляр WebDriver. Если экземпляр уже существует, он будет повторно использован, и будет открыто новое окно.

## Ведение журнала и отладка

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, настройки или выполнения, будут регистрироваться для облегчения отладки.

### Пример журналов

- **Ошибка во время инициализации WebDriver**: `Error initializing Edge WebDriver: <error details>`
- **Проблемы с конфигурацией**: `Error in edge.json file: <issue details>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](../../LICENSE).

### Как использовать этот блок кода

Описание
-------------------------
Этот код описывает структуру и использование модуля Edge WebDriver для Selenium. Он предоставляет информацию о настройке, требованиях и примеры использования для автоматизации браузера Edge.

Шаги выполнения
-------------------------
1. **Установка зависимостей**: Установите Selenium и Fake User Agent с помощью `pip install selenium fake_useragent`.
2. **Настройка Edge WebDriver**: Убедитесь, что двоичный файл `msedgedriver` доступен в системном `PATH` или укажите его путь в конфигурации.
3. **Создание файла конфигурации**: Создайте файл `edge.json` с необходимыми параметрами, такими как `options`, `profiles`, `executable_path` и `headers`.
4. **Инициализация Edge WebDriver**: Импортируйте класс `Edge` из `src.webdriver.edge` и инициализируйте его с необходимыми параметрами.
5. **Использование WebDriver**: Используйте методы `get` для открытия веб-сайтов и `quit` для закрытия браузера.

Пример использования
-------------------------

```python
from src.webdriver.edge import Edge

# Инициализация Edge WebDriver с настройками user-agent и пользовательскими параметрами
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()