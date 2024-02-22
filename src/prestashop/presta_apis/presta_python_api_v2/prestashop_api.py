"""  Prestashop API V2

 @section libs imports:
  - requests 
  - xmltodict 

"""
from src.helpers import logger 
import requests
import xmltodict




class PrestashopError_V2(RuntimeError):
    """! """
    #logger.error("Error in PrestashopApi_V2", RuntimeError)
    pass


class PrestashopApi_V2:
    STATUSES = (200, 201)
    
    def __init__(self, API_DOMAIN, API_KEY):
        self.api_domain = API_DOMAIN
        self.key = API_KEY

    def _get_url(self, resource):
        return self.api_domain + '/' + resource

    def _check_response(self, res, ret):
        if res.status_code not in self.STATUSES:
            raise PrestashopError_V2('Status %s, %s' % (res.status_code, ret))
        return ret

    def _request(self, method, resource, data = None, params = None,  data_format = 'JSON', files=None):
        if data is not None:
            #data = xmltodict.unparse({'prestashop': data}).encode('utf-8')
            data = xmltodict.unparse({'prestashop': data})
        res = requests.request(method, self._get_url(resource), auth=(self.key, ''), params=params, data=data, files=files)
        """! res может вернуться пустой строкой вида '[]'.  """
        return self._check_response(res, xmltodict.parse(res.text)['prestashop'] if not files and res.text and res.text != '[]' else None)

    def add(self, resource, data, data_format = 'JSON'):
        return self._request('POST', resource, data = data, data_format = data_format )

    def add_image(self, resource, fp, exists = False):
        with open(fp, 'rb') as fp:
            return self._request('POST', 'images/' + resource, {'ps_method': 'PUT'} if exists else None,
                                 files={'image': fp})

    def get(self, resource, params=None):
        return self._request('GET', resource = resource, params = params)

    def edit(self, resource, data):
        return self._request('PUT', resource, data=data)

    def delete(self, resource):
        return self._request('DELETE', resource)
