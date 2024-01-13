#! /usr/share/projects/hypotez/venv/scripts python
import header
from header import gs
from header import gs,pprint,jprint


from src.prestashop_api import PrestaAPIV1 as PrestaAPIV1V2
# https://github.com/DavidkaBenAvraham/prestashop_api

api: PrestaAPIV1V2 = \
    PrestaAPIV1V2(gs.prestashop_api['api_domain'],
    gs.prestashop_api['api_key']
    )




print('Add')
data = {'manufacturer': {'active': 1, 'name': 'Sample Manufacturer'}}  # Delete 'name' to get error
res = api.add('manufacturers', data)['manufacturer']
id = res['id']
print(id, res['name'])

print('Add Image')
res = api.add_image('manufacturers/' + id, 'ps_logo.png')  # set exists=True to replace image
pprint(res)

print('Edit')
data = {'manufacturer': {'id': id, 'name': 'Sample Manufacturer Edited'}}
res = api.edit('manufacturers', data)['manufacturer']
pprint(res['id'], res['name'])

print('Delete')
res = api.delete('manufacturers/' + res['id'])
pprint (res)
