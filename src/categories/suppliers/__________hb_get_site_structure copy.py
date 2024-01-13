""" HB spider categoruies
@namespace src: 
    src
\package
    src.categories.suppliers
\file 
    hb_get_site_structure.py
Modules:
  - gs (local)
  - helpers (local)
  - gs (local)
  - io_interface (local)
  - requests 
  - bs4 
  - re 
  - json 
Author:
  - Created by Davidka on 09.11.2023 .
"""
# ---------------------------------
from typing import Union
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator,  jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import Product as PrestaProduct, Category as PrestaCategory
# ---------------------------------

import requests
from bs4 import BeautifulSoup
import re

def get_links_with_text(url) -> Union[dict, False]:
    """ Возвращает ссылки на категории со страницы
    @param
        url (str) : URL страницы для парсинга категорий
    @returns
        dict (dict) : Словарь собранных категорий
        False (bool) : В случае неудачи

    """
    # Отправляю GET-запрос к указанному URL и получаю содержимое страницы
    response = requests.get(url)
    
    # Проверяю успешность запроса
    if response.status_code != 200:
        return {}
    
    # Создаю объект BeautifulSoup для анализа содержимого страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все ссылки на странице
    links = soup.find_all('a', href=True)
    
    # Создаю словарь, где ключ - это ссылка, а значение - текст ссылки
    links_with_text = {link['href']: link.text.strip() for link in links if re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])}
    
    return links_with_text

def recursive_crawl(url, depth) -> list[dict]:
    """ Рекурсивный обход ссылок на категории
        @param
            url (str) : стартовый URL
            depth (int) : глубина рекурсии 
        @returns
            Список словарей {url : text}
    """
    if depth == 0:
        return {}
    
    links_with_text = get_links_with_text(url)

    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        # Рекурсивно вызываю функцию для каждой найденной ссылки на указанной глубине
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[link] = {
            "text": text,
            "children": child_links
        }
    
    return all_links_with_hierarchy

def get_site_structure(starting_url: str = 'https://hbdeadsea.co.il',    depth: int = 5) -> list[dict]:
    """ Возвращает структуру категорий сайта заданной глубины
        @param
            starting_url (str) : стартовая страница для паука
            depth (int) : глубина рекурсии
        @returns
            list[dict({url : text})]

    """
    
    # Запускаю сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Выводим результаты в виде словаря с иерархией
    import json
    
    print(json.dumps(all_links_with_hierarchy, indent=5, ensure_ascii=False))


if __name__ == '__main__':
    """ Start spider """
    get_site_structure()


get_site_structure()
""" Start spider """