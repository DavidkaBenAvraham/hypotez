# Модуль обучения модели машинного обучения кодовой базе, составления документации к проекту, примеров кода и тестов

## Обзор

Модуль `code_assistant.py` предоставляет функциональность для обучения моделей машинного обучения кодовой базе проекта `hypotez`, составления документации, примеров кода и тестов. 

## Подробнее

Модуль `code_assistant.py` использует класс `CodeAssistant`, который читает файлы кода, передает их в выбранную модель машинного обучения (например, Google Gemini или OpenAI), обрабатывает результаты и сохраняет их в директории `docs/gemini`. 

## Классы

### `CodeAssistant`

**Описание**: Класс, который реализует функциональность ассистента программиста для взаимодействия с моделями ИИ. 

**Атрибуты**:

- `role` (str): Роль, которую выполняет ассистент (например, `doc_writer_md`, `code_checker`).
- `lang` (str): Язык, на котором ассистент работает (например, `ru`, `en`).
- `gemini` (`GoogleGenerativeAi`): Экземпляр класса `GoogleGenerativeAi` для взаимодействия с Google Gemini.
- `openai` (`OpenAIModel`): Экземпляр класса `OpenAIModel` для взаимодействия с моделями OpenAI.

**Методы**:

- `__init__`: Инициализирует ассистента с заданными параметрами.
- `send_file`: Отправляет файл в модель.
- `process_files`: Обрабатывает файлы в указанных директориях.
- `_create_request`: Создает запрос к модели.
- `_yield_files_content`: Генерирует пары (путь к файлу, содержимое) для обработки.
- `_save_response`: Сохраняет ответ модели в файл.
- `_remove_outer_quotes`: Удаляет внешние кавычки в начале и конце строки.
- `run`: Запускает процесс обработки файлов.
- `_signal_handler`: Обрабатывает прерывание выполнения.

### `Config`

**Описание**: Класс для хранения конфигурационных параметров. 

**Атрибуты**:

- `ENDPOINT`: Путь к директории с конфигурационными файлами.
- `config`: Объект `SimpleNamespace`, содержащий конфигурационные данные из файла `code_assistant.json`.
- `roles_list`: Список доступных ролей.
- `languages_list`: Список доступных языков.
- `role`: Текущая роль ассистента.
- `lang`: Текущий язык работы.
- `process_dirs`: Список директорий для обработки файлов.
- `exclude_dirs`: Список директорий, которые нужно исключить из обработки.
- `exclude_files_patterns`: Список паттернов для исключения файлов.
- `include_files_patterns`: Список паттернов для включения файлов.
- `exclude_files`: Список файлов, которые нужно исключить из обработки.
- `response_mime_type`: Тип контента ответа модели.
- `output_directory_patterns`: Список паттернов для вывода результата.
- `remove_prefixes`: Список префиксов для удаления из ответа модели.
- `code_instruction`: Инструкция для кода.
- `system_instruction`: Инструкция для модели.
- `gemini`: Объект `SimpleNamespace` для настройки модели Google Gemini.

## Функции

### `parse_args`

**Назначение**: Разбирает аргументы командной строки.

**Параметры**:

- None

**Возвращает**:

- `dict`: Словарь с аргументами командной строки.

### `main`

**Назначение**: Функция запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.

**Параметры**:

- None

**Возвращает**:

- None

**Как работает**:

- Функция `main` запускает цикл, в котором перебираются все роли и языки, определенные в классе `Config`.
- Для каждой комбинации роли и языка создается экземпляр класса `CodeAssistant`, который обрабатывает файлы в указанных директориях. 
- `main` вызывает метод `process_files`, который перебирает все файлы в указанных директориях, читает их содержимое и отправляет запрос к модели машинного обучения. 
- После обработки файлов, `process_files` сохраняет ответ модели в файл с соответствующим расширением, в зависимости от роли.

## Параметры класса

### `Config`

