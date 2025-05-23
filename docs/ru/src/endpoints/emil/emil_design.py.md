# Модуль `src.endpoints.emil.emil_design`

## Обзор

Модуль предназначен для управления и обработки изображений, а также для продвижения товаров в Facebook и PrestaShop, связанных с магазином `emil-design.com`.

## Подробней

Этот модуль предоставляет функциональность для:
- Описания изображений с использованием Gemini AI.
- Загрузки описаний товаров в PrestaShop.
- Автоматизации процессов продвижения и управления контентом для магазина `emil-design.com`.

## Классы

### `Config`

**Описание**: Класс конфигурации для `EmilDesign`.

**Атрибуты**:
- `ENDPOINT` (str): Конечная точка API, по умолчанию `'emil'`.
- `MODE` (str): Определяет конечную точку API. Возможные значения: `'dev'` (PrestaShop 1.7), `'dev8'` (PrestaShop 8), `'prod'` (рабочий магазин PrestaShop 1.7). По умолчанию `'dev'`.
- `POST_FORMAT` (str): Формат POST-запросов, по умолчанию `'XML'`.
- `API_DOMAIN` (str): Домен API.
- `API_KEY` (str): Ключ API.
- `suppliers` (list): Список поставщиков, загружаемый из файла `emil.json`.

**Принцип работы**:
Класс `Config` предназначен для хранения и управления конфигурационными параметрами, необходимыми для работы с API PrestaShop и другими сервисами. Он определяет параметры подключения к различным окружениям PrestaShop (dev, dev8, prod) и загружает список поставщиков из JSON-файла.
В зависимости от значения `USE_ENV` класс либо использует переменные окружения, либо значения, заданные непосредственно в коде или в файле конфигурации.

### `EmilDesign`

**Описание**: Класс для проектирования и продвижения изображений через различные платформы.

**Атрибуты**:
- `gemini` (Optional[GoogleGenerativeAi]): Экземпляр класса `GoogleGenerativeAi` для работы с Gemini AI.
- `openai` (Optional[OpenAIModel]): Экземпляр класса `OpenAIModel` для работы с OpenAI.
- `base_path` (Path): Базовый путь к каталогу с данными, связанными с `EmilDesign`.
- `config` (SimpleNamespace): Объект, содержащий конфигурационные параметры, загруженные из `emil.json`.
- `data_path` (Path): Путь к каталогу для хранения данных, таких как изображения и описания.
- `gemini_api` (str): Ключ API для Gemini AI.
- `presta_api` (str): Ключ API для PrestaShop.
- `presta_domain` (str): Доменное имя PrestaShop.

**Методы**:
- `process_suppliers`: Обрабатывает поставщиков на основе предоставленного префикса.
- `describe_images`: Описывает изображения на основе предоставленной инструкции и примеров.
- `promote_to_facebook`: Продвигает изображения и их описания в Facebook.
- `upload_described_products_to_prestashop`: Загружает информацию о продуктах в PrestaShop.

## Методы класса

### `process_suppliers`

```python
async def process_suppliers(self, supplier_prefix: Optional[str | List[str, str]] = '') -> bool:
    """
    Обрабатывает поставщиков на основе предоставленного префикса.

    Args:
        supplier_prefix (Optional[str | List[str, str]], optional): Префикс для поставщиков. По умолчанию ''.

    Returns:
        bool: True, если обработка прошла успешно, False в противном случае.

    Raises:
        Exception: Если во время обработки поставщиков произошла ошибка.

    
    - Проверяет, был ли предоставлен префикс поставщика. Если да, использует его; в противном случае использует список поставщиков из конфигурации.
    - Итерируется по префиксам поставщиков.
    - Для каждого префикса пытается получить грабер с помощью функции `get_graber_by_supplier_prefix`.
    - Если грабер не найден, записывает предупреждение в лог и переходит к следующему префиксу.
    - Если грабер найден, асинхронно выполняет сценарии обработки и записывает информацию в лог.
    - Обрабатывает любые исключения, возникшие в процессе, записывает ошибки в лог и возвращает False.
    """
```

**Примеры**:
```python
emil = EmilDesign()
asyncio.run(emil.process_suppliers(supplier_prefix='supplier1'))
```

### `describe_images`

