from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.transaccion_completa.mall_request import TransactionCreateRequest, TransactionCommitRequest, \
    TransactionRefundRequest, TransactionCaptureRequest, TransactionInstallmentsRequest
from transbank.webpay.transaccion_completa.mall_schema import TransactionCreateRequestSchema, \
    TransactionCommitRequestSchema, TransactionInstallmentsRequestSchema, TransactionRefundRequestSchema, TransactionCaptureRequestSchema
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.error.transaction_installments_error import TransactionInstallmentsError

class MallTransaction(WebpayTransaction):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'
    INSTALLMENTS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/installments'

    def __init__(self, options: WebpayOptions):
        super().__init__(options)

    def create(self, buy_order: str, session_id: str, card_number: str, card_expiration_date: str, details: list, cvv: str = None):
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        ValidationUtil.has_text_with_max_length(session_id, ApiConstants.SESSION_ID_LENGTH, "session_id")
        ValidationUtil.has_text_with_max_length(card_number, ApiConstants.CARD_NUMBER_LENGTH, "card_number")
        ValidationUtil.has_text_with_max_length(card_expiration_date, ApiConstants.CARD_EXPIRATION_DATE_LENGTH, "card_expiration_date")
        ValidationUtil.has_elements(details, "details")
        for item in details:
            ValidationUtil.has_text_with_max_length(item['commerce_code'], ApiConstants.COMMERCE_CODE_LENGTH, "details.commerce_code")
            ValidationUtil.has_text_with_max_length(item['buy_order'], ApiConstants.BUY_ORDER_LENGTH, "details.buy_order")
        try:
            endpoint = MallTransaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, card_number, card_expiration_date, details, cvv)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str, details: list):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = MallTransaction.COMMIT_ENDPOINT.format(token)
            request = TransactionCommitRequest(details)
            return RequestService.put(endpoint, TransactionCommitRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)

    def status(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)

    def refund(self, token: str, child_buy_order: str, child_commerce_code: str, amount: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(child_buy_order, ApiConstants.BUY_ORDER_LENGTH, "child_buy_order")
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(token)
            request = TransactionRefundRequest(buy_order=child_buy_order, commerce_code=child_commerce_code, amount=amount)
            return RequestService.post(endpoint, TransactionRefundRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, token: str, child_commerce_code: str, child_buy_order: str, authorization_code: str, capture_amount: float):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(child_commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "child_commerce_code")
        ValidationUtil.has_text_with_max_length(child_buy_order, ApiConstants.BUY_ORDER_LENGTH, "child_buy_order")
        ValidationUtil.has_text_with_max_length(authorization_code, ApiConstants.AUTHORIZATION_CODE_LENGTH, "authorization_code")
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT.format(token)
            request = TransactionCaptureRequest(commerce_code=child_commerce_code, buy_order=child_buy_order,
                                            authorization_code=authorization_code, capture_amount=capture_amount)
            return RequestService.put(endpoint, TransactionCaptureRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def installments(self, token: str, details: list):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_elements(details, "details")
        for item in details:
            ValidationUtil.has_text_with_max_length(item['commerce_code'], ApiConstants.COMMERCE_CODE_LENGTH, "details.commerce_code")
            ValidationUtil.has_text_with_max_length(item['buy_order'], ApiConstants.BUY_ORDER_LENGTH, "details.buy_order")
        try:
            return [
                self.single_installment(token,
                                        installments_number=det['installments_number'],
                                        buy_order=det['buy_order'],
                                        commerce_code=det['commerce_code']
                                        ) for det in details
            ]
        except TransbankError as e:
            raise TransactionInstallmentsError(e.message, e.code)

    def single_installment(self, token: str, installments_number: float, buy_order: str, commerce_code: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        ValidationUtil.has_text_with_max_length(commerce_code, ApiConstants.COMMERCE_CODE_LENGTH, "commerce_code")
        ValidationUtil.has_text_with_max_length(buy_order, ApiConstants.BUY_ORDER_LENGTH, "buy_order")
        try:
            endpoint = MallTransaction.INSTALLMENTS_ENDPOINT.format(token)
            request = TransactionInstallmentsRequest(installments_number=installments_number, buy_order=buy_order,
                                                 commerce_code=commerce_code)
            return RequestService.post(endpoint, TransactionInstallmentsRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise TransactionInstallmentsError(e.message, e.code)


