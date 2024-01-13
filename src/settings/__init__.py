"""!
@~english
@brief Project settings passwords, server addresses, and other sensitive information.  
@details Passwords are stored in a database in KeyPass format. The file extension of the database is kdbx.  
To open the database, a master password is required.  
[More details about KeyPass](https://keepass.info/help/base/index.html) 


@~russian
@brief Дефолтные настройки программы
@details Класс `ProjectSetting` (`src.settings.global_settings.ProjectSettings`) 
определяет основные параметры запуска: 
- список поставщиков, который будет исполнятся, если не определён другой
- локаль - основной язык сбора информации от поставщика
- пароли, логины и адреса серверов для подлючения к внешним исочником
- внутренние пути проекта

Класс вызывается как синглтон через инстанс `gs`:
@code
from src.settings import gs
@endcode
@note
Пароли хранятся в базе данных формата keypass Расширение файла базы данных - `.kdbx`.  
Для открытия базы данных необходим мастер пароль.  
[Подробней о keypass](https://keepass.info/help/base/index.html)  
 

---


@section libs imports:
- src.settings.gs (local)


---


@todo Я перенес модуль интерфейсов в `settings`.  
 Новое имя модуля `gui` старое `launchers`.   
 нет реализации пользовательского интерфейса.  
 Не срочно  
"""

from .global_settings import gs
from .gui import *
