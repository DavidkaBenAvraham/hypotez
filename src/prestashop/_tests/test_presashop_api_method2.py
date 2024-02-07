#! /usr/share/projects/hypotez/venv/scripts python
import header
from header import gs



from src.prestashop_api import PrestaAPIV1 as PrestaAPIV2
# https://github.com/DavidkaBenAvraham/prestashop_api
api: PrestaAPIV2 = \
    PrestaAPIV2(gs.prestashop_api['API_DOMAIN'],
    gs.prestashop_api['API_KEY']
    )




print('Get')
res = api.get('products')
for p in res['products']['product']:
    print(p['@id'], p['@xlink:href'])

print('Search')
res = api.get('search', {'query': 'lorem', 'language': 1})
for p in res['products']['product']:
    print(p['@id'], p['@xlink:href'])

print('Add')
data = {'manufacturer': {'active': 1, 'name': 'Sample Manufacturer'}}  # Delete 'name' to get error
res = api.add('manufacturers', data)['manufacturer']
id = res['id']
print(id, res['name'])

print('Add Image')
res = api.add_image('manufacturers/' + id, 'ps_logo.png')  # set exists=True to replace image
print(res)

print('Edit')
data = {'manufacturer': {'id': id, 'name': 'Sample Manufacturer Edited'}}
res = api.edit('manufacturers', data)['manufacturer']
print(res['id'], res['name'])

print('Delete')
res = api.delete('manufacturers/' + res['id'])
print (res)
