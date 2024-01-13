"""  [File's Description]

 @namespace src
 \package src.prestashop.presta_apis.presta_python_api_v1.presta_python_api_v1
\file version.py
 
 @section libs imports:
  - importlib.metadata 
  - importlib_metadata 
Author(s):
  - Created by Davidka on 10.11.2023 .
"""
try:
    from importlib.metadata import version, PackageNotFoundError
except:
    # for python < 3.8
    from importlib_metadata import version, PackageNotFoundError

__author__ = "Guewen Baconnier <guewen.baconnier@gmail.com>"

try:
    __version__ = version("prestapyt")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"
