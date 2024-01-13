"""! @brief   [File's Description]

@namespace src: src
 \package src.suppliers.kualastyle
\file kualastyle_get_site_structure.py
 @section libs imports:
  - requests 
  - bs4 
  - re 
  - json 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import requests
from bs4 import BeautifulSoup
import re

def get_links_with_text(url):
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

def recursive_crawl(url, depth):
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

def get_site_structure():
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 5
    
    # Запускаю сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Выводим результаты в виде словаря с иерархией
    import json
    print(json.dumps(all_links_with_hierarchy, indent=5, ensure_ascii=False))


if __name__ == '__main__':
    get_site_structure()

get_site_structure()