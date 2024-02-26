import requests
import os
from PIL import Image
from pathlib import Path
from typing import Union, Dict, List
import asyncio

# ------------------------------
from src.settings import gs
from src.helpers import logger

def write_temp_file_from_url_as_png(image_url: str, save_path: str):
    try:
        response = requests.get(image_url)
        image_data = response.content
        with open(save_path, 'wb') as file:
            file.write(image_data)

        image = Image.open(save_path)
        save_path = f'{save_path}.png' 
        if os.path.exists(save_path): os.remove(save_path)
        """! Если файл существует, удаляем его """
        
        image.save(save_path, 'PNG')
        return  save_path
    except Exception as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return False

def save_image_from_url_to_temp(url: str, filename: str, save_path: str) -> Union[str, False]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_path = str(Path(save_path, filename))
            with open(save_path, 'wb') as f:
                f.write(response.content)
            logger.info("Изображение успешно сохранено как", save_path)
            return save_path
        else:
            logger.error("Не удалось загрузить изображение. Код состояния:", response.status_code)
            return False
    except Exception as ex:
        logger.error("Произошла ошибка:", ex)
        return False

def save_image_from_url_to_temp_as_png(url: str, filename: str, save_path: str = gs.dir_temp) -> Union[str, False]:
    """! функция save_image_from_url_to_temp_as_png загружает изображение по заданному URL, сохраняет его во временный файл и конвертирует его в формат PNG. """
    temp_filename = str(Path(save_path, filename))
    if save_image_from_url_to_temp(url, filename, save_path):
        saved_file_path = write_temp_file_from_url_as_png(url, temp_filename)
        return  saved_file_path or False
