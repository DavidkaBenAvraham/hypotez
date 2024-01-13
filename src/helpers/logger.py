"""! @russian 
@brief Класс логгера
@details 
"""
import asyncio
import logging
import colorama
import traceback
from threading import Lock
from .beeper import Beeper, BeepLevel

# Инициализация colorama


class LoggerSingleton():
    """!
    @brief Класс логгирования 
    @details Класс `Singleton` для управления единственным экземпляром логгера.
    Инстанс класса вызывается через `get_instance()` 
    """

    _instance = None
    _logger = None
    level = None
    colorama.init()
    
    def __new__(cls, *args, **kwargs):
        """!
        @brief Создает инстанс класса LoggerSingleton.

        @details Если инстанс класса еще не создан, создает новый экземпляр, иначе возвращает существующий.

        @param cls: Класс LoggerSingleton.
        @param args: Позиционные аргументы.
        @param kwargs: Именованные аргументы.

        @return: Экземпляр LoggerSingleton.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """!
        @brief Возвращает единственный экземпляр LoggerSingleton.

        @details Если инстанс класса еще не создан, создает новый экземпляр, иначе возвращает существующий.

        @param cls: Класс LoggerSingleton.

        @return: Экземпляр LoggerSingleton.
        """
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self, name: str = 'l', level: str = logging.DEBUG, filename=None):
        """!
        @brief Инициализирует объект LoggerSingleton.

        @details Метод настраивает логгер при первом вызове.

        @param self: Экземпляр LoggerSingleton.
        @param name: Имя логгера.
        @param level: Уровень логирования (по умолчанию INFO).
        @param filename: Имя файла лога (по умолчанию None).
        """
        if not self._logger:
            self._logger = logging.getLogger(name)
            
            self._logger.setLevel(level)
            self.level_name = logging.getLevelName(level)

            #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            if filename:
                file_handler = logging.FileHandler(filename)
                file_handler.setFormatter(formatter)
                self._logger.addHandler(file_handler)
            else:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                self._logger.addHandler(console_handler)

    def _get_colored_message(self, message, ex, color):
        """!
        @brief Возвращает окрашенное сообщение.

        @param self: Экземпляр LoggerSingleton.
        @param message: Исходное сообщение.
        @param color: Цвет для окрашивания.

        @return: Окрашенное сообщение.
        """
        ret = f'''{color}{message}'''
        if ex: ret += ex
        ret += colorama.Style.RESET_ALL
        return ret

    def _get_formatted_traceback(self, ex = None):
        """!
        @brief Возвращает отформатированный traceback.

        @param self: Экземпляр LoggerSingleton.
        @param ex: Исключение
        @return: Отформатированный traceback.
        """
        trbk = traceback.format_exc (ex)
        #trbk = traceback.print_exception(ex)
        if not trbk: return ''
        #return trbk.format_exc()
        return trbk

    def info(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает информационное сообщение в лог и бибикает.
        @todo Здесь надо оформить выввод в файл
        
        @param self: Экземпляр LoggerSingleton.
        @param message: Информационное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.INFO) )
        colored_message = self._get_colored_message (message, None, colorama.Fore.GREEN)
        self._logger.info (colored_message)

    def success(self, message, ex = None, exc_info=True ):
        """!@~russian
        @brief Записывает сообщение о успешном завершении в лог и бибикает.
        @param self: Экземпляр LoggerSingleton.
        @param message: Информационное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.ATTENTION))
        colored_message = self._get_colored_message (message, None, colorama.Fore.BLUE)
        self._logger.info (f"{colored_message}", exc_info=exc_info)     

    def warning(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает предупреждение в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Предупреждение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.WARNING) )
        colored_message = self._get_colored_message(message, None, colorama.Fore.YELLOW)
        self._logger.warning(f"{colored_message}")        

    def debug(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает отладочное сообщение в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Отладочное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.DEBUG))
        colored_message = self._get_colored_message(message, None, colorama.Fore.CYAN)
        self._logger.debug(colored_message, exc_info=exc_info)        

    def error(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает сообщение об ошибке в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Сообщение об ошибке.
        @param exc_info: Флаг, указывающий, следует ли включать информацию об исключении (по умолчанию True).
        """
        if not Beeper.silent: asyncio.run ( Beeper.beep (BeepLevel.ERROR) )
        # colored_message = self._get_colored_message(message, colorama.Fore.RED)
        # self._logger.error(f"{colored_message}\n{self._get_formatted_traceback(ex)}", exc_info=exc_info)
        #colored_message = self._get_colored_message(self._get_formatted_traceback(ex), colorama.Fore.RED)

        colored_message = self._get_colored_message(message, self._get_formatted_traceback(ex), colorama.Fore.RED)
        self._logger.error(colored_message, exc_info = exc_info)

    def critical(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает сообщение об ошибке в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Сообщение об ошибке.
        @param exc_info: Флаг, указывающий, следует ли включать информацию об исключении (по умолчанию True).
        """
        if not Beeper.silent: asyncio.run ( Beeper.beep (BeepLevel.CRITICAL) )
        colored_message = self._get_colored_message(message, self._get_formatted_traceback(ex), colorama.Fore.MAGENTA)
        self._logger.critical(colored_message, exc_info=exc_info)        

    
logger = LoggerSingleton.get_instance()
