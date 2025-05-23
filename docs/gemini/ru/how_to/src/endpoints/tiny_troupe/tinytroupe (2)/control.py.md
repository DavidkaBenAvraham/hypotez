## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный блок кода реализует механизм управления симуляцией, включающий в себя:

- **Создание и управление симуляцией:** Создание симуляции с уникальным идентификатором, добавление в нее агентов, окружений и фабрик.
- **Состояние симуляции:** Управление состоянием симуляции (запущена/остановлена), возможность создания контрольных точек и загрузки состояния из кэша.
- **Механизмы кэширования:** Сохранение истории состояния симуляции в кэше для ускорения повторных запусков. 
- **Транзакции:** Управление транзакциями, позволяющее выполнять операции с объектами в симуляции, сохраняя их состояние и отслеживая изменения.

Шаги выполнения
-------------------------
1. **Создание объекта `Simulation`:**
    - Создается объект `Simulation` с уникальным идентификатором.
    - Опционально можно задать начальное состояние кэша.
2. **Начало симуляции:**
    - Вызов метода `begin()` для начала симуляции.
    - Задается путь к файлу кэша (опционально).
    - Включается автоматическое сохранение контрольных точек после каждой транзакции (опционально).
3. **Добавление агентов, окружений и фабрик:**
    - Вызов методов `add_agent()`, `add_environment()` и `add_factory()` для добавления соответствующих объектов в симуляцию.
4. **Управление транзакциями:**
    - Используется декоратор `transactional` для выполнения функций в рамках транзакции. 
5. **Окончание симуляции:**
    - Вызов метода `end()` для завершения симуляции.
    - Автоматически сохраняется контрольная точка.
6. **Сохранение контрольной точки:**
    - Вызов метода `checkpoint()` для сохранения текущего состояния симуляции в кэше.

Пример использования
-------------------------

```python
from tinytroupe.control import Simulation, transactional
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory.tiny_factory import TinyFactory

# Создаем симуляцию
simulation = Simulation(id="my_simulation")

# Добавляем агентов, окружения и фабрики в симуляцию
agent1 = TinyPerson(name="Agent1")
agent2 = TinyPerson(name="Agent2")
environment = TinyWorld(name="MyWorld")
factory = TinyFactory(name="MyFactory")

simulation.add_agent(agent1)
simulation.add_agent(agent2)
simulation.add_environment(environment)
simulation.add_factory(factory)

# Запускаем симуляцию
simulation.begin(cache_path="my_simulation.cache.json", auto_checkpoint=True)

# Выполняем транзакцию
@transactional
def do_something(agent: TinyPerson):
    # ... some code ... 
    return agent.say("Hello!")

# Вызываем функцию в рамках транзакции
result = do_something(agent1)
print(result)

# Завершаем симуляцию
simulation.end()
```

В этом примере создается симуляция с идентификатором "my_simulation", затем добавляются агенты, окружения и фабрика. Затем запускается симуляция с кэшированием и автоматическим сохранением контрольных точек. Функция `do_something` помечена декоратором `transactional`, что делает ее транзакционной. При ее вызове выполняется функция и сохраняется ее состояние.