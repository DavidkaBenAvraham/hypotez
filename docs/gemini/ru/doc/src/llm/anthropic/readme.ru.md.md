# Клиент для модели Claude от Anthropic

## Обзор

Этот модуль предоставляет простой Python-интерфейс для взаимодействия с языковой моделью Claude от Anthropic. Он включает основные функции для генерации текста, анализа тональности и перевода текста.

## Подробнее

Модуль `claude_client` обеспечивает доступ к модели Claude от Anthropic через API. Он предоставляет несколько функций для работы с моделью, в том числе:

- **Генерация текста**: `generate_text(prompt, max_tokens_to_sample=100)`
- **Анализ тональности**: `analyze_sentiment(text)`
- **Перевод текста**: `translate_text(text, source_language, target_language)`

## Установка

Для использования этого модуля вам необходимо установить библиотеку `anthropic`:

```bash
pip install anthropic
```

## Использование

### Инициализация

Сначала необходимо инициализировать `ClaudeClient` с вашим API-ключом от Anthropic:

```python
from claude_client import ClaudeClient

api_key = "ваш-api-ключ"
claude_client = ClaudeClient(api_key)
```

### Генерация текста

Чтобы сгенерировать текст на основе заданного промпта, используйте функцию `generate_text`:

```python
prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)
```

### Анализ тональности

Для анализа тональности заданного текста используйте функцию `analyze_sentiment`:

```python
text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)
```

### Перевод текста

Переведите текст с одного языка на другой с помощью функции `translate_text`:

```python
text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```

## Пример кода

Вот полный пример использования `ClaudeClient`:

```python
from claude_client import ClaudeClient

api_key = "ваш-api-ключ"
claude_client = ClaudeClient(api_key)

# Генерация текста
prompt = "Напишите короткую историю о роботе, который учится любить."
generated_text = claude_client.generate_text(prompt)
print("Сгенерированный текст:", generated_text)

# Анализ тональности
text_to_analyze = "Сегодня я очень счастлив!"
sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
print("Анализ тональности:", sentiment_analysis)

# Перевод текста
text_to_translate = "Привет, как дела?"
source_language = "ru"
target_language = "en"
translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
print("Переведенный текст:", translated_text)
```

## Методы

### `generate_text(prompt, max_tokens_to_sample=100)`

Генерирует текст на основе заданного промпта.

- **Параметры:**
  - `prompt`: Промпт для генерации текста.
  - `max_tokens_to_sample`: Максимальное количество токенов для генерации.
- **Возвращает:** Сгенерированный текст.

### `analyze_sentiment(text)`

Анализирует тональность заданного текста.

- **Параметры:**
  - `text`: Текст для анализа.
- **Возвращает:** Результат анализа тональности.

### `translate_text(text, source_language, target_language)`

Переводит заданный текст с одного языка на другой.

- **Параметры:**
  - `text`: Текст для перевода.
  - `source_language`: Код исходного языка.
  - `target_language`: Код целевого языка.
- **Возвращает:** Переведенный текст.

## Вклад

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

**Примечание:** Замените `"ваш-api-ключ"` на ваш реальный API-ключ от Anthropic.