from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.webpay.webpay_plus.schema import MallTransactionCreateRequestSchema, MallTransactionRefundRequestSchema, MallTransactionCaptureRequestSchema
from transbank.webpay.webpay_plus.request import MallTransactionCreateDetails, MallTransactionCreateRequest, MallTransactionRefundRequest, MallTransactionCaptureRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError

class MallTransaction(object):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS_MALL, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def create(self, buy_order: str, session_id: str, return_url: str, details: MallTransactionCreateDetails):
        try:
            endpoint = MallTransaction.CREATE_ENDPOINT
            request = MallTransactionCreateRequest(buy_order, session_id, return_url, details.details)
            return RequestService.post(endpoint, MallTransactionCreateRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str):
        try:
            endpoint = MallTransaction.COMMIT_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)
    
    def status(self, token: str):
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, token: str, child_buy_order: str, child_commerce_code:str, amount: float):
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(token)
            request = MallTransactionRefundRequest(commerce_code=child_commerce_code, buy_order=child_buy_order,  amount=amount)
            return RequestService.post(endpoint, MallTransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, child_commerce_code: str, token: str, buy_order: str, authorization_code: str, capture_amount: float):
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT.format(token)
            request = MallTransactionCaptureRequest(child_commerce_code, buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, MallTransactionCaptureRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

