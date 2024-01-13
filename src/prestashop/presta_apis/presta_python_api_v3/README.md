# Presta Python API v3 Plugin

🙏 The `presta_python_api_v3` plugin is a custom integration for my personal affiliate link management system. It enables integration with various affiliate platforms such as Amazon, eBay, AliExpress, Walmart, Best Buy, and more.

## Acknowledgements

A big thank you to the developer [https://github.com/AiSyS-Next/prestashop](https://github.com/AiSyS-Next/prestashop) for creating this amazing plugin. Their hard work and dedication have been invaluable.

😊

## Disclaimer

Please note that I am simply utilizing an existing solution and integrating it into my own system. The credit for the core functionality and development of the `presta_python_api_v3` plugin goes to the original developer mentioned above.


# Presta Python API v3 Plugin
presta_python_api_v3 is a library for Python to interact with the PrestaShop's Web Service PrestaAPIV3.

Learn more about the Prestashop Web Service from the [Official Documentation](https://devdocs.prestashop-project.org/1.7/webservice/)






## Installation

using pip :
`pip install --ignore-installed git+https://github.com/DavidkaBenAvraham/presta_python_api_v3@master`

the git repo:

```bash
git clone https://github.com/DavidkaBenAvraham/presta_python_api_v3 
cd presta_python_api_v3
pip install . 
```

## Usage

### init api

for json data format

```python
from presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format

PrestaAPIV3: PrestaAPIV3 = PrestaAPIV3(
    url = "https://myprestashop.com",
    api_key="4MV3E41MFR7E3N9VNJE2W5EHS83E2EMI",
    default_lang=1,
    debug=True,
    data_format=PrestaAPIV3Format.JSON,
)
```

for xml data format

```python
from presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format

PrestaAPIV3: PrestaAPIV3 = PrestaAPIV3(
    url = "https://myprestashop.com",
    api_key="4MV3E41MFR7E3N9VNJE2W5EHS83E2EMI",
    default_lang=1,
    debug=True,
    data_format=PrestaAPIV3Format.XML,
)
```

### Test API

test if you webservice run

```python
PrestaAPIV3.ping()
```

### Create Record

```python
data = {
        'tax':{
            'rate' : 3.000,
            'active': '1',
            'name' : {
                'language' : {
                    'attrs' : {'id' : '1'},
                    'value' : '3% tax'
                }
            }
        }
    }

rec = PrestaAPIV3.create('taxes',data)
```
#### Add product image

```python
file_name = 'sample.jpg'

PrestaAPIV3.create_binary('images/products/30',file=file_name , _type='image')
```



### Update record

```python
update_data = {
        'tax':{
            'id' : str(rec['id']),
            'rate' : 3.000,
            'active': '1',
            'name' : {
                'language' : {
                    'attrs' : {'id' : '1'},
                    'value' : '3% tax'
                }
            }
        }
    }

update_rec = PrestaAPIV3.write('taxes',update_data)
```
### Remove record

```python
PrestaAPIV3.unlink('taxes',str(rec['id']))
```

remove many records at once

```python
PrestaAPIV3.unlink('taxes',[2,4,5])
```

### Read

```python
import pprint
result = PrestaAPIV3.read('taxes','2',display='[id,name]')

pprint(result)
```

### Search

```python
 # search the first 3 taxes with 5 in the name 
import pprint
recs = PrestaAPIV3.search('taxes',_filter='[name]=%[5]%',limit='3')

for rec in recs:
    pprint(rec)


# search with id = 3 or id = 5

recs = PrestaAPIV3.search('taxes' ,_filter='[id]=[3 | 5]')
```


## Copyright and License

prestashop is copyright (c) 2023 Aymen Jemi (AISYSNEXT)

prestashop is free software: you can redistribute it and/or modify
it under the terms of the GPLv3 General Public License as
published by the Free Software Foundation, version 3 of
the License .
