"""! @brief   Исполнитель сценариеев
@details Функции экзекьютера:
- `run_scenario_files()` - Принимает список файлов сценария. Разбирает список и отдает испонителю файла
- `run_scenario_file()` - разбирает файл сценария на список сценариев и отдает каждый в екзекьютор `run_scenario()` 
- `run_scenario()`  - исполняет сценарий. Типичный сценарий содержит информацию об одной категории товаров. Драйвер переводит URl на страницу категории,
с нее получает ссылки на товары в категории, переходит по каждой из них и отдает грабберу конкретного поставщика собрать информацию с полей страницы товара. 
Получив поля функция передает их в обработчик престашоп
- `run_scenarios()` - Добавляет гибкость: я могу собрать список сценариев из разных файлов
 @section libs imports:
  - sys 
  - os 
  - pathlib 
  - typing 
  - src.gs 
  - src.gs 
  - src.gs 
  - src.product 
  - .grabber 
@file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

# Imports
from ast import Str
from math import log, prod
import os, sys
import requests
from pathlib import Path
from typing import Union, Dict, List
import asyncio

# ------------------------------
from src.settings import gs
from src.helpers import logger,  logs_and_errors_decorator, DriverException, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.product import Product, ProductFields
from src.prestashop import save_image_from_url_to_temp_as_png
from src.prestashop import PrestaAPIV
# -------------------------------

################################################################################################################
#
#                                на протяжении всего кода  `s` Supplier
#                                                          `gs` Global Settings 
#
################################################################################################################

#@logs_and_errors_decorator(default_return =  False)
def run_scenario_files(s, list_scenario_files_paths: Union [list[Path], Path] ) -> bool:
    """!@~russian функция запускает список файлов сценариев один за другим
    
    @param s `src.suppliers.Supplier`
    @param scenario_files `list[str] | str` = `None` : A list of file paths for the JSON scenario files to be executed. 
    If None, the default list of scenarios from s.scenario_files will be used.
    @returns bool `True` if all scenarios were executed successfully, else `False`
    
    @details Набор сценариев можно передать через `scenario_files`. 
    Если список сценариев не передан, он берется из установок поставщика по умолчанию  `s.settings.scenarios`. 
    Для каждого сценария из списка будет вызвана функция `src.scenarios.executor.run_scenario_file()`, 
    которая загружает файл сценариев в формате JSON и передает и запускет для каждого сценария функцию
   `src.scenarios.executor.run_scenario()`.
   
   @note Я могу подменить набор файлов сценариев по умолчанию на свой. 
    
    
     @en_details Runs the set of scenarios passed in scenario_files. If the list of scenarios is not passed, it is taken from 
    s.settings['scenarios']. For each scenario in the list, the function run_scenario_file(s, current_scenario_filename)
    is called, which loads the JSON scenario file and passes it to the function run_scenario(s, scenario).

    @todo Если я позволяю пустое значение в `scenario_files` - по умолчанию я должен исполнить все сценарии
    
    """
 
    list_scenario_files_paths = [list_scenario_files_paths] if isinstance(list_scenario_files_paths, str) else (list_scenario_files_paths or s.list_scenario_files_paths)
    
    for current_scenario_file_path in list_scenario_files_paths:
        """! получив список файлов сценариев разбираю их по одному """
        if run_scenario_file(s, current_scenario_file_path):
            s.settings['last_runned_scenario_filename'] = current_scenario_file_path
            j_dumps(s.settings, Path(s.supplier_abs_path, f'{s.supplier_prefix}.json'))
            """! @~russian записываю измемения в файл 
            @details запоминаю последний выполненный файл сценария, чтобы знать откуда продолжать в случае перезапуска """
        else:
            logger.error(f'Сценарий {current_scenario_file_path} Не выполнился !')
            
    return True #"""! @todo <- это плохо реализовано. У меня бегут несколько сценариев, если хоть один из них упадет - надо разбираться в причине """
    # Return True to indicate successful execution of all scenarios

#@logs_and_errors_decorator(default_return =  False)
def run_scenario_file(s, scenario_file_path: Union[Path, str]) -> bool:
    """! @~en Runs the scenario file specified in `scenario_file_path`.
    @~russian Загружаю сценарий из файла, указанного в `scenario_file_path`

    @param s `Supplier`
    @param scenario_file_path `str` The name of the scenario file in the scenarios directory.
    @returns bool `True` if the scenario file was successfully run, `False` otherwise.

    """
    logger.info(f'Старт файла сценария {scenario_file_path}')
   
    scenarios_dict: dict = j_loads (scenario_file_path)['scenarios']
    for scenario_name, scenario in scenarios_dict.items ():
        """! @~russian прочитав сценарии из файла запускаю их по одному """
        s.current_scenario: dict = scenario
        if run_scenario (s, scenario, scenario_name):
            """! @~russian запуск сценария """
            s.supplier_settings['last_runned_scenario'] = scenario_name
            logger.info(f'''last runned scenario {s.supplier_settings['last_runned_scenario']}''')
        else:
            logger.critical(f'Сценарий {scenario} завершился ошибкой')
            s.supplier_settings['scenario_interrupted'] = scenario_name

        j_dumps(s.supplier_settings, Path(s.supplier_abs_path, f'{s.supplier_prefix}.json'))
        """! оставляю запись в файле сценариев информацию о последнем сценарии.
        В случае непредвидинного краша позволяет мне знать с какого сценария продолжать сбор товаров."""
        """! @todo Сделать такой -же контроль но на уровне файлов в файле поставщика """

    return True

#@logs_and_errors_decorator(default_return =  False)
def run_scenarios(s, scenarios: Union [ list[dict], dict ] = None) -> Union[list, dict, False]:
    """! Функция выполняет список сценариев (НЕ ФАЙЛОВ) 
    @param `scenarios` На вход принимает список сценариев, или одиночный сценарий как dict
    Для исполнения сценариев вызывается `run_scenario(s, scenario)
    @param s `Supplier` поставщик
    """
    if not scenarios:
        scenarios = [s.current_scenario]
        """! Если не заданы сценарии - беру из s.current_scenario
        @todo - проверить со всех сторон эту опцию. Например, не задан `s.current_scenario` и не задан `scenarios` 
        """
        
        
    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res.append ( run_scenario(s, scenario) ) 
    return res

#@logs_and_errors_decorator(default_return =  False)
def run_scenario(s, scenario: dict, scenario_name: str = None) -> Union[list, dict, False]:
    """! Функция запускает полученный сценарий.
    @param s `Supplier`
    @param scenario `dict` : dictionary containing scenario details
    @param scenario_name `str` : name of scenario f.e. ???? Мне непонятно зачем этот параметр ???
    @todo проверить надобность в `scenario_name`
    @returns результат исполнения сценария

    """
    # 1.
    logger.info (f'Старт сценария: {scenario_name}')
    d = s.driver
    d.get_url(scenario['url'])
    
    # 2.
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)
    

    # Нет товаров в категории (ну, или не успели загрузиться)
    if not list_products_in_category:
        logger.warning ('Не собран список товаров со страницы категории. Возможно пустая категория  - ', d.current_url)
        return False

    # 3.
    for url in list_products_in_category:
        """! Перехожу по url товара и вытаскиваю данные со страницы """
        if not d.get_url(url):
            logger.error(f'Ошибка перехода на страницу товара по адресу: {url}' )
            continue ## <- Ошибка перехода на страницу. Пропускаю

        # 4.
        product_fields = s.related_modules.grab_product_page(s)
        """! Собираю со страницы товара значения элементов и привожу их к полям ProductFields 
        Внимание! В словаре `product_fields` находится служебный словарь `dict_assist_fields`.
        Его надо вычленить в отдельный словарь
        """
        if not product_fields:
            logger.error(f'не удалось собрать значение полей товара по адресу {url}')
            continue   ## <- Ошибка сбора данных со страницы. 

           
        dict_presta_fields: Dict = {key: value for key, value in product_fields.dict_presta_fields.items() if value is not None and value != ''}
        """! очищаю словарь от пустых значений """
            
        """! dict: Словарь полей товара для престасшоп """
        dict_assist_fields: Dict = product_fields.dict_assist_fields
        """! dict: Словарь дополнительных полей для меня (images urls etc.)"""
                        
        if 'quantity' in dict_presta_fields: del dict_presta_fields['quantity']
        """! `quantity` нельзя задавать при добавлении нового товара """
            

        # 5.
        execute_prestashop_insert(dict_presta_fields, dict_assist_fields)
        
           
        

#@logs_and_errors_decorator(default_return=False)
def execute_prestashop_insert(dict_presta_fields:Dict, dict_assist_fields:Dict) -> bool:
    """! @~russian   Добавляю или проверяю наличия товара. Делаю последовательное содинение с Пресашоп АПИ
    @brief Это оч плохое решение. Но это не костыь, а проверка работоспособности
    @details
    @todo - Сделать здесь многопотчонсть (или асинхронность)
    """

       
    """! Для каждого товара я заново переопрделяю класс `Product`, 
    иначе может попасть мусор (данные прошлого товара) """ 
    pass
    # 5.1 строю фильтр API запроса
    reference = dict_presta_fields["reference"]
    search_filter: Dict = { 'filter[reference]': '['+ reference + ']',  }
    """! Для `V3` Я могу передать фильтр, как строку `filter[id] = [5]` и как словарь `{'filter[id]':'[5]'}`	
    По умолчанию я использую словарь """
    display: Dict = {'display':'full'}
    search_filter.update(display) 
    
    for api_credentials in gs.list_prestashop_api_credentials:
        """! Подключаюсь к каждому клиенту по очереди  """
        p = Product(api_credentials)    
        # 5.2 Получаю ответ от престашоп. 
        check_prod_presence = p.get( search_filter, api_credentials)
        """!  Проверка наличия товара в базе данных.
        если товара еще нет в бд - вернется пустое значение.
        Если товар уже существует - редактирую поля если они изменились (цена, описание итп)"""
        pass
                 
        if check_prod_presence is False or not check_prod_presence or len(check_prod_presence) == 0:  ## <- вернулся пустой responce от сервера. Значит товара с таким reference нет в бд престашоп
            try: ## <- add new product
                added_prod_dict = p.add(dict_presta_fields, 'JSON')['products'][0] 
                """! Добавляю товар в бд. В ответ получаю словарь с параметрами добавленного товара """
                # 6.1
                product_id = added_prod_dict['id']
                product_reference = added_prod_dict['reference']
                """! Мне нужен id товара и reference """
                if not save_img(product_id, dict_assist_fields):
                    logger.error(f'''Images for produt reference {product_reference} not saved! ''')
                logger.info (f''' pprint(product_id) ''')
            except Exception as ex:
                logger.error (f'ошибка добавления нового товара {ex}')
                return False
            
            
            
            i: int = 0 ## <- счетчик картинок
            def save_img(product_id:int , dict_assist_fields: Dict) -> Union[object, bool]:
                """! Функция сохранения картинок товара
                @param product_id `int` - id  только что добавленного товара
                """
                ...
                url_parts = image_url.rsplit('.', 1)
                url_without_extension = url_parts[0]
                extension = url_parts[1] if len(url_parts) > 1 else ''
                filename = str(product_reference)+f'_{i}.{extension}'
                saved_file_path = save_image_from_url_to_temp_as_png(image_url, filename)
                
                return p.upload_image(product_id, saved_file_path)

            

            """! @todo Реализовать проверку изменения картинок. 
            Для этого я должен где-то хранить полный URL загруженных картинок """            
            # 6.2 сохрняю картинки на диск, а потом поднимаю в базу престашоп
            

            # 6.2.1 сохраняю дефолтную картинку
            saved_img_dict: dict = save_img(product_id, dict_assist_fields['product_image_default_url'][0], i)
            """! Если картинка загрузилась - вернется словарь 
            `{'product_id':'int', 'image_id':'int', 'cover':'int', 'position':'int', 'legend':'{dict}'}` """
            
            # 6.2.2 добавляю к товару id дефолтной картинки
            added_prod_dict['id_default_image'] = saved_img_dict['id']
            pass
            
            # 6.2.3 Сохраняю остальные картинки
            for url in dict_assist_fields['product_images_additional_urls']:
                i+=1
                save_img(product_id, url, i)
            pass
            
            
    # 7. Товар уже есть в бд престашоп    
    else:
        pass
        """! @todo Товар в бд. Реализовать редактирование """
                









#########################################################################################################################
#                                                                                                                       #
#                                                                                                                       #
#                                                    ФУНКЦИИ для ДЕБАГГИНГА                                             #
#                                                                                                                       #
#########################################################################################################################



    def update_locators_file(self, locators: dict, entity: str = 'product | category | login | store' ) -> dict:
        """! @~russian Редактор локаторов  
        Если я меняю локатор на лету - я могу заменить его в файле  
        Хорош для дебаггера и изменения локатора при изменении дизайна целевой страницы.
        Целевые страницы часто меняют дизайн, поэтому есть необходимость менять локатор "на лету".
        Перед сохранением измененного значения создается файл бекап. 
        @todo Помнить об этой особенности. Она плодит сущности!
        @param issue `str` сущность 
        @param locator `dict`: json для сохранения в файл
        @returns locator dict : перезагруженый словарь локаторов
        """
        locators_file = Path (self.supplier_abs_path, 'locators', f'{entity}.json')
        backup_locators_file = Path (self.supplier_abs_path, 'locators', f'{gs.get_now}_{entity}.json')
        shutil.copy2 (locators_file, backup_locators_file)
        j_dumps (locators, locators_file)
        self.locators [entity] = j_loads (locators_file)
        return self.locators [entity]

