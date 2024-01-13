"""  [File's Description]

@namespace src: src
 \package src.categories
\file category.py
 
 @section libs imports:
  - pathlib 
  - sys 
  - os 
  - typing 
  - gs 
  - helpers 
  - gs 
  - prestashop 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python



from pathlib import Path
import sys
import os
from typing import Union

hypotez_root_path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
sys.path.append(hypotez_root_path)  # Добавляю корневую папку в sys.path
# ---------------------------------
from src.settings import gs
from src.helpers import  logger, jprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import Category as PrestaCategory
# -----------------------------------

class Category():
    """
     Управляет категориями
    """

    categories_from_templates: dict = {}
    def __init__(self, *args, **kwards):
        self.categories_from_templates = self.get_categories_from_template_files()
    


    def get_categories_from_template_files(self, normalize: bool = True) -> dict:
        """
        Build a dictionary of template categories based on JSON files in the specified directory.

        @param
            normalize (bool): If True, move the 'template' key to the first position in the dictionary.

        @returns
            dict: A dictionary containing all categories defined in the JSON files. If there are errors reading the files or building the dictionary, an empty dictionary is returned.
        """

        _product_categories_templates = dict()
        """ Create an empty dictionary to hold the templates """

        product_categories_templates_path = Path(gs.dir_root,'categories','templates')

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
                        #   """ Update the `_product_categories_templates dictionary` with the contents of the JSON file """
                    except Exception as ex:
                        logger.error(f"""Error adding _product_categories_templates from {file}: {ex} """)
                        continue

            else:
                _product_categories_templates.update(j_loads(Path(root, file)))

        return _product_categories_templates

    @staticmethod
    def move_templates_to_first_position(dictionary: dict) -> dict:
        """
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




    def get_list_categories_for_scenario_category(self, category_name: str) -> list:
        category_path = []
        current_category = category_name

        while current_category != "ROOT":
            if current_category in self.categories_from_templates:
                category_path.append(current_category)
                current_category = categories_from_template[current_category]['template'][current_category]
            else:
                break

        category_path.reverse()
        return category_path
