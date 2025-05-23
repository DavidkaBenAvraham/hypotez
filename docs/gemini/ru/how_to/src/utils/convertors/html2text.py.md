## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода преобразует HTML-код в соответствующий текст, форматированный как Markdown. Он использует библиотеку html2text версии 3.1 для выполнения преобразования.

Шаги выполнения
-------------------------
1. **Инициализация**: Создается объект класса `_html2text`, который представляет собой HTML-парсер. 
2. **Обработка данных**: Метод `feed` объекта `_html2text` принимает HTML-код в качестве входных данных и обрабатывает его.
3. **Создание текста Markdown**: Метод `close` объекта `_html2text` завершает обработку и возвращает текст в формате Markdown.

Пример использования
-------------------------

```python
from src.utils.convertors.html2text import html2text

html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Пример HTML-кода</title>
</head>
<body>
  <h1>Заголовок</h1>
  <p>Это абзац текста.</p>
  <ul>
    <li>Первый пункт списка</li>
    <li>Второй пункт списка</li>
  </ul>
</body>
</html>
"""

markdown_text = html2text(html_code)

print(markdown_text)
```

**Вывод:**

```
# Заголовок

Это абзац текста.

- Первый пункт списка
- Второй пункт списка
```

**Важно:** В данном примере мы импортируем функцию `html2text` из модуля `src.utils.convertors.html2text` проекта `hypotez`.