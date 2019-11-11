import requests

from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_capture_error import TransactionCaptureError
from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank.webpay.webpay_plus import webpay_plus_mall_deferred_default_commerce_code, default_api_key, \
    default_integration_type
from transbank.webpay.webpay_plus.request import MallTransactionCreateDetails, MallTransactionCreateRequest,\
                                                 MallDeferredTransactionRequest, MallDeferredTransactionRefundRequest
from transbank.webpay.webpay_plus.response import MallTransactionCreateResponse, MallTransactionCommitResponse, TransactionRefundResponse,\
                                                 TransactionStatusResponse, DeferredTransactionResponse
from transbank.webpay.webpay_plus.schema import MallTransactionCreateRequestSchema, MallTransactionCreateResponseSchema, \
    MallTransactionCommitResponseSchema,TransactionRefundResponseSchema, MallDeferredTransactionRefundRequestSchema,\
    MallDeferredTransactionRequestSchema, DeferredTransactionResponseSchema


class MallDeferredTransaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType) -> str:
        return "{}/rswebpaytransaction/api/webpay/v1.0/transactions".format(
            webpay_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = WebpayOptions(webpay_plus_mall_deferred_default_commerce_code, default_api_key, default_integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or webpay_plus_mall_deferred_default_commerce_code
            alt_options.api_key = options.api_key or default_api_key
            alt_options.integration_type = options.integration_type or default_integration_type

        return alt_options

    @classmethod
    def create(cls, buy_order: str, session_id: str, return_url: str, details: MallTransactionCreateDetails,
               options: Options = None) -> MallTransactionCreateResponse:
        options = cls.build_options(options)
        endpoint = cls.__base_url(options.integration_type)
        request = MallTransactionCreateRequest(buy_order, session_id, return_url, details.details)

        response = requests.post(endpoint, data=MallTransactionCreateRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder().build(options))
        json_response = response.text
        dict_response = MallTransactionCreateResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionCreateError(message=dict_response["error_message"], code=response.status_code)

        return MallTransactionCreateResponse(**dict_response)

    @classmethod
    def commit(cls, token: str, options: Options = None) -> MallTransactionCommitResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), token)

        response = requests.put(url=endpoint, headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = MallTransactionCommitResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionCommitError(message=dict_response["error_message"], code=response.status_code)

        return MallTransactionCommitResponse(**dict_response)
    
    @classmethod
    def status(cls, token: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), token)

        response = requests.get(url=endpoint, headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = MallTransactionCommitResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionStatusError(message=dict_response["error_message"], code=response.status_code)

        return MallTransactionCommitResponse(**dict_response)
    
    @classmethod
    def capture(cls, token: str, buy_order: str, authorization_code: str, capture_amount: float, commerce_code: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = "{}/{}/capture".format(cls.__base_url(options.integration_type), token)
        request = MallDeferredTransactionRequest(commerce_code, buy_order, authorization_code, capture_amount)

        response = requests.put(url=endpoint, headers=HeadersBuilder.build(options),
                                 data = MallDeferredTransactionRequestSchema().dumps(request).data)
        json_response = response.text
        dict_response = DeferredTransactionResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionCaptureError(message=dict_response["error_message"], code=response.status_code)
        
        return DeferredTransactionResponse(**dict_response)

    @classmethod
    def refund(cls, token: str, buy_order: str, amount: float, commerce_code: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = "{}/{}/refunds".format(cls.__base_url(options.integration_type), token)
        request = MallDeferredTransactionRefundRequest(buy_order, commerce_code, amount)

        response = requests.post(url=endpoint, headers=HeadersBuilder.build(options),
                                 data=MallDeferredTransactionRefundRequestSchema().dumps(request).data)
        json_response = response.text
        dict_response = TransactionRefundResponseSchema().loads(json_response).data

        if response.status_code not in range(200, 299):
            raise TransactionRefundError(message=dict_response["error_message"], code=response.status_code)

        return TransactionRefundResponse(**dict_response)