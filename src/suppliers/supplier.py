"""! @~russian <b>класс</b> `Supplier` <b> базовый класс для всех поставщиков </b>

@details
`Supplier` - предоставляет методы и атрибуты для конкретного 
поставщика данных: например, amazon.com, wallmart.com, mouser.com, digikey.com либо заданный клиентом. 
В програме уже соданы несколько поставщиков, другие будут определены заказчиком.

Для доступа к данным класс обращается к коннекторам, которые предоставляют досту к источнику информации. Реализованые коннекторы:
- `HTML` grabber:  Mетод получения информации с помощью вебдрайвера (например, для Firefox, Chrome, Edge)
- `API` connection:  Mетод предполагает взаимодействие с API поставщика данных. 
- `DB` connection:  Метод прямого подключения к базе данных поставщика
- `XML, CSV` import:  Методы для обработки данных в форматах XML и CSV. 


@section libs imports:
  - importlib 
  - pathlib 
  - typing 
  - time 
  - shutil 
  - gs (local)
  - io_interface (local)
  - helpers (local)
  - webdriver (local)
  - scenarios (local)
 @file 
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import importlib
from pathlib import Path
from typing import Union
import time
import shutil

# ----------------------------------
from src.settings import gs
from src.io_interface import j_loads, j_dumps
from src.helpers import logger,  logs_and_errors_decorator, DefaultSettingsException, jprint, pprint
from src.webdriver import Driver
from src.scenarios.executor import run_scenario, run_scenarios, run_scenario_file, run_scenario_files
# ----------------------------------


class Supplier():
    """! Класс поставщика. Исполняет сценарии: `scenario->executer` -> `executor->grabber` -> `grabber->prestashop`
    @image html supplier.png
    @details По сути - это центральный класс, вокруг которого крутится программа.
    `Supplier` получает на вход префикс конретного поставщика (amazon, aliexpress, ...)  подключает его функции через
    интерфейс `related_modules`. Все, что относится к конкретному поставщику находится в директории,
    название которой соответствуют имени поставщика.
    @param supplier_prefix `str`  :   Префикс поставщика. Префиксы см. в гуглтаблице:
        Table of suppliers: https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
                
    @param scenario_language `str`  :    scenario_language code in ISO 639-1  
            `en`, `he`, `ru`   
            Язык работы  сценария  
            двухбуквенный код ISO 639-1 
    @param supplier_settings `dict`  :   Each supplier has unique settings defined in the `src/suppliers/<supplier_prefix>/settinglobal_settings.json file in the specific supplier's directory
    @param price_rule `str`  :   Determines the price calculation.  
        For example, to add VAT, the multiplication use `*1.17`, тo decrease the price by 100, use `-100`.
    @param login_data 'dict`  :   Dictionary of login data for accessing the website (if required).
        *[ru]* Словарь данных логин для захода на сайт (если требуется)
    @param related_modules   :   функции, релевантные каждому поставщику 
    @param current_scenario `dict`  :   Исполняемый сценарий 
    @param locators `dict`  :   Локаторы элементов страницы 
    @param driver `Driver`  :  вебдрайвер
    @param parsing_method `str`  :   Каким способом производится парсинг:   
        - `webdirver` : WEB
        - `api` : API 
        - `xls` : Excell
        - `csv` : Table
        
      
    """

    # supplier_id: int = attrib ( kw_only=True, default=None )
    # """ supplier id in the system
    # Table of suppliers:
    # https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
    # """

    supplier_id : int = None
    supplier_prefix: str = None
    supplier_settings: dict = None
    scenario_language: str = None
    price_rule: str = None
    related_modules = None
    scenario_files: list = None
    current_scenario: dict = None

    login_data : dict = {
        'if_login': None,
        'login_url': None,
        'user': None,
        'password': None,
    }
    locators: dict = {
        'store': None,
        'login': None,
        'category': None,
        'product': None,
    }
    """! @~russian _var locators  словарь локаторов вебэлементов на страницах `product`,`category`,`login`,`store`.
    каждый из ключей будет заполнен словарем вебэлементов из файлов `product.json`,`category.json`,`login.json`,`store.json`
    из директории `<supplier_prefix>/locators` """        

    def __init__(self, supplier_prefix: str, scenario_language : str = 'en',   *attrs, **kwards):
        """! Constructor

        Parameters : 
            `self` : pointer
            `*attrs` : variable number of positional arguments
            `**kwards` : variable number of named (keyword) arguments

        @param supplier_prefix `str` supplier_prefix s.e. 'aliexpress'
                        Table of suppliers: https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
        @param scenario_language `str`  scenario_languageuage in ISO 639-1 
        @param parsing_method `str` - Enum('api', 'webdriver')
        @param scenarios `dict | list[dict]`: scenario or list of scenarios or file or list of scenario files """
        
        self.supplier_prefix = supplier_prefix
        self.scenario_language = scenario_language
        logger.info('Start supplier')        
        if not self._payload(*attrs, **kwards): 
            raise DefaultSettingsException(f'Ошибка запуска поставщика ', supplier_prefix )


    def _payload(self, *attrs, **kwards):
        """! @~russian @brief Функция загружает установки для запуска поставщика
            @details Функция получает управление от `__init()__`, с аргументами, используемыми при инициализации (`*attrs, **kwards`).
            Это удобно тем, что не надо менять логику каждый раз, если понадобится добавить или изменить какой-нибудь параметр 
            я перебрасываю его через `*attrs, **kwards`"""
            
        logger.info(f'''
        -----------------------------------------
                Старт {self.supplier_prefix}
        -----------------------------------------''')        

        self.supplier_abs_path = Path(gs.dir_src, 'suppliers', self.supplier_prefix)
        
        self.related_modules = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
        """! `self.related_modules`  дополнительные функции из модуля `<supplier_pefix>` """
        
        
        self.supplier_settings = j_loads(
            Path(self.supplier_abs_path, f'{self.supplier_prefix}.json'))
        """! supplier_settings: `self.supplier_settings` Установки по умолчанию для данного поставщика, читаются из файла <supplier_prefix>.json """
       
       
        self.price_rule = self.supplier_settings.get('price_rule',0)
        self.supplier_id = self.supplier_settings['supplier_id']
        """! ID поставщика
        @details Гугл таблица поставщиков находится здесь:  
        https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
       """
       
        
        # Получаем список файлов сценариев
        self.scenario_files = [ Path (self.supplier_abs_path, 'scenarios', scenario_filename) for scenario_filename 
                               in self.supplier_settings.get ('scenario_files', 
                            [ Path(self.supplier_abs_path, 'scenarios', scenario_filename) for scenario_filename 
                             in Path(self.supplier_abs_path, 'scenarios').iterdir() 
                             if scenario_filename.suffix == '.json' ] ) ]
        
        """! @~russian Если список сценариев НЕ определен при Инициализации класса - беру все из папки сценариев поставщика.  
        Я все равно оставил опцию подменять список до старта сбора сценариев.  
        Все пути файлов сценариев дополняю до абсолютного пути
        """
        
        
        self.login_data = {
            'if_login': self.supplier_settings.get('if_login'),
            'login_url': self.supplier_settings.get('login_url'),
            'user': None,
            'password': None,
        }
       
        self.locators: dict = {
            'store': j_loads(self.relatvie_to_abs_path('locators','store.json')),
            'login': j_loads(self.relatvie_to_abs_path('locators','login.json')),
            'category': j_loads(self.relatvie_to_abs_path('locators','category.json')),
            'product': j_loads(self.relatvie_to_abs_path('locators','product.json')),
        }
        """! @~russian locators `dict` - Словарь локаторов вебэлементов на страницах `product`,`category`,`login`,`store`.
        Каждому типу страницы соответствует свой файл json: `product.json, category.json, login.json, store.json`
        Файлы для каждого из поставщиков находятся в соответствующих директориях `<supplier_prefix>/locators` """     

        logger.info(f"""{self.supplier_prefix} Begin to attach driver ... """)
        _start_time = int(time.time())
        """! @todo needs for debugging. Start driver takes too long """        
        self.driver = Driver()
        """! @todo Здесь надо делать подключение вебдрайвера по условию, если работа с поставщиком может быть реализована другими методами 
        Может быть (апи, база данных, импорт файла)"""
        logger.debug(f""" ... драйвер подключился за {int(time.time()) - _start_time} seconds """)
           
        return True


    def relatvie_to_abs_path(self, directories_names: Union[Path, list[Path], str, list[str]] = None, file_names:Union[Path, list[Path], str, list[str]] = None) -> Union[list[Path], Path]:
        """! @~russian  функция конвертирует относительные пути в абсолютные
        @param self  `pointer`
        @param directories_names `Path | list[Path] | list[str] | str` = None : пути директорий. 
        @param file_names `Path | list[Path] | list[str] | str` = None :  пути файлов
        
         если `directories_names = None`  функция будет строить путь для `file_names`, 
        которые могут содержать часть пути.  
        Например: `foo.txt` | `bar/foo.txt` | `bar,foo.txt`  
        В качестве разделителя пути можно использовать  косую черту `/` или запятую `,`.  
        Хотя бы один из параметров `directories_names` или `files_names` должен содержать данные. 
        
        @returns:
        @~russian абсолютный путь как `Path` или список `list[Path]`
        @~english Absolute path as `Path` or `list[Path]`

        @todo 
        1. уже есть одна реализация в gs 
        2. Вынести в модуль helpers
        """

        if directories_names is not None and file_names is None:
            """! @~russian _rem функция получила имя дирекатории. Функция строит для нее абсолютный путь """
            return Path(self.supplier_abs_path, directories_names)

        if isinstance(file_names, str):
            """! @~russian _rem функция получила один файл. Функция строит для него абсолютный путь"""
            return Path(self.supplier_abs_path, directories_names, file_names)

        if isinstance(file_names, list):
            """! @~russian _rem функция получила список файлов. Функция строит для каждого файла абсолютный путь" """
            abs_filenames = [
                Path(self.supplier_abs_path, directories_names, filename)
                    for filename in file_names
        ]
        
        return abs_filenames


    def login(self) -> bool:
        """! @~en Log in to the supplier website.  
        @~russian Обработка ситуации, когда вход на сайт поставщика требует авторизации.
        @param self : pointer
        @returns bool : `True` if login successful, else `False`
        @details Вызыаваю функцию `login()` из модуля поставщика и получаю от нее флаг завершения авторизации: 
        `True` в случае успеха, иначе `False`
        """
        
        return self.related_modules.login(self)


    def run_supplier(self, scenario_files: Union [list[str], str] = None) -> bool:
        """! @~russian Запуск выполнения сценариев
        @~russian _param scenario_files `list[str] | str` = None : Файлы с именами, содержащими сценарии выполнения для поставщика.
        @details 
        Если они не предоставлены, будут запущены сценарии из файла настроек поставщика.
        Значение по умолчанию - `None`.
        
        Файлы сценариев находятся в каталоге `suppliers/<supplier_prefix>/scenarios`.
            Список сценариев выполнения по умолчанию определен в файле `<supplier>/<supplier_prefix>.json`.
            Например, для поставщика `aliexpress.com`:
            - `supplier_prefix` = `aliexpress`
            - Каталог поставщика: `suppliers/aliexpress`
            - Путь к файлу настроек: `suppliers/aliexpress/aliexpress.json`

        @returns bool : `True` if succefull else `False`
        
        @en_param self : pointer
        @en_param scenario_files `list[str] | str` : Filenames containing execution scenarios for the supplier.
        @en_details
             If not provided, the scenarios from the supplier's settings file will be used. Defaults to None. By default self.scenarios 
            The default list of execution scenarios is specified in the supplier's settings file.
            Scenarios are located in the directory suppliers/<supplier_prefix>/scenarios.
            The default list of execution scenarios is defined in the file <supplier>/<supplier_prefix>.json.
            For example, for the supplier `aliexpress.com`:
            `supplier_prefix` = `aliexpress`
            Supplier directory: `suppliers/aliexpress`
            Path to the settings file: `suppliers/aliexpress/aliexpress.json`
        """
      
        # 1. if login
        if self.login_data['if_login']:
           success = self.login()
           if not success:
               return False
           
        #2. run scenarios
        logger.info('Старт сбора сценариев')
        """! @todo тут надо сделать поинтересней: `файл / список файлов / сценарий / список сценариев` """
        return self.run_scenario_files(scenario_files)


    def run_scenario_files(self, scenario_files: Union [list[str], str] = None) -> bool:
        """! @~en Execute one or more scenario files.
        @~russian  Функция запускает исполнитель `run_scenarios()` и передает ему в переменной `scenario_files` список файлов сценариев 
        @details (`src.scenarios.executor.run_scenarios()`).
        @param scenario_files `list[str] | str`: список имен файлов сценариев
        @returns bool `True` в случае успешного завершения всего списка сценариев исполнителем, иначе: `False`
        @todo А если один сценарий завершился `False`, а остальные `True`, все равно получаю общий `False`? 
        Надо протестировать эту ситуацию
        """
        
        scenario_files = self.scenario_files if not scenario_files else scenario_files
        return run_scenario_files (self, scenario_files)

    def run_scenarios(self, scenarios: Union[dict, list[dict]]) -> bool:
        """! @~russian Функция запускает исполнение списка или одиночного сценария.
        @param scenarios `dict | list[dict]` : сценарий / список сценариев на исполнение.
        @returns bool `True` в случае успешного завершения сценария испонителем, иначе: `False`
        """
        return run_scenarios (self, scenarios)

