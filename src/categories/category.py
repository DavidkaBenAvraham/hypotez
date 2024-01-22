"""! @brief Работа с категориями товара 


@section libs imports:  
  - pathlib 
  - os 
  - typing 
  - src.gs 
  - src.helpers 
  - src.io_interface 
  - src.prestashop 
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python



from pathlib import Path
import os
from typing import Union


from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import PrestaCategory
# -----------------------------------

class Category (PrestaCategory):
    """ Класс категорий товара 
    Methods:
         __init__(self, *args, **kwards)
         get_list_categories_from_template_files(self, normalize: bool = True) -> dict
         move_templates_to_first_position(dictionary: dict) -> dict:
         get_list_categories_from_scenario_category(self, category_name: str) -> list:
    @var:
        categories_tree_from_template_files (list[dict]) : Категории, построенные из файлов шаблонов
    """

    categories_tree_from_template_files: dict = {}
    """! дерево категорий, восстановленное из файлов JSON в `templates` """
    
    categories_tree_from_prestashop: dict = {} 
    """! Дерево категорий, полученнное от Pestashop """
    
    def __init__(self, *args, **kwards):
        self._payload(*args, **kwards)
    
        

    #@logs_and_errors_decorator(default_return =  False)
    def _payload(self, *args, **kwards):
        self.categories_tree_from_template_files = self.get_list_categories_from_template_files()
        
    #@logs_and_errors_decorator(default_return =  False)
    def get_list_categories_from_template_files(self, normalize: bool = True) -> dict:
        """ Build a dictionary of template categories based on JSON files in the specified directory.

        @param
            normalize (bool): If True, move the 'template' key to the first position in the dictionary.

        @returns
            dict: A dictionary containing all categories defined in the JSON files. If there are errors reading the files or building the dictionary, an empty dictionary is returned.
        @var:
            _product_categories_templates (dict) :  dictionary to hold the templates
            
            product_categories_templates_path (Path) : path to categories template
        """
        
        _product_categories_templates : dict = {}

        product_categories_templates_path : Path = Path(gs.dir_src,'categories','templates')

        try:
            for root, dirs, files in os.walk(product_categories_templates_path):
                if isinstance(files, list):
                    for file in files:
                        category_from_template = j_loads(Path(root, file), ordered=True)
                        #   """ Load the contents of the JSON file """

                        if normalize:
                            """pop up templates"""
                            category_from_template = self.move_templates_to_first_position(category_from_template)
                        try:
                            _product_categories_templates.update(category_from_template)
                            #   """ Update the _product_categories_templates dictionary with the contents of the JSON file """
                        except Exception as ex:
                            logger.error(f"""Error adding _product_categories_templates from {file}: {ex} """)
                            continue

                else:
                    _product_categories_templates.update(j_loads(Path(root, file)))

            return _product_categories_templates

        except Exception as ex :
            logger.error('', ex)
            return False



    
    #@logs_and_errors_decorator(default_return =  False)
    def move_templates_to_first_position(self, dictionary: dict) -> dict:
        """
        сдвигаю темплейт в JSON файлах на первую позицию. Так я знаю, что она будет дефолтной
        Move the 'templates' key to the first position in the dictionary.

        @param
            dictionary (dict): The dictionary to modify.

        @returns
            dict: The modified dictionary.
        """
        for key, value in dictionary.items():
            if "template" in value:
                template = value.pop("template")
                value = {"template": template, **value}
            dictionary[key] = value

        return dictionary
    

    #@logs_and_errors_decorator(default_return =  False)
    def get_list_categories_from_scenario_category(self, category_name: str) -> list:
        category_path = []
        current_category = category_name

        while current_category != "ROOT":
            """! поднимаюсь по родительским категориям до ROOT """
            if current_category in self.categories_tree_from_template_files:
                category_path.append(current_category)
                current_category = self.categories_tree_from_template_files[current_category]['template'][current_category]
            else:
                break

        category_path.reverse()
        return category_path

    