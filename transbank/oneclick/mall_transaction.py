import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank import oneclick
from transbank.error.transaction_authorize_error import TransactionAuthorizeError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.oneclick.request import TransactionAuthorizeRequest, TransactionRefundRequest, \
    MallTransactionAuthorizeDetails
from transbank.oneclick.response import TransactionAuthorizeResponse, TransactionRefundResponse, \
    TransactionStatusResponse
from transbank.oneclick.schema import TransactionAuthorizeRequestSchema, TransactionAuthorizeResponseSchema, \
    TransactionRefundRequestSchema, TransactionRefundResponseSchema, TransactionStatusResponseSchema


class MallTransaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType):
        return "{}/rswebpaytransaction/api/oneclick/v1.0".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(oneclick.commerce_code, oneclick.api_key,
                                    oneclick.integration_type)
        if options is not None:
            alt_options.commerce_code = options.commerce_code or oneclick.commerce_code
            alt_options.api_key = options.api_key or oneclick.api_key
            alt_options.integration_type = options.integration_type or oneclick.integration_type

        return alt_options

    @classmethod
    def authorize(cls, user_name: str, tbk_user: str, buy_order: str, details: MallTransactionAuthorizeDetails,
                  options: Options = None) -> TransactionAuthorizeResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), 'transactions')
        request = TransactionAuthorizeRequest(user_name, tbk_user, buy_order, details.details)

        data = TransactionAuthorizeRequestSchema().dumps(request).data
        response = requests.post(endpoint, data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = TransactionAuthorizeResponseSchema().loads(response_json).data
        if response.status_code not in range(200, 299):
            raise TransactionAuthorizeError(message=response_dict["error_message"])

        return TransactionAuthorizeResponse(**response_dict)

    @classmethod
    def refund(cls, buy_order: str, child_commerce_code: str, child_buy_order: str, amount: float,
               options: Options = None) -> TransactionRefundResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}/{}/refunds'.format(cls.__base_url(options.integration_type), 'transactions', buy_order)
        request = TransactionRefundRequest(child_commerce_code, child_buy_order, amount)
        response = requests.post(endpoint, data=TransactionRefundRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = TransactionRefundResponseSchema().loads(response_json).data
        if response.status_code not in range(200, 299):
            raise TransactionRefundError(message=response_dict["error_message"])

        return TransactionRefundResponse(**response_dict)

    @classmethod
    def status(cls, buy_order: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}/{}'.format(cls.__base_url(options.integration_type), 'transactions', buy_order)

        response = requests.get(endpoint, headers=HeadersBuilder.build(options))
        response_json = response.text
        response_dict = TransactionStatusResponseSchema().loads(response_json).data

        if response.status_code not in range(200, 299):
            raise TransactionStatusError(message=response_dict["error_message"])

        return TransactionStatusResponse(**response_dict)
