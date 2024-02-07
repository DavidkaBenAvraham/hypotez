"""  [File's Description]


 @namespace src
 \package src.prestashop.presta_apis.presta_python_api_v1
\file prestapyt_dict.py
 @section libs imports:
  - __future__ 
  - presta_python_api_v1 
  - xml.etree 
Author(s):
  - Created by Davidka on 10.11.2023 .
"""
from __future__ import print_function
from presta_python_api_v1 import PrestaShopWebServiceDict
from xml.etree import ElementTree


prestashop = PrestaShopWebServiceDict('http://localhost:8080/api',
                                  'API_KEY',)
print(prestashop.get(''))
print(prestashop.head(''))
print(prestashop.get('addresses', 1))
print(prestashop.get('products', 1))

address_data = prestashop.get('addresses', 1)
address_data['address']['firstname'] = 'Robert'
prestashop.edit('addresses', address_data)

address_data = prestashop.get('addresses', options={'schema': 'blank'})
address_data['address'].update({'address1': '1 Infinite Loop',
                                'address2': '',
                                'alias': 'manufacturer',
                                'city': 'Cupertino',
                                'company': '',
                                'deleted': '0',
                                'dni': '',
                                'firstname': 'STEVE',
                                'id_country': '21',
                                'id_customer': '',
                                'id_manufacturer': '1',
                                'id_state': '5',
                                'id_supplier': '',
                                'lastname': 'JOBY',
                                'other': '',
                                'phone': '(800) 275-2273',
                                'phone_mobile': '',
                                'postcode': '95014',
                                'vat_number': ''})
prestashop.add('addresses', address_data)
