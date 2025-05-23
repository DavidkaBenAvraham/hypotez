# Модуль для работы с Llama.cpp

## Обзор

Этот модуль предоставляет интерфейс для взаимодействия с моделью Llama.cpp, используемой для генерации текста. Он импортирует библиотеку `llama_cpp` и конфигурирует модель для использования. 

## Подробее

Модуль `src/ai/llama/model.py` устанавливает связь с моделью Llama.cpp с помощью  библиотеки `llama_cpp`. 

## Классы

### `Llama`

**Описание**: Класс `Llama` предоставляет  доступ к модели Llama.cpp, используя библиотеку `llama_cpp`. 

**Атрибуты**:

* `repo_id` (str): Идентификатор репозитория модели Llama.cpp, который используется для загрузки модели.
* `filename` (str): Имя файла модели Llama.cpp.

**Методы**:

* `from_pretrained(repo_id: str, filename: str)`: Статический метод, который создает экземпляр `Llama` и загружает модель Llama.cpp из указанного репозитория и файла.

**Принцип работы**:
Класс `Llama` обеспечивает доступ к модели Llama.cpp. Используя методы этого класса, можно получить доступ к модели для  генерации текста.

## Функции

### `llm`

**Назначение**:  Создает экземпляр модели `Llama` с помощью функции `Llama.from_pretrained`  из библиотеки `llama_cpp`.

**Параметры**:

* `repo_id` (str): Идентификатор репозитория модели Llama.cpp.
* `filename` (str): Имя файла модели Llama.cpp.

**Возвращает**:
* `Llama`:  Экземпляр модели `Llama`.

**Принцип работы**:
Функция `llm` инициализирует экземпляр модели `Llama`.

### `output`

**Назначение**:  Запускает процесс генерации текста с помощью модели `Llama`.

**Параметры**:

* `text` (str): Текст, который используется для запуска генерации.
* `max_tokens` (int): Максимальное количество токенов, которые генерируются.
* `echo` (bool): Флаг, который включает/отключает вывод исходного текста, заданного в параметре `text`.

**Возвращает**:
* `str`: Сгенерированный текст.

**Принцип работы**:
Функция `output` использует модель `Llama` для генерации текста на основе указанного `text`, устанавливает максимальное количество токенов и  включает/отключает вывод исходного текста.

## Примеры:

```python
# Создание экземпляра модели Llama
llm = Llama.from_pretrained(
    repo_id="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
    filename="Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf",
)

# Запуск генерации текста
output = llm(
    "Once upon a time,",
    max_tokens=512,
    echo=True
)

# Вывод сгенерированного текста
print(output)