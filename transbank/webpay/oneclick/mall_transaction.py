from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.oneclick.schema import MallTransactionAuthorizeRequestSchema, MallTransactionRefundRequestSchema, MallTransactionCaptureRequestSchema
from transbank.webpay.oneclick.request import MallTransactionAuthorizeDetails, MallTransactionAuthorizeRequest, MallTransactionRefundRequest, MallTransactionCaptureRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_authorize_error import TransactionAuthorizeError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError

class MallTransaction(WebpayTransaction):
    AUTHORIZE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions'
    STATUS_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/transactions/capture'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.configure_for_testing()
        else: 
            super().__init__(options)

    def authorize(self, username: str, tbk_user: str, parent_buy_order: str, details: MallTransactionAuthorizeDetails):        
        ValidationUtil.has_text_with_max_length(username, ApiConstants.USER_NAME_LENGTH, "username")
        ValidationUtil.has_text_with_max_length(tbk_user, ApiConstants.TBK_USER_LENGTH, "tbk_user")
        ValidationUtil.has_text_with_max_length(parent_buy_order, ApiConstants.BUY_ORDER_LENGTH, "parent_buy_order")
        ValidationUtil.has_elements(details.details, "details")

        for item in details.details:
            ValidationUtil.has_text_with_max_length(item.commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "details.commerce_code")
            ValidationUtil.has_text_with_max_length(item.buy_order, ApiConstants.BUY_ORDER_LENGTH, "details.buy_order")
        try:
            endpoint = MallTransaction.AUTHORIZE_ENDPOINT
            request = MallTransactionAuthorizeRequest(username, tbk_user, parent_buy_order, details.details)
            return RequestService.post(endpoint, MallTransactionAuthorizeRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionAuthorizeError(e.message, e.code)

    def capture(self, child_commerce_code: str, child_buy_order: str, authorization_code: str, capture_amount: float):
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(child_buy_order, ApiConstants.BUY_ORDER_LENGTH, "child_buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT
            request = MallTransactionCaptureRequest(child_commerce_code, child_buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, MallTransactionCaptureRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def status(self, buy_order: str):
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(buy_order)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, buy_order: str, child_commerce_code: str, child_buy_order: str, amount: float):
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(child_buy_order, ApiConstants.BUY_ORDER_LENGTH, "child_buy_order")
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(buy_order)
            request = MallTransactionRefundRequest(child_commerce_code, child_buy_order, amount)
            return RequestService.post(endpoint, MallTransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def configure_for_testing(self):
        return self.configure_for_integration(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_deferred(self):
        return self.configure_for_integration(IntegrationCommerceCodes.ONECLICK_MALL_DEFERRED, IntegrationApiKeys.WEBPAY)
