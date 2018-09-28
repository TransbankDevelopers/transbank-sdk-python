class Onepay(object):

    __api_key = None
    __shared_secret = None
    __callback_url = None
    __app_scheme = None

    @classmethod
    def set_api_key(cls, api_key: str):
        if not isinstance(api_key, str):
            raise ValueError('api_key must be a string')
        cls.__api_key = api_key

    @classmethod
    def set_shared_secret(cls, shared_secret: str):
        if not isinstance(shared_secret, str):
            raise ValueError('shared_secret must be a string')
        cls.__shared_secret = shared_secret

    @classmethod
    def set_callback_url(cls, callback_url: str):
        if not isinstance(callback_url, str):
            raise ValueError('callback_url must be a string')
        cls.__callback_url = callback_url

    @classmethod
    def set_app_scheme(cls, app_scheme: str):
        if not isinstance(app_scheme, str):
            raise ValueError('app_scheme must be a string')
        cls.__app_scheme = app_scheme

    @classmethod
    def get_api_key(cls):
        return cls.__api_key

    @classmethod
    def get_shared_secret(cls):
        return cls.__shared_secret

    @classmethod
    def get_callback_url(cls):
        return cls.__callback_url

    @classmethod
    def get_app_scheme(cls):
        return cls.__app_scheme
