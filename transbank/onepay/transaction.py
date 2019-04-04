# encoding: utf-8
from datetime import datetime
from enum import Enum
import requests

from transbank.onepay.schema import ItemSchema, TransactionCreateRequestSchema, TransactionCreateResponseSchema, SendTransactionResponseSchema, TransactionCommitRequestSchema, SendCommitResponseSchema

from transbank.onepay.cart import ShoppingCart
from transbank.onepay.error import TransactionCreateError, SignError, TransactionCommitError
from transbank.onepay import Options, Signable

from transbank import onepay

class Channel(Enum):
    WEB = "WEB"
    MOBILE = "MOBILE"
    APP = "APP"

class TransactionCreateRequest(Signable):

    signable_attributes = ['external_unique_number', 'total', 'items_quantity', 'issued_at', 'callback_url']

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
        self.generate_ott_qr_code = True
        self.options = options or onepay
        self.api_key = self.options.api_key
        if self.options.commerce_logo_url is not None:
            self.commerce_logo_url = self.options.commerce_logo_url
        if self.options.qr_width_height is not None:
            self.qr_width_height = self.options.qr_width_height

    @property
    def signature(self):
        return self.sign(self.options.shared_secret)

class TransactionCreateResponse(Signable):
    signable_attributes = ['occ', 'external_unique_number', 'issued_at']

    def __init__(self, occ, ott, signature, external_unique_number, issued_at, qr_code_as_base64):
        self.occ = occ
        self.ott = ott
        self.signature = signature
        self.external_unique_number = external_unique_number
        self.issued_at = issued_at
        self.qr_code_as_base64 = qr_code_as_base64

class TransactionCommitRequest(Signable):

    signable_attributes = ['occ', 'external_unique_number', 'issued_at']

    def __init__(self, occ, external_unique_number, issued_at, options = None):
        self.occ = occ
        self.external_unique_number = external_unique_number
        self.issued_at = issued_at
        self.app_key = onepay.integration_type.value.app_key
        self.api_key = (options or onepay).api_key
        self.options = options or onepay

    @property
    def signature(self):
        return self.sign(self.options.shared_secret)

class TransactionCommitResponse(Signable):
    signable_attributes = ['occ', 'authorization_code', 'issued_at', 'amount', 'installments_amount', 'installments_number', 'buy_order']

    def __init__(self, occ, authorization_code, signature, transaction_desc, buy_order, issued_at, amount, installments_amount, installments_number):
        self.occ = occ
        self.authorization_code = authorization_code
        self.signature = signature
        self.transaction_desc = transaction_desc
        self.buy_order = buy_order
        self.issued_at = issued_at
        self.amount = amount
        self.installments_amount = installments_amount
        self.installments_number = installments_number

class Transaction(object):

    __SEND_TRANSACTION = "sendtransaction"
    __COMMIT_TRANSACTION = "gettransactionnumber"
    __TRANSACTION_BASE_PATH = '/ewallet-plugin-api-services/services/transactionservice/'

    @classmethod
    def create(cls, shopping_cart: ShoppingCart, channel = Channel.WEB, external_unique_number = None, options = None):

        if (channel != None and channel == Channel.APP and not onepay.app_scheme):
            raise TransactionCreateError("You need to set an app_scheme if you want to use the APP channel")

        if (channel != None and channel == Channel.MOBILE and not onepay.callback_url):
            raise TransactionCreateError("You need to set valid callback if you want to use the MOBILE channel")

        if not hasattr(shopping_cart, 'items') or (hasattr(shopping_cart, 'items') and not shopping_cart.items):
            raise ValueError("Shopping cart must not be null or empty")

        path = cls.__TRANSACTION_BASE_PATH + cls.__SEND_TRANSACTION
        api_base = onepay.integration_type.value.api_base

        external_unique_number_req = external_unique_number or int(datetime.now().timestamp() * 1000)
        options = Options.build(options)

        req = TransactionCreateRequest(external_unique_number_req,
              shopping_cart.total, shopping_cart.item_quantity,
              int(datetime.now().timestamp()), shopping_cart.items,
              onepay.callback_url, (channel or Channel.WEB).value , onepay.app_scheme, options)

        data_response = requests.post(api_base + path, data = TransactionCreateRequestSchema().dumps(req).data).text

        transaction_response = SendTransactionResponseSchema().loads(data_response).data

        if transaction_response['response_code'] != "OK":
            raise TransactionCreateError("%s : %s" % (transaction_response['response_code'], transaction_response['description']))

        result = TransactionCreateResponse(**transaction_response['result'])

        if not result.is_valid_signature((options or onepay).shared_secret, result.signature):
            raise TransactionCreateError("The response signature is not valid.", -1)

        return result

    @classmethod
    def commit(cls, occ, external_unique_number, options = None):

        path = cls.__TRANSACTION_BASE_PATH + cls.__COMMIT_TRANSACTION
        api_base = onepay.integration_type.value.api_base

        req = TransactionCommitRequest(occ, external_unique_number, int(datetime.now().timestamp()), options)

        data_response = requests.post(api_base + path, data = TransactionCommitRequestSchema().dumps(req).data).text

        transaction_response = SendCommitResponseSchema().loads(data_response).data

        if transaction_response['response_code'] != "OK":
            raise TransactionCommitError("%s : %s" % (transaction_response['response_code'], transaction_response['description']))

        result = TransactionCommitResponse(**transaction_response['result'])

        if not result.is_valid_signature((options or onepay).shared_secret, result.signature):
            raise TransactionCommitError("The response signature is not valid.", -1)

        return result