```python
def describe_images(
    self,
    lang: str,
    models: dict = {
        'gemini': {'model_name': 'gemini-1.5-flash'},
        'openai': {'model_name': 'gpt-4o-mini', 'assistant_id': 'asst_uDr5aVY3qRByRwt5qFiMDk43'},
    },
) -> None:
    """
    Описывает изображения на основе предоставленной инструкции и примеров.

    Args:
        lang (str): Язык для описания.
        models (dict, optional): Конфигурация моделей. По умолчанию модели Gemini и OpenAI.

    Returns:
        None

    Raises:
        FileNotFoundError: Если файлы инструкций не найдены.
        Exception: Если во время обработки изображения произошла ошибка.

    
    - Определяет пути к файлам инструкций и категорий мебели на основе предоставленного языка.
    - Читает содержимое файлов инструкций и категорий мебели.
    - Объединяет системную инструкцию с категориями мебели и промптом.
    - Определяет пути к выходному JSON-файлу и файлу с описанными изображениями.
    - Читает список уже описанных изображений из файла.
    - Получает список файлов изображений из указанной директории.
    - Фильтрует список изображений, чтобы оставить только те, которые еще не были описаны.
    - Инициализирует модели Gemini и/или OpenAI, если они должны использоваться.
    - Для каждого изображения выполняет следующие действия:
        - Получает необработанные данные изображения.
        - Отправляет запрос в Gemini для получения описания изображения.
        - Если описание получено успешно, сохраняет его в JSON-файл, добавляет путь к изображению в список описанных изображений и сохраняет список в файл.
        - Если описание не получено, записывает отладочное сообщение в лог.
        - Делает задержку между запросами.
    - Обрабатывает исключения, которые могут возникнуть в процессе, и записывает ошибки в лог.
    """
```

**Примеры**:
```python
emil = EmilDesign()
emil.describe_images(lang='he')
```

### `promote_to_facebook`

```python
async def promote_to_facebook(self) -> None:
    """
    Продвигает изображения и их описания в Facebook.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Если во время продвижения в Facebook произошла ошибка.

    
    - Инициализирует драйвер Chrome.
    - Открывает указанный URL группы Facebook.
    - Загружает описания изображений из JSON-файла.
    - Для каждого описания создает объект `SimpleNamespace` с информацией о заголовке, описании и пути к изображению.
    - Вызывает функцию `post_message` для публикации сообщения в Facebook.
    - Обрабатывает исключения, которые могут возникнуть в процессе, и записывает ошибки в лог.
    """
```

**Примеры**:
```python
emil = EmilDesign()
asyncio.run(emil.promote_to_facebook())
```

### `upload_described_products_to_prestashop`

```python
def upload_described_products_to_prestashop(
    self, products_list: Optional[List[SimpleNamespace]] = None, id_lang: Optional[int | str] = 2, *args, **kwargs
) -> bool:
    """
    Загружает информацию о продуктах в PrestaShop.

    Args:
        products_list (Optional[List[SimpleNamespace]], optional): Список информации о продуктах. По умолчанию None.
        id_lang (Optional[str], optional): ID языка для базы данных PrestaShop.
        Обычно я назначаю языки в таком порядке 1 - en;2 - he; 3 - ru. 
        Важно проверить порядок якыков целевой базе данных.
        Вот образец кода для получения слопваря языков из конкретной базы данных
        >>import language
        >>lang_class = PrestaLanguage()
        >>print(lang_class.get_languages_schema())

    Returns:
        bool: True, если загрузка прошла успешно, False в противном случае.

    Raises:
        FileNotFoundError: Если файл локалей не найден.
        Exception: Если во время загрузки в PrestaShop произошла ошибка.

    
    - Получает список файлов продуктов из указанной директории.
    - Загружает информацию о продуктах из JSON-файлов.
    - Инициализирует класс `PrestaProduct` с доменом и ключом API.
    - Определяет ID языка, на котором будут отображаться названия и характеристики товара.
    - Загружает локали из файла `locales.json`.
    - Итерируется по списку продуктов.
    - Для каждого продукта создает объект `ProductFields` и заполняет его данными из JSON.
    - Вызывает метод `add_new_product` класса `PrestaProduct` для добавления продукта в PrestaShop.
    - Обрабатывает исключения, которые могут возникнуть в процессе, и записывает ошибки в лог.
    """
```

**Примеры**:
```python
emil = EmilDesign()
emil.upload_described_products_to_prestashop(id_lang=2)
```

## Параметры класса

- `gemini` (Optional[GoogleGenerativeAi]): Экземпляр класса `GoogleGenerativeAi` для работы с Gemini AI.
- `openai` (Optional[OpenAIModel]): Экземпляр класса `OpenAIModel` для работы с OpenAI.
- `base_path` (Path): Базовый путь к каталогу с данными, связанными с `EmilDesign`.
- `config` (SimpleNamespace): Объект, содержащий конфигурационные параметры, загруженные из `emil.json`.
- `data_path` (Path): Путь к каталогу для хранения данных, таких как изображения и описания.
- `gemini_api` (str): Ключ API для Gemini AI.
- `presta_api` (str): Ключ API для PrestaShop.
- `presta_domain` (str): Доменное имя PrestaShop.