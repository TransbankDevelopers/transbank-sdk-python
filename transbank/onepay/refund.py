from datetime import datetime
import requests

from transbank import onepay

from transbank.onepay.schema import RefundCreateRequestSchema, SendRefundResponseSchema
from transbank.onepay.error import RefundCreateError
from transbank.onepay import Options, Signable

class RefundCreateRequest(Signable):

    signable_attributes = ['occ', 'external_unique_number', 'authorization_code', 'issued_at' ,'nullify_amount']

    def __init__(self, occ, external_unique_number, authorization_code, issued_at, nullify_amount, options = None):
        self.occ = occ
        self.external_unique_number = external_unique_number
        self.authorization_code = authorization_code
        self.nullify_amount = nullify_amount
        self.app_key = onepay.integration_type.value.app_key
        self.api_key = (options or onepay).api_key
        self.options = options or onepay
        self.issued_at = issued_at

    @property
    def signature(self):
        return self.sign(self.options.shared_secret)

class RefundCreateResponse(Signable):
    signable_attributes = ['occ', 'external_unique_number', 'reverse_code', 'issued_at']

    def __init__(self, occ, external_unique_number, reverse_code, issued_at, signature):
        self.occ = occ
        self.external_unique_number = external_unique_number
        self.reverse_code = reverse_code
        self.issued_at = issued_at
        self.signature = signature

class Refund(object):
    __CREATE_REFUND = 'nullifytransaction'
    __TRANSACTION_BASE_PATH = '/ewallet-plugin-api-services/services/transactionservice/'

    @classmethod
    def create(cls, amount, occ, external_unique_number, authorization_code, options = None):
        req = RefundCreateRequest(occ, external_unique_number,authorization_code, int(datetime.now().timestamp()), amount, options)

        api_base = onepay.integration_type.value.api_base + cls.__TRANSACTION_BASE_PATH

        data_response = requests.post(api_base + cls.__CREATE_REFUND, data = RefundCreateRequestSchema().dumps(req).data).text

        refund_response = SendRefundResponseSchema().loads(data_response).data

        if refund_response['response_code'] != "OK":
            raise RefundCreateError("%s : %s" % (refund_response['response_code'], refund_response['description']))

        result = RefundCreateResponse(**refund_response['result'])

        if not result.is_valid_signature((options or onepay).shared_secret, result.signature):
            raise RefundCreateError("The response signature is not valid.", -1)

        return result
