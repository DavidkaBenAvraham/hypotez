# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import json
from pathlib import Path
import sys
import os
from attr import attr, attrs
from typing import Union
hypotez_root_path = os.getcwd()[:os.getcwd().rfind(r'\hypotez')+7]
sys.path.append(hypotez_root_path)  # Добавляю корневую папку в sys.path

# ---------------------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps

# -----------------------------------