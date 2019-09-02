import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_type_host_helper import IntegrationTypeHostHelper
from transbank.common.options import Options, WebpayOptions
from transbank import patpass_by_webpay
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.patpass_by_webpay.transaction_create_request import TransactionCreateRequest
from transbank.patpass_by_webpay.schema import CreateTransactionRequestSchema, CreateTransactionResponseSchema
from transbank.patpass_by_webpay.transaction_create_response import TransactionCreateResponse


class Transaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType):
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            IntegrationTypeHostHelper.webpay_host(integration_type))

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
        json_response = requests.post(endpoint, data=CreateTransactionRequestSchema().dumps(request).data,
                                      headers=HeadersBuilder.build(options)).text
        dict_response = CreateTransactionResponseSchema().loads(json_response).data

        if "error_message" in dict_response.keys():
            raise TransactionCreateError(message=dict_response["error_message"])

        return TransactionCreateResponse(dict_response["token"], dict_response["url"])
