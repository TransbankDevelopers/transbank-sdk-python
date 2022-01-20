from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.patpass_by_webpay.schema import TransactionCreateRequestSchema
from transbank.patpass_by_webpay.request import TransactionCreateRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError

class Transaction(object):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.PATPASS_BY_WEBPAY, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def create(self, buy_order: str, session_id: str, amount: float, return_url: str, service_id: str,
               card_holder_id: str,
               card_holder_name: str, card_holder_last_name1: str, card_holder_last_name2: str, card_holder_mail: str,
               cellphone_number: str, expiration_date: str, commerce_mail: str, uf_flag: bool):
        try:
            endpoint = Transaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, amount, return_url, service_id, card_holder_id,
                                           card_holder_name, card_holder_last_name1, card_holder_last_name2,
                                           card_holder_mail, cellphone_number, expiration_date, commerce_mail, uf_flag)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str):
        try:
            endpoint = Transaction.COMMIT_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)
    
    def status(self, token: str):
        try:
            endpoint = Transaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)


