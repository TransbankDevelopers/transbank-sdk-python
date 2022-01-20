from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.webpay.oneclick.schema import MallTransactionAuthorizeRequestSchema, MallTransactionRefundRequestSchema, MallTransactionCaptureRequestSchema
from transbank.webpay.oneclick.request import MallTransactionAuthorizeDetails, MallTransactionAuthorizeRequest, MallTransactionRefundRequest, MallTransactionCaptureRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_authorize_error import TransactionAuthorizeError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError

class MallTransaction(object):
    AUTHORIZE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions'
    STATUS_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/capture'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def authorize(self, username: str, tbk_user: str, parent_buy_order: str, details: MallTransactionAuthorizeDetails):        
        try:
            endpoint = MallTransaction.AUTHORIZE_ENDPOINT
            request = MallTransactionAuthorizeRequest(username, tbk_user, parent_buy_order, details.details)
            return RequestService.post(endpoint, MallTransactionAuthorizeRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionAuthorizeError(e.message, e.code)

    def capture(self, child_commerce_code: str, child_buy_order: str, authorization_code: str, capture_amount: float):
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT
            request = MallTransactionCaptureRequest(child_commerce_code, child_buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, MallTransactionCaptureRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def status(self, buy_order: str):
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(buy_order)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, buy_order: str, child_commerce_code: str, child_buy_order: str, amount: float):
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(buy_order)
            request = MallTransactionRefundRequest(child_commerce_code, child_buy_order, amount)
            return RequestService.post(endpoint, MallTransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

