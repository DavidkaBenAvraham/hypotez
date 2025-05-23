# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Содержание

- [Основные особенности](#основные-особенности)
- [Установка](#установка)
- [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Методы](#методы)
        - [Генерация стихотворения](#генерация-стихотворения)
        - [Анализ тональности](#анализ-тональности)
        - [Краткое изложение текста](#краткое-изложение-текста)
        - [Перевод текста](#перевод-текста)
    - [Пример использования](#пример-использования)
- [Зависимости](#зависимости)
- [Лицензия](#лицензия)

## Основные особенности

1. **Генерация стихотворения**:
   - Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

2. **Анализ тональности**:
   - Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

3. **Краткое изложение текста**:
   - Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

4. **Перевод текста**:
   - Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

5. **Логирование завершений**:
   - Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их с помощью pip:

```bash
pip install openai helicone
```

## Использование

### Инициализация

Инициализируйте класс `HeliconeAI`:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

### Методы

#### Генерация стихотворения

```python
def generate_poem(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

**Назначение**: Генерация стихотворения на основе заданного запроса.

**Параметры**:
- `prompt` (str): Запрос для генерации стихотворения.

**Возвращает**:
- `str`: Сгенерированное стихотворение.

**Как работает функция**:
1. Функция отправляет запрос к OpenAI API для генерации стихотворения на основе предоставленного промпта.
2. Используется модель `gpt-3.5-turbo`.
3. Запрос логируется с использованием `helicone.log_completion` для мониторинга и анализа.
4. Возвращается содержимое сгенерированного стихотворения.

**Примеры**:

```python
helicone_ai = HeliconeAI()
poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
print(poem)
```

#### Анализ тональности

```python
def analyze_sentiment(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Назначение**: Анализ тональности заданного текста.

**Параметры**:
- `text` (str): Текст для анализа тональности.

**Возвращает**:
- `str`: Результат анализа тональности.

**Как работает функция**:
1. Функция отправляет запрос к OpenAI API для анализа тональности текста.
2. Используется модель `text-davinci-003`.
3. Максимальное количество токенов ограничено 50.
4. Запрос логируется с использованием `helicone.log_completion`.
5. Возвращается результат анализа тональности текста.

**Примеры**:

```python
helicone_ai = HeliconeAI()
sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
print(sentiment)
```

#### Краткое изложение текста

```python
def summarize_text(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Назначение**: Создание краткого изложения заданного текста.

**Параметры**:
- `text` (str): Текст для краткого изложения.

**Возвращает**:
- `str`: Краткое изложение текста.

**Как работает функция**:
1. Функция отправляет запрос к OpenAI API для создания краткого изложения текста.
2. Используется модель `text-davinci-003`.
3. Максимальное количество токенов ограничено 100.
4. Запрос логируется с использованием `helicone.log_completion`.
5. Возвращается краткое изложение текста.

**Примеры**:

```python
helicone_ai = HeliconeAI()
summary = helicone_ai.summarize_text("Длинный текст для изложения...")
print(summary)
```

#### Перевод текста

```python
def translate_text(self, text: str, target_language: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

**Назначение**: Перевод заданного текста на указанный целевой язык.

**Параметры**:
- `text` (str): Текст для перевода.
- `target_language` (str): Целевой язык для перевода.

**Возвращает**:
- `str`: Переведенный текст.

**Как работает функция**:
1. Функция отправляет запрос к OpenAI API для перевода текста на указанный язык.
2. Используется модель `text-davinci-003`.
3. Максимальное количество токенов ограничено 200.
4. Запрос логируется с использованием `helicone.log_completion`.
5. Возвращается переведенный текст.

**Примеры**:

```python
helicone_ai = HeliconeAI()
translation = helicone_ai.translate_text("Hello, how are you?", "русский")
print(translation)
```

### Пример использования

Вот пример того, как использовать класс `HeliconeAI`:

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\\n", translation)

if __name__ == "__main__":
    main()
```

## Зависимости

- `helicone`
- `openai`

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `HeliconeAI`.