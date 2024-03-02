"""! @~russian Вебдрайвер Firefox

@en_details Этот код определяет подкласс webdriver.Firefox с именем Firefox. 
        Он предоставляет дополнительные функции, такие как возможность запуска Firefox 
        в полноэкранном режиме и настройка профиля Firefox для веб-драйвера.

        Метод __init__ инициализирует веб-драйвер Firefox с указанными параметрами запуска и профилем. 
        
        Метод _options возвращает объект selenium.webdriver.firefox.options.Options 
        с указанными параметрами запуска. 
        
        Метод _profile настраивает профиль Firefox для веб-драйвера, 
        хотя фактическая логика настройки профиля еще не реализована.

        Каждый метод сопровождается строкой документации, которая объясняет его назначение, 
        аргументы и возвращаемое значение (если оно есть). 
        Класс и его методы также аннотированы подсказками типа для более читаемого кода и удобства обслуживания.

        @details Класс webdriver.Firefox 

@image html class_firefox.png
 
@section libs Импорты:
  - pathlib 
  - attr 
  - os 
  - selenium.webdriver 
  - selenium.webdriver.firefox.options 
  - selenium.webdriver.firefox.service 
  - selenium.webdriver.firefox.firefox_profile 
  - selenium.common.exceptions 
  - gs 
  - gs 
  - gs 


"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


from pathlib import Path
import os
from selenium.webdriver import Firefox as FF
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException

# -----------------------------------
from src.settings import gs
from src.helpers import logger, logs_and_errors_decorator, pprint, jprint
from src.io_interface import j_loads, j_dumps
# ------------------------------------



class Firefox(FF):
    """! @~russian Подкласс `webdriver.Firefox`, предоставляющий дополнительные функции.

    Атрибуты:
        actions (ActionChains): Объект `selenium.webdriver.common.action_chains.ActionChains`, 
        который можно использовать для выполнения расширенных взаимодействий с веб-драйвером Firefox.
    """
    #actions: ActionChains = ActionChains(webdriver.Firefox)

    #@logs_and_errors_decorator(default_return=False)
    def __init__(self, *args, **kwards) -> None:
        """! @~russian Инициализирует веб-драйвер Firefox с указанными параметрами запуска и профилем.
        @details Определяет стартовые параметры для `Firefox`.
        @param args `*args`  :  Дополнительные аргументы.
        @param kwards `**kwards`  :  Дополнительные именованные аргументы.
        """
        logger.info(f''' Firefox ... ''')
        self._payload(self, *args, **kwards)

    #@logs_and_errors_decorator(default_return=False)        
    def _payload(self, *args, **kwards):
        """! @~russian Загрузка стартовых параметров для запуска  `Firefox` 
        @param args `*args`  :  Дополнительные аргументы.
        @param kwards `**kwards`  :  Дополнительные именованные аргументы.
        

        @param profile `FirefoxProfile`  :  Профиль Firefox для веб-драйвера. Предоставляет возможность настройки профиля Firefox для веб-драйвера. 
        Профиль включает в себя такие параметры, как настройки пользовательского агента, 
        блокировка всплывающих окон и другие параметры.

        Примеры использования:

        1. **Создание профиля с пользовательским агентом:**
            ```python
            profile = FirefoxProfile()
            profile.set_preference("general.useragent.override", "user-agent-string")
            ```

        2. **Отключение изображений:**
            ```python
            profile = FirefoxProfile()
            profile.set_preference("permissions.default.image", 2)
            ```

        3. **Блокировка всплывающих окон:**
            ```python
            profile = FirefoxProfile()
            profile.set_preference("dom.disable_open_during_load", False)
            ```

        4. **Настройка пути сохранения файлов:**
            ```python
            profile = FirefoxProfile()
            profile.set_preference("browser.download.dir", "/path/to/download/folder")
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            ```

        5. **Отключение браузерных уведомлений:**
            ```python
            profile = FirefoxProfile()
            profile.set_preference("dom.webnotifications.enabled", False)
            ```

        @see [Документация по настройкам профиля Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)

        @param options `Options`  :  Ниже приведены некоторые распространенные опции, которые можно использовать.
        Примеры использования:
        @note
        1. **Запуск в режиме "headless" (без отображения окна браузера):**
            ```python
            options = FirefoxOptions()
            options.headless = True
            ```

        2. **Установка языка браузера:**
            ```python
            options = FirefoxOptions()
            options.add_argument('-lang=es')  # Здесь устанавливается испанский язык.
            ```

        3. **Задание пользовательских параметров командной строки:**
            ```python
            options = FirefoxOptions()
            options.add_argument('--some-option=value')
            ```

        4. **Управление отладочными сообщениями:**
            ```python
            options = FirefoxOptions()
            options.add_argument('-vv')  # Установка высокого уровня отладочных сообщений.
            ```

        5. **Запуск в режиме полноэкранного окна:**
            ```python
            options = FirefoxOptions()
            options.add_argument('--kiosk')  # Запуск в полноэкранном режиме.
            ```

        @see [Документация по опциям Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)

        options = FirefoxOptions()

  
        @returns options `selenium.webdriver.firefox.options.Options`  :  Объект с указанными параметрами запуска.
        """
        """
        ff_settings: dict = j_loads(Path(gs.dir_root, 'src', 'webdriver', 'firefox.json'))
        geckodriver_path: str = str(Path(gs.dir_binaries, 'geckodriver.exe'))
        profile: FirefoxProfile = self.set_profile(ff_settings)
        options: Options = self.set_options(ff_settings.get('options'))

        # selenium < 4.0.0
        #params: dict = {}
        ##TODO: проверить, куда записывается лог!
        #params['service_log_path'] = gs.path_to_dev_null
        #if not geckodriver_path is None:
        #    params['executable_path'] = geckodriver_path
        #if not _firefox_profile_path is None:
        #    params['firefox_profile'] = _firefox_profile_path
        #if not _options is None:
        #    params['options'] = _options
        #super().__init__(**params)
        # END selenium < 4.0.0)

        # selenium  4
        if not profile is None:
            options.profile = profile

        # selenium  4
        
        @~russian _param service `Service`  :  `selenium.webdriver.firefox.service` представляет собой компонент `Selenium`, 
        который предоставляет возможность запуска драйвера `Firefox`. Он используется для настройки и запуска 
        сервиса драйвера `Firefox`. Обычно это делается с помощью `geckodriver`, который является драйвером для `Firefox`, 
        предоставляемым `Mozilla`. У меня он лежит в директории `bin`
        """
        ff_settings: dict = j_loads (Path (gs.dir_root, 'src', 'webdriver', 'firefox.json' ) )
        
        geckodriver_path: str = str (Path ( gs.dir_binaries, 'geckodriver.exe' ) )
 
        profile: FirefoxProfile = self.set_profile (ff_settings)

        options: Options = self.set_options (ff_settings.get ('options') )
        
        service = Service(geckodriver_path, log_output=gs.dev_null)
        
        try:
            super().__init__(service=service, options=options)
        except WebDriverException as ex:
            logger.critical(f'''
        ---------------------------------
                Не поднялся драйвер
                так бывает при обновлениях самого Firefox
                ну, или он не установлен в ос.
        ----------------------------------
                         '' {ex}')
            return False
        except Exception as ex:
            logger.error(' Упал webdriver Firefox  {ex}')
            return False
         # END selenium 4
         
        logger.info(f''' ... стартовал ''')

    #@logs_and_errors_decorator(default_return=False)
    def set_options(self, opts=None) -> Options:
        """! @~russian Опции запуска веб-драйвера Firefox Запуск вариантов для веб-драйвера Firefox включает в себя:
            `kiosk` : Запускает Firefox в полноэкранном режиме.
            `headless` : Окно Firefox скрыто
            
        @param opt `list | ? options` входные опции 
        @тодо проверить
        
        
        @param options `Options`  :  Ниже приведены некоторые распространенные опции, которые можно использовать.

        Примеры использования:

        1. **Запуск в режиме "headless" (без отображения окна браузера):**
            ```python
            options = FirefoxOptions()
            options.headless = True
            ```

        2. **Установка языка браузера:**
            ```python
            options = FirefoxOptions()
            options.add_argument('-lang=es')  # Здесь устанавливается испанский язык.
            ```

        3. **Задание пользовательских параметров командной строки:**
            ```python
            options = FirefoxOptions()
            options.add_argument('--some-option=value')
            ```

        4. **Управление отладочными сообщениями:**
            ```python
            options = FirefoxOptions()
            options.add_argument('-vv')  # Установка высокого уровня отладочных сообщений.
            ```

        5. **Запуск в режиме полноэкранного окна:**
            ```python
            options = FirefoxOptions()
            options.add_argument('--kiosk')  # Запуск в полноэкранном режиме.
            ```

        @see [Документация по опциям Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)

        options = FirefoxOptions()

  
        @returns options `selenium.webdriver.firefox.options.Options`  :  Объект с указанными параметрами запуска.
        """
        options = Options()
        for opt in opts:
            if 'headless' in opt:
                options.headless = True
            else:
                options.add_argument(opt)
        return options

    #@logs_and_errors_decorator(default_return=False)
    def set_profile(self, ff_settings: dict) -> FirefoxProfile:
        """! @brief Настраивает профиль Firefox для веб-драйвера.
        @param ff_settings `dict`  :  Словарь установок из файла `firefox.json`.
        @returns profile `selenium.webdriver.FirefoxProfile`  :  Объект, представляющий профиль.
        """
        _profile_directory = ff_settings['profiles_path'][ff_settings['profile_from']]
        if '%APPDATA%' in _profile_directory:
            """!  Подключаюсь к профилю пользователя внутри ОС
            переменную окружения `%APPDATA%` разворачиваю в абсолютный путь """
            _profile_directory: Path = Path(_profile_directory.replace('%APPDATA%', os.environ.get('APPDATA')))
            """! @todo Здесь нужно рассмотреть, какой именно профиль использовать в ОС """
            logger.info ('Подключаюпрофиль из %APPDATA% ')
        else:
            _profile_directory: Path = Path(gs.dir_root, 'src', 'webdriver', 'profiles', 'firefox_profiles',
                                        ff_settings['default_profile_directory'][0])
            logger.info ('Подключаю локальный профиль из папки `profiles`')
            """!  Подключаю локальный профиль из папки `profiles` """

        profile = FirefoxProfile(profile_directory=_profile_directory)
        # TODO: Реализовать логику настройки профиля
        return profile
