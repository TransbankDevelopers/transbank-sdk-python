# encoding: utf-8
import calendar
import http.client
import json

from datetime import datetime
from enum import Enum
from urllib.parse import urlparse

from transbank.onepay.schema import ItemSchema, TransactionCreateRequestSchema, TransactionCreateResponseSchema, SendTransactionResponseSchema

from transbank.onepay.cart import ShoppingCart
from transbank.onepay.error import TransactionCreateError, SignError
from transbank.onepay import sign

from transbank import onepay

class Channel(Enum):
    WEB = "WEB"
    MOBILE = "MOBILE"
    APP = "APP"

class Options(object):
    def __init__(self, api_key: str, shared_secret: str):
        self.api_key = api_key
        self.shared_secret = shared_secret

class TransbankRequestResponse(object):
    signable_attributes = []

    def get_signable_data(self, append_data = []):
        signable_data = [getattr(self, item) for item in self.signable_attributes]
        return signable_data + append_data

class TransactionCreateRequest(TransbankRequestResponse):

    signable_attributes = ['external_unique_number', 'total', 'items_quantity', 'issued_at']

    def __init__(self, external_unique_number, total, items_quantity, issued_at, items,
                 callback_url = None, channel = "WEB", app_scheme = None, options = None):

        self.external_unique_number = external_unique_number
        self.total = total
        self.items_quantity = items_quantity
        self.issued_at = issued_at
        self.items = items
        self.callback_url = callback_url
        self.channel = channel
        self.app_scheme = app_scheme
        self.app_key = onepay.integration_type.value.app_key
        self.api_key = (options or onepay).api_key
        self.generate_ott_qr_code = True
        self.options = options or onepay

    @property
    def signature(self):
        return sign.build_signature_for_transaction_create_request(self, self.options.shared_secret)

class TransactionCreateResponse(TransbankRequestResponse):
    signable_attributes = ['occ', 'external_unique_number', 'issued_at']

    def __init__(self, occ, ott, signature, external_unique_number, issued_at, qr_code_as_base64):
        self.occ = occ
        self.ott = ott
        self.signature = signature
        self.external_unique_number = external_unique_number
        self.issued_at = issued_at
        self.qr_code_as_base64 = qr_code_as_base64

class Transaction(object):

    __SEND_TRANSACTION = "sendtransaction"
    __COMMIT_TRANSACTION = "gettransactionnumber"
    __TRANSACTION_BASE_PATH = '/ewallet-plugin-api-services/services/transactionservice/'

    @classmethod
    def create(cls, shopping_cart: ShoppingCart, channel = None, external_unique_number = None, options = None):

        if (channel != None and channel == Channel.APP and onepay.app_scheme):
            raise TransactionCreateError("You need to set an app_scheme if you want to use the APP channel")

        if (channel != None and channel == Channel.MOBILE and onepay.callback_url):
            raise TransactionCreateError("You need to set valid callback if you want to use the MOBILE channel")

        if not hasattr(shopping_cart, 'items') or (hasattr(shopping_cart, 'items') and not shopping_cart.items):
            raise ValueError("Shopping cart must not be null or empty")

        path = cls.__TRANSACTION_BASE_PATH + cls.__SEND_TRANSACTION
        api_base = onepay.integration_type.value.api_base

        parsed_url = urlparse(api_base)
        if parsed_url.scheme.lower() == "http":
            conn = http.client.HTTPConnection(parsed_url.netloc)
        else:
            conn = http.client.HTTPSConnection(parsed_url.netloc)

        external_unique_number_req = external_unique_number or datetime.utcnow().timestamp() * 1e3

        req = TransactionCreateRequest(external_unique_number_req,
              shopping_cart.total, shopping_cart.item_quantity,
              calendar.timegm(datetime.utcnow().utctimetuple()), shopping_cart.items,
              onepay.callback_url, channel.value , onepay.app_scheme, options)

        try:
            conn.request("POST", path, TransactionCreateRequestSchema().dumps(req).data)
        except Exception:
            raise TransactionCreateError("Could not obtain a response from the service")

        data_response = conn.getresponse().read()
        conn.close()

        transaction_response = SendTransactionResponseSchema().loads(data_response.decode('utf-8')).data

        if transaction_response['response_code'] != "OK":
            raise TransactionCreateError("%s : %s" % (transaction_response['response_code'], transaction_response['description']))

        result = TransactionCreateResponse(**transaction_response['result'])

        if not sign.validate_create_response(result, (options or onepay).shared_secret, result.signature):
            raise TransactionCreateError("The response signature is not valid.", -1)

        return result