- `ENDPOINT`: Путь к директории с конфигурационными файлами.
- `config`: Объект `SimpleNamespace`, содержащий конфигурационные данные из файла `code_assistant.json`.
- `roles_list`: Список доступных ролей.
- `languages_list`: Список доступных языков.
- `role`: Текущая роль ассистента.
- `lang`: Текущий язык работы.
- `process_dirs`: Список директорий для обработки файлов.
- `exclude_dirs`: Список директорий, которые нужно исключить из обработки.
- `exclude_files_patterns`: Список паттернов для исключения файлов.
- `include_files_patterns`: Список паттернов для включения файлов.
- `exclude_files`: Список файлов, которые нужно исключить из обработки.
- `response_mime_type`: Тип контента ответа модели.
- `output_directory_patterns`: Список паттернов для вывода результата.
- `remove_prefixes`: Список префиксов для удаления из ответа модели.
- `code_instruction`: Инструкция для кода.
- `system_instruction`: Инструкция для модели.
- `gemini`: Объект `SimpleNamespace` для настройки модели Google Gemini.

## Методы класса `CodeAssistant`

### `__init__`

**Описание**: Инициализирует ассистента с заданными параметрами.

**Параметры**:

- `role` (Optional[str], optional): Роль для выполнения задачи. По умолчанию `'doc_writer_md'`.
- `lang` (Optional[str], optional): Язык выполнения. По умолчанию `'en'`.
- `model_name` (Optional[str], optional): Название модели для инициализации. По умолчанию `''`.
- `system_instruction` (Optional[str | Path], optional): Общая инструкция для модели. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для инициализации моделей.

**Возвращает**:

- None

**Как работает**:

- Метод `__init__` устанавливает значения параметров `role` и `lang` из аргументов функции или из значений по умолчанию. 
- Затем метод инициализирует модель Google Gemini (`GoogleGenerativeAi`) с использованием параметров `model_name`, `api_key`, `system_instruction` и `response_mime_type`, которые передаются в метод `__init__` или берутся из класса `Config`.

### `send_file`

**Описание**: Отправляет файл в модель.

**Параметры**:

- `file_path` (Path): Абсолютный путь к файлу, который нужно отправить.
- `file_name` (Optional[str]): Имя файла для отправки. Если не указано, используется имя файла без изменений.

**Возвращает**:

- Optional[str | None]: URL файла, если отправлен успешно, иначе `None`.

**Как работает**:

- Метод `send_file` отправляет файл в модель Google Gemini (`GoogleGenerativeAi`) с использованием метода `upload_file`. 
- Если отправка прошла успешно, метод возвращает URL файла. 
- В случае ошибки, метод возвращает `None`.

### `process_files`

**Описание**: Обрабатывает файлы в указанных директориях.

**Параметры**:

- `process_dirs` (Optional[str | Path | list[str | Path]], optional): Список директорий для обработки. По умолчанию `None`.
- `save_response` (bool, optional): Флаг, указывающий, нужно ли сохранять ответ модели. По умолчанию `True`.

**Возвращает**:

- bool: `True`, если обработка завершена успешно, иначе `False`.

**Как работает**:

- Метод `process_files` перебирает все директории в списке `process_dirs` и для каждой директории вызывает метод `_yield_files_content` для получения списка файлов и их содержимого. 
- Затем, для каждого файла метод `process_files` создает запрос к модели с использованием метода `_create_request`, отправляет запрос с использованием метода `gemini.ask_async` и сохраняет ответ в файл с использованием метода `_save_response`.

### `_create_request`

**Описание**: Создает запрос к модели с учетом роли и языка.

**Параметры**:

- `file_path` (str): Путь к файлу.
- `content` (str): Содержимое файла.

**Возвращает**:

- str: Запрос к модели в виде строки.

**Как работает**:

- Метод `_create_request` формирует запрос к модели в виде словаря, который содержит следующие поля:
    - `role`: Роль, которую выполняет ассистент.
    - `output_language`: Язык, на котором ассистент работает.
    - `file_location_in_project_hypotez`: Путь к файлу относительно корневой директории проекта `hypotez`.
    - `instruction`: Инструкция для кода.
    - `input_code`: Содержимое файла в формате ````python\n...````.
- Затем, метод преобразует словарь в строку и возвращает его.

