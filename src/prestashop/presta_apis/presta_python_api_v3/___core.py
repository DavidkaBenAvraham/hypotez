"""! 
Prestashop is a Python library to interact with PrestaShop's Web Service API.

:copyright: (c) 2023 Aymen Jemi
:copyright: (c) 2023 AISYSNEXT
:license: GPLv3, see LICENSE for more details
"""



import os
from enum import Enum


from http.client import HTTPConnection
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest

from packaging import version

from .exceptions import PrestaShopError,PrestaShopAuthenticationError
from .utils import dict2xml
from .utils import base64_to_tmpfile


class Format(Enum):
    """!Data types return (JSON,XML)

    Args:
        Enum (int): 1 => JSON, 2 => XML
    """
    JSON = 1
    XML = 2


class Prestashop():
    """! Interact with Prestashop webservice API, using JSON and XML for message

    Raises:
        PrestaShopAuthenticationError: Authentication error.
        when: wrong api key or api key not exist.
        PrestaShopError: Generic PrestaShop WebServices error .

    Example:  
        Usage:
        ```python
        
            init api
            for json data format

            from prestashop import Prestashop, Format

            api = Prestashop(
                url = "https://myprestashop.com",
                API_KEY="4MV3E41MFR7E3N9VNJE2W5EHS83E2EMI",
                default_lang=1,
                debug=True,
                data_format=Format.JSON,
            )
            for xml data format

            from prestashop import Prestashop, Format

            api = Prestashop(
                url = "https://myprestashop.com",
                API_KEY="4MV3E41MFR7E3N9VNJE2W5EHS83E2EMI",
                default_lang=1,
                debug=True,
                data_format=Format.XML,
            )
            Test API
            test if you webservice run

            api.ping()
            Create Record
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

            rec = api.create('taxes',data)
            Add product image
            file_name = 'sample.jpg'

            api.create_binary('images/products/30',file=file_name , _type='image')
            Update record
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

            update_rec = api.write('taxes',update_data)
            Remove record
            api.unlink('taxes',str(rec['id']))
            remove many records at once

            api.unlink('taxes',[2,4,5])
            Read
            import pprint
            result = api.read('taxes','2',display='[id,name]')

            pprint(result)
            Search
             # search the first 3 taxes with 5 in the name 
            import pprint
            recs = api.search('taxes',_filter='[name]=%[5]%',limit='3')

            for rec in recs:
                pprint(rec)


            # search with id = 3 or id = 5

            recs = api.search('taxes' ,_filter='[id]=[3 | 5]')

            #######################################################################         
            
            from prestashop import Prestashop, Format

            api = Prestashop(
                url = "https://myprestashop.com",
                API_KEY="4MV3E41MFR7E3N9VNJE2W5EHS83E2EMI",
                default_lang=1,
                debug=True,
                data_format=Format.JSON,
            )

            api.ping()

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

            # create tax record
            rec = api.create('taxes',data)

            # update the same tax record

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

            update_rec = api.write('taxes',update_data)

            # remove this tax
            api.unlink('taxes',str(rec['id']))

            # search the first 3 taxes with 5 in the name 
            import pprint
            recs = api.search('taxes',_filter='[name]=%[5]%',limit='3')

            for rec in recs:
                pprint(rec)

            # create binary (product image)

            api.create_binary('images/products/22','img.jpeg','image')
            # or
            api.create_binary('images/products/22','img.jpeg','image')
    
    ```
    """
    API_KEY = ''
    API_DOMAIN = ''
    client = None
    debug = False
    lang = None
    data_format = Format.JSON
    ps_version = ''

    def __init__(self, API_DOMAIN:str, API_KEY:str, data_format=Format.JSON, default_lang:str=None,session:Session=None,debug:bool=False) -> None:
        """! Prestashop class

        Args:
            url (str): url of your shop (https://myprestashop.com)
            API_KEY (str): api key generate from prestashop 
            https://devdocs.prestashop-project.org/1.7/webservice/tutorials/creating-access/
            data_format (Format, optional): default data format (Format.JSON or Format.XML). Defaults to Format.JSON.
            default_lang (str, optional): default language id (1). Defaults to None.
            @note я могу выбирать язык из престашоп на котором я получу `response`
            session (Session, optional): requests.Session() for old sessing. Defaults to None.
            debug (bool, optional): activate debug mode. Defaults to False.
        """
        
        self.API_DOMAIN = API_DOMAIN
        self.API_KEY = API_KEY
        self.debug = debug
        self.lang = default_lang
        self.data_format = data_format


        # fix url 
        if not self.API_DOMAIN.endswith('/'):
            self.API_DOMAIN += '/'
        if not self.API_DOMAIN.endswith('/api/'):
            self.API_DOMAIN += 'api/'


        if session is None:
            self.client = Session()
        else:
            self.client = session

        if not self.client.auth:
            self.client.auth = (self.API_KEY , '')
        
        
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        self.ps_version = response.headers.get('psws-version')

    def ping(self):
        """ Test if webservice work perfectly else raise error

        Returns:
            bool: Result of ping test
        """
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        content = {
            "errors": [
                {
                    "code": 0,
                    "message": "Ping not working "
                }
            ]
        }

        return self._error(response.status_code,content)

    def _error(self,status_code,content):
        message_by_code = {204: 'No content',
                           400: 'Bad Request',
                           401: 'Unauthorized',
                           404: 'Not Found',
                           405: 'Method Not Allowed',
                           500: 'Internal Server Error',
                           }
        if status_code in (200, 201):
            return True
        elif status_code == 401:
            # the content is empty for auth errors
            raise PrestaShopAuthenticationError(
                message_by_code[status_code],
                status_code
            )
        elif status_code in message_by_code:
            ps_error_code, ps_error_msg = self._parse_error(content)
            raise PrestaShopError(
                message_by_code[status_code],
                status_code,
                ps_error_msg=ps_error_msg,
                ps_error_code=ps_error_code,
            )
        else:
            ps_error_code, ps_error_msg = self._parse_error(content)
            raise PrestaShopError(
                'Unknown error',
                status_code,
                ps_error_msg=ps_error_msg,
                ps_error_code=ps_error_code,
            )
        
    def _parse_error(self,content):
        if self.data_format == Format.JSON:
            code = content['errors'][0]['code']
            msg = content['errors'][0]['message']
            return (code, msg)

        error_answer = self._parse(content)
        if isinstance(error_answer, dict):
            error_content = (error_answer
                             .get('prestashop', {})
                             .get('errors', {})
                             .get('error', {})
                             )
            if isinstance(error_content, list):
                error_content = error_content[0]
            code = error_content.get('code')
            message = error_content.get('message')
        elif isinstance(error_answer, type(ElementTree.Element(None))):
            error = error_answer.find('errors/error')
            code = error.find('code').text
            message = error.find('message').text
        return (code, message)
    
    def _prepare(self,url,params):
        req = PreparedRequest()
        req.prepare_url(url , params)
        return req.url

    #def _exec(self,resource,_id=None,ids=None, method='GET',data=None,_headers=None, display: str = 'full' ,_filter=None,sort=None,limit=None):
    def _exec(self,
              resource,
              _id: int=None,
              method='GET',
              data=None,
              headers:dict=None,
              params: dict = {'display':'full', 
                              'filter':None, 
                              'sort':None, 
                              'limit':None, 
                              'language':None, 
                              'io_format' : 'JSON' , 
                              'output_format' : 'JSON'} ):
        
        #params = params

        # if self.lang:
        #     params.update({'language' : self.lang})

        # if self.data_format == Format.JSON:
        #     params.update({'io_format' : 'JSON' , 'output_format' : 'JSON'})
        
        #params.update(params)
        # if display:
        #     params.update({'display' : display})

        """! @todo Переделать парсер параметров """

        # if _filter:
        #     lst = _filter.split('=',1)
        #     key = 'filter{}'.format(lst[0])
        #     params.update({key : lst[1]})
        # if sort:
        #     params.update({'sort' : sort})
        # if limit:
        #     params.update({'limit' : limit})

      

        _url = fr'{self.API_DOMAIN}{resource}/{_id}' if _id else fr'{self.API_DOMAIN}{resource}'

        
        # if ids:
        #     params.update({'id' : ids})

        url = self._prepare (_url, params)

        if self.debug:
            HTTPConnection.debuglevel = 1


        if self.data_format == Format.JSON:
            _headers = {'Content-Type': 'application/json'}
            if not headers:
                headers = _headers
            else:
                headers.update(_headers)
                
            response = self.client.request(
                method=method,
                url=url,
                data=data,
                headers=headers
            )

            if response.content == b'' and response.status_code == 200:
                """! Empty content """
                
                self._error(response.status_code,response.json())
                return True
                """! @todo проверить """
            return response.json()
        
        headers = {'Content-Type': 'text/xml'}
        if _headers:
            headers = _headers
        response = self.client.request(
                method=method,
                url=url,
                data=data,
                headers=headers
        )

        if response.content == b'' and response.status_code == 200:
            """! вернулся пустой `response` """
            self._error(response.status_code,response.content)
            
            return False
        
        
        return self._parse(response.content)

    def _parse(self, content):
        """Parse the response of the webservice.

        :param content: response from the webservice
        :return: an ElementTree of the content
        """
        if not content:
            raise PrestaShopError('HTTP response is empty')

        try:
            parsed_content = ElementTree.fromstring(content)
        except ExpatError as err:
            raise PrestaShopError(
                'HTTP XML response is not parsable : %s' % (err,)
            )
        except ElementTree.ParseError as e:
            raise PrestaShopError(
                'HTTP XML response is not parsable : %s. %s' %
                (e, content[:512])
            )

        return parsed_content
    
    def search(self,resource, filter:str = None, params: dict = {'display':'full', 
                              'filter':None, 
                              'sort':None, 
                              'limit':None, 
                              'language':None, 
                              'io_format' : Format.JSON , 
                              'output_format' : Format.JSON} ):
        
        """! search from prestashop with options, for more details check the official doc \n
        https://devdocs.prestashop-project.org/1.7/webservice/tutorials/advanced-use/additional-list-parameters/

        
            @param resource (str): resource to search ( taxes,customers,products ...)
            @param     display (str, optional): display parameter (full | [field1,field2]). Defaults to 'full'.
            @param _filter (str, optional): filter parameter ([id]=[1|5] , [name]=[app]%). Defaults to None.
            @param  sort (str, optional): sort parameter ([{fieldname}_{ASC|DESC}] ,[lastname_ASC,id_DESC] ). Defaults to None.
            @param limit (str, optional): limit parameter ('offset,limit' , '9,2' , '5'). Defaults to None.

            @returns dict : result of search
        """
        if filter: params['filter'] = f'filter{}'
            
        return self._exec (resource = resource, method = 'GET', params = params )

    def read(self,resource:str, _id:str = None, _reference: str = None, params: dict = {}) -> dict:
        """get one result from prestashop with options .
        for more details check the official doc \n
        https://devdocs.prestashop-project.org/1.7/webservice/tutorials/advanced-use/additional-list-parameters/

        Args:
            resource (str): resource to search ( taxes,customers,products ...)
            _id (str, optional): the id if you wan one record. Defaults to None.
            display (str, optional): display parameter (full | [field1,field2]). Defaults to 'full'.
        Returns:
            dict : result of get request
        """


        if version.parse(self.ps_version)  <= version.parse('1.7.6.8') :
            display = None


        return self._exec (resource, _id, 'GET', params  )

    def write(self,resource:str,data:dict):
        """update record from prestashop

        Args:
            resource (str): resource to search ( taxes,customers,products ...)
            data (dict): data in dict format (
                    data = {
                        'tax':{
                            'id': 2,
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
        )

        Returns:
            dict: the updated record.
        """
        data  = {'prestashop' : data}
        _data = dict2xml(data)
        return self._exec(resource=resource,method='PUT',data=_data,display=None)

    def unlink(self,resource:str,ids:list):
        """remove one or multiple records

        Args:
            resource (str): resource to search ( taxes,customers,products ...)
            ids (list[int] | tuple(int) | str): list|tuple|str of ids to remove. ([1,3,9] , [9] , '3')

        Returns:
            boolean: result of remove (True,False)
        """
        if isinstance(ids , (tuple,list)):
            resource_ids = ','.join([str(id) for id in ids])
            resource_ids = '[{}]'.format(resource_ids)
            return self._exec(resource=resource ,ids=resource_ids, method='DELETE' , display=None)
            
        else:
            return self._exec(resource=resource ,ids=ids, method='DELETE' , display=None)
    
    def create(self,resource:str,data:dict):
        """create record 

        Args:
            resource (str): resource to search ( taxes,customers,products ...).
            data (dict): data in dict format (
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
        )

        Returns:
            dict: record added.
        """


        data  = {'prestashop' : data}
        _data = dict2xml(data)
        return self._exec(resource=resource,data=_data,method='POST',display=None)

    def create_binary(self,resource:str, file:str,_type:str = 'image',file_name=None):
        """create binary record

        Args:
            resource (str): resource to add file ( 'images/products/22' ...).
            files (str):  a path of file ('image.png', 'image.jpg') or binary.
            _type (str, optional): a type of file (image,pdf ...) Default to 'image'
            file_name (str, optinal): name of file in case of base64. Default to None
        """

        params = {}

        if self.lang:
            params.update({'language' : self.lang})
        
        if self.data_format == Format.JSON:
            params.update({'io_format' : 'JSON' , 'output_format' : 'JSON'})
    

        _url = '{}{}'.format(self.url,resource)
        url = self._prepare(_url,params)


        if os.path.exists(file):

            _file = {_type : open(file,'rb')}

        elif isinstance(file ,str):
            _file = {_type : open(base64_to_tmpfile(file,file_name),'rb') }
        else:
            raise PrestaShopError('File not found',404)


        response = self.client.post(
            url=url,
            files=_file
        )

        if response.status_code == 200:
            return True
        return False

    def get_image_product(self,product_id:int,image_id:int):
        """ get product image from prestashop

        Args:
            product_id (int): the id of product
            image_id (int): the id of image
        
        Returns:
            binary: image of product
        
        Raise:
            PrestaShopError: 'This image id does not exist'
        """
        params = {}

        if self.lang:
            params.update({'language' : self.lang})

        if self.data_format == Format.JSON:
            params.update({'io_format' : 'JSON' , 'output_format' : 'JSON'})

        _url = f'{self.url}images/products/{product_id}/{image_id}'
        _url = self._prepare(_url,params)
        
        response = self.client.request(
            method='GET',
            url = _url,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            return response.content
        
        self._error(response.status_code,response.json())
        return response.json()