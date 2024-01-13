"""  [File's Description]

@namespace src: src
 \package src.google.gtranslater
\file __init__.py
 
 @section libs imports:
  - googletrans 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from googletrans import Translator

translator = Translator()
result = translator.translate('Mitä sinä teet')
