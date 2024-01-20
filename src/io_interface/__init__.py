"""! @~en  input/output interfaces, such as `file`, `ftp`, `smtp`  
@~russian  Модуль ввода/вывода
@details Интерфейсы подключения к внешним службам `file`, `ftp`, `smtp` итп

 
@section libs imports:
- .jjson (local)
- .jjson (local)
- .jjson (local)
- .file (local)
- .ftp (local)
- .smtp (local)
  

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .jjson import json_loads as j_loads
from .jjson import json_dumps as j_dumps

from .file import save_text_file
from .ftp import send, receive
from .smtp import send

pass
