## \file /src/suppliers/aliexpress/api/skd/api/rest/AliexpressAffiliateOrderGetRequest.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.suppliers_list.aliexpress.api.skd.api.rest """
"""
Created by auto_sdk on 2021.03.05
"""
from ..base import RestApi


class AliexpressAffiliateOrderGetRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.fields = None
        self.order_ids = None

    def getapiname(self):
        return "aliexpress.affiliate.order.get"

