# Документация модуля `switch_account`

## Обзор

Модуль `switch_account` предназначен для автоматизации процесса переключения между аккаунтами в Facebook с использованием веб-драйвера. Он содержит функцию `switch_account`, которая выполняет переключение аккаунта, если на странице присутствует соответствующая кнопка.

## Подробней

Этот модуль является частью системы автоматизации взаимодействия с Facebook и предназначен для использования в сценариях, где необходимо переключаться между различными учетными записями. Он использует локаторы, определенные в JSON-файле, для поиска кнопки переключения аккаунта и выполнения клика по ней.

## Функции

### `switch_account`

```python
def switch_account(driver: Driver):
    """ Функция нажимает на кнопку "Переключить", если она существует.
    Args:
        driver (Driver): Инстанс веб-драйвера для управления браузером.

    Returns:
        None

    Raises:
        None

    Example:
        >>> from src.webdriver.driver import Driver
        >>> from src.webdriver.chrome import Chrome
        >>> driver = Driver(Chrome)
        >>> switch_account(driver)
    """
    def execute_locator(locator: dict):
        """Выполняет действие, определенное в локаторе, используя веб-драйвер.

        Args:
            locator (dict): Словарь, содержащий параметры локатора элемента на веб-странице.

        Returns:
            WebElement | None: Найденный веб-элемент или None, если элемент не найден.

        Raises:
            Exception: Если элемент не найден или происходит другая ошибка при выполнении локатора.
        """
        ...

    # Функция выполняет клик по кнопке "Переключить", используя веб-драйвер, если такая кнопка присутствует на странице.

    # Читает параметры кнопки из `locator.switch_to_account_button`.
    # Вызывает `driver.execute_locator` для поиска и клика по элементу.