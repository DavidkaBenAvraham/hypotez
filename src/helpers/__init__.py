"""! @en_brief  Auxiliary utilities
@ru_brief Вспомогательные утилиты: логер, печать, ошибки

 
 @section libs imports:
  - .logger 
  - .printer 
  - .exceptions
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .logger import logger
from .logger_decorators import logs_and_errors_decorator
from .printer import jprint, pprint
from .beeper import Beeper, BeepLevel
from .exceptions import *
pass