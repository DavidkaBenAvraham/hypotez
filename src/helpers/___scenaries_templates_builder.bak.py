# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import os
from pathlib import Path

from src.settings import GlobalSettings
logger = gs.logger



def build_templates(templates_dir_path: str = None) -> dict:
    '''Build a dictionary of templates categories based on JSON files in the specified directory.

    @param
        templates_dir_path (str, optional): The path to the directory containing the JSON files. If None, the function will return an empty dictionary.

    @returns
        dict: A dictionary containing all categories defined in the JSON files. If there are errors reading the files or building the dictionary, an empty dictionary is returned.
    '''
    # Create an empty dictionary to hold the templates
    templates = dict()

    # Recursively walk through the specified directory and its subdirectories
    for root, dirs, files in os.walk(templates_dir_path):
        # If there are any files in the directory, iterate over them
        if isinstance(files, list):
            for f in files:
                # Load the contents of the JSON file
                _d = gs.j_loads(Path(root, f))
                try:
                    # Update the templates dictionary with the contents of the JSON file
                    templates.update(_d)
                except Exception as ex:
                    # If there was an error updating the dictionary, log the error and continue to the next file
                    logger.error(f'''Error adding templates from {f}: ''', ex)
                    continue
        # If there are no files in the directory, move on to the next directory
        else:
            templates.update(gs.j_loads(Path(root, f)))
    # Return the completed templates dictionary
    return templates
