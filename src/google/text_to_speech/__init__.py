"""  [File's Description]

@namespace src: src

\file __init__.py

 @section libs imports:
  - attr 
  - pyttsx3 
  - gtts 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""


from attr import attr, attrs

import pyttsx3


from gtts import gTTS


class TTS():
    """ Google text to speach """
    def __init__(self,*args,**kwards):
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        for v in voices:
            print(v)
    pass


_tts = TTS()

