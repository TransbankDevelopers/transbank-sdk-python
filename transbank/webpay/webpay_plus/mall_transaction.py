from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.webpay_plus.mall_schema import MallTransactionCreateRequestSchema, MallTransactionRefundRequestSchema, MallTransactionCaptureRequestSchema, \
    MallTransactionIncreaseAmountRequestSchema, MallTransactionIncreaseAuthorizationDateRequestSchema, MallTransactionReversePreAuthorizedAmountRequestSchema, MallTransacionDeferredCaptureHistoryRequestSchema
from transbank.webpay.webpay_plus.request import MallTransacionDeferredCaptureHistoryRequest, MallTransactionCreateDetails, MallTransactionCreateRequest, \
    MallTransactionIncreaseAmountRequest, MallTransactionIncreaseAuthorizationDateRequest, MallTransactionRefundRequest, MallTransactionCaptureRequest, MallTransactionReversePreAuthorizedAmountRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.error.transaction_increase_amount_error import TransactionIncreaseAmountError
from transbank.error.transaction_increase_authorization_date_error import TransactionIncreaseAuthorizationDateError
from transbank.error.transaction_reverse_pre_authorized_amount_error import TransactionReversePreAuthorizedAmountError
from transbank.error.transaction_deferred_capture_history_error import TransactionDeferredCaptureHistoryError

class MallTransaction(WebpayTransaction):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'
    INCREASE_AMOUNT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/amount'
    INCREASE_AUTHORIZATION_DATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/authorization_date'
    REVERSE_PRE_AUTHORIZE_AMOUNT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/reverse/amount'
    DEFERRED_CAPTURE_HISTORY_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/details'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.configure_for_testing()
        else:
            super().__init__(options)

    def create(self, buy_order: str, session_id: str, return_url: str, details: MallTransactionCreateDetails):
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(session_id, ApiConstants.SESSION_ID_LENGTH, "session_id")
        ValidationUtil.has_text_with_max_length(return_url, ApiConstants.RETURN_URL_LENGTH, "return_url")
        ValidationUtil.has_elements(details.details, "details")

        for item in details.details:
            ValidationUtil.has_text_with_max_length(item.commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "details.commerce_code")
            ValidationUtil.has_text_with_max_length(item.buy_order, ApiConstants.BUY_ORDER_LENGTH, "details.buy_order")

        try:
            endpoint = MallTransaction.CREATE_ENDPOINT
            request = MallTransactionCreateRequest(buy_order, session_id, return_url, details.details)
            return RequestService.post(endpoint, MallTransactionCreateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = MallTransaction.COMMIT_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)

    def status(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, token: str, child_buy_order: str, child_commerce_code:str, amount: float):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(child_buy_order, ApiConstants.BUY_ORDER_LENGTH, "child_buy_order")
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(token)
            request = MallTransactionRefundRequest(commerce_code=child_commerce_code, buy_order=child_buy_order,  amount=amount)
            return RequestService.post(endpoint, MallTransactionRefundRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, child_commerce_code: str, token: str, buy_order: str, authorization_code: str, capture_amount: float):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT.format(token)
            request = MallTransactionCaptureRequest(child_commerce_code, buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, MallTransactionCaptureRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def increaseAmount(self, buy_order: str, token: str, authorization_code: str, amount: float, child_commerce_code:str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.INCREASE_AMOUNT_ENDPOINT.format(token)
            request = MallTransactionIncreaseAmountRequest(buy_order, authorization_code, amount, child_commerce_code)
            return RequestService.put(endpoint, MallTransactionIncreaseAmountRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionIncreaseAmountError(e.message, e.code)

    def increaseAuthorizationDate(self, token: str, buy_order: str, authorization_code: str, child_commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.INCREASE_AUTHORIZATION_DATE_ENDPOINT.format(token)
            request = MallTransactionIncreaseAuthorizationDateRequest(buy_order, authorization_code, child_commerce_code)
            return RequestService.put(endpoint, MallTransactionIncreaseAuthorizationDateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionIncreaseAuthorizationDateError(e.message, e.code)

    def reversePreAuthorizedAmount(self, buy_order: str, token: str, authorization_code: str, amount: float, child_commerce_code:str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.REVERSE_PRE_AUTHORIZE_AMOUNT_ENDPOINT.format(token)
            request = MallTransactionReversePreAuthorizedAmountRequest(buy_order, authorization_code, amount, child_commerce_code)
            return RequestService.put(endpoint, MallTransactionReversePreAuthorizedAmountRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionReversePreAuthorizedAmountError(e.message, e.code)

    def deferredCaptureHistory(self, token:str, buy_order: str, child_commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        try:
            endpoint = MallTransaction.DEFERRED_CAPTURE_HISTORY_ENDPOINT.format(token)
            request = MallTransacionDeferredCaptureHistoryRequest(buy_order, child_commerce_code)
            return RequestService.post(endpoint, MallTransacionDeferredCaptureHistoryRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionDeferredCaptureHistoryError(e.message, e.code)

    def configure_for_testing(self):
        return self.configure_for_integration(IntegrationCommerceCodes.WEBPAY_PLUS_MALL, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_deferred(self):
        return self.configure_for_integration(IntegrationCommerceCodes.WEBPAY_PLUS_MALL_DEFERRED, IntegrationApiKeys.WEBPAY)
