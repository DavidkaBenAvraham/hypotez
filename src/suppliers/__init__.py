"""! @~russian Модуль `suppliers` oтвечает за все манипуляции с товаром относительно поставщика.

@details 
- для каждого конкретного поставщика есть свои специфичные методы (функции) извлечения информации. 
Эти функции дополняют базовый класс `Supplier` и подключаются через интерфейс  `related_functions`
Методы каждого конкретного поставщика находятся в директориях с именем `supplier_prefix`, 
например: 
`amazon`,`aliexpress`,`morlevi`,...  
- `supplier_prefix` задается во время создания в системе нового поставщика и обычно основывается на сокращении имени или сайта поставщика  


---

## Взаимосвязь сущностей Supplier, Driver, Product
@image html supplier-warehouse-client.png

Modules:
  - .supplier 
 @file
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

from .supplier import Supplier