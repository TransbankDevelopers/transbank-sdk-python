import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank import transaccion_completa
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.transaccion_completa.transaction_create_request import TransactionCreateRequest
from transbank.transaccion_completa.schema import CreateTransactionRequestSchema, CreateTransactionResponseSchema
from transbank.transaccion_completa.transaction_create_response import TransactionCreateResponse


class Transaction(object):
    @classmethod
    def __base_url(clscls, integration_type: IntegrationType):
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
            return TransactionCreateResponse(token=response_dict["token"])
        raise TransactionCreateError(message=response_dict["error_message"])

    @classmethod
    def commit(cls, token: str, id_query_installments:str, deferred_period_index: int, grace_period: int,
               options: Options = None):
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        request = TransactionCommitRequest(buy_order, session_id, amount, card_number, cvv, card_expiration_date)
        response = requests.post(endpoint, data=CreateTransactionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = CreateTransactionResponseSchema().loads(response_json).data
        if response.status_code in range(200, 299):
            return TransactionCreateResponse(token=response_dict["token"])
        raise TransactionCreateError(message=response_dict["error_message"])



