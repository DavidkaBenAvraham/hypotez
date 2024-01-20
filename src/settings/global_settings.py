"""! @~russian @brief Стартовые настройки программы 
@details Все логины, пути, аккаунты, API и другая чувствительная информация хранится в базе данных keepass.
Открытые настройки находятся в файле `global_settings.json`

@~english
@brief  
@details Global Project Settings:  
 paths, passwords, logins, and API settings.
 Sensitive information such as passwords, keys, APIs, and other credentials 
 are stored in `src/gs/db.kdbx` Needs the master password to open database

--------

### Flowchart

@image html diagrams-gs.png

@section libs imports:
  - gs 
  - os 
  - sys 
  - datetime 
  - pathlib 
  - getpass 
  - pykeepass 
  - attr 
  - src.io_interface 
  - src.helpers 

 @~russian 
@note Для однозначной интерпретации слешей в разных ос я все пути объявляю как объекты `Path`
@todo корневая директория может иметь любое название. Сейчас в коде жестко зашито `hypotez` Надо добавить опцию выбора имени коревой директории в файл конфигурации.
        (не срочно)
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

# Imports
import asyncio
import os
import sys
import datetime
from pathlib import Path
from attr import setters
from typing import Union

from src.helpers.beeper import Beeper


# -----------------------------------
# 1.

# dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind(r'\hypotez\src')])
dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind('hypotez') + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))
"""! @~english Adding my working directory to the system variable `OS.Path`"""
"""! @~russian Добавляю свою рабочую директорию в системную переменную `OS.Path`"""

# -----------------------------------

# Imports
from typing import Union
import os
import sys
import datetime
from pathlib import Path
from pykeepass import PyKeePass, entry
import getpass  # <- модуль поля ввода типа password
from src.helpers import logger, logger_decorators, logs_and_errors_decorator, KeepassException, DefaultSettingsException,  Beeper, BeepLevel, jprint, pprint
from src.io_interface import j_loads
# -----------------------------------


class ProjectSettings():
    """!@~russian @brief `ProjectSettings` - определяяет параметры запуска программы.
     @details Класс-синглтон, который хранит основные параметры и настройки проекта. 
      Класс разработан таким образом, чтобы существовал только один его экземпляр в программе. Он использует шаблон проектирования "Singleton", чтобы гарантировать, что у нас есть единственный и общий источник настроек для всего проекта.
      
    Основные параметры:
    - Источники Настроек хранятся в двух местах - в файле `global_settings.json` и в базе данных Keepass `db.kdbx`. В Keepass хранятся пароли и другая чувствительная информация.
    - Параметры Подключения: Предоставляет методы для получения параметров подключения к различным службам и базам данных, таким как AliExpress API, PrestaShop API, OpenAI, FTP, SMTP и т.д.
    - Настройки Поставщиков: Хранит список поставщиков, для которых выполняются сценарии.
    - Режимы Запуска: Возможность выбора между многозадачным и последовательным режимами выполнения программы.
    - Пути Директорий: Предоставляет абсолютные пути к различным директориям проекта, таким как логи, экспорт, бинарные файлы и временная директория.
    - `default_webdriver`: Хранит информацию об инстансе вебдрайвера, который может быть использован для автоматизации действий в браузере.
    - Словарь Поставщиков: Содержит информацию о поставщиках из файла suppliers/suppliers_dict.json. (Зачем???)
    - Локаль: Устанавливает язык, на котором будет выполняться сценарий.
    - PyKeePass: Используется для работы с базой данных Keepass.
  

    При инициализации класса `ProjectSettings` программа считывает настройки по умолчанию из файла `src/gs/global_settings.json`. \n
     Пароли, ключи, API и другие учетные данные хранятся в базе данных `src/gs/db.kdbx`. \n
     <b>Для открытия базы данных от вас требуется ввести мастер пароль</b>. 

     Настройки хранятся в двух местах: открытые данные, например, пути и защищенные данные, например, пароли 
     - файл `global_settings.json` (`src/gs/global_settings.json`)
     - база данных keepass<sup>1)</sup> `db.kdbx` (`src/gs/db.kdbx`)
     @note
    <sup>1)</sup> KeePass - хранилище паролей с AES  шифрованием . 
    Для работы с ним я использую библиотеку `pykeepass`. Для открытия базы данных необходим мастер пароль. 
    Подробней о [keepass](https://keepass.info/help/base/index.html)  
    @todo переделать логику работы с базой keepass. Брать парамерты группами и потом получать их через цикл
    
    @param async_run `bool` : Флаг разрешения испонения в асинхронном режиме.
    @note Асинхронный режим не работает в jupyter.
    
    @param dir_root
    
    
    @~russian _note Переменные для хранения и управления различными типами учетных данных, 
    используются для хранения учетных данных для различных сервисов, таких как `AliExpress API, 
    PrestaShop API, база данных PrestaShop, FTP и SMTP`. Переменные включают в себя как списки, используемые для хранения 
    нескольких наборов учетных данных, так и словари, используемые для конкретных учетных данных, 
    связанных с определенным сервисом.
    
    @param supplier_prefix `list` : Список поставщиков для которых будут исполняться сценарии.
    
    @param kp `PyKeePass` объект keepass (создается, читается и унчтожается при инициализации класса)
    
    @param api_aliexpress `dict` ключ API aliexpress
    
    @param prestashop_api `dict` ключ  API Prestashop
    
    @param api_openai `str` ключ  openAI
    
    @param keepass_prestashop_db `(list [dict])` список ключей к базам данных Prestashop
    
    @param list_api_aliexpress_credentials: `list` = список ключей к базам данных Prestashop
    
    @param list_prestashop_api_credentials: `list` = []
    
    @param list_prestashop_db_credentials: `list` = []
    
    @param list_ftp_credentials: `list` = [] : 
    
    @param list_smtp_credentials: `list` = [] : 
    
    @param default_api_openai_credentials: `str` = None : 
    
    @param default_prestashop_api_credaentials: `dict` : 
    
    @param default_prestashop_db_credentials: `dict` : 
    
    @param default_ftp_credentials: `dict` : 
    
    @param default_smtp_credentials: `dict` :  
    
    @param settings `dict`  :  содержит словарь, полученый из файла установок по умолчанию `global_settings.json`
    
    ### Fragment global_settings.json:
        <code><pre>
        {
      "venv": "venv",
      "mode": "debug",
      "modes": [ "debug", "prod" ],
      "languages": [ "en", "he", "ru" ],
      "languages_excluded": [ "es", "fr", "it", "uk" ],
      "scenario_language": [ "en" ],
      "threads": false,
      "about threads": "многопоточность программы",

      "program_paths": {
        "export": "export",
        "export_images": "export_images",
        "logs": "log",
        "binaries": "binaries",
        "temp": "tmp"
      },

      "beeper and decorator": {
        "silent": true,
        "onoff_log_decorator": true
      },


      "default_webdriver": "firefox",
      "default_aliexpress_api_title": "katia",
      "default_prestashop_api_title": "emil-design.com",
      "default_openai_api_title": "hypotez",
      "default_prestashop_db_title": "emil-design.com",
      "default_ftp_title": "emil-design.com",
      "default_smtp_title": "davidka",
      "default_prestashop_api_domain": "emil-design.com",
      "list_prestashop_api_domains": [ "emil-design.com", "sergey.mymaster.co.il", "dev.e-cat.co.il" ],

      "supplier_prefix": [
        "aliexpress",
        "hb",
        "kualastyle",
        "amazon",
        "bangood",
        "kualastyle",
        "ksp",
        "morlevi"
      ]
        </pre></code>
    
    @param beep `bool` : Флаг вкл/выкл звуковой сигнал логера. 
    @note При запуске из `jupyter` не получается запускать асинхронные вызовы. Бипер работает асинхронно, 
    он не зависит от хода прогаммы
    
    @param supplier_prefix `list` :  Список поставщиков для запуска по умолчанию, 
    
    @param async_run `bool` : Флаг асинхронного выполненения кода
    ### Flowchart

    @image html global_settings.ProjectSettings.png
    
    @todo разделить значения по группам: `runtime environment`, `development environment`, `suppliers`, `log setings`, etc
    """
    
    dir_root = dir_root
    dir_src = dir_src
    settings: dict = j_loads (Path (dir_root, 'src', 'settings', 'global_settings.json') )
    
    # -------------------------------- CREDENTIALS ------------------------------------
    
    list_openai_credentials: list = []
    
    # List to store AliExpress API credentials
    list_api_aliexpress_credentials: list = []
    """! @param list_api_aliexpress_credentials список API ключей Aliexpress """
    
    # List to store PrestaShop API credentials
    list_prestashop_api_credentials: list = []

    # List to store PrestaShop database credentials
    list_prestashop_db_credentials: list = []

    # List to store FTP credentials
    list_ftp_credentials: list = []

    # List to store SMTP credentials
    list_smtp_credentials: list = []

    # Default OpenAI API key
    default_api_openai_credentials: str = None


    # Default PrestaShop API credentials
    default_prestashop_api_credentials: dict = {}

    # Default PrestaShop database credentials
    default_prestashop_db_credentials: dict = {}

    # Default FTP credentials
    default_ftp_credentials: dict = {}

    # Default SMTP credentials
    default_smtp_credentials: dict = {}
    """
    @english
    @brief Variables to store and manage various types of credentials.

    @details These variables are used to store credentials for different services, such as AliExpress API, PrestaShop API,
    PrestaShop database, FTP, and SMTP. The variables include both lists and dictionaries, where lists are used for storing
    multiple sets of credentials, and dictionaries for specific credentials associated with a particular service.

    """

    # ---------------------------------------------- DEFAULT SETTINGS ------------------------------------

    logger_onoff_decorator: bool = None
    """! вкл/выкл декоратор ошибок 
    @todo Не работает. Надо пилить """
     
    beeper = settings['beeper_and_log_decorator']['silent']
    """! @~russian Бипер в декораторе запускается асинхронно! 
    Это не работает в jupyter, поэтому я его отключаю еще до запуска  декорированных функций """

    threads: bool = None
    """! Флаг запуска многопоточности """
    
    scenario_language: str = None
    
    default_webdriver: str = None
    
    async_run: bool = None
    """! флаг асинхронного исполнения функций """
    
    supplier_prefix: list = None
    """! @~russian _note  `supplier_prefix` Список поставщиков для которых я буду выполнять сценарии 
    @details `supplier_prefix` на протяжении всего кода означает  список поставщиков над которым будет выполнятся операция
    При инициализации класса `Supplier` служит указателем, какого именно поставщика будет содержать инициализируемый класс
    """

    _instance = None
    
    ##@logs_and_errors_decorator(default_return=False)
    def __new__(cls, *args, **kwargs):
        """! @~russian Создаю инстанс  """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    ##@logs_and_errors_decorator(default_return=False)
    @classmethod
    def get_instance (cls) -> _instance:
        """! @~russian Проверяю, а есть ли инстанс?
       @details Если инстанса класса еще нет - создаю, иначе возвращаю сам инстанс"""
        if not cls._instance:
            cls._instance = cls()
            logger.info('Старт инстанса `gs`')
        return cls._instance


    #@logs_and_errors_decorator (default_return=None)
    def __init__ (self, *attrs, **kwards) -> None:
        """! @~russian Конструктор        
         @param self  :  pointer
         @param *attrs `tuple`  :  collects positional arguments into a tuple
         @param **kwards `dict`  :  collects keyword arguments into a dictionary
        """
        
        if not self._payload (*attrs, **kwards): 
            raise DefaultSettingsException('Возникло исключение в функции `_payload()`')
        


# ----------------------------------------------------------------------------------------------------------#
#                                                        PAYLOAD                                            #
# __________________________________________________________________________________________________________#



    #@logs_and_errors_decorator (default_return = False)
    def _payload (self, *attrs, **kwargs) -> bool:
        """! @~russian 
        @brief функция начальных установок программы
        @details Функция берет данные из файла `global_settings.json` и базы данных `db.kdbx` 
        Функция вызывается из конструктора класса. Возвращает `True` в случае успеха, иначе `False`

        @param self  :  pointer
        @param *attrs `tuple`  :  собирает позиционные аргументы в кортеж
        @param **kwargs `dict`  :  собирает именованные аргументы в словарь
        
        @param settings `json`  :  установки программы, записаные в файле `global_settings.json`
        
        @param default_aliexpress_api_title
        @param default_prestashop_api_title `str`  :  поле `Title` в базе данных keepass.
        @param default_prestashop_db_title `str`  :  поле `Title` в базе данных keepass
        @param default_openai_api_title `str`  :  поле `Title` в базе данных keepass
        @param default_ftp_title `str`  :  поле `Title` в базе данных keepass
        @param default_smtp_title `str`  :  поле `Title` в базе данных keepass
        @returns `True` if succes, `Flase` otherwise
        
        """
        

        # Чтение настроек из файла JSON 
        self.settings = j_loads (Path (self.dir_root, 'src', 'settings', 'global_settings.json') )
        
        
        if not self.settings:
            logger.critical(f'ошибка чтения файла global_settings.json', ex)
            return False
        try:
            """! key names for keypass """
            default_aliexpress_api_title: str = self.settings ['default_aliexpress_api_title']
            default_prestashop_api_title: str = self.settings ['default_prestashop_api_title']
            default_prestashop_db_title: str = self.settings ['default_prestashop_db_title']
            default_openai_api_title: str =  self.settings ['default_openai_api_title']
            default_ftp_title: str =  self.settings ['default_ftp_title']
            default_smtp_title: str =  self.settings ['default_smtp_title']
            
            self.async_run: bool = self.settings ['async_run']
            
            self.supplier_prefix: list = self.settings ['supplier_prefix']
            """! получаю список поставщиков для выполнения сценариев """
            
            self.logger_onoff_decorator = self.settings ['beeper_and_log_decorator']['onoff_log_decorator']
            Beeper.silent: bool = self.settings ['beeper_and_log_decorator']['silent']
            """! Включаю / отлючаю лог декораторы. При работе с jupyter ne получается испоьзовать асинхронность """    

        except DefaultSettingsException as ex:
            logger.critical ('Ошибка в получении дaнных из `global_settings.json', ex)
            return False



        # Подключение к базе данных Keepass
        kp: PyKeePass = self.open_kp()
        if not kp: return False


        # ------------------------------- default_webdriver, scenario_language, threads ----------------
        try:
            self.default_webdriver = self.settings.get ('default_webdriver', 'firefox')
            self.scenario_language = self.settings.get ('scenario_language', 'en')
            self.threads = self.settings.get ('threads', False)
            
        except DefaultSettingsException as ex:
            logger.error(f'ошибка установки дефолтного вебдрайвера', ex)
            return False
                

        # ----------------------- ALIEXPRESS ------------------------
        try:
            entries = kp.find_groups (path= ['suppliers', 'aliexpress', 'api'] ).entries
        except KeepassException as ex:   
            logger.critical (f'Ошибка извлечения ключа Aliexpress ')    
            return False
        try:    
            for entry in entries:
                entry_dict = {
                 'api_key': entry.custom_properties ['api_key'],
                 'secret': entry.custom_properties ['secret'],
                 'tracking_id': entry.custom_properties ['tracking_id'],
                 'email': entry.custom_properties ['email'],
                 'kp_user_name' : entry.username,
                 }
                
                self.list_api_aliexpress_credentials.append(entry_dict)
                
                if entry.title == default_aliexpress_api_title: 
                    self.default_aliexpress_api_credentials = entry_dict
                
        except Exception as ex:
            logger.error(f'Не удалось вытащить ключ API Aliepress из KeePass. Ошибка ', ex)
            return False
            
        # ----------------------- OPENAI ----------------------------
        try:
            """! """
            entries = kp.find_groups (path= ['openai']).entries
        except KeepassException as ex:   
            logger.critical (f'Ошибка извлечения ключа OpenAI ')
            return False
        try:
            entry_dict: dict = {}
            for entry in entries:
                entry_dict = {
                 'api_key': entry.custom_properties ['api_key'],
                 'kp_username': entry.username,
                 
                 }
                
                self.list_openai_credentials.append(entry_dict)
                
                """! @~russian _note У меня только один API OpenAI ключ"""
                if entry.title == default_openai_api_title: 
                        self.default_openai_api_credentials = entry_dict      
                
        except Exception as ex:
            logger.error(f'Ошибка openai из KeePass', ex)
            return False
        
       
        
        # ------------------------- PRESTASHOP API ----------------------
        try:
            """! """
            entries = kp.find_groups(path=['prestashop','api']).entries

            for entry in entries:
                entry_dict = {
                        'api_key' : entry.custom_properties['api_key'],
                        'api_domain': entry.custom_properties['api_domain'],
                        'kp_username': entry.username,
                        }
                self.list_prestashop_api_credentials.append(entry_dict)
                
                if entry.title == default_prestashop_api_title: 
                        self.default_prestashop_api_credentials = entry_dict   
                        
        except Exception as ex:
            logger.error(f'ошибка установки значений престашоп ', ex)
            return False
            
        # ------------------------- DB -------------------------------
        
        try:
            """! """
            entries = kp.find_groups(path=['prestashop','db']).entries
            
            for entry in entries:
                entry_dict = {
                        'server' : entry.custom_properties['server'],
                        'port' : entry.custom_properties['port'],
                        'db_name' : entry.custom_properties['db_name'],
                        'user' : entry.username,
                        'password' : entry.password,
                        'kp_username' : entry.username,
                        }
                self.list_prestashop_db_credentials.append(entry_dict)
                
                if entry.title == default_prestashop_db_title:
                    self.default_prestashop_db_credentials = entry_dict
                    
        except Exception as ex:
            logger.error(f'ошибка установки значений престашоп DB', ex)
            return False                    
                    
         # ------------------------- FTP -------------------------------
        
        try:
            """! """
            entries = kp.find_groups(path=['ftp']).entries
            
            for entry in entries:
                entry_dict = {
                        'server' : entry.url,
                        'port' : entry.custom_properties['port'],
                        'user' : entry.username,
                        'password' : entry.password,
                        'kp_username' : entry.username,
                        }
                self.list_ftp_credentials.append(entry_dict)
                if entry.title == default_ftp_title:
                    self.default_ftp_credentials = entry_dict
                    
        except Exception as ex:
            logger.error(f'ошибка установки значений FTP', ex)
            return False                     
                
                
        # --------------------------- SMTP ---------------------------
        try:
            """! """
            entries = kp.find_groups(path=['smtp']).entries
            
            for entry in entries:
                entry_dict = {
                'server': entry.custom_properties['server'],
                'user' : entry.username,
                'password' : entry.password,
                'receiver': entry.custom_properties['receiver'],
                'kp_username' : entry.username,
                }
                self.list_smtp_credentials.append(entry_dict)
                
                if entry.title == default_smtp_title:
                    self.default_smtp_credentials = entry_dict
                    
        except Exception as ex:
            logger.error(f'ошибка установки значений SMTP', ex)
            return False            

                
        # -------------------------- PATH ---------------------------
        try:
            """! """
            # Определение абсолютных путей к директориям
            self.dir_export = Path(self.dir_root, 'export').absolute()
            self.dir_logs = Path(self.dir_root, 'logs').absolute()
            self.dir_binaries = Path(self.dir_root, 'bin').absolute()
            self.dir_temp = Path(self.dir_root, 'tmp').absolute()
        except Exception as ex:
            logger.error(f'ошибка ', ex)
            return False
                


        # Определение пути к null операционной системы
        self.dev_null = r'/dev/null' if os.name != 'nt' else 'nul'

        return True




    #------------------------------------------------------------- kp() -------------------------------------


    #@logs_and_errors_decorator (default_return =  False)
    def open_kp(self, attempts:int = 3) -> Union[PyKeePass, False]:
        """! @~russian 
        @brief Открываю файл keepass паролём
        @details Даю три попытки на открытие            
        
        @param attempts `int`  :  кол-во попыток            
        @returns kp `PyKeePass`  :  объект keepass            
        @todo неправильная логика обработки неправильного ввода пароля
        """
        
        if not Beeper.silent: asyncio.run(Beeper.beep(BeepLevel.INFO_LONG))
        
        password = getpass.getpass ('Master password for keepass database: ')   
        if len(password) == 0: self.open_kp(attempts)
        kp: PyKeePass =  None
        try:
            
            """! Возвращаю объект `KeePass` """
            kp = PyKeePass (str (Path (self.dir_root, 'src', 'settings', 'db.kdbx') ), password = password)
            return kp
        except Exception as ex:
            logger.error(f'ошибка ', ex)

            if attempts > 0:
                self.open_kp (attempts - 1)
                
            else:
                logger.error("Превышено максимальное количество попыток.")
                
                if logger.level_name.upper() == 'DEBUG':
                    logger.info(f'да и хуй с ним. Дебажим ')
                    self.open_kp (3)
                    
                else: return False
                
            
 

    # ------------------------------------------------------------- get_now() -------------------------------------
    #@logs_and_errors_decorator (default_return =  False)
    def get_now(self, dformat: str = '%Y%m%d%H%M%S') -> str:
        """! @~english
        @brief Returns a datestamp in the chosen format
        @details Returns a datestamp in the chosen format
        
        @param self `pointer`
        @param dformat  `str` = '%Y%m%d%H%M%S' : Output format for datetime 
        """
        """! @~russian 
        @brief Возвращает метку даты в выбранном формате
        @details Возвращает метку даты в выбранном формате
        
        @param self `указатель`
        @param dformat  `str` = '%Y%m%d%H%M%S' : Формат вывода для datetime 
        """
        return datetime.datetime.now().strftime(dformat)



    # ------------------------------------------------------------- GET API ALIEXPRESS -------------------------------------

    
    #@logs_and_errors_decorator (default_return =  False)
    def get_credentials_api_aliexpress(self, client: str ) ->  Union[dict, False]:
        """! 
        @~russian 
        @brief функция возвращает параметры подлючения к `aliexpress` через API 
        @param client `str`  :  клиент на другом конце провода
        @returns 
        @details Сегодня есть один API для Aliexpress - `katia`
        @~english
        @brief Returns aliexpress API dictionary
        @details
        Returns aliexpress API dictionary
        
        
        @returns dict
        
        ### Example of the returned dictionary
        <code>
            {
                'key': 'aliexpress affiliate api',
                'secret': 'secret',
                'tracking_id': 'affiliate tracking id'
            }
        </code>
        """
        """! @~russian        
        @returns dict
        
        ### Пример возвращаемого словаря
        <code>
            {
                'key': 'aliexpress affiliate api',
                'secret': 'secret',
                'tracking_id': 'affiliate tracking id'
            }
        </code>
        """

        for credentials in self.list_api_aliexpress_credentials:
            if client in credentials['username']:
                return credentials

        logger.warning ('`username = [{client}]` ALIEXPRESS не найден')
        return False
        
    # ------------------------------------------------------------- GET API PRESTASHOP -------------------------------------

    #@logs_and_errors_decorator (default_return =  False)
    def get_credentials_api_pestashop(self, client: str ) ->  Union[dict, False]:
        """! @~russian функция возвращает параметры подлючения к `prestashop` через API 
        @param client `str`  :  клиент на другом конце провода
        @returns dict  
        <code>
        {
            'api_key' : value,
            'api_domain': value,
            'kp_username': value,
        }
        </code>
        """       
        
        for credentials in self.list_prestashop_api_credentials:
            if client in credentials['username']: 
                return credentials

        logger.warning ('`username = [{client}]` PRESTASHOP не найден')
        return False
        pass

    #@logs_and_errors_decorator (default_return =  False)
    def get_credentials_db(self, client: str ) -> Union[dict, False]:
        """! @~english
        @brief Settings for connecting to databases
        @details 'db.dev.e-cat.co.il', 'db.emil-design.com' , ...
        @returns dict
        @~russian 
        @brief  Функция возвращает параметры подлючения к `prestashop` через API 
        @param client `str`  :  клиент на другом конце провода. Например, 'db.dev.e-cat.co.il', 'db.emil-design.com'
        
        @returns dict 
        <code>
       {
            'server' : value,
            'port' :value,
            'db_name' : value,
            'user' : value,
            'password' : value,
            'kp_username' : value,        
        }
        </code>
        """
        
        for credentials in self.list_prestashop_db_credentials:
            if client in credentials['username']: 
                return credentials

        logger.warning ('`username = [{client}]` PRESTASHOP не найден')
        return False
        pass
                
        
     # ------------------------------------------------------------- GET credentials FTP -------------------------------------
    #@logs_and_errors_decorator (default_return =  False)
    def get_credentials_ftp(self, client: str ) -> Union[dict, False]:
        """! @~english
        @brief Settings for connecting to databases
        
        @details 'db.dev.e-cat.co.il', 'db.emil-design.com'
        @returns dict
        """
        """! @~russian 
        @brief Установки для подключения к базам данных
        @param client `str = None`  :   ftp аккаунты. Если было передано имя клиента, функция вернет
       словарь с параметрами подключения для конкретного клиента(например, 'db.dev.e-cat.co.il', 'db.emil-design.com' ... ),  
       иначе будет возвращен сипок всех хранимых keepass словарей клиентов ftp
        @returns dict 
        <code>
        {
        }
        </code>
        """
        
        try:
            """! """
            return self.settings['ftp'][client] if client else self.settings['ftp']
        except Exception as ex:
            logger.error(f'ошибка в коннекторах ftp ', ex)
            return False
                
        

    # ------------------------------------------------------------- GET CREDENTIALS SMTP -------------------------------------
    #@logs_and_errors_decorator (default_return =  False)
    def get_credentials_smtp(self, client: str ) -> dict:
        """! @~english
        @brief Connection to mail
        @details To receive Google mail api, two-factor authentication is required.
        Authentication at Google is required to get the password
        @returns `dict` <pre>{
            'server': 'smtp.server.com',
            'user': 'user@server.com',
            'port': 587,
            'password': 'xxxxxxxxxxx',
            'receiver': 'user@server.com'
        }</pre>
        """
        """! @~russian 
        @brief Подключение к почте
        @details Для получения api почты Google требует двухфакторную авторизацию.
        Надо произвести аутентификацию у Google, чтобы получить пароль
        @returns `dict` <pre>{
            'server': 'smtp.server.com',
            'user': 'user@server.com',
            'port': 587,
            'password': 'xxxxxxxxxxx',
            'receiver': 'user@server.com'
        }</pre>
        """
        


        """! @~english
        @brief Settings for connecting to databases
        @details 'db.dev.e-cat.co.il', 'db.emil-design.com'
        @returns dict
        """
        """! @~russian 
        @brief Установки для подключения к базам данных
        @param client `str | list[str]`  :   аккаунты ваз данных 'db.dev.e-cat.co.il', 'db.emil-design.com' ...
        @returns dict <pre>{
            
        }</pre>
        """

        for credentials in self.list_prestashop_db_credentials:
            if client in credentials['username']: 
                return credentials

        logger.warning ('`username = [{client}]` SMTP не найден')
        return False
        pass
    
        if not client:
            """! @~russian У меня всего один клиент SMTP """
            try:
                """! """
                return {
                'server': self.settings['smtp'][client]['server'],
                'user': self.settings['smtp'][client]['user'],
                'port': self.settings['smtp'][client]['port'],
                'password': self.settings['smtp'][client]['password'],
                'receiver': self.settings['smtp'][client]['receiver'],
            }
            except Exception as ex:
                logger.error(f'ошибка smtp ', ex)
                return False
                

        

    # ------------------------------------------------------------- suppliers_dict() -------------------------------------
    @property
    def suppliers_dict(self) -> dict:
        """! @~russian *[getter]* Словарь поставщиков из `suppliers/suppliers_dict.json` """
        """! @~english
        @brief Dictionary of suppliers from `suppliers/suppliers_dict.json`
        """

        return self._suppliers_dict
    
    @suppliers_dict.setter
    def suppliers_dict(self):
        """! *[setter]* """
        self._suppliers_dict = j_loads (Path (self.dir_root, 'suppliers', 'suppliers_dict.json'))

    # ... (остальные методы)



gs: ProjectSettings = ProjectSettings().get_instance()
"""! @~russian Инстанс `ProjectSettings"""