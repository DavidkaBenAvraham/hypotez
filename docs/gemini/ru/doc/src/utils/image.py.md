# Модуль обработки изображений

## Обзор

Модуль `src.utils.image` предоставляет асинхронные функции для загрузки, сохранения и манипулирования изображениями. Он включает в себя функциональность, такую как сохранение изображений из URL-адресов, сохранение данных изображения в файлы, получение данных изображения, поиск случайных изображений в каталогах, добавление водяных знаков, изменение размера и преобразование форматов изображений.

## Подробно

Данный модуль используется для обработки изображений в проекте. Модуль предоставляет набор функций для:
- Загрузки изображений из URL-адресов
- Сохранения изображений в файлы
- Изменения размера изображений
- Преобразования форматов изображений
- Добавления водяных знаков

## Классы

### `ImageError`

**Описание**: Класс пользовательского исключения для ошибок, связанных с изображениями. 
**Наследует**: `Exception`

**Атрибуты**:
-  Нет

**Методы**:
-  Нет

## Функции

### `save_image_from_url_async`

**Назначение**: Асинхронно загружает изображение по URL-адресу и сохраняет его локально.

**Параметры**:
- `image_url` (str): URL-адрес для загрузки изображения.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция завершилась неудачей.

**Вызывает исключения**:
- `ImageError`: Если загрузка или сохранение изображения завершились неудачей.

**Как работает функция**:
- Функция использует библиотеку `aiohttp` для асинхронной загрузки изображения по указанному URL-адресу.
- После успешной загрузки изображение сохраняется в файл с помощью функции `save_image_async`.

**Примеры**:
```python
# Загружаем изображение и сохраняем его в файл
image_url = "https://example.com/image.jpg"
filename = "image.jpg"
image_path = await save_image_from_url_async(image_url, filename)
if image_path:
    print(f"Image saved to: {image_path}")
```

### `save_image`

**Назначение**: Сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат для сохранения изображения, по умолчанию `PNG`.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция завершилась неудачей.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен или если сохраненный файл пуст.

**Как работает функция**:
- Функция сначала создает каталог, в котором будет сохранен файл.
- Затем данные изображения записываются в файл в указанном формате.
- После сохранения функция проверяет, был ли файл создан и не пуст ли он.

**Примеры**:
```python
# Сохраняем данные изображения в файл
image_data = b"image_data"
file_name = "image.jpg"
image_path = save_image(image_data, file_name, format="JPEG")
if image_path:
    print(f"Image saved to: {image_path}")
```

### `save_image_async`

**Назначение**: Асинхронно сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат для сохранения изображения, по умолчанию `PNG`.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция завершилась неудачей.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен или если сохраненный файл пуст.

**Как работает функция**:
- Функция использует библиотеку `aiofiles` для асинхронного создания каталога и записи данных изображения в файл.
- После сохранения функция асинхронно проверяет, был ли файл создан и не пуст ли он.

**Примеры**:
```python
# Асинхронно сохраняем данные изображения в файл
image_data = b"image_data"
file_name = "image.jpg"
image_path = await save_image_async(image_data, file_name, format="JPEG")
if image_path:
    print(f"Image saved to: {image_path}")
```

### `get_image_bytes`

**Назначение**: Считывает изображение с помощью Pillow и возвращает его байты в формате JPEG.

**Параметры**:
- `image_path` (Path): Путь к файлу изображения.
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; в противном случае возвращает байты. По умолчанию `True`.

**Возвращает**:
- `Optional[Union[BytesIO, bytes]]`: Байты изображения в формате JPEG или `None`, если произошла ошибка.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при чтении изображения.

**Как работает функция**:
- Функция открывает изображение с помощью Pillow и сохраняет его в объект `BytesIO` в формате JPEG.
- Затем функция возвращает объект `BytesIO` или его байты в зависимости от значения параметра `raw`.

**Примеры**:
```python
# Получаем байты изображения
image_path = Path("image.jpg")
image_bytes = get_image_bytes(image_path, raw=False)
if image_bytes:
    print(f"Image bytes: {image_bytes}")
```

### `get_raw_image_data`

**Назначение**: Получает необработанные двоичные данные файла, если он существует.

**Параметры**:
- `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла или `None`, если файл не существует или произошла ошибка.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при чтении файла.

**Как работает функция**:
- Функция проверяет, существует ли файл по указанному имени или пути.
- Если файл существует, функция считывает его необработанные двоичные данные и возвращает их.

**Примеры**:
```python
# Получаем необработанные данные изображения
file_name = "image.jpg"
image_data = get_raw_image_data(file_name)
if image_data:
    print(f"Image data: {image_data}")
```

### `random_image`

**Назначение**: Рекурсивно ищет случайное изображение в указанном каталоге.

**Параметры**:
- `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
- `Optional[str]`: Путь к случайному изображению или `None`, если изображения не найдены.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при чтении каталога.

**Как работает функция**:
- Функция рекурсивно обходит указанный каталог и собирает все файлы изображений.
- Затем функция выбирает случайное изображение из списка файлов изображений и возвращает его путь.

