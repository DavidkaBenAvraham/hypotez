## Как использовать класс Pi
=========================================================================================

Описание
-------------------------
Класс `Pi` представляет собой провайдера для общения с моделью Pi через API. Он реализует интерфейс `AsyncGeneratorProvider` и предоставляет методы для асинхронной генерации ответов модели, а также для управления сессиями и сохранения истории чата. 

Шаги выполнения
-------------------------
1. **Создание экземпляра класса Pi**: Создайте экземпляр класса Pi, используя конструктор класса.
2. **Инициализация сессии**: Если используется бессерверное окружение (без драйвера браузера), класс автоматически инициализирует сессию и получает cookie и заголовки, необходимые для общения с API.
3. **Запуск новой беседы**: Метод `start_conversation` запускает новую беседу с моделью Pi и возвращает идентификатор беседы (conversation_id).
4. **Отправка запроса**: Метод `ask` отправляет текстовый запрос (prompt) в API модели Pi, используя идентификатор беседы.
5. **Получение ответов**:  Метод `ask` возвращает асинхронный генератор, который позволяет получить ответы модели Pi построчно.
6. **Обновление cookie**:  Метод `ask` после каждого запроса обновляет cookie, чтобы поддерживать сессию активной.
7. **Обработка ответов**:  Обработайте ответы модели Pi, используя полученный асинхронный генератор.

Пример использования
-------------------------

```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.Pi import Pi

async def main():
    # Создание экземпляра класса Pi
    pi_provider = Pi()

    # Запуск новой беседы
    conversation_id = await pi_provider.start_conversation(pi_provider.session)

    # Отправка запроса
    messages = [
        {"role": "user", "content": "Привет, как дела?"},
    ]
    answer_generator = await pi_provider.ask(pi_provider.session, messages[-1]["content"], conversation_id)
    
    # Получение ответа
    async for line in answer_generator:
        print(line["text"]) 

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```