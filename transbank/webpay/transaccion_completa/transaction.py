from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.transaccion_completa.request import TransactionCreateRequest, TransactionCommitRequest, \
    TransactionRefundRequest, TransactionCaptureRequest, TransactionInstallmentsRequest, TransactionIncreaseAmountRequest, TransactionIncreaseAuthorizationDateRequest, \
    TransactionReversePreAuthorizedAmountRequest
from transbank.webpay.transaccion_completa.schema import TransactionCreateRequestSchema, \
    TransactionCommitRequestSchema, TransactionInstallmentsRequestSchema, TransactionRefundRequestSchema, TransactionCaptureRequestSchema, TransactionIncreaseAmountRequestSchema, \
    TransactionIncreaseAuthorizationDateRequestSchema, TransactionReversePreAuthorizedAmountRequestSchema
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.error.transaction_installments_error import TransactionInstallmentsError
from transbank.error.transaction_increase_amount_error import TransactionIncreaseAmountError
from transbank.error.transaction_increase_authorization_date_error import TransactionIncreaseAuthorizationDateError
from transbank.error.transaction_reverse_pre_authorized_amount_error import TransactionReversePreAuthorizedAmountError
from transbank.error.transaction_deferred_capture_history_error import TransactionDeferredCaptureHistoryError

class Transaction(WebpayTransaction):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'
    INSTALLMENTS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/installments'
    INCREASE_AMOUNT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/amount'
    INCREASE_AUTHORIZATION_DATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/authorization_date'
    REVERSE_PRE_AUTHORIZE_AMOUNT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/reverse/amount'
    DEFERRED_CAPTURE_HISTORY_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/details'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.configure_for_testing()
        else:
            super().__init__(options)

    def create(self, buy_order: str, session_id: str, amount: float, cvv: str, card_number: str, card_expiration_date: str):
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(session_id, ApiConstants.SESSION_ID_LENGTH, "session_id")
        ValidationUtil.has_text_with_max_length(card_number, ApiConstants.CARD_NUMBER_LENGTH, "card_number")
        ValidationUtil.has_text_with_max_length(card_expiration_date, ApiConstants.CARD_EXPIRATION_DATE_LENGTH, "card_expiration_date")

        try:
            endpoint = Transaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, amount, card_number, cvv, card_expiration_date)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str, id_query_installments: str, deferred_period_index: int, grace_period: int):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.COMMIT_ENDPOINT.format(token)
            request = TransactionCommitRequest(id_query_installments, deferred_period_index, grace_period)
            return RequestService.put(endpoint, TransactionCommitRequestSchema().dumps(request), self.options)
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
            return RequestService.post(endpoint, TransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, token: str, buy_order: str, authorization_code: str, capture_amount: float):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = Transaction.CAPTURE_ENDPOINT.format(token)
            request = TransactionCaptureRequest(buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, TransactionCaptureRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def installments(self, token: str, installments_number: int):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.INSTALLMENTS_ENDPOINT.format(token)
            request = TransactionInstallmentsRequest(installments_number)
            return RequestService.post(endpoint, TransactionInstallmentsRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionInstallmentsError(e.message, e.code)

    def increaseAmount(self, token: str, buy_order: str, authorization_code: str, amount: float, commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        ValidationUtil.has_text_with_max_length(commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "commerce_code")
        try:
            endpoint = Transaction.INCREASE_AMOUNT_ENDPOINT.format(token)
            request = TransactionIncreaseAmountRequest(buy_order, authorization_code, amount, commerce_code)
            return RequestService.put(endpoint, TransactionIncreaseAmountRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionIncreaseAmountError(e.message, e.code)

    def increaseAuthorizationDate(self, token: str, buy_order: str, authorization_code: str, commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        ValidationUtil.has_text_with_max_length(commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "commerce_code")
        try:
            endpoint = Transaction.INCREASE_AUTHORIZATION_DATE_ENDPOINT.format(token)
            request = TransactionIncreaseAuthorizationDateRequest(buy_order, authorization_code, commerce_code)
            return RequestService.put(endpoint, TransactionIncreaseAuthorizationDateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionIncreaseAuthorizationDateError(e.message, e.code)

    def reversePreAuthorizedAmount(self, token: str, buy_order: str, authorization_code: str, amount: float, commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        ValidationUtil.has_text_with_max_length(commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "commerce_code")
        try:
            endpoint = Transaction.REVERSE_PRE_AUTHORIZE_AMOUNT_ENDPOINT.format(token)
            request = TransactionReversePreAuthorizedAmountRequest(buy_order, authorization_code, amount, commerce_code)
            return RequestService.put(endpoint, TransactionReversePreAuthorizedAmountRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionReversePreAuthorizedAmountError(e.message, e.code)

    def deferredCaptureHistory(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = Transaction.DEFERRED_CAPTURE_HISTORY_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionDeferredCaptureHistoryError(e.message, e.code)


    def configure_for_testing(self):
        return self.configure_for_integration(IntegrationCommerceCodes.TRANSACCION_COMPLETA, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_deferred(self):
        return self.configure_for_integration(IntegrationCommerceCodes.TRANSACCION_COMPLETA_DEFERRED, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_sin_cvv(self):
        return self.configure_for_integration(IntegrationCommerceCodes.TRANSACCION_COMPLETA_SIN_CVV, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_deferred_sin_cvv(self):
        return self.configure_for_integration(IntegrationCommerceCodes.TRANSACCION_COMPLETA_DEFERRED_SIN_CVV, IntegrationApiKeys.WEBPAY)

