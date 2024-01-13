from pathlib import Path
from typing import Union
import requests
from PIL import Image

import header
from header import gs, \
            Supplier, start_supplier


supplier_prefix = 'amazon'
s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """

print(" Можно продолжать ")


""" ТЕСТОВЫЙ СЛОВАРЬ """
from dict_scenarios import scenario
s.current_scenario = scenario['Murano Glass']

# -------------- сокращения -------
l = s.reread_locators('product')
d = s.driver
_ = d.execute_locator

s.run_scenario(s.current_scenario)