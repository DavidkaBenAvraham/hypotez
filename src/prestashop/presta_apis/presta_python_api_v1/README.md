# presta_python_api_v1 AKA Prestapyt

prestapyt is a library for Python to interact with the PrestaShop's Web Service API.

Learn more about the PrestaShop Web Service from the [Official Prestashop Documentation].

prestapyt is a direct port of the PrestaShop PHP API Client, PSWebServiceLibrary.php

Similar to PSWebServiceLibrary.php, prestapyt is a thin wrapper around the PrestaShop Web Service:
it takes care of making the call to your PrestaShop instance's Web Service,
supports the Web Service's HTTP-based CRUD operations (handling any errors)
and then returns the XML ready for you to work with in Python
(as well as prestasac if you work with scala).

## Installation


FOR hypotez: use pip from this repo with the following command !!! :

    pip install --ignore-installed git+https://github.com/DavidkaBenAvraham/presta_python_api_v1.git

## Usage


### Message as xml
```python
from presta_python_api_v1 import PrestaShopWebService
PrestaAPIV1 = PrestaShopWebService('http://localhost:8080/api', WEBSERVICE_KEY)
```

### Message as dictionary
```python
from prestapyt import PrestaShopWebServiceDict
prestashop = PrestaShopWebServiceDict('http://localhost:8080/api', WEBSERVICE_KEY)
```

### Search

#### Get all addresses
```python
PrestaAPIV1.get('addresses') # will return the same xml message than
PrestaAPIV1.search('addresses')
```
Note: when using PrestaShopWebServiceDict ``prestashop.search('addresses')`` will return a list of ids.


#### Search with filters
```python
PrestaAPIV1.search('addresses', options={'limit': 10})
PrestaAPIV1.search('addresses', options={'display': '[firstname,lastname]', 'filter[id]': '[1|5]'})
```
For additional info [check reference for the options](http://doc.prestashop.com/display/PS14/Cheat+Sheet_+Concepts+Outlined+in+this+Tutorial).

#### Get single address
```python
PrestaAPIV1.get('addresses', resource_id=1) or prestashop.get('addresses/1')
```
returns ElementTree (PrestaShopWebService) or dict (PrestaShopWebServiceDict).

You can use the full api URL

```python
PrestaAPIV1.get('http://localhost:8080/api/addresses/1')
```

#### Head request

```python
PrestaAPIV1.head('addresses')
```

### Manipulate records

#### Delete
```python
PrestaAPIV1.delete('addresses', resource_ids=4)
```

#### Delete many records at once
```python
PrestaAPIV1.delete('addresses', resource_ids=[5,6])
```

#### Add record
```python
PrestaAPIV1.add('addresses', xml)
```

#### Edit record
```python
PrestaAPIV1.edit('addresses', xml)
```

#### Get model blank xml schema
```python
PrestaAPIV1.get('addresses', options={'schema': 'blank'})
```

#### Add product image

```python
file_name = 'sample.jpg'
fd = io.open(file_name, "rb")
content = fd.read()
fd.close()

PrestaAPIV1.add('/images/products/123', files=[('image', file_name, content)])
```

## API Documentation

Documentation for the PrestaShop Web Service can be found on the
PrestaShop wiki: [Using the REST webservice]


## Credits:

Thanks to Prestashop SA for their PHP API Client PSWebServiceLibrary.php

Thanks to Alex Dean for his port of PSWebServiceLibrary.php
to the Scala language, [prestasac] from which I also inspired my library.


## Copyright and License

prestapyt is copyright (c) 2012 Guewen Baconnier

prestapyt is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

prestapyt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public
License along with prestapyt. If not, see [GNU licenses](http://www.gnu.org/licenses/).



[Official Prestashop Documentation]: http://doc.prestashop.com/display/PS14/Using+the+REST+webservice
[Using the REST webservice]: http://doc.prestashop.com/display/PS14/Using+the+REST+webservice
[Prestapyt Source Archives]: https://github.com/guewen/prestapyt/downloads
[prestasac]: https://github.com/orderly/prestashop-scala-client