### `_yield_files_content`

**Описание**: Генерирует пары (путь к файлу, содержимое) для обработки.

**Параметры**:

- `process_directory` (Path | str): Абсолютный путь к стартовой директории.

**Возвращает**:

- bool: Iterator

**Как работает**:

- Метод `_yield_files_content` перебирает все файлы в указанной директории и ее поддиректориях, исключая файлы и директории, которые указаны в конфигурации. 
- Для каждого файла, метод считывает его содержимое и возвращает пару (путь к файлу, содержимое).

### `_save_response`

**Описание**: Сохраняет ответ модели в файл с добавлением суффикса.

**Параметры**:

- `file_path` (Path): Исходный путь к файлу, в который будет записан ответ.
- `response` (str): Ответ модели, который необходимо сохранить.
- `model_name` (str): Имя модели, использованной для генерации ответа.

**Возвращает**:

- bool: `True`, если сохранение прошло успешно, иначе `False`.

**Как работает**:

- Метод `_save_response` формирует путь к файлу, в который будет записан ответ. 
- Путь к файлу зависит от роли, языка, модели и исходного пути к файлу. 
- Затем, метод создает директорию, если она не существует, и записывает ответ модели в файл. 

### `_remove_outer_quotes`

**Описание**: Удаляет внешние кавычки в начале и конце строки.

**Параметры**:

- `response` (str): Ответ модели, который необходимо обработать.

**Возвращает**:

- str: Очищенный контент как строка.

**Как работает**:

- Метод `_remove_outer_quotes` проверяет, начинается ли строка с `'```python'` или `'```mermaid'`. 
- Если да, то строка возвращается без изменений. 
- В противном случае, метод удаляет внешние кавычки из строки и возвращает результат.

### `run`

**Описание**: Запускает процесс обработки файлов.

**Параметры**:

- `start_from_file` (int, optional): Номер файла, с которого начать обработку. По умолчанию `1`.

**Возвращает**:

- None

**Как работает**:

- Метод `run` запускает асинхронный процесс обработки файлов с использованием метода `process_files`. 
- Метод также устанавливает обработчик сигнала `SIGINT`, который позволяет прервать выполнение процесса с помощью `Ctrl+C`.

### `_signal_handler`

**Описание**: Обрабатывает прерывание выполнения.

**Параметры**:

- `signal`: Сигнал, который был получен.
- `frame`: Текущий кадр стека.

**Возвращает**:

- None

**Как работает**:

- Метод `_signal_handler` выводит сообщение о том, что процесс был прерван, и завершает работу программы.

## Примеры

### **Пример использования `CodeAssistant`**

```python
# Создание экземпляра класса `CodeAssistant`
assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
# Запуск процесса обработки файлов
assistant.process_files()
```

### **Пример создания запроса к модели**

```python
file_path = 'hypotez/src/endpoints/hypo69/code_assistant/code_assistant.py'
content = """
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
content_request = assistant._create_request(file_path, content)
print(content_request)
```

## Дополнительные сведения

- Документация для `GoogleGenerativeAi` и `OpenAIModel` находится в соответствующих модулях.
- Для работы модуля `code_assistant.py` необходимо указать конфигурационные параметры в файле `code_assistant.json`.
- Модель `Google Gemini` использует API-ключ, который нужно указать в переменной окружения `GEMINI_API_KEY`.

## Твое поведение при анализе кода:

- В коде ты можешь встретить выражение между `<` `>`. Например: `<инструкция для модели gemini:Загрузка описаний продуктов в PrestaShop.>, <далее, если есть>. Это заготовки, куда ты вставляешь релевантное значение
- Всегда смотри системную инструкцию для обработки кода проекта `hypotez`;
- Анализируй расположение файла в проекте. Это поможет понять его назначение и взаимосвязь с другими файлами. Расположение файла ты найдешь в самой превой строке кода, начинающейся с `## \\file /...`;
- Запоминай предоставленный код и анализируй его связь с другими частями проекта;
- В этой инструкции не надо предлагать улучшение кода. Четко следуй пункту 5. **Пример файла** при составлении ответа