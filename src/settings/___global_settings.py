"""! @~russian 
@brief  Модуль стартовых настроек 
@details При инициализации класса `ProjectSettings` программа считывает настройки по умолчанию \n
 из файла `src/gs/global_settings.json`. \n
 Пароли, ключи, API и другие учетные данные хранятся в базе данных `src/gs/db.kdbx`. \n
 Для открытия базы данных от вас требуется ввести мастер пароль. 
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
 @file
 @var ProjectSettings `gs` инстанс ProjectSettings Класс инициализируется единожды, а потом вызывается его инстанс
 @var `dir_root` корневая директория для всей программы. 
 @details В най расположены:
            - рабочaя директория - src
            - бинарные файлы - bin
            - документация - docs
            - временные файлы - tmp
            - файлы экспорта - export

@info Для однозначной интерпретации слешей я все пути объвляю как объекты `Path`
@todo корневая директория можен иметь любое название. Надо добавить эту опцию в файл конфигурации.
        (не срочно)
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


# Imports
from typing import Union
import os
import sys
import datetime
from pathlib import Path

# -----------------------------------
# 1.

#dir_root : Path = Path (os.getcwd() [:os.getcwd().rfind(r'\hypotez\src')])

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
pass


sys.path.append (dir_root)
"""! @~russian _note Добавляю свою рабочую директорию в системную переменную `OS.Path`"""

from pykeepass import PyKeePass, entry
import getpass # <- модуль поля ввода типа password
from src.helpers import logger, beep, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads
# -----------------------------------


class ProjectSettings():
    """!@~russian @brief ProjectSettings - класс синглтон с основными параметрами запуска программы.
     @details Есть два источника, в которых хранятся настройки: 
     - файл `global_settings.json` (`src/gs/global_settings.json`)
     - база данных keepass<sup>1)</sup> `db.kdbx` (`src/gs/db.kdbx`)
     @note
    <sup>1)</sup> KeePass - хранилище паролей с AES  шифрованием . 
    Для работы с ним я использую библиотеку `pykeepass`. Для открытия базы данных необходим мастер пароль. 
    Подробней о [keepass](https://keepass.info/help/base/index.html)  
    @todo переделать логику работы с базой keepass. Брать парамерты группами и потом получать их через цикл
    
    @~english
    @brief ProjectSettings - singleton class 
    @details
    Project settings: passwords, server addresses, and other sensitive information.  
    Passwords are stored in a database in keepass format. The file extension of the database is kdbx.  
    To open the database, a master password is required.  
    More details about  [keepass](https://keepass.info/help/base/index.html)   


    ### Flowchart

    @image html gs.ProjectSettings.png
    
         

    @var _kp `PyKeePass` объект keepass (создается, читается и унчтожается при инициализации класса)
    @var self.api_aliexpress `dict` содержимое ключа API aliexpress
    @var self.prestashop_api `dict` словарь подключений  API Prestashop
    @var self.api_openai `str` словарь подключений  openAI
    @var self.keepass_prestashop_db `(list [dict])` список словарей подключений к базам данных Prestashop
    
    """
    
    dir_root = dir_root

    #2.
    settings: dict = j_loads (Path (dir_root, 'src', 'settings', 'global_settings.json' ))

    supplier_prefix: list = settings ['supplier_prefix']
    """! @~russian _note  `supplier_prefix` Список поставщиков для которых я буду выполнять сценарии 
    @details `supplier_prefix` на протяжении всего кода означает  или поставщика или список поставщиков над которым будет выполнятся операция
    При инициализации класса `Supplier` служит указателем, какого именно поставщика будет содержать инициализируемый класс
    
    """
    
    _instance = None
    
    #@logs_and_errors_decorator(default_return=False)
    def __new__ (cls, *args, **kwargs):
        """! @~russian Создаю инстанс  """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    

    #@logs_and_errors_decorator(default_return=False)
    @classmethod
    def get_instance (cls) -> _instance:
        """! @~russian Проверяю, а есть ли инстанс?
       @details Если инстанса класса еще нет - создаю, иначе возвращаю сам инстанс"""
        if not cls._instance:
            cls._instance = cls()
            logger.info('Старт инстанса `gs`')
        return cls._instance
    
    #@logs_and_errors_decorator(default_return = None)
    def __init__(self,   *attrs, **kwards) -> None:
        """! @~russian Конструктор 
        
        
         @param self  :  pointer
         @param *attrs `tuple`  :  collects positional arguments into a tuple
         @param **kwards `dict`  :  collects keyword arguments into a dictionary
        """
        self._payload( *attrs, **kwards)
        

    #@logs_and_errors_decorator(default_return = True)
    def _payload(self,   *attrs, **kwards) -> bool:
        """! 
         @~russian Функция загружает установки в методы и аттрибуты класса `ProjectSettings`
         @details
         - Обязателен мастер пароль от базы данных keepass. 
         - Для создания своей базы запустите `keepass.exe` из `bin/keepass/keepass.exe`  
         - <b>Мастер пароль не хранится в системе. Его надо знать, чтобы открыть базу данных keepass. <b>
         
         
         @~english The function loads settings into the methods and attributes of the ProjectSettings class
         @details   
         Must have the master password for keepass database. 
         The master password is not stored in the system. You need to know it to open the keepass database. 

        """
        _kp : PyKeePass = self.kp()
       
        if not _kp: return False

        # api aliexpress -------------------------------------------------------------------------
        try:
            self.settings.update ( {'api_aliexpress' : _kp.find_entries_by_title('api_aliexpress_katia')[0]} )
            """! @~russian _note API Aliexpress """
        except Exception as ex:
            logger.error (f'''ключ `api_aliexpress_katiа` завершился ошибкой {ex} ''')
        
        # api openAI ------------------------------------------------------------------------------
        try:
            self.settings.update ( {'api_openai' : _kp.find_entries_by_title('devhypotez')[0].custom_properties['key']} )
            """! @~russian _note API OpenAI """
        except Exception as ex:
            logger.error (f'''key 'api_openai_api' not found ''')
      
        # apis prestashop -------------------------------------------------------------------------
        try:
            """! @~russian _note Вытаскиваю api ключи для клиентских баз данных Prestashop из внутренней структуры keepass
            @~russian _bug Падает с ошибкой 'list index out of range' если нет ключа в keepass базе данных
            @todo 1. обработать ситуацию, когда не найден ключ в базе данных. 
            2. ситуация когда несколько ключей с одним именем в разных папках. 
            """
            prestashop_api : dict = {}
            for api_domain in self.settings ['list_prestashop_api_domains']:
                prestashop_api.update({api_domain : _kp.find_entries_by_title(api_domain) [0].custom_properties ['api_key'] })
            # api_e_cat : dict =  { 'api.dev.e-cat.co.il' : _kp.find_entries_by_title('dev.e-cat.co.il') [0].custom_properties ['api_key'] }
            # api_emil : dict =  { 'api.emil-design.com' : _kp.find_entries_by_title('emil-design.com') [0].custom_properties ['api_key'] }
            # prestashop_api : dict = {}
            # prestashop_api.update ( api_e_cat )
            # prestashop_api.update ( api_emil )
            prestashop_api = { 'prestashop_api' : prestashop_api }
            self.settings.update ( prestashop_api )
            
        except Exception as ex:

            logger.error (f''' error {ex} ''')
            print(ex)
        
        # ftp connections ---------------------------------------------------------------------------
        try:
            
            ftp_conn_dict: dict ={
                'ftp.dev.e-cat.co.il' : _kp.find_entries_by_title('ftp.dev.e-cat.co.il')[0],
                'ftp.emil-design.com' : _kp.find_entries_by_title('ftp.emil-design.com')[0],
                }
            self.settings.update ( {'ftp':ftp_conn_dict} )
        except Exception as ex:
            logger.error (f'''key 'ftp.dev.e-cat.co.il' as error {ex} ''')


        # smtp connections ----------------------------------------------------------------------------
        try:
            smpt_conn_dict: dict = {'smtp.one.last.bit@gmail.com' : _kp.find_entries_by_title('smtp.one.last.bit@gmail.com')[0]}
            self.settings.update (smpt_conn_dict)
        except Exception as ex:
            
            logger.error (f'''key 'smtp.one.last.bit@gmail.com' as error {ex} ''')
            



    #------------------------------------------------------------- kp() -------------------------------------
    #@logs_and_errors_decorator(default_return = PyKeePass)
    def kp(self) -> Union[PyKeePass, bool]:
        """! @~russian 
        @brief Открываю файл keepass паролём
        @details Даю три попытки на открытие            
        
        @var attempts `int`  :  кол-во попыток            
        @returns _kp `PyKeePass`  :  объект keepass            
        @todo неправильная логика обработки неправильного ввода пароля
        """
        attempts = 0

        while attempts < 3:
            try:
                beep(BeepLevel.ATTENTION)
                _kp = PyKeePass(str(Path(self.dir_root, 'src', 'settings', 'db.kdbx')),
                                password=getpass.getpass('Master password for keepass database: '))
                print('OK')
                return _kp
            except Exception as ex:
                attempts += 1
                logger.error(f"Произошла ошибка: {ex}")

            if attempts == 3:
                logger.error("Превышено максимальное количество попыток.")
                return False
 



    #------------------------------------------------------------- get_now() -------------------------------------                
    @property
    def get_now (self, dformat: str = '%Y%m%d%H%M%S') -> str:
        """! @~en Returns a datestamp in the chosen format 
             @~russian Returns a datestamp in the chosen format 
        
             @param self `pointer`
             @param dformat  `str` = '%Y%m%d%H%M%S' : Output format for datetime 
        """
        
        return datetime.datetime.now().strftime (dformat)
        

    #------------------------------------------------------------- api_aliexpress() -------------------------------------
    @property
    def api_aliexpress (self) -> dict:
        """! @~en Returns aliexpress API dictonary
            @~russian словарь `API` алиекспресс
            
            @returns dict
            
           ### Пример возвращаемого словаря
            <code>
                {
                    'key' : 'aliexpress affiliate api',
                    'secret' : 'secret',
                    'tracking_id' : 'affiliate tracking id'
                }
            </code>
        """
        try:
            return  {
                'key' : self.settings['api_aliexpress'].custom_properties['api_key'],
                'secret' : self.settings['api_aliexpress'].custom_properties['secret'],
                'tracking_id' : self.settings['api_aliexpress'].custom_properties['tracking_id']
                }
        except Exception as ex:
            logger.error(f'Ошибка в api_aliexpress ', ex)
    
    @property
    def prestashop_api (self) -> str:
        """! @~russian 
        @brief список словарей `API` `PrestaShop`
        @details Я обслужваю несколько заказчиков: `emil-design.com, sergey.mymaster.co.il, e-cat.co.il, shalom-phones.co.il`   
        Для каждого из них я держу параметры подключения через `API`
        
        @~english
        @~en Connecting to PrestaShop API client database.  
        @en_details 
        Examples of clients:  
        * `emil-design.com`
        * `e-cat.co.il`
        @~russian  API от клиентов Prestashop.
        @details 
        Примеры клиентов: 
        * `emil-design.com`
        * `e-cat.co.il`
       
        
        @returns dict 
        
        ### Пример возвращаемого словаря
        <code>  
            {    
                "api_domain": "https://api.domain.com",  
                "product_manipulations_key": "xxxxxxxxxxxxxxxxxx"  
            }
        </code> 
        """
        if self.settings ['default_prestashop_api_domain'] in self.settings ['prestashop_api']:
            return {
                'api_domain' : self.settings ['default_prestashop_api_domain'],
                'api_key': self.settings ['prestashop_api'] [self.settings ['default_prestashop_api_domain']]
                }
        
        else:
            logger.error (f'''Не найден Prestashop API для {self.settings ['default_prestashop_api_domain']}''')
            return False

    @property
    def api_openai (self) -> str:
        """!  @brief api_openai `str`  "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
              @returns api_openai
        """

        return self.settings ['api_openai']


    @property
    def dir_export (self) -> Path:
        """! @~en absolute path for export files directory
        @~russian абсолютный путь к директории экспорта файлов
        @returns Path
        """
        return Path ( self.dir_root, 'export' ).absolute()

    @property
    def dir_logs(self) -> Path:
        """! @~en Returns absolute directory for log files
        @~russian абсолютный путь к директории логов 
        @returns Path	"""
        return Path ( self.dir_root, 'logs' ).absolute()

    @property
    def dir_binaries(self) -> Path:
        """! @~en returns absolute path to binary files
             @~russian возвращает абсолютный путь к директории с бинарными файлами
             @details в директории хранятся вспомогательные файлы для работы кода.
             Например, драйверы веббраузеров `geckodriver.exe`, 
             GUI базы данных паролей `kypass.exe`,
             Генератор документации `doxygen.exe`
        
             @returns Path
    	"""
        return Path ( self.dir_root, 'bin' ).absolute()
        
        
    
    @property
    def dir_temp(self) -> Path:
        return Path (self.dir_root, 'tmp' ).absolute()
        
    @property
    def dev_null(self) -> Path:
        """! @~russian определяет `null` операционной системы.  
        @details Для `windows` это `nul`  
        Для линуксподобных `/devull`  
        """
                 
        if os.name != 'nt':
            return r'/devull'
        else:
            """! WINDOWS (NT) """
            return 'nul'
        

    @property
    def scenario_language(self) -> str:
        """! @~russian Установка локали
        
        @details
        *[ru]*  
        Установка локали (для какого языка будет запущен сценарий) по умолчанию  
        
        @returns scenario_language `str` ISO 639-1
    	"""
        return self.settings.get('scenario_language', 'en')
        
    @property
    def db_connection(self, client : str) -> dict:
        """@~russian Установки для подлючения к базам данных:
        'db.dev.e-cat.co.il'
        'db.emil-design.com'
        
        @returns dict
    	"""
        return self.settings ['prestashop'][client]
      

    @property
    def connection_ftp(self, client : str) -> dict:
        """ @~russian настройки доступа по FTP к файлам клиента
            @returns dict
    	"""
        return self.settings ['ftp'][client]

    @property
    def connection_smtp(self, client : str = 'smtp.one.last.bit@gmail.com') -> dict:
        """! @~russian подключние к почте
         @details Для получения api почты Google требуется двухфакторная авторизация. 
         Надо произвести аутентификацию у Google, чтобы получить пароль 

        @returns `dict` <pre>{
            'server' : 'smtp.server.com', 
            'user' : 'user@server.com', 
            'port' : 587, 
            'password' : 'xxxxxxxxxxx',
            'receiver' : 'user@server.com'
        }</pre>
        """
        return {
            'server' : self.settings ['smtp'][client]['server'], 
            'user' : self.settings ['smtp'][client]['port'], 
            'server' : self.settings ['smtp'][client]['user'], 
            'password' : self.settings ['smtp'][client]['password'],
            'receiver' : self.settings ['smtp'][client]['receiver'],
        }


    @property
    def threads(self) -> bool:
        """! @~russian 
        @brief флаг, режима запуска программы в потоках (иначе - конвеер)
        @details 
        - `True`  :  программа будет выполняться в многозадачном режиме - это дает возможность обрабатывать 
        сценарии параллельно, создавая поток для каждого поставщика из `supplier_prefix`.
        Имеет смысл запускать многопоточный режим только на многоядерных процессорах
        - `False`  :  Установлен по умолчанию. Программа будет последовательно запускать поставщиков из списка.
        
        @~english
        @details   
        `True`: the program will run in multithreaded mode - each supplier from the variable `supplier_prefix` will be launched in a separate thread.  
        `False`: the program will sequentially run suppliers from the list.  

        @returns bool  :  @~russian  
        - `True` : Запустить список поставщиков в ***многопоточном режиме*** (*для каждого поставщика создается отдельный поток выполнения*)
        - `False` : Запустить список поставщиков ***по очереди***
        @~english `True` - run suppliers list in multithread, `False` - run suppliers sequentially

        @note @~russian Запуск многопоточного режима, если задан всего один поставщик не имеет смысла
        """
        return self.settings ['threads']
    
        

    @property
    def webdriver(self) -> str:
        """! @~russian 
        @brief инстанс вебдрйавера (`Mozilla, Chrome, Edge`, или другого)
         @details По умолчанию все настройки сделаны для Firefox (`geckodriver.com`).  
         Подробней о настройках вебдрайвера см `src.webdriver.Driver`, а настройки Firefox в `src.webdriver.Firefox`
        """
        return self.settings [ 'default_webdriver' ]

    @property
    def suppliers_dict(self) -> dict:
        """! @~russian 
        @brief Словарь поставщиков из `suppliers/suppliers_dict.json"""
        return j_loads (Path ( self.dir_root, 'suppliers', 'suppliers_dict.json' ))


gs: ProjectSettings = ProjectSettings().get_instance()
"""! @~russian Инстанс `ProjectSettings"""