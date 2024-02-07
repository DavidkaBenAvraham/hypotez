"""  [File's Description]


 @section libs imports:
  - .core 
  - .exceptions 
  - .version 

"""
from .core import \
    Prestashop as PrestaAPIV3 , \
    Format as PrestaAPIV3Format
from .exceptions import \
    PrestaShopError as PrestaAPIV3Error ,\
    PrestaShopAuthenticationError as PrestaAPIV3AuthenticationError
from .version import __author__,__version__