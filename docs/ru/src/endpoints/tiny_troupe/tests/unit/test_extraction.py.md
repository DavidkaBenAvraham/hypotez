# Модуль тестирования извлечения (`test_extraction.py`)

## Обзор

Модуль содержит юнит-тесты для проверки функциональности извлечения и нормализации данных в проекте `tinytroupe`. Он проверяет правильность экспорта артефактов в различных форматах (JSON, текст, DOCX) и нормализацию концепций с использованием класса `Normalizer`.

## Подробнее

Этот модуль использует библиотеку `pytest` для организации и запуска тестов. Он проверяет экспорт данных в различных форматах, таких как JSON, текст и DOCX, с использованием класса `ArtifactExporter`. Также модуль тестирует нормализацию концепций с использованием класса `Normalizer`.

## Классы

### `ArtifactExporter`

**Описание**: Класс для экспорта артефактов в различные форматы.

**Методы**:

-   `export(name, data, content_type, content_format=None, target_format="json")`: Экспортирует данные артефакта в указанный формат.

### `Normalizer`

**Описание**: Класс для нормализации концепций.

**Атрибуты**:

*   `normalized_elements (int)`: количество нормализованных элементов
*   `normalizing_map (dict)`: словарь нормализации

**Методы**:

-   `__init__(concepts, n=10, verbose=True)`: инициализирует класс Normalizer с заданными концепциями, количеством нормализованных элементов и флагом verbose.
-   `normalize(bucket)`: Нормализует список концепций.

## Фикстуры

### `exporter`

```python
@pytest.fixture
def exporter():
    return ArtifactExporter(base_output_folder=EXPORT_BASE_FOLDER)
```

**Назначение**: Создает экземпляр класса `ArtifactExporter` с базовой папкой для экспорта, используемой в тестах.

**Возвращает**:

*   `ArtifactExporter`: Экземпляр класса `ArtifactExporter`.

## Функции

### `test_export_json`

```python
def test_export_json(exporter):
    """Функция проверяет экспорт артефакта в формате JSON.

    Args:
        exporter: Экземпляр класса `ArtifactExporter`, используемый для экспорта.
    """
    # Define the artifact data
    artifact_data = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Engineer",
        "content": "This is a sample JSON data."
    }
    
    # Export the artifact data as JSON
    exporter.export("test_artifact", artifact_data, content_type="record", target_format="json")
    
    #check if the JSON file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/record/test_artifact.json"), "The JSON file should have been exported."

    # does it contain the data?
    with open(f"{EXPORT_BASE_FOLDER}/record/test_artifact.json", "r") as f:
        exported_data = json.load(f)
        assert exported_data == artifact_data, "The exported JSON data should match the original data."
```

**Назначение**: Проверяет экспорт данных в формате JSON с использованием класса `ArtifactExporter`.

**Параметры**:

*   `exporter`: Экземпляр класса `ArtifactExporter`, предоставляемый фикстурой `exporter`.

**Как работает функция**:

1.  Определяются данные артефакта в виде словаря `artifact_data`.
2.  Вызывается метод `export` класса `ArtifactExporter` для экспорта данных в формате JSON.
3.  Проверяется, существует ли файл JSON в указанной директории.
4.  Файл открывается, и его содержимое сравнивается с оригинальными данными.

### `test_export_text`

```python
def test_export_text(exporter):
    """Функция проверяет экспорт артефакта в формате текста.

    Args:
        exporter: Экземпляр класса `ArtifactExporter`, используемый для экспорта.
    """
    # Define the artifact data
    artifact_data = "This is a sample text."
    
    # Export the artifact data as text
    exporter.export("test_artifact", artifact_data, content_type="text", target_format="txt")
    
    # check if the text file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/text/test_artifact.txt"), "The text file should have been exported."

    # does it contain the data?
    with open(f"{EXPORT_BASE_FOLDER}/text/test_artifact.txt", "r") as f:
        exported_data = f.read()
        assert exported_data == artifact_data, "The exported text data should match the original data."
```

**Назначение**: Проверяет экспорт данных в формате текста с использованием класса `ArtifactExporter`.

**Параметры**:

*   `exporter`: Экземпляр класса `ArtifactExporter`, предоставляемый фикстурой `exporter`.

**Как работает функция**:

1.  Определяются данные артефакта в виде строки `artifact_data`.
2.  Вызывается метод `export` класса `ArtifactExporter` для экспорта данных в формате текста.
3.  Проверяется, существует ли файл TXT в указанной директории.
4.  Файл открывается, и его содержимое сравнивается с оригинальными данными.

### `test_export_docx`

