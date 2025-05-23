# Документация для Telegram Movie Bot

## Обзор

Этот документ предоставляет информацию о Telegram-боте для поиска ссылок на бесплатный просмотр фильмов и сериалов. Бот использует библиотеку Aiogram, сервисы Google для ассоциативного поиска, библиотеку Кинопоиска и сервис [w2.kpfr/wiki](https://w2.kpfr.wiki/). В боте реализована защита от флуда и парсинг с использованием BeautifulSoup.

## Подробнее

Telegram Movie Bot - это бот, разработанный для поиска ссылок на бесплатный просмотр фильмов и сериалов. Он создан с использованием библиотеки Aiogram для работы с Telegram API. Для поиска бот использует сервисы Google, библиотеку Кинопоиска и сервис [w2.kpfr/wiki](https://w2.kpfr.wiki/). Также в боте реализована защита от флуда с использованием middlewares.

## Быстрый старт

### 1. Клонирование проекта

Склонируйте проект на свой компьютер.

### 2. Файл `.env`

Создайте файл `.env` и заполните его в следующем формате:

```
TOKEN=123456789 # Токен вашего telegram бота
```

### 3. Виртуальное окружение

Если у вас нет виртуального окружения, создайте и активируйте его:

```shell
python -m venv venv
```

```shell
venv\\Scripts\\activate.bat
```

### 4. Установка зависимостей

Обновите `pip` и установите необходимые зависимости:

```shell
pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

### 5. Запуск `run.py`

Запустите `run.py`:

```shell
python run.py
```

## Ссылки

- Ссылка на бота: https://t.me/Guarava_bot
- Для связи: https://t.me/qdi2k