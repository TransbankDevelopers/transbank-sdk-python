# encoding: utf-8
from __future__ import unicode_literals
from enum import Enum

class Integration(object):
    __key = None
    __api_base = None
    __app_key = None

    def __init__(self, key: str, api_base: str, app_key: str):
        self.__key = key
        self.__api_base = api_base
        self.__app_key = app_key

    def get_key(self):
        return self.__key

    def get_api_base(self):
        return self.__api_base

    def get_app_key(self):
        return self.__app_key


class IntegrationType(Enum):
    LIVE = Integration("LIVE","https://www.onepay.cl","66535F26-5918-435C-ACAB-F628F4CC65EF")
    TEST = Integration("TEST","https://onepay.ionix.cl","8e279b4e-917d-4cbf-b0e3-9432adefff6a")
    MOCK = Integration("MOCK","http://onepay.getsandbox.com","04533c31-fe7e-43ed-bbc4-1c8ab1538afp")

class Onepay(object):
    __api_key = None
    __shared_secret = None
    __callback_url = None
    __app_scheme = None
    __integration_type = None

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
    def set_integration_type(cls, integration_type: Enum):
        if not isinstance(integration_type, IntegrationType):
            raise ValueError('integration_type must be an enum of IntegrationType')
        cls.__integration_type = integration_type

    @classmethod
    def get_current_integration_type(cls):
        return cls.__integration_type

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
