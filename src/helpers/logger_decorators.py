import functools
import asyncio
from .logger import logger

"""! @var Определяет вкл/выкл декоратора.
@details  Jupyter notebook плохо работает с моим декоратором.
@todo Надо разобраться с этой проблемой.
"""

def logs_and_errors_decorator(default_return: bool = False):
    """!
    @brief Декоратор, перехватывающий исключения и логирующий различные уровни сообщений синхронных и асинхронных функций.

    @param default_return: Значение, которое возвращает декорированная функция при возникновении исключения.
    
    @details `default_return` может принимать любые значения в зависимости от того, что имеет смысл в контексте вашей программы. Это может быть `None`, число, строка, булево значение, объект, список и так далее.

    Выбор значения `default_return` зависит от конкретного случая использования вашей функции и того, какой результат вы хотите предоставить в случае возникновения исключения.

    Примеры значений `default_return`:

    1. **None:** Часто используется, если функция должна вернуть объект, но возможны ситуации, когда это не удается, например, из-за ошибки ввода.

        ```python
        def some_function(value):
            try:
                result = int(value)
            except ValueError:
                return None
            return result
        ```

    2. **0 или другое числовое значение:** Если функция выполняет какие-то вычисления, и вы хотите вернуть "безопасное" значение в случае ошибки.

        ```python
        def divide(a, b):
            try:
                result = a / b
            except ZeroDivisionError:
                return 0
            return result
        ```

    3. **Пустой объект (список, строка, словарь и т.д.):** Если функция обычно возвращает объект, но может не смочь это сделать из-за ошибки.

        ```python
        def read_file_contents(file_path):
            try:
                with open(file_path, 'r') as file:
                    contents = file.read()
            except FileNotFoundError:
                return ''
            return contents
        ```

    Выбор значения `default_return` зависит от того, что для вашей функции является "безопасным" или "уместным" значением в случае ошибки.
    
    @return Обернутая функция с логированием исключений и дополнительной информации.

    @details
    Декоратор, который можно применять как к обычным методам, так и к статическим методам.
    При возникновении исключения логируется как имя метода, так и имя объекта (если метод является обычным методом).
    Также логируется информационное сообщение после успешного выполнения метода, отладочная информация и критическая информация.

    
    <pre>
    #@logs_and_errors_decorator(default_return=False)
    def some_method(self, *args, **kwargs):
        try:
            # код
        except Exception as eх:
            logger.error('text', ex)
            #####################################
            #   ЗДЕСЬ СРАБАТЫВАЕТ ДЕКОРАТОР.    #
            #####################################
    </pre>

    """

    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(obj, *args, **kwargs):
            """Обертка для синхронных методов."""
            obj_name = obj.__class__.__name__ if hasattr(obj, '__class__') else 'UnknownClass'
            func_name = func.__name__
          
            try:
                return func(obj, *args, **kwargs)
            except Exception as ex:
                obj_name = obj.__class__.__name__ if hasattr(obj, '__class__') else 'UnknownClass'
                func_name = func.__name__

                # Логирование ошибки с подробной информацией
                logger.error(
                    f"Ошибка при выполнении метода {func_name} объекта {obj_name}: {ex}",
                    exc_info=True
                )
                return default_return

        @functools.wraps(func)
        async def async_wrapper(obj, *args, **kwargs):
            """Обертка для асинхронных методов."""
            obj_name = obj.__class__.__name__ if hasattr(obj, '__class__') else 'UnknownClass'
            func_name = func.__name__
            
            try:
                return await func(obj, *args, **kwargs)
            except Exception as ex:
                obj_name = obj.__class__.__name__ if hasattr(obj, '__class__') else 'UnknownClass'
                func_name = func.__name__

                # Логирование ошибки с подробной информацией
                logger.error(
                    f"Ошибка при выполнении асинхронного метода {func_name} объекта {obj_name}: {ex}",
                    exc_info=True
                )
                return default_return

        # Возвращаю либо синхронную, либо асинхронную обертку в зависимости от функции
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return wrapper
    return decorator

pass     ## <- дебаг отсюда