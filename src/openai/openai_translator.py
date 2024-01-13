"""! @brief   [File's Description]
@namespace src: src
 \package src.tools
\file openai_translator.py
 @section libs imports:
  - os 
  - sys 
  - openai 
  - src.gs 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import os
import sys
import openai


# --------------------
from src.settings import gs
# --------------------
openai.api_key = gs.api_openai

def translate(input_text: str, target_lang: str) -> str:
    """! @brief OpenAI translator

    Parameters : 
         origin : str : original text
         target_lang : str : translate to language
    Returns : 
         str : transpaled text

    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this into {target_lang}:\n\n{input_text}\n\n",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    translated_text = response.choices[0].text.strip()
    return translated_text
