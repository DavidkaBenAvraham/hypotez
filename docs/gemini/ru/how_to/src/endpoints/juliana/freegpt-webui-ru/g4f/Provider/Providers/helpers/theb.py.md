## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код взаимодействует с API chatbot.theb.ai для получения ответа от языковой модели. Он обрабатывает получение конфигурации, формирование запроса, отправку запроса с помощью `requests`, обработку ответа и вывод результата.

Шаги выполнения
-------------------------
1. Загрузка конфигурации: код извлекает конфигурацию из аргумента командной строки `sys.argv[1]`, которая должна быть в формате JSON. 
2. Извлечение подсказки: извлекает текст подсказки (prompt) из последнего сообщения в конфигурации.
3. Формирование заголовков запроса: устанавливает заголовки `headers` для отправки запроса к API.
4. Формирование данных запроса: формирует `json_data`, включающий текст подсказки и дополнительные опции (в этом случае пустой словарь).
5. Определение функции `format`: эта функция обрабатывает отдельные части ответа, извлекая текст ответа и выводя его по частям.
6. Цикл отправки запроса: код отправляет POST-запрос к API `https://chatbot.theb.ai/api/chat-process` с использованием `requests` и `content_callback` для передачи ответа в функцию `format` для обработки.
7. Обработка ошибок: код обрабатывает ошибки во время отправки запроса и перевыполняет запрос в цикле.
8. Завершение работы: после успешной отправки запроса код завершает работу с кодом 0.

Пример использования
-------------------------

```python
# Запускаем скрипт с JSON конфигурацией в качестве аргумента
python theb.py '{"messages": [{"role": "user", "content": "Как дела?"}]}' 
```

В этом примере `'{"messages": [{"role": "user", "content": "Как дела?"}]}'` — это конфигурация JSON, содержащая одно сообщение от пользователя. После выполнения скрипта в консоли будет выведен ответ от языковой модели.