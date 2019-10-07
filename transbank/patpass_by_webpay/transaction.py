import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank import patpass_by_webpay
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.patpass_by_webpay.request import TransactionCreateRequest
from transbank.patpass_by_webpay.schema import TransactionCreateRequestSchema, TransactionCreateResponseSchema
from transbank.patpass_by_webpay.response import TransactionCreateResponse
from transbank.webpay.webpay_plus.response import TransactionCommitResponse, TransactionStatusResponse
from transbank.webpay.webpay_plus.transaction import Transaction as T


class Transaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType) -> str:
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(patpass_by_webpay.commerce_code, patpass_by_webpay.api_key,
                                    patpass_by_webpay.integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or patpass_by_webpay.commerce_code
            alt_options.api_key = options.api_key or patpass_by_webpay.api_key
            alt_options.integration_type = options.integration_type or patpass_by_webpay.integration_type

        return alt_options

    @classmethod
    def create(cls, buy_order: str, session_id: str, amount: float, return_url: str, service_id: str,
               card_holder_id: str,
               card_holder_name: str, card_holder_last_name1: str, card_holder_last_name2: str, card_holder_mail: str,
               cellphone_number: str, expiration_date: str, commerce_mail: str, uf_flag: bool,
               options: Options = None) -> TransactionCreateResponse:
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        request = TransactionCreateRequest(buy_order, session_id, amount, return_url, service_id, card_holder_id,
                                           card_holder_name, card_holder_last_name1, card_holder_last_name2,
                                           card_holder_mail, cellphone_number, expiration_date, commerce_mail, uf_flag)

        response = requests.post(endpoint, data=TransactionCreateRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = TransactionCreateResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionCreateError(message=dict_response["error_message"], code=response.status_code)

        return TransactionCreateResponse(**dict_response)

    @classmethod
    def commit(cls, token: str, options: Options = None) -> TransactionCommitResponse:
        return T.commit(token, cls.build_options(options))

    @classmethod
    def status(cls, token: str, options: Options = None) -> TransactionStatusResponse:
        return T.status(token, cls.build_options(options))
