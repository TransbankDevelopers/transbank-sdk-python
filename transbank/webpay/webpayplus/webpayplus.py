import requests
from transbank.webpay.options import *


class WPPMeta(type):
    INTEGRATION_TYPES = {
        "LIVE": "https://webpay3g.transbank.cl/",
        "TEST": "https://webpay3gint.transbank.cl/",
        "MOCK": ""
    }

    _http_client = None
    _api_key = Options.DEFAULT_API_KEY
    _commerce_code = Options.DEFAULT_COMMERCE_CODE
    _integration_type = Options.DEFAULT_INTEGRATION_TYPE
    _integration_type_url = INTEGRATION_TYPES["TEST"]

    def __init__(self, *args, **kwargs):
        pass

    @property
    def api_key(cls):
        return cls._api_key

    @api_key.setter
    def api_key(cls, api_key):
        cls._api_key = api_key

    @classmethod
    def api_key(cls):
        return str(cls._api_key)

    @property
    def commerce_code(cls):
        return cls._commerce_code

    @commerce_code.setter
    def commerce_code(cls, commerce_code):
        cls._commerce_code = commerce_code

    @classmethod
    def commerce_code(cls):
        return cls._commerce_code

    @property
    def integration_type(cls):
        return cls._integration_type

    @integration_type.setter
    def integration_type(cls, integration_type):
        cls._integration_type = integration_type

    @property
    def http_client(cls):
        if cls._http_client is None:
            cls._http_client = requests.Session()
        return cls._http_client

    @http_client.setter
    def http_client(cls, http_client):
        cls._http_client = http_client

    @property
    def integration_type_url(cls, integration_type=None):
        if integration_type is None:
            return cls.INTEGRATION_TYPES[cls._integration_type]
        return cls.INTEGRATION_TYPES[integration_type]

    @classmethod
    def integration_type_url(cls, integration_type=None):
        if integration_type is None:
            return cls.INTEGRATION_TYPES[cls._integration_type]
        return cls.INTEGRATION_TYPES[integration_type]


class WebpayPlus(metaclass=WPPMeta):
    pass
