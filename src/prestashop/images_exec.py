"""! @en_brief   Images preparation
@ru_brief загрузка изображений в `Prestashop`
 
 @section libs imports:
  - sys 
  - os 
  - pathlib 
  - requests 
  - PIL 
  - typing 
  - src.gs 
  - src.helpers 
  - src.tools 
  - src.prestashop.prestashop 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import sys
import os


from pathlib import Path
import requests
from PIL import Image
from typing import Union

# --------------------
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.tools import randomizer
from src.prestashop.prestashop import \
    PrestaAPIV1, PrestaAPIV2, PrestaAPIV3, \
    PrestaAPIV1Error, PrestaAPIV2Error, PrestaAPIV3Error
#from . import PrestaShopWebServiceError
# --------------------

#@logs_and_errors_decorator(default_return =  False)
def upload_image(resource: str, image_data: bytes = None, \
                 image_name: str = 'default.png', image_url: str = None) -> Union[dict, False]:
    """ Загружаю картинку через API

    Args:
        resource `str`  :  entity/id
                        
                        The entity is: "general", "products", "categories", "manufacturers", "suppliers", "stores", "customizations"
                        id: id of entity
                        -------------------------
                        F.E.
                        `products/15`

        image_data (bytes): the binary data of the image. 
                            Binary data is a sequence of bytes that represents information about the image. 
                            This data can include the image pixels, metadata, file format, and other information 
                            necessary for representing and reproducing the image.

        image_name (str, optional): _description_. Defaults to 'img.png'.

        image_url `str`  :  Я могу не передавать бинарный файл, если у меня есть откуда его скачать. 
        Если нет - я передаю URl картинки

    @returns
        Union[dict, False]:  dictionary object if success else False
    """


    #------------------------------------------------------------------------------------
#                  Блядский цирк с форматами. Этот костыль мне вырвет глаз 

    temp_filename = str(Path(gs.dirs.get('temp'), 'temp.png'))
    
    def write_temp_file_from_url_as_png(image_url: str):
    
        response = requests.get(image_url)
        image_data = response.content
        with open(temp_filename, 'wb') as file:
            file.write(image_data)

        image = Image.open(temp_filename)
        image.save(temp_filename, 'PNG')
    
    def read_temp_file() -> bytes:
        with open(temp_filename, 'rb') as file:
            image_data = file.read()  
        return image_data


    if image_data is None:
        
        write_temp_file_from_url_as_png(image_url)
        image_data = read_temp_file()

# -----------------------------------------------------



    try:

        # Добавление изображения в базу данных PrestaShop


        resource = fr'images/{resource}'
        image_name = image_name if image_name != 'default.png' else str(f'default_{randomizer.get_random_string(10)}.png')
        image_info = PrestaAPIV1.add(resource,  files = [('image', image_name, image_data)] )
        logger.debug(f"""
        Дефолтное изображение для {resource.capitalize()} 
        успешно загруженo""")
        return image_info


    #except PrestaShopWebServiceError as ex:
    except Exception as ex:
        print(f""" 
        Ошибка при загрузке дефолтного изображения для 
        {resource}: 
        Ошибка
        {ex}
        {image_data}
        """)
        return False
