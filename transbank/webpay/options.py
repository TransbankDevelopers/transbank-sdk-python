from transbank.webpay.webpayplus import WebpayPlus


class Options:
    # All the following values could be set from envvars
    DEFAULT_API_KEY = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
    DEFAULT_COMMERCE_CODE = '597055555532'
    DEFAULT_INTEGRATION_TYPE = "TEST"
    DEFAULT_INTEGRATION_TYPE_URL = "https://webpay3gint.transbank.cl/"

    _api_key = None
    _commerce_code = None

    _integration_type = None

    def __init__(self, api_key, commerce_code):
        self._api_key = api_key
        self._commerce_code = commerce_code

    @classmethod
    def default_configuration(cls):
        return Options(cls.DEFAULT_API_KEY, cls.DEFAULT_COMMERCE_CODE)

    @property
    def integration_type(self):
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        self._integration_type = integration_type

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    @property
    def commerce_code(self):
        return self._commerce_code

    @commerce_code.setter
    def commerce_code(self, commerce_code):
        self._commerce_code = commerce_code

    def integration_type_url(self):
        return WebpayPlus.INTEGRATION_TYPES[self.integration_type]
