import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, patpass_comercio_host
from transbank.common.options import Options, PatpassComercioOptions
from transbank import patpass_comercio
from transbank.error.transaction_inscription_error import TransactionInscriptionError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.patpass_comercio.request import TransactionInscriptionRequest, TransactionStatusRequest
from transbank.patpass_comercio.response import TransactionInscriptionResponse, TransactionStatusResponse
from transbank.patpass_comercio.schema import TransactionInscriptionRequestSchema, \
    TransactionInscriptionResponseSchema, TransactionStatusResponseSchema, TransactionStatusRequestSchema


class Transaction(object):
    @classmethod
    def __base_url(cls, integration_type: IntegrationType):
        return "{}/restpatpass/v1/services".format(
            patpass_comercio_host(integration_type))

    @classmethod
    def build_options(cls, options: Options = None) -> Options:
        alt_options = PatpassComercioOptions(patpass_comercio.commerce_code, patpass_comercio.api_key,
                                             patpass_comercio.integration_type)

        if options is not None:
            alt_options.commerce_code = options.commerce_code or patpass_comercio.commerce_code
            alt_options.api_key = options.api_key or patpass_comercio.api_key
            alt_options.integration_type = options.integration_type or patpass_comercio.integration_type

        return alt_options

    @classmethod
    def inscription(cls,
                    url: str,
                    name: str,
                    first_last_name: str,
                    second_last_name: str,
                    rut: str,
                    service_id: str,
                    final_url: str,
                    max_amount: float,
                    phone_number: str,
                    mobile_number: str,
                    patpass_name: str,
                    person_email: str,
                    commerce_email: str,
                    address: str,
                    city: str,
                    options: Options = None) -> TransactionInscriptionResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), 'patInscription')
        m_amount = max_amount
        if max_amount == 0:
            m_amount = ''

        request = TransactionInscriptionRequest(url, name, first_last_name, second_last_name, rut,
                                                service_id, final_url, options.commerce_code, m_amount,
                                                phone_number, mobile_number, patpass_name, person_email, commerce_email,
                                                address, city)

        response = requests.post(endpoint, data=TransactionInscriptionRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = TransactionInscriptionResponseSchema().loads(json_response).data
        if response.status_code not in range(200, 299):
            raise TransactionInscriptionError(message=dict_response["description"], code=response.status_code)

        return TransactionInscriptionResponse(**dict_response)

    @classmethod
    def status(cls, token: str, options: Options = None) -> TransactionStatusResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), 'status')

        request = TransactionStatusRequest(token)

        response = requests.post(url=endpoint, data=TransactionStatusRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = TransactionStatusResponseSchema().loads(json_response).data
        if response.status_code not in range(200, 299):
            raise TransactionStatusError(message=dict_response["error_message"], code=response.status_code)

        return TransactionStatusResponse(**dict_response)
