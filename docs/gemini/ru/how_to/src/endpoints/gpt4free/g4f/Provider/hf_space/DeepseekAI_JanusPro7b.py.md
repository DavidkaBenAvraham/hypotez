## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода реализует класс `DeepseekAI_JanusPro7b`, который представляет собой асинхронный генератор для работы с моделью DeepseekAI Janus-Pro-7B на платформе Hugging Face Spaces. Класс предоставляет функциональность для отправки запросов к API модели, получения результатов в виде асинхронного генератора, поддержки потоковой передачи данных и обработки изображений.

Шаги выполнения
-------------------------
1. **Инициализация класса**: Создается экземпляр класса `DeepseekAI_JanusPro7b`, который содержит информацию о модели, ее пространстве на Hugging Face и API-адресах. 
2. **Создание асинхронного генератора**: Вызывается метод `create_async_generator()`, который получает параметры, такие как модель, сообщения, мультимедиа, промпт, прокси, куки, API-ключ, UUID для ZeroGPU, флаг возврата информации о разговоре, сам разговор и seed для генерации.
3. **Форматирование запроса**: Процедура форматирует промпт в соответствии с требованиями модели, добавляя к нему необходимую информацию. 
4. **Получение токена ZeroGPU**: Если API-ключ не указан, метод `get_zerogpu_token()`  получает токен ZeroGPU и UUID, необходимых для авторизации на Hugging Face Spaces. 
5. **Обработка мультимедиа**: Если в качестве входных данных переданы медиафайлы, то они преобразуются в формат, пригодный для передачи в API модели.
6. **Отправка запроса**: Метод `run()` отправляет запрос к API модели, используя выбранный метод (POST или IMAGE) для отправки запроса.
7. **Потоковая обработка ответа**: Полученный ответ от API модели обрабатывается потоково, возвращая результаты по мере их готовности в виде асинхронного генератора.
8. **Возврат результатов**: Из асинхронного генератора получаются результаты в виде текста или изображения.

Пример использования
-------------------------

```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.hf_space import DeepseekAI_JanusPro7b

async def main():
    provider = DeepseekAI_JanusPro7b()
    messages = [
        {"role": "user", "content": "Напиши мне стихотворение про кота."}
    ]
    async for response in provider.create_async_generator(messages=messages):
        print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

**В данном примере мы:**

- **Создаем экземпляр класса `DeepseekAI_JanusPro7b`**.
- **Передаем в метод `create_async_generator()` список сообщений (`messages`).**
- **Получаем результаты из асинхронного генератора и выводим их на печать.**

**В результате будет выведено стихотворение про кота, сгенерированное моделью Janus-Pro-7B.**