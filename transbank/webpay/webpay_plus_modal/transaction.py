from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.webpay_plus_modal.schema import TransactionCreateRequestSchema, TransactionRefundRequestSchema
from transbank.webpay.webpay_plus_modal.request import TransactionCreateRequest, TransactionRefundRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError

class Transaction(WebpayTransaction):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.configure_for_testing()
        else: 
            super().__init__(options)  

    def create(self, buy_order: str, session_id: str, amount: float):
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(session_id, ApiConstants.SESSION_ID_LENGTH, "session_id")
        try:
            endpoint = Transaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, amount)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.COMMIT_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)
    
    def status(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, token: str, amount: float):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.REFUND_ENDPOINT.format(token)
            request = TransactionRefundRequest(amount)
            return RequestService.post(endpoint, TransactionRefundRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def configure_for_testing(self):
        return self.configure_for_integration(IntegrationCommerceCodes.WEBPAY_PLUS_MODAL, IntegrationApiKeys.WEBPAY)
