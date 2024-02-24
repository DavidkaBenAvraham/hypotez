"""! @~russian 
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
    logger_console = None
    logger_file: logging.Logger = None
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

    def __init__(self, name: str = 'l', level: str = logging.DEBUG, logger_file = None):
        """!
        @brief Инициализирует объект LoggerSingleton.

        @details Метод настраивает логгер при первом вызове.

        @param self: Экземпляр LoggerSingleton.
        @param name: Имя логгера.
        @param level: Уровень логирования (по умолчанию INFO).
        @param filename: Имя файла лога (по умолчанию None).
        """
        if not self.logger_console:
            self.logger_console = logging.getLogger(name)
            self.logger_console.setLevel(level)
            self.level_name = logging.getLevelName(level)

            #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


            # else:
            #     console_handler = logging.StreamHandler()
            #     console_handler.setFormatter(formatter)
            #     self.logger_console.addHandler(console_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger_console.addHandler(console_handler)
      
            """! 
            # Настроим вывод логов на экран
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_formatter = logging.Formatter('%(levelname)s: %(message)s')
            console_handler.setFormatter(console_formatter)
            logging.getLogger().addHandler(console_handler)

            # Настроим запись логов в файл
            file_handler = logging.FileHandler(filename='webdriver.log', mode='a')
            file_handler.setLevel(logging.DEBUG)  # Например, мы записываем все сообщения в файл
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logging.getLogger().addHandler(file_handler)
            """
    def set_log_file(self, filename: str, level:str = logging.DEBUG, name = 'file_logger'):
        self.logger_file = logging.getLogger(name)
        file_handler = logging.FileHandler(filename = filename, mode='a')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        #logging.getLogger().addHandler(file_handler)
        self.logger_file.addHandler(file_handler)
        self.logger_file.setLevel(level)
        
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

        return traceback.print_exc ()

    def info(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает информационное сообщение в лог и бибикает.
        @todo Здесь надо оформить выввод в файл
        
        @param self: Экземпляр LoggerSingleton.
        @param message: Информационное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.INFO) )
        colored_message = self._get_colored_message (message, None, colorama.Fore.GREEN)
        self.logger_console.info (colored_message)
        self.logger_file.info (message)

    def success(self, message, ex = None, exc_info=True ):
        """!@~russian 
        @brief Записывает сообщение о успешном завершении в лог и бибикает.
        @param self: Экземпляр LoggerSingleton.
        @param message: Информационное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.ATTENTION))
        colored_message = self._get_colored_message (message, None, colorama.Fore.BLUE)
        self.logger_console.info (f"{colored_message}", exc_info=exc_info) 
        self.logger_file.info (message)

    def warning(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает предупреждение в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Предупреждение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.WARNING) )
        colored_message = self._get_colored_message(message, None, colorama.Fore.YELLOW)
        self.logger_console.warning(f"{colored_message}")  
        self.logger_file.warning (message)

    def debug(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает отладочное сообщение в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Отладочное сообщение.
        """
        if not Beeper.silent: asyncio.run (Beeper.beep (BeepLevel.DEBUG))
        colored_message = self._get_colored_message(message, None, colorama.Fore.CYAN)
        self.logger_console.debug(colored_message, exc_info=exc_info) 
        self.logger_file.debug (message)

    def error(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает сообщение об ошибке в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Сообщение об ошибке.
        @param exc_info: Флаг, указывающий, следует ли включать информацию об исключении (по умолчанию True).
        """
        if not Beeper.silent: asyncio.run ( Beeper.beep (BeepLevel.ERROR) )
        # colored_message = self._get_colored_message(message, colorama.Fore.RED)
        # self.logger_console.error(f"{colored_message}\n{self._get_formatted_traceback(ex)}", exc_info=exc_info)
        #colored_message = self._get_colored_message(self._get_formatted_traceback(ex), colorama.Fore.RED)

        colored_message = self._get_colored_message(message, self._get_formatted_traceback(ex), colorama.Fore.RED)
        self.logger_console.error(colored_message, exc_info = exc_info)
        self.logger_file.error (message, self._get_formatted_traceback(ex))

    def critical(self, message, ex = None, exc_info=True):
        """!
        @brief Записывает сообщение об ошибке в лог и бибикает.

        @param self: Экземпляр LoggerSingleton.
        @param message: Сообщение об ошибке.
        @param exc_info: Флаг, указывающий, следует ли включать информацию об исключении (по умолчанию True).
        """
        if not Beeper.silent: asyncio.run ( Beeper.beep (BeepLevel.CRITICAL) )
        colored_message = self._get_colored_message(message, self._get_formatted_traceback(ex), colorama.Fore.MAGENTA)
        self.logger_console.critical(colored_message, exc_info=exc_info) 
        self.logger_file.critical (message)

    
logger = LoggerSingleton.get_instance()
pass