**Примеры**:
```python
# Получаем путь к случайному изображению
root_path = Path("images")
image_path = random_image(root_path)
if image_path:
    print(f"Random image path: {image_path}")
```

### `add_text_watermark`

**Назначение**: Добавляет текстовый водяной знак к изображению.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст, который будет использоваться в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком. По умолчанию перезаписывается исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком или `None`, если произошла ошибка.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при добавлении водяного знака к изображению.

**Как работает функция**:
- Функция открывает изображение и создает прозрачный слой для водяного знака.
- Затем функция рисует текст водяного знака на прозрачном слое и объединяет его с исходным изображением.
- Изображение с водяным знаком сохраняется в указанном пути.

**Примеры**:
```python
# Добавляем водяной знак к изображению
image_path = Path("image.jpg")
watermark_text = "Copyright 2023"
watermarked_image_path = add_text_watermark(image_path, watermark_text)
if watermarked_image_path:
    print(f"Watermarked image saved to: {watermarked_image_path}")
```

### `add_image_watermark`

**Назначение**: Добавляет водяной знак к изображению и сохраняет результат в указанном пути.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком. Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком или `None`, если операция завершилась неудачей.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при добавлении водяного знака к изображению.

**Как работает функция**:
- Функция открывает исходное изображение и изображение водяного знака.
- Затем функция изменяет размер водяного знака до 8% ширины исходного изображения и помещает его в нижний правый угол.
- После этого функция объединяет исходное изображение и изображение водяного знака и сохраняет результат в указанном пути.

**Примеры**:
```python
# Добавляем водяной знак к изображению
input_image_path = Path("image.jpg")
watermark_image_path = Path("watermark.png")
output_image_path = add_image_watermark(input_image_path, watermark_image_path)
if output_image_path:
    print(f"Watermarked image saved to: {output_image_path}")
```

### `resize_image`

**Назначение**: Изменяет размер изображения до указанных размеров.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с измененным размером. По умолчанию перезаписывается исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с измененным размером или `None`, если произошла ошибка.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при изменении размера изображения.

**Как работает функция**:
- Функция открывает изображение и изменяет его размер с помощью Pillow.
- Затем функция сохраняет изображение с измененным размером в указанном пути.

**Примеры**:
```python
# Изменяем размер изображения
image_path = Path("image.jpg")
size = (100, 100)
resized_image_path = resize_image(image_path, size)
if resized_image_path:
    print(f"Resized image saved to: {resized_image_path}")
```

### `convert_image`

**Назначение**: Преобразует изображение в указанный формат.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `format` (str): Формат, в который нужно преобразовать изображение (например, "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения. По умолчанию перезаписывается исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к преобразованному изображению или `None`, если произошла ошибка.

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при преобразовании изображения.

**Как работает функция**:
- Функция открывает изображение и сохраняет его в указанном формате с помощью Pillow.
- Затем функция сохраняет преобразованное изображение в указанном пути.

**Примеры**:
```python
# Преобразуем изображение в формат PNG
image_path = Path("image.jpg")
format = "PNG"
converted_image_path = convert_image(image_path, format)
if converted_image_path:
    print(f"Converted image saved to: {converted_image_path}")
```

### `process_images_with_watermark`

**Назначение**: Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в каталог "output".

**Параметры**:
- `folder_path` (Path): Путь к папке, содержащей изображения.
- `watermark_path` (Path): Путь к изображению водяного знака.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ImageError`: Если произошла ошибка при обработке изображений.

**Как работает функция**:
- Функция проверяет, существует ли указанная папка.
- Если папка существует, функция создает каталог "output" в ней, если он еще не существует.
- Затем функция проходит по всем файлам в папке и добавляет водяной знак к изображениям с помощью функции `add_image_watermark`.

**Примеры**:
```python
# Обработка изображений с водяным знаком
folder_path = Path("images")
watermark_path = Path("watermark.png")
process_images_with_watermark(folder_path, watermark_path)
```

## Примеры

```python
# Импортируем модуль
from src.utils.image import save_image_from_url_async, resize_image, add_text_watermark, add_image_watermark

# Загружаем и сохраняем изображение
image_url = "https://example.com/image.jpg"
filename = "image.jpg"
image_path = await save_image_from_url_async(image_url, filename)

# Изменяем размер изображения
size = (100, 100)
resized_image_path = resize_image(image_path, size)

# Добавляем текстовый водяной знак
watermark_text = "Copyright 2023"
watermarked_image_path = add_text_watermark(image_path, watermark_text)

# Добавляем водяной знак в виде изображения
watermark_image_path = Path("watermark.png")
watermarked_image_path = add_image_watermark(image_path, watermark_image_path)

# Выводим результаты
print(f"Image saved to: {image_path}")
print(f"Resized image saved to: {resized_image_path}")
print(f"Watermarked image saved to: {watermarked_image_path}")
```

## Дополнительные замечания

- В коде используется вебдрайвер, который импортируется из модуля `webdriver` проекта `hypotez`.
- Для обработки ошибок используется модуль `logger` из `src.logger`.
- Все функции и методы документированы на русском языке.
- Код написан в соответствии с PEP 8.