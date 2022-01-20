from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
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

class MallTransaction(object):
    CREATE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/'
    COMMIT_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    STATUS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}'
    REFUND_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/refunds'
    CAPTURE_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/capture'
    INSTALLMENTS_ENDPOINT = ApiConstants.WEBPAY_ENDPOINT + '/transactions/{}/installments'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.TRANSACCION_COMPLETA_MALL, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def create(self, buy_order: str, session_id: str, card_number: str, card_expiration_date: str, details: list, cvv: str = None):
        try:
            endpoint = MallTransaction.CREATE_ENDPOINT
            request = TransactionCreateRequest(buy_order, session_id, card_number, card_expiration_date, details, cvv)
            return RequestService.post(endpoint, TransactionCreateRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCreateError(e.message, e.code)      

    def commit(self, token: str, details: list):
        try:
            endpoint = MallTransaction.COMMIT_ENDPOINT.format(token)
            request = TransactionCommitRequest(details)
            return RequestService.put(endpoint, TransactionCommitRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCommitError(e.message, e.code)

    def status(self, token: str):
        try:
            endpoint = MallTransaction.STATUS_ENDPOINT.format(token)
            return RequestService.get(endpoint, self.options)
        except TransbankError as e:
            raise TransactionStatusError(e.message, e.code)  

    def refund(self, token: str, child_buy_order: str, child_commerce_code: str, amount: str):
        try:
            endpoint = MallTransaction.REFUND_ENDPOINT.format(token)
            request = TransactionRefundRequest(buy_order=child_buy_order, commerce_code=child_commerce_code, amount=amount)
            return RequestService.post(endpoint, TransactionRefundRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionRefundError(e.message, e.code)

    def capture(self, token: str, child_commerce_code: str, child_buy_order: str, authorization_code: str, capture_amount: float):
        try:
            endpoint = MallTransaction.CAPTURE_ENDPOINT.format(token)
            request = TransactionCaptureRequest(commerce_code=child_commerce_code, buy_order=child_buy_order,
                                            authorization_code=authorization_code, capture_amount=capture_amount)
            return RequestService.put(endpoint, TransactionCaptureRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionCaptureError(e.message, e.code)

    def installments(self, token: str, details: list):
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
        try:
            endpoint = MallTransaction.INSTALLMENTS_ENDPOINT.format(token)
            request = TransactionInstallmentsRequest(installments_number=installments_number, buy_order=buy_order,
                                                 commerce_code=commerce_code)
            return RequestService.post(endpoint, TransactionInstallmentsRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise TransactionInstallmentsError(e.message, e.code)   