```python
def test_export_docx(exporter):
    """Функция проверяет экспорт артефакта в формате DOCX.

    Args:
        exporter: Экземпляр класса `ArtifactExporter`, используемый для экспорта.
    """
    # Define the artifact data. Include some fancy markdown formatting so we can test if it is preserved.
    artifact_data ="""
    # This is a sample markdown text
    This is a **bold** text.
    This is an *italic* text.
    This is a [link](https://www.example.com).
    """
    
    # Export the artifact data as a docx file
    exporter.export("test_artifact", artifact_data, content_type="Document", content_format="markdown", target_format="docx")
    
    # check if the docx file was exported correctly
    assert os.path.exists(f"{EXPORT_BASE_FOLDER}/Document/test_artifact.docx"), "The docx file should have been exported."

    # does it contain the data?
    from docx import Document
    doc = Document(f"{EXPORT_BASE_FOLDER}/Document/test_artifact.docx")
    exported_data = ""
    for para in doc.paragraphs:
        exported_data += para.text

    assert "This is a sample markdown text" in exported_data, "The exported docx data should contain some of the original content."
    assert "#" not in exported_data, "The exported docx data should not contain Markdown."
```

**Назначение**: Проверяет экспорт данных в формате DOCX с использованием класса `ArtifactExporter`.

**Параметры**:

*   `exporter`: Экземпляр класса `ArtifactExporter`, предоставляемый фикстурой `exporter`.

**Как работает функция**:

1.  Определяются данные артефакта в виде строки `artifact_data` с использованием Markdown-форматирования.
2.  Вызывается метод `export` класса `ArtifactExporter` для экспорта данных в формате DOCX.
3.  Проверяется, существует ли файл DOCX в указанной директории.
4.  Файл открывается с использованием библиотеки `docx`, и его содержимое извлекается.
5.  Проверяется, содержит ли экспортированный файл часть оригинального содержимого, но не содержит Markdown-разметку.

### `test_normalizer`

```python
def test_normalizer():
    """Функция проверяет нормализацию концепций с использованием класса `Normalizer`."""
    # Define the concepts to be normalized
    concepts = ['Antique Book Collection', 'Medical Research', 'Electrical safety', 'Reading', 'Technology', 'Entrepreneurship', 'Multimedia Teaching Tools', 'Photography', 
     'Smart home technology', 'Gardening', 'Travel', 'Outdoors', 'Hiking', 'Yoga', 'Finance', 'Health and wellness', 'Sustainable Living', 'Barista Skills', 'Oral health education',
     'Patient care', 'Professional Development', 'Project safety', 'Coffee', 'Literature', 'Continuous learning', 'Model trains', 'Education', 'Mental and Physical Balance', 'Kayaking',
     'Social Justice', 'National Park Exploration', 'Outdoor activities', 'Dental technology', 'Teaching electrical skills', 'Volunteering', 'Cooking', 'Industry trends', 
     'Energy-efficient systems', 'Mentoring', 'Empathetic communication', 'Medical Technology', 'Historical Research', 'Public Speaking', 'Museum Volunteering', 'Conflict Resolution']
    
    unique_concepts = list(set(concepts))

    normalizer = Normalizer(concepts, n=10, verbose=True)

    assert len(normalizer.normalized_elements) == 10, "The number of normalized elements should be equal to the specified value."

    # sample 5 random elements from concepts using standard python methods
    
    random_concepts_buckets = [random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15), random.sample(concepts, 15)]


    assert len(normalizer.normalizing_map.keys()) == 0, "The normalizing map should be empty at the beginning."
    for bucket in random_concepts_buckets:
        init_cache_size = len(normalizer.normalizing_map.keys())
        
        normalized_concept = normalizer.normalize(bucket)
        assert normalized_concept is not None, "The normalized concept should not be None."
        logger.debug(f"Normalized concept: {bucket} -> {normalized_concept}")
        print(f"Normalized concept: {bucket} -> {normalized_concept}")

        next_cache_size = len(normalizer.normalizing_map.keys())

        # check same length
        assert len(normalized_concept) == len(bucket), "The normalized concept should have the same length as the input concept."

        # assert that all elements from normalized concepts are in normalizing map keys
        for element in bucket:
            assert element in normalizer.normalizing_map.keys(), f"{element} should be in the normalizing map keys."

        assert next_cache_size > 0, "The cache size should be greater than 0 after normalizing a new concept."
        assert next_cache_size >= init_cache_size, "The cache size should not decrease after normalizing a new concept."
```

**Назначение**: Проверяет нормализацию списка концепций с использованием класса `Normalizer`.

**Как работает функция**:

1.  Определяется список концепций `concepts`.
2.  Создается экземпляр класса `Normalizer` с заданным списком концепций, количеством нормализованных элементов и флагом verbose.
3.  Проверяется, что количество нормализованных элементов соответствует ожидаемому значению.
4.  Создается несколько случайных выборок из списка концепций.
5.  Для каждой выборки вызывается метод `normalize` класса `Normalizer`.
6.  Проверяется, что возвращаемое значение не равно `None`.
7.  Проверяется, что длина нормализованного списка соответствует длине входного списка.
8.  Проверяется, что все элементы из нормализованного списка присутствуют в ключах словаря `normalizing_map`.
9.  Проверяется, что размер кэша увеличивается после каждой нормализации.