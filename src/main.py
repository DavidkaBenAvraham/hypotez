# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! @~russian <b> Модуль запуска программы. </b>

@details Здесь я устанавливаю порядок запуска поставщиков (в потоки или по очереди), интерфейс пользователя (`GUI`, `JUPYTER`, `CMD`). \n 
            Расширенные параметры запуска поставщиков вы можете задать при вызове функции  `launcher()`. Подробности см 
            в комментариях в теле функции `launcher()` (`src.main.launcher()` )
            
@todo Расписать `GUI`, `JUPYTER` интерфейсы (не срочно)

--------


@code
> python main.py
@endcode

-------

### Flowchart
            
@image html main.png

--------

@section libs imports:
- src.launchers (local)
- src.suppliers (local)
- threading
- typing
- sys
- os

@file
@var gs предстартовая подготовка
"""
# Imports
import os
import sys
import datetime
from pathlib import Path


dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 

from src.settings import gs         
"""! @var gs предстартовая подготовка """


#from launchers import QTWindow <- оконный интерфейс
#from launchers import jupyter
from src.suppliers import Supplier
from src.helpers import logger, logs_and_errors_decorator

from threading import Thread
from typing import Union

   

class Thread4Supplier(Thread):
    """! @~en This class runs lot of supppliers in multitheads 
    @~russian Класс запуска списка поставщиков в отдельных потоках
    @~russian Программу можно запустить в многопоточном режиме. Поскольку поставщики 
    не зависят друг от друга их вполне можно запускать каждого в своем потоке. \n Класс `Thread4Supplier` (src.main.Thread4Supplier) реализует механизм многопоточности
    Режим многопоточности задается в файле `global_settings.json` ключ: `threads`:`True` включает режим многопоточности.
    
    @~russian _note Запуск многопоточности нагружает цпу

    @todo не тестирован

    """
    
    #@logs_and_errors_decorator(default_return=False)
    def __init__ (self, supplier_prefix: str, scenario_language: str = 'en', threads : Thread = []):
        """!
        @brief конструктор класса
        @param self `(pointer)`
        @param supplier_prefix `(str)` Префикс поставщика
        @param scenario_language `(scenario_language)` локаль - язык на котором будет испонянтся сценарий, по умолчанию `en` 
        @var threads_list `(scenario_language)` Список запущенных потоков   
        """  
        # 1.
        self.supplier : Supplier = Supplier ( supplier_prefix = supplier_prefix, scenario_language = scenario_language )
        self.threads = threads
        # 2.
        Thread.__init__(self)
        
    #@logs_and_errors_decorator(default_return=False)
    def run(self, supplier_prefix, scenario: Union [str, list[str] ]  = None):
        """!
        @brief запуск потока     
        @details  []
        @param self `pointer`
        @param supplier `Supplier` - Supplier class instance
        @param scenario `str | list[str]`  the list of scenarios for execution. None by default
        """
        
        # 1. Заношу поставщика в список потоков
        # 2. Запускаю поставщика на исполнение
        # 3. Финиш. Поставщик закончил исполнение
        
        
        # 1.
        self.threads.append (self.supplier)

        # 2.
        try:
            self.supplier.run_supplier(scenario)
            # The suppliers.__init__.py file is run here
        except Exception as ex:
            logger.error (f"""Oшибка запуска потока {ex.with_traceback(ex.__traceback__)}""")

        # 3.
        self.supplier.driver.close()
        



###############################################################################################################

#@logs_and_errors_decorator(default_return=False)
def launcher (supplier_prefix: Union [ list[str], str ] = None,
            scenarios_any: dict = None,
            scenario_files: list = None,
            scenario_language: Union[ list[str], str ] = None,
            threads: bool = False,
            gui_mode: str = None) -> bool:
    """! @~russian 
        @brief <b>функция стартер программы</b>
        @details 
        Функция получает на вход параметры запуска инстанса `Supplier` и корректно запускает инстaнс поставщика коммадой `run_supplier()`        
       
        @image html 'func_launcher.png'
                
        Функция принимает на вход:
       - список поставщиков `supplier_prefix`. <sub>[Опционально]</sub> Если аргумент не задан - то берется дефолтный из `gs.supplier_prefix`.
       - список сценариев <sub>[Опционально]</sub>
       - список файлов сценариев <sub>[Опционально]</sub>
       - язык исполнения сценариев <sub>[Опционально]</sub>
       - Флаг многопоточности `threads` (`gs.threads`) <sub>[Опционально]</sub>
       - Выбор пользовательского интерфейса <sub>[Опционально]</sub>

       
       По умолчанию функция создаст очередь поставщиков на исполнение. 
        Порядок такой: 
        - supplier_1 -> lang_1 -> scenario_1
        - supplier_1 -> lang_1 -> scenario_2
        - supplier_1 -> lang_2 -> scenario_1
        - supplier_1 -> lang_2 -> scenario_2
        - supplier_2 -> lang_1 -> scenario_1
        - supplier_2 -> lang_1 -> scenario_2
        - supplier_2 -> lang_2 -> scenario_1
        - supplier_2 -> lang_2 -> scenario_2
        - ...
        
        @todo не обработана ситуация, когда заказчик устанавливает настройку `threads = True` для запуска единственного поставщика в `supplier_prefix`
        @todo Сделать возможность запускать сценарий/ии, без указания поставщика. 
        - Извлекать поставщика из сценария
        - упорядочить полученные сценарии по поставщику

        @param supplier_prefix `str | list[str]` : <sub>[Опционально]</sub>  Префикс поставщика. Для каждого поставщика существует набор действий и настроек, расположенных в папке 
                с именем <supplier_prefix>. Если supplier_prefix не указан, программа запускает поставщиков, определенных в файле 
                <b>настроек по умолчанию </b>  в разделе suppliers. `src/settings/global_settings.json['suppliers']`

                current defined suppliers:
                    * aliexpress
                    * amazon
                    * bangood
                    * cdata
                    * ebay
                    * etzmaleh
                    * gearbest
                    * grandadvance
                    * hb
                    * ksp
                    * kualastyle
                    * morlevi
                    * visualdg
                    * wallashop
                    * wallmart
                    
                
        @param scenarios_any `dict` <sub>[Опционально]</sub>  сценарий (список сценариев) исполнения.  
        Сценарий! НЕ ФАЙЛ! Опция позволяет составлять свои наборы сценариев из разных файлов сценариев.    
        
        
        @param  scenario_files `str | list[str]`  <sub>[Опционально]</sub>  Список файлов сценария к исполнению. По умолчанию список сценарив выполнения находится в установках поставщика по адресу   
                                            `src/suppliers/<supplier_prefix>/<supplier_prefix>.json`       
                                     
        @~russian @note `scenario` и `scenario_files` Позволяют осуществить все варианты сбора товара. Можно задать один из параметров, 
        оба параметра или вовсе их не задавать, тогда программа возьмет параметры из файла настроек.
        
        @param scenario_language `str | list[str]` <sub>[Опционально]</sub> Язык на котором исполняется сценарий. Выбирается из ISO 639-1 двухбуквенного кода. Может получать строку или список. 
                                            Список будет обрабатыавться по очереди в таком порядке:  
                                            - suppliers_list_1 -> scenario_language_1 
                                            - suppliers_list_1 -> scenario_language_2
                                            - suppliers_list_2 -> scenario_language_1
                                            - suppliers_list_2 -> scenario_language_2
                                            
                                            
        @param gui_mode `str` <sub>[Опционально]</sub> Пользовательский тип интерфейса. Возможные значения: 
        - `cmd` (командная строка)
        - `window` (оконный режим)
        - `jupyter`
        - `None` 
        Если этот аргумент не предоставлен, по умолчанию используется интерфейс командной строки `cmd`.
            
        
        @returns `True` в случае успешного завершения сценариев поставщиком, иначе `False`
        
        
        ---
        
        ## Примеры

        
        @code
        > ./python
        >>> import main
        >>> from main import launcher
        @endcode
        
        @code
        ''' Запуск поставщиков с установками по умолчанию. Список 
        поставщиков для запуска находятся в файле `project_setting.json`, разделе `suppliers`
        Самый простой способ запуска
        '''
        
        >>> launcher()
        @endcode
        @code
        ''' Запускает все сценарии по умолчанию у поставщика `supplier1`, затем `supplier2`
        парамерт supplier_prefix может принимать имя одного поставщика или список 
        поставщиков для запуска парсера/ов
        '''
        
        >>> supplier_prefix : list = ['supplier1', 'supplier2', ...]
        >>> launcher(supplier_prefix = supplier_prefix)
        @endcode
        @code
        ''' определяет язык сбора сценариев. Стандартный двухбуквенный код языка ISO 639-1 '''
        
        >>> launcher( scenario_language = 'ru')
        @endcode
        @code
        ''' Запускает один / несколько сценариев. В этом случает поставщик определяется из сценария '''  
        
        scenarios_list : list = ['scenario1', 'scenario2', ...]
        >>> launcher(scenario = scenarios_list)
        ```
        @endcode
        @code
        ''' запуск в графическом интерфейсе '''
        
        >>> launcher(window_mode = 'window')
        # Не реализован
        @endcode
        @code
        '''Запуск в Jupyter notebook. Удобно для экспериментов '''
        
        >>> launcher(window_mode = 'jupyter') 
        @endcode
        
        
        
        src.suppliers.supplier.Supplier.run_supplier()
        
        @~english    
        @brief Based on the `supplier_prefix`, creates an instance of the supplier and launches it.  
        If multithreading is defined, control is passed to the `Thread4Supplier` class; otherwise,  
        each supplier is launched sequentially from `supplier_prefix`. If `supplier_settings` are not passed as a function parameter,
        `supplier_settings` are taken from the global settings `gs.supplier_prefix`
 
        """

    # 1. Defines `GUI`/`JUPYTER`/`CMD` interface
    # 2. Defines  `supplier` class
    # 3. Settings `scenario_language`
    # 4. Running `supplier` in `threads` or `pipeline`.
    
    # # 1. --------------------------------------------- GUI mode
    # if gui_mode == 'window':
    #     """! @bief Start QT Window """
    #     pass

    # elif gui_mode == 'jupyter':
    #     """! @bief start JUPYTER """
    #     return jupyter.run_notebook()

    # elif gui_mode == 'jupyter lab':
    #     # """!
    #     # \bief Start Jupyter Lab mode
    #     # \todo
    #     # Jupiter-lab не хочет работать по ошибке access denied :()
    #     # Костыль - запускать через anaconda->jupiter - lab,
    #     # добавив свою среду venv:
    #     # python -m venv venv
    #     # ./venv/scripts/activate.ps1
    #     # """
    #     try:
    #         return jupyter.run_lab()
    #     except Exception as ex:
    #         logger.error (f"""Ошибка {ex}""")
    #         pass
        

    # elif gui_mode == 'cmd' or gui_mode is None:
    #     """! @bief start in command prompt
    #     @todo это заглушка. Комманд промпт не реализован 
    #     """
    #     pass 



    # 2. ----------------------------------------------------- Supplier settings   
    #  
    supplier_prefix = gs.supplier_prefix if supplier_prefix is None else supplier_prefix



    # 3. ------------------------------------------------ scenario_language
    scenario_language = ['en'] if scenario_language is None else scenario_language


    # 4. --------------------------------------------------- threads/pipeline
    if gs.threads:
        """!  Многопоточный режим  """
        threads: list = []
        """! @var threads `(list)` Список потоков """
        for supplier_prefix in supplier_prefix:
            for scenario_language in scenario_language:
                thrd: Thread = Thread4Supplier (supplier_prefix, scenario_language, threads )
                threads.append ( thrd )
                thrd.start ()

        for thrd in threads:
            thrd.join()
    else:
        for supplier_prefix in supplier_prefix:
            for lang in scenario_language:
                supplier: Supplier  = Supplier ( supplier_prefix = supplier_prefix, scenario_language = lang )
                """! @~russian _note здесь появляется `supplier` от `Supplier`. 
                    @todo В этой части кода можно сделать интересный интерфейс запуска
                """
                logger.info (f'''Старт поставщика {supplier.supplier_prefix} ''')
                supplier.run_supplier ( scenarios_any )
                
                # if scenario:
                #     """! @~russian _note Здесь я могу запустить сценарий заданный при вызове launcher()"""
                #     supplier.run_supplier ( scenario )
                # else:
                #     """! @~russian _note Иначе будет запущен список по умолчанию, определенный в `gs`
                #     @~russian _bug - а если не найдется список - все наебнется
                #     """
                #     supplier.run_supplier ()
                    
                logger.info (f'''Supplier {supplier.supplier_prefix} FINISHED!''')
    return True

##@logs_and_errors_decorator(default_return = False)
def main(supplier_prefix: Union[list[str], str] = None,
            scenario: dict = None,
            scenario_files: Union[list[str],str] = None,
            scenario_language: Union[list[str], str] = None,
            gui_mode: str = None
         ) -> bool:
    """! @~russian Точка входа. Детали запуска смотри в launcher()
    
    @param supplier_prefix `str | list[str]` <sub>[Опционально]</sub>  список поставщиков с которых мне надо получить info
    @param scenario `dict`  <sub>[Опционально]</sub> одиночный сценарий исполнения.  Сценарий! НЕ ФАЙЛ! Опция позволяет составлять свои надоры сценариев из разных файлов сценариев
    @param scenario_files `list | str` <sub>[Опционально]</sub> Список файлов сценариев
    @param scenario_language `( str | list [str])` <sub>[Опционально]</sub>  Язык/и исполнения сценариев двухбукванный код ISO -  
    @param gui_mode `(str)`  <sub>[Опционально]</sub>   ` ['window' | 'jupyter lab' | 'jupyter notebook' | 'None'] ` 

    @returns `True` if success, else `False`

    """
    
    return launcher (supplier_prefix, scenario, scenario_files, scenario_language, gui_mode)

if __name__ == '__main__':
    """! @brief Поехали! """
    #launcher()
    main()

"""!



@var threads `(list)` List of execution threads  
**[en]**  List of execution threads.  
In multithreaded mode, each supplier from the supplier_prefix list will be added to the list   
**[ru]**  Список потоков выполнения.  
В многопоточном режиме в список будет добавлен каждый поставщик из списка `supplier_prefix`

@details Параметры запуска задаются в функции `launcher()`. Функция предоставляет возможность гибко настраивать парамерты запуска.  
        Настройки можно: 
         - прописать в файле  `src/project_setting/global_settings.json` или
         - явно передать параметрами в `launcher(supplier_prefix, scenario, scenario_language, gui_mode)`
         
"""

