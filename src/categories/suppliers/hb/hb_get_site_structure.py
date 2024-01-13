"""! @ru_brief Строит структу сайта

@section libs imports:
  - typing 
  - src.gs 
  - src.helpers 
  - src.io_interface 
  - src.prestashop 
  - requests 
  - bs4 
  - re 
  - json 

"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

# ---------------------------------
from typing import Union
from src.settings import gs
from src.helpers import  logger, logs_and_errors_decorator, jprint, pprint
from src.io_interface import j_loads, j_dumps
from src.prestashop import Product as PrestaProduct, Category as PrestaCategory
# ---------------------------------

import requests
from bs4 import BeautifulSoup
import re

def get_links_with_text(url) -> Union[dict, False]:
    """@brief Возвращает ссылки на категории со страницы
    @param str `url` URL страницы для парсинга категорий
    @returns dict|False Словарь собранных категорий | False В случае неудачи
    @var requests `response`   Ответ сервера
    @var BeautifulSoup `soup`   HTML парсер результата, полученного в response
    @var list[str] `links`   Найденные в супе ссылки
    @var dict `links_with_text_dict`  Создаю словарь, где ключ - это ссылка, а значение - текст ссылки
    \todo Проверить, что находится в links_with_text_dict

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
    links_with_text_dict = {link['href']: link.text.strip() for link in links if re.match(r'^https://hbdeadsea\.co\.il/product-category', link['href'])}
    
    return links_with_text_dict

def recursive_crawl(url, depth) -> list[dict]:
    """ Рекурсивный обход ссылок на категории
        @param str `url` стартовый URL
        @param int `depth`  глубина рекурсии 
        @returns list Список словарей {url : text}
        @var list[dict({url:text})]) `links_with_text`  Список ссылок, поуцченных от get_links_with_text(url)
        @var list[dict({url:text})] `all_links_with_hierarchy`  Дерево ссылок

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
        @param str `starting_url`  стартовая страница для паука
        @param int `depth` глубина рекурсии
        @returns list[dict({url:text})] Список категорий
        @var list[dict({url:text})] `all_links_with_hierarchy`  Дерево ссылок, полученных от паука
        
    """
    
    # Запускаю сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Выводим результаты в виде словаря с иерархией
    import json
    
    print(json.dumps(all_links_with_hierarchy, indent=5, ensure_ascii=False))


if __name__ == '__main__':
    """! Start spider """
    get_site_structure()


get_site_structure()
"""! Start spider """