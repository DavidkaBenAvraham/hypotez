# Генерация изображения с помощью GPT-4Free API

## Обзор

Этот файл содержит пример кода для генерации изображения с помощью API GPT-4Free. API GPT-4Free - это бесплатная альтернатива API OpenAI для доступа к моделям искусственного интеллекта, включая возможность генерации текста, перевода и создания изображений. 

## Подробей

Файл демонстрирует отправку POST-запроса к API GPT-4Free с использованием библиотеки `requests` для генерации изображения по текстовому запросу. 

## Код

```python
import requests

url = "http://localhost:1337/v1/images/generations"
body = {
    "model": "flux",
    "prompt": "hello world user",
    "response_format": None,
    #"response_format": "url",
    #"response_format": "b64_json",
}
data = requests.post(url, json=body, stream=True).json()
print(data)

```

## Пример

### Параметры запроса

- **`model`**:  имя модели для генерации изображения. В данном примере используется `flux`.
- **`prompt`**: текстовый запрос для генерации изображения. В данном примере - `hello world user`.
- **`response_format`**: формат ответа. В данном примере не указан (`None`), что означает, что API вернет ответ в формате JSON. Другие доступные варианты:
    - `url`: API возвращает URL-ссылку на сгенерированное изображение.
    - `b64_json`: API возвращает изображение в формате Base64, закодированное в JSON.

### Ответ

API GPT-4Free возвращает JSON-ответ, содержащий информацию о сгенерированном изображении, включая его URL, формат и размер.

## Дополнительные сведения

Для более детального ознакомления с API GPT-4Free и доступными моделями, параметрами и форматами ответов, обратитесь к документации API GPT-4Free.