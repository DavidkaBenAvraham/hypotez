## \file /src/suppliers/aliexpress/campaign/_experiments/edit_campaign.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.suppliers_list.aliexpress.campaign._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.suppliers_list.aliexpress.campaign._experiments """



""" Редактор рекламной кампании """
...


import header
from pathlib import Path

from src import gs
from src.suppliers.suppliers_list.aliexpress.campaign import AliCampaignEditor
from src.suppliers.suppliers_list.aliexpress.campaign import  process_campaign, process_campaign_category, process_all_campaigns
from src.utils import get_filenames, get_directory_names
from src.utils.printer import pprint

locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}


# campaign_name = "030724_men_summer_fashion"
# category_name = "men_summer_tshirts"

campaign_name = "building_bricks"
category_name = "building_bricks"
a = AliCampaignEditor(campaign_name,'EN','USD')
...


