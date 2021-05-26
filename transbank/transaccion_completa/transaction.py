import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank import transaccion_completa
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.error.transaction_installments_error import TransactionInstallmentsError
from transbank.transaccion_completa.request import TransactionCreateRequest, TransactionCommitRequest, \
    TransactionStatusRequest, TransactionRefundRequest, TransactionCaptureRequest, TransactionInstallmentsRequest
from transbank.transaccion_completa.response import TransactionCreateResponse, TransactionCommitResponse, \
    TransactionStatusResponse, TransactionRefundResponse, TransactionCaptureResponse, TransactionInstallmentsResponse
from transbank.transaccion_completa.schema import CreateTransactionRequestSchema, CreateTransactionResponseSchema, \
    CommitTransactionRequestSchema, CommitTransactionResponseSchema, InstallmentsTransactionRequestSchema, \
    InstallmentsTransactionResponseSchema, RefundTransactionRequestSchema, RefundTransactionResponseSchema, \
    CaptureTransactionRequestSchema, CaptureTransactionResponseSchema


class Transaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType):
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(transaccion_completa.commerce_code, transaccion_completa.api_key,
                                    transaccion_completa.integration_type)
        if options is not None:
            alt_options.commerce_code = options.commerce_code or transaccion_completa.commerce_code
            alt_options.api_key = options.api_key or transaccion_completa.api_key
            alt_options.integration_type = options.integration_type or transaccion_completa.integration_type
        return alt_options

    @classmethod
    def create(cls, buy_order: str, session_id: str, amount: float, card_number: str, cvv: str,
               card_expiration_date: str,
               options: Options = None) -> TransactionCreateResponse:
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        request = TransactionCreateRequest(buy_order, session_id, amount, card_number, cvv, card_expiration_date)
        response = requests.post(endpoint, data=CreateTransactionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = CreateTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionCreateResponse(**response_dict)
        raise TransactionCreateError(message=response_dict["error_message"])

    @classmethod
    def commit(cls, token: str, id_query_installments: str, deferred_period_index: int, grace_period: int,
               options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), token)
        request = TransactionCommitRequest(id_query_installments, deferred_period_index, grace_period)
        response = requests.put(endpoint, data=CommitTransactionRequestSchema().dumps(request).data,
                                headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = CommitTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionCommitResponse(**response_dict)
        raise TransactionCommitError(message=response_dict["error_message"])

    @classmethod
    def status(cls, token: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), token)
        request = TransactionStatusRequest(token=token)
        response = requests.get(endpoint, headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = CommitTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionStatusResponse(**response_dict)
        raise TransactionStatusError(message=response_dict["error_message"])

    @classmethod
    def refund(cls, token: str, amount: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}/refunds'.format(cls.__base_url(options.integration_type), token)
        request = TransactionRefundRequest(amount=amount)
        response = requests.post(endpoint, data=RefundTransactionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = RefundTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionRefundResponse(**response_dict)
        raise TransactionRefundError(message=response_dict["error_message"])

    @classmethod
    def capture(cls, token: str, buy_order: str, authorization_code: str, capture_amount: float, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}/capture'.format(cls.__base_url(options.integration_type), token)
        request = TransactionCaptureRequest(buy_order=buy_order, authorization_code=authorization_code,
                                            capture_amount=capture_amount)
        response = requests.put(endpoint, data=CaptureTransactionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = CaptureTransactionResponseSchema().loads(response_json).data
        if response.status_code in range (200,209):
            return TransactionCaptureResponse(**response_dict)
        raise TransactionCaptureError(message=response_dict["error_message"])


    @classmethod
    def installments(cls, token: str, installments_number: float, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}/installments'.format(cls.__base_url(options.integration_type), token)

        request = TransactionInstallmentsRequest(installments_number=installments_number)
        response = requests.post(endpoint, data=InstallmentsTransactionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = InstallmentsTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionInstallmentsResponse(**response_dict)
        raise TransactionInstallmentsError(message=response_dict["error_message"])
