## \file hypotez/src/webdriver/playwright/README.MD
# Модуль Playwright Crawler для автоматизации браузера

Этот модуль предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Playwright. Он позволяет настраивать параметры запуска браузера, такие как user-agent, настройки прокси, размер области просмотра и другие параметры, определенные в файле `playwrid.json`.

## Основные характеристики

- **Централизованная конфигурация**: Управление конфигурацией осуществляется через файл `playwrid.json`.
- **Поддержка пользовательских опций**: Возможность передачи пользовательских опций во время инициализации.
- **Улучшенное ведение журнала и обработка ошибок**: Предоставляет подробные журналы для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Поддержка прокси**: Настройка прокси-серверов для обхода ограничений.
- **Гибкие настройки браузера**: Настройка размера области просмотра, user-agent и других параметров браузера.

## Требования

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

- Python 3.x
- Playwright
- Crawlee

Установите необходимые зависимости Python:

```bash
pip install playwright crawlee
```

Кроме того, убедитесь, что Playwright установлен и настроен для работы с браузером. Установите браузеры с помощью команды:

```bash
playwright install
```

## Конфигурация

Конфигурация для Playwright Crawler хранится в файле `playwrid.json`. Ниже приведена примерная структура файла конфигурации и его описание:

### Пример конфигурации (`playwrid.json`)

```json
{
  "browser_type": "chromium",
  "headless": true,
  "options": [
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-gpu"
  ],
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "proxy": {
    "enabled": false,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "timeout": 30000,
  "ignore_https_errors": false
}
```

### Описание полей конфигурации

#### 1. `browser_type`

Тип используемого браузера. Возможные значения:

- `chromium` (по умолчанию)
- `firefox`
- `webkit`

#### 2. `headless`

Логическое значение, указывающее, должен ли браузер работать в режиме без графического интерфейса. По умолчанию `true`.

#### 3. `options`

Список аргументов командной строки, передаваемых в браузер. Примеры:

- `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker.
- `--no-sandbox`: Отключает режим песочницы.
- `--disable-gpu`: Отключает аппаратное ускорение GPU.

#### 4. `user_agent`

Строка user-agent, используемая для запросов браузера.

#### 5. `proxy`

Настройки прокси-сервера:

- **enabled**: Логическое значение, указывающее, следует ли использовать прокси.
- **server**: Адрес прокси-сервера.
- **username**: Имя пользователя для аутентификации прокси.
- **password**: Пароль для аутентификации прокси.

#### 6. `viewport`

Размеры окна браузера:

- **width**: Ширина окна.
- **height**: Высота окна.

#### 7. `timeout`

Максимальное время ожидания для операций (в миллисекундах). По умолчанию `30000` (30 секунд).

#### 8. `ignore_https_errors`

Логическое значение, указывающее, следует ли игнорировать ошибки HTTPS. По умолчанию `false`.

## Использование

Чтобы использовать `Playwrid` в своем проекте, просто импортируйте и инициализируйте его:

```python
from src.webdriver.playwright import Playwrid

# Инициализация Playwright Crawler с пользовательскими опциями
browser = Playwrid(options=["--headless"])

# Запуск браузера и переход на веб-сайт
browser.start("https://www.example.com")
```

Класс `Playwrid` автоматически загружает настройки из файла `playwrid.json` и использует их для настройки WebDriver. Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

## Ведение журнала и отладка

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, настройки или выполнения, будут регистрироваться для облегчения отладки.

### Пример журналов

- **Ошибка во время инициализации WebDriver**: `Error initializing Playwright Crawler: <error details>`
- **Проблемы с конфигурацией**: `Error in playwrid.json file: <issue details>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](../../LICENSE).

                ```rst
 .. module:: src.webdriver.playwright
```

Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный раздел документации описывает модуль `Playwright Crawler` для автоматизации браузера с использованием библиотеки Playwright. Он предоставляет информацию о конфигурации, использовании и настройке модуля.

Шаги выполнения
-------------------------
1. **Установка зависимостей**: Установка необходимых библиотек, таких как `playwright` и `crawlee`, с помощью `pip install playwright crawlee`.
2. **Установка Playwright**: Установка браузеров для Playwright с помощью команды `playwright install`.
3. **Конфигурация модуля**: Настройка параметров браузера в файле `playwrid.json`, таких как тип браузера, режим headless, user-agent и настройки прокси.
4. **Использование модуля**: Импорт класса `Playwrid` и инициализация его с пользовательскими опциями.
5. **Запуск браузера**: Запуск браузера и переход на указанный веб-сайт с помощью метода `start`.
6. **Ведение журнала**: Просмотр журналов для отладки и выявления проблем с инициализацией и конфигурацией.

Пример использования
-------------------------

```python
from src.webdriver.playwright import Playwrid

# Инициализация Playwright Crawler с пользовательскими опциями
browser = Playwrid(options=["--headless"])

# Запуск браузера и переход на веб-сайт
browser.start("https://www.example.com")