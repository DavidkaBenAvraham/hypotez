from typing import Union
from selenium.webdriver.common.keys import Keys
from src.webdriver import Driver
from helpers import logs_and_errors_decorator
import asyncio
# ...

#@logs_and_errors_decorator(default_return=False)
def execute_locator(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union[str, list, dict, None, False]:
    return sync_execute_locator(driver, locator, keys)

#@logs_and_errors_decorator(default_return=False)
async def sync_execute_locator(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union[str, list, dict, None, False]:
    return await asyncio.to_thread(_execute_locator_sync, driver, locator, keys)

def _execute_locator_sync(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union[str, list, dict, None, False]:
    if all([locator['action'], locator['attribute']]) is None:
        return get_webelements_from_page(driver, locator)

    elif locator['action'] is None:
        return get_attributes_from_webelements(driver, locator)

    elif isinstance (locator['action'], str):
        return execute_action(driver, locator, keys)

    elif isinstance (locator['action'], list):
        attrs = []
        while len(locator['action']) > 0:
            _l = {
                "logic for attribue[AND|OR|XOR|VALUE|null]": locator['logic for attribue[AND|OR|XOR|VALUE|null]'],
                "attribute": locator['attribute'].pop(0),
                "by": locator['by'].pop(0),
                "selector": locator['selector'].pop(0),
                "use_mouse": locator['use_mouse'].pop(0),
                "action": locator['action'].pop(0),
                "logic for action[AND|OR|XOR|VALUE|null]": locator['logic for action[AND|OR|XOR|VALUE|null]'],
            }
            attrs.append(_execute_locator_sync(driver, _l, keys))

        return attrs

    elif isinstance(locator['action'], dict):
        # Feature not yet implemented
        pass
"""
Данный код представляет собой функцию execute_locator, которая предназначена для выполнения локаторов. 
Локатор - это спецификация, которая указывает, как найти элементы на веб-странице. Функция может быть вызвана как в асинхронном, так и в синхронном контексте.

Давайте разберемся с кодом:

#@logs_and_errors_decorator(default_return=False): Это декоратор, который, видимо, предназначен для обработки ошибок и логирования, 
возвращая False по умолчанию в случае ошибки.

async def execute_locator(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union[str, list, dict, None, False]: - 
Это асинхронная функция, которая принимает driver (объект WebDriver), locator (спецификация локатора) и необязательный аргумент keys (например, для отправки клавиш). 
Возвращает Union[str, list, dict, None, False], что означает, что функция может вернуть строку, список, словарь, None или False.

await asyncio.to_thread(_execute_locator_sync, driver, locator, keys): Эта строка использует asyncio.to_thread, чтобы выполнить синхронную функцию 
_execute_locator_sync в отдельном потоке. Это нужно, чтобы обеспечить совместимость асинхронного кода с синхронными библиотеками, такими как Selenium.

def _execute_locator_sync(driver: Driver, locator: dict, keys: Union[Keys, None] = None) -> Union[str, list, dict, None, False]: - 
Это синхронная функция, которая реализует логику выполнения локаторов. Она также принимает driver, locator и keys и возвращает аналогичный Union типов.

Основная логика в _execute_locator_sync состоит из проверок различных условий в локаторе и вызова соответствующих функций, 
таких как get_webelements_from_page, get_attributes_from_webelements, execute_action. 
Также, если locator['action'] является списком, функция рекурсивно вызывает _execute_locator_sync для каждого элемента списка.

В целом, этот код выполняет асинхронную обертку для выполнения локаторов, позволяя использовать его в асинхронном коде, например, 
вместе с асинхронным вызовом await execute_locator(...).
"""
