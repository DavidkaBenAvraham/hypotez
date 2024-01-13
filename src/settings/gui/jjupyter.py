""" 
 Jupyter notebook or Jupyter lab interface

 @section libs imports: 
  - src.settings 
  - src.helpers (local)
  - subprocess 
  - os 
  - pathlib 

"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from src.settings import gs
from src.helpers import logger, logs_and_errors_decorator
import subprocess
import os
from pathlib import Path

class JupyterNotebook:
    """
     [Class's description]


    """
    
    
    notebook_dir = 'notebooks'
    start_notebook = 'gheets.ipynb'

    #url = 'http://localhost:8888/notebooks/example.ipynb'
    url = 'notebooks/OneDrive/repos/DavidkaBenAvraham/hypotez/launchers/run.ipynb'


    notebook_path = os.path.join(notebook_dir, start_notebook)
    notebook_path_rel = os.path.join(os.pardir, notebook_path)
    notebook_path_abs = os.path.abspath(notebook_path)
      
    def run_notebook(self) -> bool:
        """ Набросок на память для запуска блокнота Юпитера"""
        try:
            webbrowser.open_new_tab(self.url)
        except Exception as ex:
            logger.debug (ex)
        # subprocess.run(
        #     ['jupyter', 'nbconvert', '--execute', '--inplace', self.url])
        subprocess.call(['jupyter', 'notebook', '--NotebookApp.default_url='+self.url])
    
    def run_lab(self) -> bool:
        """ Запуск Jupyter lab 
        из виртуального окружения
        """
        jupyther_path = Path(gs.dir_root,'venv','scripts')
        #jupyther_path = Path(gs.dir_root,'bin')
        
        try:
            subprocess.run([ str(jupyther_path), 'jupyter-lab'])
            #subprocess.run('jupyter-lab')
        except Exception as ex:
            logger.error(f""" Юпитер пал! """,ex)
            return False