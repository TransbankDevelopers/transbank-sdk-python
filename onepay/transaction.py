# encoding: utf-8
from __future__ import unicode_literals
from enum import Enum
from onepay.onepay import Onepay
from onepay.cart import ShoppingCart

class Channel(Enum):
    WEB = "WEB"
    MOBILE = "MOBILE"
    APP = "APP"

class Options(object):
    def __init__(self, api_key: str, shared_secret: str):
        if not isinstance(api_key, str):
            raise ValueError('api_key must be a string')

        if not isinstance(shared_secret, str):
                raise ValueError('shared_secret must be a string')

        self.api_key = api_key
        self.shared_secret = shared_secret

class Transaction(object):

    @staticmethod
    def create(shopping_cart: ShoppingCart, channel = None, external_unique_number = None, options = None):
        if (channel != None and channel == Channel.APP and Onepay.get_app_scheme):
            raise Exception("You need to set an app_scheme if you want to use the APP channel")

        if (channel != None and channel == Channel.MOBILE and Onepay.get_callback_url):
            raise Exception("You need to set valid callback if you want to use the MOBILE channel")

        if not isinstance(shopping_cart, ShoppingCart) or (isinstance(shopping_cart, ShoppingCart) and not shopping_cart.get_items()):
            raise Exception("Shopping cart is null or empty")
