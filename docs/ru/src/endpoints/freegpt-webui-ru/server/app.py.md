# Документация для `app.py`

## Обзор

Файл `app.py` создает экземпляр Flask-приложения, используемого для веб-интерфейса. Он определяет точку входа для приложения и указывает каталог с HTML-шаблонами.

## Подробней

Этот файл является отправной точкой для веб-приложения, используемого для взаимодействия с пользователем. Он использует Flask для создания веб-сервера и указывает, где находятся HTML-шаблоны, которые будут использоваться для отображения веб-страниц.

## Переменные

### `app`

```python
app = Flask(__name__, template_folder='./../client/html')
```

- **Назначение**: Экземпляр Flask-приложения.
- **Тип**: `Flask`
- **Параметры**:
  - `__name__` (str): Имя текущего модуля. Flask использует это для определения местоположения ресурсов приложения.
  - `template_folder` (str): Путь к папке, содержащей HTML-шаблоны. В данном случае, папка `html` находится на уровень выше текущей директории в поддиректории `client`.

**Принцип работы**:
   - Создает экземпляр Flask-приложения с указанием имени текущего модуля и пути к каталогу с шаблонами.

**Примеры**:

```python
from flask import Flask

app = Flask(__name__, template_folder='./../client/html')