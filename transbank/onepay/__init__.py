from enum import Enum

api_key = None
shared_secret = None
callback_url = None
app_scheme = None
integration_type = None

class Integration(object):
    __key = None
    __api_base = None
    __app_key = None

    def __init__(self, key: str, api_base: str, app_key: str):
        self.__key = key
        self.__api_base = api_base
        self.__app_key = app_key

    @property
    def key(self):
        return self.__key

    @property
    def api_base(self):
        return self.__api_base

    @property
    def app_key(self):
        return self.__app_key

class IntegrationType(Enum):
    LIVE = Integration("LIVE","https://www.onepay.cl","66535F26-5918-435C-ACAB-F628F4CC65EF")
    TEST = Integration("TEST","https://onepay.ionix.cl","8e279b4e-917d-4cbf-b0e3-9432adefff6a")
    MOCK = Integration("MOCK","http://onepay.getsandbox.com","04533c31-fe7e-43ed-bbc4-1c8ab1538afp")
