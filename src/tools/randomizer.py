"""! @brief   Generates a random

@namespace src: src
 \package src.tools
\file randomizer.py
 @section libs imports:
  - random 
  - string 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import random
import string

def get_random_string(length: int = 10) -> str:
    """
     Generates a random string of specified length.

    Parameters : 
         length : int = 10 : The length of the random string. Defaults to 10.
    Returns : 
         str : The generated random string.

    Examples:
    >>> get_random_string()
    '4K0J6R2T7I'
    >>> get_random_string(5)
    '1Y8N7'
    """

    
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
