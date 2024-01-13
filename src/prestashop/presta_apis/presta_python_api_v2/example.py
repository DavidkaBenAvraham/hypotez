"""!  [File's Description]

 
 @section libs imports:
  - presta_python_api_v2 
Author(s):
  - Created by Davidka on 10.11.2023 .
"""
from presta_python_api_v2 import PrestashopApi

# Careful, api calls raise PrestashopError if request fails
api = PrestashopApi('http://localhost:8888/api', 'FRMIF6HLPH1ZCUK39MR9RSTDTJPD2K21')

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
print res
