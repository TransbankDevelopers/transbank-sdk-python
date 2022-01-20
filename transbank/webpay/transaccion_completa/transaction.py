from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.webpay.transaccion_completa.request import TransactionCreateRequest, TransactionCommitRequest, \
    TransactionRefundRequest, TransactionCaptureRequest, TransactionInstallmentsRequest
from transbank.webpay.transaccion_completa.schema import TransactionCreateRequestSchema, \
    TransactionCommitRequestSchema, TransactionInstallmentsRequestSchema, TransactionRefundRequestSchema, TransactionCaptureRequestSchema
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.error.transaction_installments_error import TransactionInstallmentsError

class Transaction(object):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'
    INSTALLMENTS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/installments'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.TRANSACCION_COMPLETA, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def create(self, buy_order: str, session_id: str, amount: float, cvv: str, card_number: str, card_expiration_date: str):
        try:
            endpoint = Transaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, amount, card_number, cvv, card_expiration_date)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)

    def commit(self, token: str, id_query_installments: str, deferred_period_index: int, grace_period: int):
        try:
            endpoint = Transaction.COMMIT_ENDPOINT.format(token)
            request = TransactionCommitRequest(id_query_installments, deferred_period_index, grace_period)
            return RequestService.put(endpoint, TransactionCommitRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)

    def status(self, token: str):
        try:
            endpoint = Transaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)   

    def refund(self, token: str, amount: float):
        try:
            endpoint = Transaction.REFUND_ENDPOINT.format(token)
            request = TransactionRefundRequest(amount)
            return RequestService.post(endpoint, TransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, token: str, buy_order: str, authorization_code: str, capture_amount: float):
        try:
            endpoint = Transaction.CAPTURE_ENDPOINT.format(token)
            request = TransactionCaptureRequest(buy_order, authorization_code, capture_amount)
            return RequestService.put(endpoint, TransactionCaptureRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def installments(self, token: str, installments_number: float):
        try:
            endpoint = Transaction.INSTALLMENTS_ENDPOINT.format(token)
            request = TransactionInstallmentsRequest(installments_number)
            return RequestService.post(endpoint, TransactionInstallmentsRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionInstallmentsError(e.message, e.code)
