from transbank.common.integration_type import IntegrationType, webpay_host

from transbank.common.options import Options, WebpayOptions
from transbank.webpay.webpay_plus import webpay_plus_mall_default_commerce_code, default_api_key, \
    default_integration_type
from transbank.webpay.webpay_plus.request import MallTransactionCreateDetails


class MallTransaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType) -> str:
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(webpay_plus_mall_default_commerce_code, default_api_key, default_integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or webpay_plus_mall_default_commerce_code
            alt_options.api_key = options.api_key or default_api_key
            alt_options.integration_type = options.integration_type or default_integration_type

        return alt_options

    @classmethod
    def create(cls, buy_order: str, session_id: str, return_url: str, details: MallTransactionCreateDetails,
               options: Options = None):
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        pass
