# Обзор модулей проекта `hypotez`

В этом документе представлен обзор основных модулей программы.

## Содержание

- [assistant](#assistant)
- [bot](#bot)
- [scenario](#scenario)
- [suppliers](#suppliers)
- [templates](#templates)
- [translators](#translators)
- [utils](#utils)
- [webdriver](#webdriver)
- [Глоссарий](#glossary)
    - [1. webdriver](#1-webdriver)
    - [2. Supplier](#2-supplier)
    - [3. Product](#3-product)
    - [4. ai](#4-ai)
- [Далее](#next)

## assistant

Модуль для взаимодействия с классом `CodeAssistant`, который помогает в задачах обработки кода.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/assistant/readme.en.md) - Исходный код модуля `assistant`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/assistant/readme.en.md) - Документация для модуля `assistant`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/assistant) - Тесты для модуля `assistant`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/assistant) - Примеры использования модуля `assistant`.

## bot

Модуль для логики бота, включая обработку сообщений и обработку команд бота.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/bot/readme.en.md) - Исходный код модуля `bot`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/bot/readme.en.md) - Документация для модуля `bot`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/bot) - Тесты для модуля `bot`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/bot) - Примеры использования модуля `bot`.

## scenario

Модуль для работы со сценариями, включая генерацию и выполнение сценариев.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/scenario/readme.en.md) - Исходный код модуля `scenario`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/scenario/readme.en.md) - Документация для модуля `scenario`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/scenario) - Тесты для модуля `scenario`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/scenario) - Примеры использования модуля `scenario`.

## suppliers

Модуль для работы с поставщиками, включая управление их данными и отношениями.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/suppliers/readme.en.md) - Исходный код модуля `suppliers`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/suppliers/readme.en.md) - Документация для модуля `suppliers`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/suppliers) - Тесты для модуля `suppliers`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/suppliers) - Примеры использования модуля `suppliers`.

## templates

Модуль для работы с шаблонами, включая создание и управление шаблонами для различных целей.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/templates/readme.en.md) - Исходный код модуля `templates`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/templates/readme.en.md) - Документация для модуля `templates`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/templates) - Тесты для модуля `templates`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/templates) - Примеры использования модуля `templates`.

## translators

Модуль для работы с переводчиками и перевода текста.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/translators/readme.en.md) - Исходный код модуля `translators`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/translators/readme.en.md) - Документация для модуля `translators`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/translators) - Тесты для модуля `translators`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/translators) - Примеры использования модуля `translators`.

## utils

Модуль для вспомогательных утилит, упрощающих общие задачи.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/utils/readme.en.md) - Исходный код модуля `utils`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/utils/readme.en.md) - Документация для модуля `utils`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/utils) - Тесты для модуля `utils`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/utils) - Примеры использования модуля `utils`.

## webdriver

Модуль для работы с драйверами веб-браузеров и управления веб-элементами.

- [Код модуля](https://github.com/hypo69/hypotez/blob/master/src/webdriver/readme.en.md) - Исходный код модуля `webdriver`.
- [Документация](https://github.com/hypo69/hypotez/blob/master/docs/gemini/en/doc/src/webdriver/readme.en.md) - Документация для модуля `webdriver`.
- [Тесты](https://github.com/hypo69/hypotez/blob/master/pytest/gemini/src/webdriver) - Тесты для модуля `webdriver`.
- [Примеры](https://github.com/hypo69/hypotez/blob/master/docs/examples/webdriver) - Примеры использования модуля `webdriver`.

## Глоссарий

### 1. **webdriver**

- **`Driver`**: Объект, который управляет браузером (например, Chrome, Firefox) и выполняет такие действия, как навигация по веб-страницам, заполнение форм и т. д.
- **`Executor`**: Интерфейс или класс, который выполняет команды или скрипты в контексте веб-драйвера.
- **`Chrome`, `Firefox`, ...**: Конкретные браузеры, которыми можно управлять с помощью веб-драйвера.
- **`locator`**: Механизм для поиска элементов на веб-странице (например, по ID, CSS-селектору, XPath).

### 2. **Supplier**

- **list of suppliers (`Amazon`, `Aliexpress`, `Morlevi`, ...)**: Список компаний или платформ, которые предоставляют товары или услуги.
- **`Graber`**: Инструмент или модуль, который автоматически собирает данные с веб-сайтов поставщиков (например, цены, доступность товаров).

### 3. **Product**

- **`Product`**: Объект, представляющий товар или услугу, которая может быть доступна на различных платформах.
- **`ProductFields`**: Поля или атрибуты, которые описывают характеристики товара (например, название, цена, описание, изображения).

### 4. **ai**
- **`Model Prompt`**: Определяет, как модель должна обрабатывать входящую информацию и возвращать ответ. Устанавливается при инициализации модели.
- **`Command Instruction`**: Небольшая команда или инструкция, отправляемая с каждым запросом.

## Далее

[Инициализация и настройка проекта]((https://github.com/hypo69/hypotez/blob/master/src/credentials.md)