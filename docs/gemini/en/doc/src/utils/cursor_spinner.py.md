# Модуль `cursor_spinner`

## Обзор

Модуль `cursor_spinner` предоставляет утилиту для отображения вращающегося курсора в консоли, чтобы имитировать процесс загрузки или ожидания. 

## Детали

Этот модуль используется для визуального представления процесса, который может занять некоторое время. Вращающийся курсор в консоли сообщает пользователю, что программа работает и ожидает завершения операции.

## Классы

### `spinning_cursor()`

**Описание**: Генератор для вращающегося курсора, который циклически перебирает символы `|`, `/`, `-`, `\`.

**Возвращает**: 
- `str`: Следующий символ в последовательности курсора.

**Пример**:

```python
>>> cursor = spinning_cursor()
>>> next(cursor)  # '|'
>>> next(cursor)  # '/'
>>> next(cursor)  # '-'
>>> next(cursor)  # '\\'
```

### `show_spinner(duration: float = 5.0, delay: float = 0.1)`

**Описание**: Отображает вращающийся курсор в консоли в течение заданного времени.

**Параметры**:

- `duration` (float): Как долго должен работать спиннер (в секундах). По умолчанию 5.0.
- `delay` (float): Задержка между каждым вращением (в секундах). По умолчанию 0.1.

**Пример**:

```python
>>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер в течение 3 секунд
```

**Принцип работы**:

Функция `show_spinner` работает следующим образом:

1. Создает экземпляр генератора `spinning_cursor()`.
2. Определяет время окончания вращения, добавляя `duration` к текущему времени.
3. В цикле до достижения времени окончания:
    - Вызывает `next()` для генератора `spinning_cursor()` и получает следующий символ.
    - Выводит символ в консоль с помощью `sys.stdout.write()`.
    - Принудительно выводит результат в консоль с помощью `sys.stdout.flush()`.
    - Делает паузу на `delay` секунд с помощью `time.sleep()`.
    - Возвращает курсор назад с помощью `sys.stdout.write('\b')`.

**Примеры**:

```python
# Example usage of the spinner in a script
print("Spinner for 5 seconds:")
show_spinner(duration=5.0, delay=0.1)
print("\nDone!")
```