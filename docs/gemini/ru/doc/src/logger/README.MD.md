# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему ведения логов, поддерживающую вывод в консоль, файлы и JSON. В основе системы лежит паттерн проектирования Singleton, гарантирующий использование только одного экземпляра логгера в приложении. Логгер поддерживает различные уровни ведения журнала (например, `INFO`, `ERROR`, `DEBUG`) и включает в себя цветной вывод для логов в консоль. Вы также можете настраивать форматы вывода журнала и управлять записью логов в различные файлы.

## Подробнее

### Классы

#### `class SingletonMeta`

**Описание**: Метакласс, реализующий паттерн проектирования Singleton для логгера.

**Наследует**:

- `type`

**Аттрибуты**:

- `instance`: Экземпляр логгера (Singleton).

**Методы**:

- `__call__`: Создает или возвращает существующий экземпляр логгера.

#### `class JsonFormatter`

**Описание**: Настраиваемый форматировщик, выводящий логи в формате JSON.

**Наследует**:

- `logging.Formatter`

**Аттрибуты**:

- `json_fields`: Список полей, которые будут включены в JSON-вывод.

**Методы**:

- `format`: Форматирует сообщение в JSON.

#### `class Logger`

**Описание**: Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

**Аттрибуты**:

- `_instance`: Экземпляр логгера (Singleton).
- `_console_logger`: Логгер для вывода в консоль.
- `_file_loggers`: Словарь логгеров для вывода в файлы.
- `_json_logger`: Логгер для вывода в JSON.

**Методы**:

- `__init__`: Инициализирует экземпляр логгера с заполнителями для различных типов логгеров (консоль, файл и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для вывода в консоль и файлы (info, debug, error и JSON).
- `log`: Выводит сообщение на заданном уровне (например, `INFO`, `DEBUG`, `ERROR`) с дополнительными параметрами для исключений и форматирования цвета.
- `info`: Выводит информационное сообщение.
- `success`: Выводит сообщение об успешном выполнении.
- `warning`: Выводит предупреждающее сообщение.
- `debug`: Выводит отладочное сообщение.
- `error`: Выводит сообщение об ошибке.
- `critical`: Выводит критическое сообщение.

### Функции

#### `__init__`

**Назначение**: Инициализирует экземпляр класса `Logger`.

**Параметры**:

- `self`: Экземпляр класса `Logger`.

**Возвращает**:

- `None`

**Как работает**:

- Инициализирует атрибуты класса `Logger`, включая заполнители для логгеров консоли, файлов и JSON.

#### `_configure_logger`

**Назначение**: Настраивает и возвращает экземпляр логгера.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `name`: Имя логгера.
- `log_path`: Путь к файлу журнала.
- `level`: Уровень ведения журнала (например, `logging.DEBUG`). По умолчанию `logging.DEBUG`.
- `formatter`: Настраиваемый форматировщик (необязательно).
- `mode`: Режим файла (например, `'a'` для добавления). По умолчанию `'a'`.

**Возвращает**:

- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Как работает**:

- Создает экземпляр `logging.Logger` с указанным именем.
- Добавляет обработчик (`StreamHandler` или `FileHandler`) в зависимости от `log_path`.
- Настраивает уровень ведения журнала и форматировщик.
- Возвращает настроенный экземпляр `logging.Logger`.

#### `initialize_loggers`

**Назначение**: Инициализирует логгеры для вывода в консоль и файлы (info, debug, error и JSON).

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `info_log_path`: Путь к файлу для info-логов (необязательно).
- `debug_log_path`: Путь к файлу для debug-логов (необязательно).
- `errors_log_path`: Путь к файлу для error-логов (необязательно).
- `json_log_path`: Путь к файлу для JSON-логов (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Настраивает логгер консоли с помощью `_configure_logger`.
- Настраивает логгеры файлов для info, debug, error и JSON с помощью `_configure_logger`.

#### `log`

**Назначение**: Выводит сообщение на заданном уровне (например, `INFO`, `DEBUG`, `ERROR`) с дополнительными параметрами для исключений и форматирования цвета.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `level`: Уровень ведения журнала (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение журнала.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `False`).
- `color`: Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает соответствующий метод логгера (например, `info`, `debug`, `error`) в зависимости от `level`.
- Передает сообщение, исключение и информацию об исключении в выбранный логгер.
- Форматирует сообщение с помощью `colorama` для цветного вывода в консоль.

#### `info`

**Назначение**: Выводит информационное сообщение.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Информационное сообщение для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.INFO` и переданными параметрами.

#### `success`

**Назначение**: Выводит сообщение об успешном выполнении.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Сообщение об успешном выполнении для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.INFO` и переданными параметрами.

#### `warning`

**Назначение**: Выводит предупреждающее сообщение.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Предупреждающее сообщение для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.WARNING` и переданными параметрами.

#### `debug`

**Назначение**: Выводит отладочное сообщение.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Отладочное сообщение для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.DEBUG` и переданными параметрами.

#### `error`

**Назначение**: Выводит сообщение об ошибке.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Сообщение об ошибке для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.ERROR` и переданными параметрами.

#### `critical`

**Назначение**: Выводит критическое сообщение.

**Параметры**:

- `self`: Экземпляр класса `Logger`.
- `message`: Критическое сообщение для записи в журнал.
- `ex`: Дополнительное исключение для записи в журнал (необязательно).
- `exc_info`: Указывает, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors`: Кортеж с цветами текста и фона для сообщения (необязательно).

**Возвращает**:

- `None`

**Как работает**:

- Вызывает `log` с `level=logging.CRITICAL` и переданными параметрами.

### Параметры для логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения ведения журнала.

- **Уровень**: Управляет серьезностью журналов, которые фиксируются. Распространенные уровни включают в себя:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, такая как успешные операции.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленного действия.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматировщик**: Определяет, как форматируются сообщения журнала. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить настраиваемый форматировщик для различных форматов, например, JSON.

- **Цвет**: Цвета для сообщений журнала в консоли. Цвета указываются как кортеж с двумя элементами:
  - **Цвет текста**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Цвет фона**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для различных уровней ведения журнала (например, зеленый для информации, красный для ошибок и т. д.).

### Настройка ведения журнала в файлы (`config`)

Чтобы записывать сообщения журнала в файл, вы можете указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня ведения журнала.

### Пример использования

#### 1. Инициализация логгера:

```python
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

#### 2. Ведение журналов на различных уровнях:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешном выполнении')
logger.warning('Это предупреждающее сообщение')
logger.debug('Это отладочное сообщение')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение будет иметь красный фон', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

Этот модуль предоставляет комплексную и гибкую систему ведения журнала для приложений Python. Вы можете настраивать ведение журнала в консоль и файлы с различными форматами и цветами, управлять уровнями ведения журнала и элегантно обрабатывать исключения. Настройка ведения журнала в файлы хранится в словаре `config`, что позволяет легко настроить параметры.