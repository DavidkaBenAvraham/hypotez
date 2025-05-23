## \file /src/suppliers/aliexpress/api/skd/api/rest/AliexpressAffiliateLinkGenerateRequest.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.suppliers_list.aliexpress.api.skd.api.rest """
"""
Created by auto_sdk on 2020.03.09
"""
from ..base import RestApi


class AliexpressAffiliateLinkGenerateRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.promotion_link_type = None
        self.source_values = None
        self.tracking_id = None

    def getapiname(self):
        return "aliexpress.affiliate.link.generate"

