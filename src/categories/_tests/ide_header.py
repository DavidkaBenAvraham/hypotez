"""! Файл заголовок, подключаемый к ide тестовым модулям """

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import json
from pathlib import Path
import sys
import os
from attr import attr, attrs
from typing import Union

dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind('hypotez') + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))

# ---------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps

# -----------------------------------
