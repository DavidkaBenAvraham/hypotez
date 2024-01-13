from . import logger

class FileNotFoundError(FileNotFoundError):
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        super().__init__(message)
        self.additional_operations = additional_operations
        
class ProductFieldException(Exception):
    """! Исключение, связанное с полями товара."""
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        super().__init__(message)
        self.additional_operations = additional_operations

class KeepassException(Exception):
    """! Исключение, связанное с проблемами подключения к базе данных Keepass."""
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        #super().__init__(message, ex)
        if 'Invalid credentials' in ex.args:
            print('Неверный пароль')
            return False
        
        super().__init__(message, ex)
        self.additional_operations = additional_operations
        
class DefaultSettingsException(Exception):
    """! Исключение, связанное с проблемами установки дефолтных значений."""
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        super().__init__(message)
        self.additional_operations = additional_operations

class DriverException(Exception):
    """! Исключение, связанное s WebDriver."""
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        
        super().__init__(message)
        self.additional_operations = additional_operations
        
class ExecuteLocatorException(Exception):
    """! Исключение, связанное с элзекьютором локатора."""
    def __init__(self, message, ex: Exception = None, additional_operations=None):
        
        super().__init__(message)
        self.additional_operations = additional_operations
