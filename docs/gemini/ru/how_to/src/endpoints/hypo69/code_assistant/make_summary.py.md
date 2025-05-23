## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код создает файл `SUMMARY.md`, необходимый для компиляции документации с помощью `mdbook`. Он рекурсивно обходит заданную директорию, находит все .md файлы и формирует список глав для `SUMMARY.md`. 

Шаги выполнения
-------------------------
1. **Инициализация**:
    -  Определяется корневой путь проекта `PROJECT_ROOT`.
    -  Функция `make_summary` принимает путь к исходной директории `docs_dir` и язык `lang`.
    -  Создается объект `summary_file`, который представляет собой путь к файлу `SUMMARY.md` в директории `docs`.
    -  Создается директория `docs` (если она не существует).
    -  Вызывается функция `_make_summary`, которая выполняет основную логику.
2. **Рекурсивный обход**:
    -  Функция `_make_summary` рекурсивно обходит директорию `src_dir`.
    -  Проверяется, существует ли файл `SUMMARY.md`. Если да, выводится сообщение о перезаписи.
    -  Открывается файл `SUMMARY.md` для записи.
    -  Добавляется заголовок `# Summary`.
    -  Происходит итерация по всем .md файлам в директории.
    -  Пропускаются файлы `SUMMARY.md`.
    -  Проверяется, соответствует ли имя файла выбранному языку:
        -  Если `lang` - `ru`, пропускаются файлы без суффикса `.ru.md`.
        -  Если `lang` - `en`, пропускаются файлы с суффиксом `.ru.md`.
    -  Формируется относительный путь к файлу `.md`.
    -  Записывается строка в `SUMMARY.md`, формирующая ссылку на файл `.md`.
3. **Обработка ошибок**:
    -  В случае возникновения ошибок при обработке файла выводится сообщение об ошибке.
4. **Формирование пути**:
    -  Функция `prepare_summary_path` формирует путь к файлу `SUMMARY.md` в директории `docs`.
    -  Заменяется часть пути `src` на `docs`.
    -  Добавляется имя файла `SUMMARY.md`.
5. **Вызов**:
    -  В блоке `if __name__ == '__main__'`:
        -  Парсятся аргументы командной строки.
        -  Преобразуется путь к исходной директории `src_dir` в объект `Path`.
        -  Вызывается функция `make_summary` с переданными аргументами.

Пример использования
-------------------------

```python
# Пример использования: 
# python make_summary.py -lang ru /src 

# С помощью этой команды в директории docs будет сформирован файл SUMMARY.md, 
# в котором будут перечислены все .md файлы из директории src. 
# Файлы будут отфильтрованы по языку (ru), то есть будут использоваться только файлы с суффиксом .ru.md.
```