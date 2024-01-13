"""! @ru_brief  Модуль распределения категорий товара.  
@ru_details Модуль переводит категории поставщика `Supplier` в категории `Prestashop`
Изначально все категории строятся из гугл таблиц 
(https://drive.google.com/drive/folders/17qfLRWRt8X4SM-M54OJhZPTi4lIJX1pO?ths=true)
Там довольно сложная иерархия, надо исправлять
@ru_todo Это надо переделывать СРОЧНО!


 @section libs imports:
  - src.categories.category 

@file
"""
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .category import Category
