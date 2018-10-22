from enum import Enum
from transbank.onepay import sign

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
    MOCK = Integration("MOCK","https://transbank-onepay-ewallet-mock.herokuapp.com","04533c31-fe7e-43ed-bbc4-1c8ab1538afp")

class Options(object):
    def __init__(self, api_key: str, shared_secret: str):
        self.api_key = api_key
        self.shared_secret = shared_secret

class Signable(object):
    signable_attributes = []

    def signable_data(self):
        signable_data = [getattr(self, item) for item in self.signable_attributes]
        return signable_data

    def sign(self, secret):
        data = sign.concat_for_signing(*self.signable_data())
        return sign.sign_sha256(secret, data)

    def is_valid_signature(self, secret, signature):
        return self.sign(secret) == signature

api_key = "dKVhq1WGt_XapIYirTXNyUKoWTDFfxaEV63-O5jcsdw"
shared_secret = "?XW#WOLG##FBAGEAYSNQ5APD#JF@$AYZ"
integration_type = IntegrationType.TEST
callback_url = "http://no.callback.has/been.set"
app_scheme = None
