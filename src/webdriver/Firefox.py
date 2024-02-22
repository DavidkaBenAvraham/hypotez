"""! @~russian вебдрайвер Firefox

@en_details This code defines a subclass of webdriver.Firefox called Firefox. 
        It provides additional functionality such as the ability to launch Firefox 
        in kiosk mode and the ability to set up a Firefox profile for the webdriver.

        The __init__method initializes the Firefox webdriver with the specified 
        launch options and profile. 
        
        The _options method returns a selenium.webdriver.firefox.options.Options object
        with the specified launch options. 
        
        The _profile method sets up a Firefox profile for the webdriver, 
        although the actual profile setup logic has not been implemented yet.

        Each method is accompanied by a docstring that explains its purpose, arguments, and return value (if any). 
        The class and its methods are also annotated with type hints to make the code more readable and easier to maintain.

        @details класс webdriver.Firefox 
        
@image html class_firefox.png
 
@section libs imports:
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
#from selenium.webdriver import FirefoxProfile
#from selenium.webdriver.common.action_chains import ActionChains <- нажималки
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

# -----------------------------------
from src.settings import gs
from src.helpers import logger, logs_and_errors_decorator, pprint, jprint
from src.io_interface import j_loads, j_dumps
# ------------------------------------



class Firefox(FF):
    """
    Subclass of `webdriver.Firefox` that provides additional functionality.

    
    @param actions (ActionChains): A `selenium.webdriver.common.action_chains.ActionChains` object that can be used to perform advanced interactions with the Firefox webdriver.

    """

    #actions: ActionChains = ActionChains(webdriver.Firefox)
    #@logs_and_errors_decorator (default_return =  False)
    def __init__(self, *args, **kwards) -> None:
        """! en_brief Initializes the Firefox webdriver with the specified launch options and profile.
        @~russian Определяю стартовые параметры для `Firefox`
        """
        logger.info(f''' Firefox ... ''')
        self._payload(self, *args, **kwards)


    #@logs_and_errors_decorator (default_return =  False)        
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

        @~russian _param service `Service`  :  `selenium.webdriver.firefox.service` представляет собой компонент `Selenium`, 
        который предоставляет возможность запуска драйвера `Firefox`. Он используется для настройки и запуска 
        сервиса драйвера `Firefox`. Обычно это делается с помощью `geckodriver`, который является драйвером для `Firefox`, 
        предоставляемым `Mozilla`. У меня он лежит в директории `bin`
  
        
        """
                         


        # selenium < 4.0.0
        #params: dict = {}
        ##TODO: проверить, куда записывается лог!
        #params['service_log_path'] = gs.path_to_dev_null
        #if not geckodriver is None:
        #    params['executable_path'] = geckodriver
        #if not _firefox_profile_path is None:
        #    params['firefox_profile'] = _firefox_profile_path
        #if not _options is None:
        #    params['options'] = _options
        #super().__init__(**params)
        # END selenium < 4.0.0)

        # selenium  4
        ff_settings: dict = j_loads (Path (gs.dir_src, 'webdriver', 'firefox.json' ) )
                                                                     
        geckodriver: str = str (ff_settings['geckodriver'] ) 
 
        profile: FirefoxProfile = self.set_profile (ff_settings.get('profile'))

        options: Options = self.set_options (ff_settings.get ('options') )

        pass

        

        # selenium < 4.0.0
        #
        #params: dict = {}
        ##TODO: проверить, куда записывается лог!
        #params['service_log_path'] = gs.path_to_dev_null
        #if not geckodriver is None:
        #    params['executable_path'] = geckodriver
        #if not _firefox_profile_path is None:
        #    params['firefox_profile'] = _firefox_profile_path
        #if not _options is None:
        #    params['options'] = _options
        #super().__init__(**params)
        # END selenium < 4.0.0)



        # selenium  4
        if not profile is None:
            options.profile = profile

        # selenium 4 ; geckodriver = 0.33
        service = Service ( str (Path (gs.dir_binaries, geckodriver) ), log_output = str( Path (gs.dir_log, f'{gs.get_now()}_firefox.txt' ) ) )
        
        # selenium 4.17; geckodriver = 0.34
        """! 64 битная версия еще не вышла """
        #options.binary_location = str (gs.dir_binaries)
        #options.binary = str (Path (gs.dir_binaries, geckodriver) )
        #service = Service (executable_path=geckodriver,  log_output = str( Path (gs.dir_log,'firefox.txt' ) ) )
        
        """! @~russian _var service `Service`
        @details 
            `Service` в модуле `selenium.webdriver.firefox.service` представляет собой компонент `Selenium`, 
            который предоставляет возможность запуска драйвера `Firefox`. Он используется для настройки и запуска 
            сервиса драйвера `Firefox`. Обычно это делается с помощью `geckodriver`, который является драйвером для `Firefox`, 
            предоставляемым `Mozilla`. У меня он лежит в директории `bin`
            """
        try:
            #super().__init__(options=options, service=service) # <- geckodriver = 0.33
            super().__init__(options=options)
            pass
        except WebDriverException as ex:
            logger.critical(f'''
            ---------------------------------
                    Не поднялся драйвер
                    так бывает при обновлениях самого Firefox
                    ну, или он не установлен в ос.
            ----------------------------------
                        ''', ex)
            return False

        except Exception as ex:
            logger.critical(' Упал webdriver Firefox. Общая ошибка: ', ex)
            return False
         # END selenium 4
         
        logger.info(f''' ... стартовал ''')
        
    #@logs_and_errors_decorator (default_return =  False)
    def set_options(self, opts = None) -> Options:
        """! Launch options for the Firefox webdriver include:
            `kiosk` : Launches Firefox in full window mode.
            `headless` : Firefox window is hidden
            
        @returns selenium.webdriver.firefox.options.Options `Options`  :  object with the specified launch options.
        An `Options` object containing the specified launch options, or `None` if no options are specified.            
        """

        options = Options()
        for opt in opts:
            
            if 'headless' in opt:
                options.headless = True
            else:
                options.add_argument(opt)
        return options

    #@logs_and_errors_decorator (default_return =  False)
    def set_profile(self, ff_profile: dict) -> FirefoxProfile:
        """! @brief Sets up a Firefox profile for the webdriver.
        @param ff_settings `dict` словарь установок из файла `firefox.json`
        @returns profile A `selenium.webdriver.FirefoxProfile` object representing the profile.
        """
        
        _profiles_path = ff_profile ['profile_path'] [ff_profile ['default_profile_from'] ]
        if '%APPDATA%' in _profiles_path:
            """!  Подключаюсь к профилю пользователя внутри ос
            переменную os `%APPDATA%` раскываю в абсолютный путь """
            _profiles_path: Path = Path (_profiles_path.replace ('%APPDATA%',os.environ.get('APPDATA')))
            """! @todo Здесь надо разобрать ситуацию а какой именно профиль брать в ос """
            _profiles_path: Path = Path(_profiles_path, ff_profile['default_profile_directory'][0])
        else:
            _profiles_path: Path = Path (gs.dir_root, 'src', 'webdriver', 'profiles','firefox_profiles', ff_profile['default_profile_directory'][0])
            """!  подключаю локальный профиль из папки `profiles` """

        profile = FirefoxProfile(profile_directory=_profiles_path)
        # TODO: Implement profile setup logic
        return profile
