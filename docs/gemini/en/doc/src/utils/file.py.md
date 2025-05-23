# Модуль `src.utils.file`

## Обзор

Модуль `src.utils.file` предоставляет набор утилит для работы с файлами, включая чтение, запись и поиск. Он поддерживает обработку больших файлов с использованием генераторов для экономии памяти.

## Более детально

Модуль содержит функции для сохранения данных в текстовые файлы, чтения содержимого файлов и каталогов, а также для рекурсивного поиска файлов по заданным шаблонам. Он также включает функции для получения списка имен файлов и каталогов, а также для удаления BOM из текстовых файлов. Этот модуль важен для работы с файловой системой и обработки текстовых данных в проекте `hypotez`.

## Функции

### `save_text_file`

```python
def save_text_file(
    data: str | list[str] | dict,
    file_path: str | Path,
    mode: str = 'w'
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).

    Returns:
        bool: `True`, если файл успешно сохранен, `False` в противном случае.

    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = save_text_file(file_path, data)
        >>> print(result)
        True
    """
```

**Назначение**: Сохраняет данные в текстовый файл.

**Параметры**:
- `file_path` (str | Path): Путь к файлу для сохранения.
- `data` (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
- `mode` (str, optional): Режим записи файла ('w' для записи, 'a' для добавления). По умолчанию 'w'.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Исключения**:
- `Exception`: Возникает при ошибке записи в файл. В блоке `except` регистрируется ошибка с использованием `logger.error`.

**Как работает функция**:
- Функция принимает путь к файлу, данные для записи и режим записи.
- Создает родительские директории, если их нет.
- Открывает файл в указанном режиме и записывает данные в файл.
- Если данные являются списком, записывает каждую строку из списка в файл.
- Если данные являются словарем, записывает их в формате JSON.
- Возвращает `True` в случае успеха и `False` в случае ошибки.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
data = 'Пример текста'
result = save_text_file(file_path, data)
print(result)
```

### `read_text_file_generator`

```python
def read_text_file_generator(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192,
    recursive: bool = False,
    patterns: Optional[str | list[str]] = None,
) -> Generator[str, None, None] | str | list[str] | None:
    """
    Читает содержимое файла(ов) или директории.

        Args:
            file_path (str | Path): Путь к файлу или директории.
            as_list (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
            extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
            chunk_size (int, optional): Размер чанка для чтения файла в байтах.
            recursive (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно.
            patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.

        Returns:
            Generator[str, None, None] | str | list[str] | None:
            - Если `as_list` is True и `file_path` является файлом, возвращает генератор строк.
            - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
            - Если `as_list` is False и `file_path` является файлом, возвращает строку.
            - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
            - Возвращает `None` в случае ошибки.
        Raises:
            Exception: При возникновении ошибки при чтении файла.

        Example:
            >>> from pathlib import Path
            >>> file_path = Path('example.txt')
            >>> content = read_text_file(file_path)
            >>> if content:
            ...    print(f'File content: {content[:100]}...')
            File content: Пример текста...
    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - Generator[str, None, None] (Генератор строк):
        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
        - Когда:
            file_path – это файл и as_list равен True.
            file_path – это директория, recursive равен True и as_list равен True. При этом в генератор попадают строки из всех найденных файлов.
            file_path – это директория, recursive равен False и as_list равен True. При этом в генератор попадают строки из всех найденных файлов в текущей директории.
        
    - str (Строка):
        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.
        - Когда:
            file_path – это файл и as_list равен False.
            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\\n).
            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\\n).
 
    - list[str] (Список строк):
        Этот тип явно не возвращается функцией, однако когда file_path – это директория, recursive равен True и as_list равен True - функция возвращает генератор, который можно преобразовать в список при помощи list()
        - Когда:
            file_path – не является ни файлом, ни директорией.
            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).


    Note:
        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте as_list = True. В этом случае вы получите генератор строк.
        Если вы хотите получить всё содержимое файла в виде одной строки используйте as_list = False.
        Если вы работаете с директорией, recursive = True будет обходить все поддиректории.
        extensions и patterns позволят вам фильтровать файлы при работе с директорией.
        chunk_size позволяет оптимизировать работу с большими файлами при чтении их по частям.
        None будет возвращён в случае ошибок.

    Важно помнить:
        В случае чтения директории, если as_list=False, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.\n        Функция полагается на другие функции-помощники (_read_file_lines_generator, _read_file_content, recursively_get_file_path, yield_text_from_files), которые здесь не определены и их поведение влияет на результат read_text_file.\n\n
    """
```

**Назначение**: Читает содержимое файла(ов) или директории с использованием генератора для экономии памяти.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию 8192.
- `recursive` (bool, optional): Если `True`, поиск файлов выполняется рекурсивно. По умолчанию `False`.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске. По умолчанию `None`.

**Возвращает**:
- `Generator[str, None, None] | str | list[str] | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Исключения**:
- `Exception`: Возникает при ошибке чтения файла. В блоке `except` регистрируется ошибка с использованием `logger.error`.

**Как работает функция**:
- Функция принимает путь к файлу или директории, флаг `as_list` для возврата списка строк или генератора, список расширений для фильтрации файлов, размер чанка для чтения файла и флаг `recursive` для рекурсивного поиска файлов.
- Если путь указывает на файл, функция возвращает либо генератор строк, либо объединенную строку в зависимости от значения `as_list`.
- Если путь указывает на директорию, функция рекурсивно или нерекурсивно обходит директорию и возвращает либо генератор строк, либо объединенную строку в зависимости от значения `as_list`.
- Если путь не является ни файлом, ни директорией, функция регистрирует ошибку и возвращает `None`.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

### `read_text_file`

```python
def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
    chunk_size: int = 8192
) -> str | list[str] | None:
    """
    Read the contents of a file.

    Args:
        file_path (str | Path): Path to the file or directory.
        as_list (bool, optional): If True, returns content as list of lines. Defaults to False.
        extensions (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.
        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.

    Returns:
        str | list[str] | None: File content as a string or list of lines, or None if an error occurs.
    """
```

**Назначение**: Читает содержимое файла.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде списка строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, логирует traceback при ошибке. По умолчанию `True`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `str | list[str] | None`: Содержимое файла в виде строки или списка строк, или `None` в случае ошибки.

**Как работает функция**:
- Функция принимает путь к файлу или директории, флаг `as_list` для возврата списка строк или одной строки, список расширений для фильтрации файлов.
- Если путь указывает на файл, функция открывает файл, читает его содержимое, заменяет множественные пробелы на одинарные и заменяет двойные кавычки на экранированные двойные кавычки. Возвращает содержимое в виде списка строк или одной строки в зависимости от значения `as_list`.
- Если путь указывает на директорию, функция рекурсивно обходит директорию и читает содержимое всех файлов. Возвращает содержимое в виде списка строк или одной строки в зависимости от значения `as_list`.
- Если путь не является ни файлом, ни директорией, функция регистрирует предупреждение и возвращает `None`.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

### `yield_text_from_files`

```python
def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    Args:
        file_path (str | Path): Путь к файлу.
        as_list (bool, optional): Если True, возвращает генератор строк. По умолчанию False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или None в случае ошибки.

    Yields:
       str: Строки из файла, если as_list is True.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
```

**Назначение**: Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Yields**:
- `str`: Строки из файла, если `as_list` is `True`.

**Как работает функция**:
- Функция принимает путь к файлу, флаг `as_list` для возврата генератора строк или одной строки, размер чанка для чтения файла.
- Если путь указывает на файл, функция возвращает либо генератор строк, либо объединенную строку в зависимости от значения `as_list`.
- Если путь не является файлом, функция регистрирует ошибку и возвращает `None`.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
for line in yield_text_from_files(file_path, as_list=True):
    print(line)
```

### `_read_file_content`

```python
def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Returns:
        str: Содержимое файла в виде строки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
```

**Назначение**: Читает содержимое файла по частям и возвращает его как строку.

**Параметры**:
- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер части для чтения файла в байтах.

**Возвращает**:
- `str`: Содержимое файла в виде строки.

**Исключения**:
- `Exception`: Возникает при ошибке чтения файла.

**Как работает функция**:
- Функция открывает файл в режиме чтения с указанной кодировкой.
- Читает файл по частям (чанкам) заданного размера.
- Объединяет все части в одну строку.
- Заменяет множественные пробелы на одинарные и заменяет двойные кавычки на экранированные двойные кавычки.
- Возвращает полученную строку.

### `_read_file_lines_generator`

```python
def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
    """
    Читает файл по строкам с помощью генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Yields:
        str: Строки из файла.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
```

**Назначение**: Читает файл построчно с использованием генератора.

**Параметры**:
- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Yields**:
- `str`: Строки из файла.

**Исключения**:
- `Exception`: Возникает при ошибке чтения файла.

**Как работает функция**:
- Функция открывает файл для чтения с указанной кодировкой.
- Читает файл по частям (чанкам) заданного размера.
- Разбивает каждую часть на строки.
- Если часть не заканчивается полной строкой, добавляет последнюю строку к следующей части.
- Для каждой строки удаляет лишние пробелы и экранирует двойные кавычки.
- Возвращает строки с помощью `yield`.

### `get_filenames_from_directory`

```python
def get_filenames_from_directory(
    directory: str | Path, ext: str | list[str] = '*'
) -> list[str]:
    """
    Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    Args:
        directory (str | Path): Путь к директории для поиска.
        ext (str | list[str], optional): Расширения для фильтрации.
            По умолчанию '*'.

    Returns:
        list[str]: Список имен файлов, найденных в директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
```

**Назначение**: Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

**Параметры**:
- `directory` (str | Path): Путь к директории для поиска.
- `ext` (str | list[str], optional): Расширения для фильтрации. По умолчанию '*'.

**Возвращает**:
- `list[str]`: Список имен файлов, найденных в директории.

**Как работает функция**:
- Функция принимает путь к директории и расширение для фильтрации файлов.
- Проверяет, является ли указанный путь директорией.
- Если указанный путь не является директорией, функция регистрирует ошибку и возвращает пустой список.
- Если указанный путь является директорией, функция получает список файлов в директории, фильтрует файлы по расширению (если указано) и возвращает список имен файлов.

**Примеры**:

```python
from pathlib import Path
directory = Path('.')
get_filenames_from_directory(directory, ['.txt', '.md'])
```

### `recursively_yield_file_path`

```python
def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> Generator[Path, None, None]:
    """
    Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Yields:
        Path: Путь к файлу, соответствующему шаблону.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
```

**Назначение**: Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Yields**:
- `Path`: Путь к файлу, соответствующему шаблону.

**Как работает функция**:
- Функция принимает корневую директорию и шаблоны для фильтрации файлов.
- Преобразует шаблоны в список, если они заданы строкой.
- Рекурсивно обходит корневую директорию и возвращает пути ко всем файлам, соответствующим заданным шаблонам.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
    print(path)
```

### `recursively_get_file_path`

```python
def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Returns:
        list[Path]: Список путей к файлам, соответствующим шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
```

**Назначение**: Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

**Как работает функция**:
- Функция принимает корневую директорию и шаблоны для фильтрации файлов.
- Преобразует шаблоны в список, если они заданы строкой.
- Рекурсивно обходит корневую директорию и добавляет пути ко всем файлам, соответствующим заданным шаблонам, в список.
- Возвращает список путей к файлам.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
print(paths)
```

### `recursively_read_text_files`

```python
def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    Args:
        root_dir (str | Path): Путь к корневой директории для поиска.
        patterns (str | list[str]): Шаблон(ы) имени файла для фильтрации.
             Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
        as_list (bool, optional): Если True, то возвращает содержимое файла как список строк.
             По умолчанию `False`.

    Returns:
        list[str]: Список содержимого файлов (или список строк, если `as_list=True`),
         соответствующих заданным шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
```

**Назначение**: Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Путь к корневой директории для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.
- `as_list` (bool, optional): Если `True`, возвращает содержимое файла как список строк. По умолчанию `False`.

**Возвращает**:
- `list[str]`: Список содержимого файлов (или список строк, если `as_list=True`), соответствующих заданным шаблонам.

**Как работает функция**:
- Функция принимает корневую директорию, шаблоны для фильтрации файлов и флаг `as_list` для возврата списка строк или одной строки.
- Проверяет, является ли указанная корневая директория директорией.
- Если указанная корневая директория не является директорией, функция регистрирует сообщение отладки и возвращает пустой список.
- Если указанная корневая директория является директорией, функция рекурсивно обходит директорию и читает содержимое всех файлов, соответствующих заданным шаблонам.
- Возвращает список содержимого файлов.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
for line in contents:
    print(line)
```

### `get_directory_names`

```python
def get_directory_names(directory: str | Path) -> list[str]:
    """
    Возвращает список имен директорий из указанной директории.

    Args:
        directory (str | Path): Путь к директории, из которой нужно получить имена.

    Returns:
        list[str]: Список имен директорий, найденных в указанной директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_directory_names(directory)
        ['dir1', 'dir2']
    """
```

**Назначение**: Возвращает список имен директорий из указанной директории.

**Параметры**:
- `directory` (str | Path): Путь к директории, из которой нужно получить имена.

**Возвращает**:
- `list[str]`: Список имен директорий, найденных в указанной директории.

**Как работает функция**:
- Функция принимает путь к директории.
- Получает список всех элементов в директории.
- Фильтрует элементы, оставляя только директории.
- Возвращает список имен директорий.

**Примеры**:

```python
from pathlib import Path
directory = Path('.')
get_directory_names(directory)
```

### `remove_bom`

```python
def remove_bom(path: str | Path) -> None:
    """
    Удаляет BOM из текстового файла или из всех файлов Python в директории.

    Args:
        path (str | Path): Путь к файлу или директории.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\ufeffПример текста с BOM')
        >>> remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
```

**Назначение**: Удаляет BOM (Byte Order Mark) из текстового файла или из всех файлов Python в директории.

**Параметры**:
- `path` (str | Path): Путь к файлу или директории.

**Как работает функция**:
- Функция принимает путь к файлу или директории.
- Если путь указывает на файл, функция открывает файл, удаляет BOM и перезаписывает файл.
- Если путь указывает на директорию, функция рекурсивно обходит директорию и удаляет BOM из всех файлов Python.
- Если путь не является ни файлом, ни директорией, функция регистрирует ошибку.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\ufeffПример текста с BOM')
remove_bom(file_path)
with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())
```

### `main`

```python
def main() -> None:
    """Entry point for BOM removal in Python files."""
```

**Назначение**: Точка входа для удаления BOM в файлах Python.

**Как работает функция**:
- Функция определяет корневую директорию как "../src".
- Регистрирует сообщение информации о начале удаления BOM.
- Вызывает функцию `remove_bom` для удаления BOM из файлов в корневой директории.

## Главная точка входа

```python
if __name__ == '__main__':
    main()
```

Если скрипт запускается как главный, вызывается функция `main`, которая удаляет BOM из файлов Python в директории `../src`.