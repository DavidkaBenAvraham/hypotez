## \file /src/suppliers/suppliers_list/aliexpress/affiliated_products_generator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.suppliers_list.aliexpress 
	:platform: Windows, Unix
	:synopsis:

"""


import asyncio
from datetime import datetime
import html
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import List

from src.logger.logger import logger
from src import gs
from src.suppliers.suppliers_list.aliexpress import AliApi
from src.suppliers.suppliers_list.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator 
from src.suppliers.suppliers_list.aliexpress.utils.ensure_https import ensure_https
from src.endpoints.prestashop.product_fields import ProductFields as f
from src.utils.image import save_image_from_url_async 
from src.utils.video import save_video_from_url
from src.utils.file import (read_text_file,
                        get_filenames_from_directory,
                        get_directory_names,
                        save_text_file
                        )
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger


class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs.
    For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`.
    """
    ...
    language:str = None
    currency:str = None
    def __init__(self,
                 language: str | dict = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Initializes the AliAffiliatedProducts class.
        Args:
            language: Language for the campaign (default 'EN').
            currency: Currency for the campaign (default 'USD').
        """
        ...
        if not language or not currency:
            logger.critical(f"No language, currency !")
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency
        


    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Processes a list of product IDs or URLs and returns a list of products with affiliate links and saved images.

        Args:
            campaign (SimpleNamespace): The promotional campaign data.
            category_name (str): The name of the category to process.
            prod_ids (list[str]): List of product URLs or IDs.

        Returns:
            list[SimpleNamespace]: A list of processed products with affiliate links and saved images.

        Example:
            >>> campaign = SimpleNamespace(category={})
            >>> category_name = "electronics"
            >>> prod_ids = ["http://example.com/product1", "http://example.com/product2"]
            >>> products = campaign.process_affiliate_products(category_name, prod_ids)
            >>> for product in products:
            ...     print(product.product_title)
            "Product 1 Title"
            "Product 2 Title"

        Raises:
            Exception: If the category name is not found in the campaign.

        Notes:
            - Fetches page content from URLs.
            - Handles affiliate links and image/video saving.
            - Generates and saves campaign data and output files.

        Flowchart:
        ┌───────────────────────────────────────────────┐
        │ Start                                         │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌─────────────────────────────────────────────────────────┐
        │ Try to get category from campaign using `category_name` │
        └─────────────────────────────────────────────────────────┘
                            │
                            ┴───────────────────────────────────────────┐
                            │                                           │
                            ▼                                           ▼
        ┌──────────────────────────────────────────────────────┐
        │ Campaign Category found: Initialize paths,           │
        │ set promotional URLs, and process products           │
        └──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ No category found: Create default category    │
        │ and initialize paths, set promotional URLs,   │
        │ and process products                          │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Initialize paths and prepare data structures  │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Process products URLs to get affiliate links  │
        └───────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────────────────────┐
                │                                       │
                ▼                                       ▼
        ┌─────────────────────────────────────────────┐
        │ No affiliate links found: Log warning       │
        └─────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Retrieve product details for affiliate URLs   │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Process each product and save images/videos   │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Prepare and save final output data            │
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ Return list of affiliated products            │    
        └───────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────────────┐
        │ End                                           │
        └───────────────────────────────────────────────┘


        """
        ...

        _promotion_links: list = []
        _prod_urls: list = []
        normilized_prod_urls = ensure_https(prod_ids) # <- привожу к виду `https://aliexpress.com/item/<product_id>.html`
        print_flag = '' # <- флаг переключения печати в одну строку


        for prod_url in normilized_prod_urls:
            _links = super().get_affiliate_links(prod_url)
            if _links:
                _links = _links[0]
            if hasattr(_links, 'promotion_link'):
                _promotion_links.append(_links.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f"found affiliate for {_links.promotion_link}")
                # pprint(              # <- печать в одну строку
                #     f'found affiliate for: {_links.promotion_link}', end=print_flag)
                # print_flag = '\r'
            else:
                continue

        if not _promotion_links:
            logger.warning(
                f'No affiliate products returned {prod_ids=}/n', None, None)
            return

        _affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(
            _prod_urls)
        if not _affiliated_products:
            return
        
        affiliated_products_list:list[SimpleNamespace] = []
        product_titles:list = []
        for product, promotion_link in zip(_affiliated_products, _promotion_links):
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            image_path = Path(category_root) / 'images' / \
                f"{product.product_id}.png"
            await save_image_from_url(product.product_main_image_url, image_path)
            #pprint(f"Saved image for {product.product_id=}", end=print_flag)
            logger.info(f"Saved image for {product.product_id=}")
            
            product.local_image_path = str(image_path)
            if len(product.product_video_url) > 1:
                parsed_url:Path = urlparse(product.product_video_url)
                suffix:str = Path(parsed_url.path).suffix

                video_path:Path = Path(category_root) / 'videos' / \
                    f'{product.product_id}{suffix}'
                await save_video_from_url(product.product_video_url, video_path)
                product.local_video_path = str(video_path)
                logger.info(f"Saved video for {product.product_id=}")

            #product.tags = f"#{f_normalizer.simplify_string(product.first_level_category_name)}, #{f_normalizer.simplify_string(product.second_level_category_name)}"
            logger.info(f"{product.product_title}")
            j_dumps(product, Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json')
            #pprint(f"Dumped in {Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json'} ")

            affiliated_products_list.append(product)
        #print_flag = 'newline'
        product_titles_path:Path = category_root / f"{self.language}_{self.currency}" / 'product_titles.txt'
        await save_text_file(product_titles, product_titles_path)
        return affiliated_products_list


