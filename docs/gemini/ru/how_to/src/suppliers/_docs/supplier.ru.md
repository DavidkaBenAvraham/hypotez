### **Инструкции для генерации документации к коду**

1. **Анализируй код**: Пойми логику и действия, выполняемые данным фрагментом кода.

2. **Создай пошаговую инструкцию**:
    - **Описание**: Объясни, что делает данный блок кода.
    - **Шаги выполнения**: Опиши последовательность действий в коде.
    - **Пример использования**: Приведи пример кода, как использовать данный фрагмент в проекте.

3. **Промер**:
4. 
Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Класс `Supplier` является базовым классом для работы с поставщиками данных. Он служит основой для реализации различных поставщиков данных (например, Amazon, AliExpress, Walmart и т.д.) и предоставляет общие методы и атрибуты, которые могут быть использованы или переопределены конкретными реализациями поставщиков.

Шаги выполнения
-------------------------
1. **Инициализация класса `Supplier`**:
   - Создается объект класса `Supplier` с указанием префикса поставщика (`supplier_prefix`), локали (`locale`) и типа веб-драйвера (`webdriver`).
   - Функция `__init__` инициализирует атрибуты класса, такие как идентификатор поставщика, настройки, локаль и веб-драйвер.

2. **Загрузка конфигурации**:
   - Вызывается метод `_payload`, который загружает конфигурационные файлы, включая локаторы для веб-элементов на страницах сайта поставщика и сценарии выполнения.
   - Метод инициализирует веб-драйвер для взаимодействия с сайтом поставщика.

3. **Вход на сайт (опционально)**:
   - Если требуется вход на сайт поставщика, вызывается метод `login`.
   - Метод выполняет процесс входа на сайт, используя данные для входа, если они предоставлены.

4. **Выполнение сценариев**:
   - Запускаются сценарии, которые определяют, какие действия нужно выполнить (например, сбор данных).
   - Сценарии могут быть запущены из файлов с помощью метода `run_scenario_files` или переданы в виде списка словарей с помощью метода `run_scenarios`.

Пример использования
-------------------------

```python
# Создаем объект для поставщика 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполняем вход на сайт поставщика
supplier.login()

# Запускаем сценарии из файлов
supplier.run_scenario_files(['example_scenario.json'])

# Или запускаем сценарии по определенным условиям
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

5. **Избегай расплывчатых терминов** вроде "получаем" или "делаем". Будь конкретным, что именно делает код, например: "проверяет", "валидирует" или "отправляет".