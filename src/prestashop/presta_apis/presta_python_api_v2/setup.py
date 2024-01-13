"""  [File's Description]

 @namespace src
 \package src.prestashop.presta_apis.presta_python_api_v2
\file setup.py
 
 @section libs imports:
  - codecs 
  - os 
  - setuptools 
Author(s):
  - Created by Davidka on 10.11.2023 .
"""
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='presta_python_api_v2',
    version='0.0.1b1',

    description='Prestashop api wrapper for python' ,
    long_description='eddited by Katia',

    url='https://github.com/savaskoc/prestashop_api',

    author='Savas Koc, Katia',
    author_email='savaskoc11@gmail.com, one.last.bit@gmail.com',

    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='prestashop api presta_python_api_v2',
    py_modules=["presta_python_api_v2"],
    install_requires=['requests', 'xmltodict'],
)
