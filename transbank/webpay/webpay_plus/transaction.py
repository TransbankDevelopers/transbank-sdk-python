import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank.common.schema import TransactionStatusResponseSchema
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.webpay.webpay_plus import default_commerce_code, default_api_key, default_integration_type, \
    TransactionStatusResponse


class Transaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType):
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(default_commerce_code, default_api_key, default_integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or default_commerce_code
            alt_options.api_key = options.api_key or default_api_key
            alt_options.integration_type = options.integration_type or default_integration_type

        return alt_options

    @classmethod
    def status(cls, token: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), token)

        response = requests.get(url=endpoint, headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = TransactionStatusResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionStatusError(message=dict_response["error_message"], code=response.status_code)

        return TransactionStatusResponse(**dict_response)
