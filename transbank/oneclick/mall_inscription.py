import requests

from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import IntegrationType, webpay_host
from transbank.common.options import Options, WebpayOptions
from transbank import oneclick
from transbank.error.inscription_delete_error import InscriptionDeleteError
from transbank.error.inscription_finish_error import InscriptionFinishError
from transbank.error.inscription_start_error import InscriptionStartError
from transbank.oneclick.request import InscriptionStartRequest, InscriptionDeleteRequest
from transbank.oneclick.response import InscriptionStartResponse, InscriptionFinishResponse
from transbank.oneclick.schema import InscriptionStartRequestSchema, InscriptionStartResponseSchema, \
    InscriptionFinishResponseSchema, InscriptionDeleteRequestSchema


class MallInscription(object):
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
    def start(cls,
              user_name: str,
              email: str,
              response_url: str,
              options: Options = None) -> InscriptionStartResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), 'inscriptions')

        request = InscriptionStartRequest(user_name, email, response_url)

        response = requests.post(endpoint, data=InscriptionStartRequestSchema().dumps(request).data,
                                 headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = InscriptionStartResponseSchema().loads(json_response).data
        if response.status_code not in range(200, 299):
            raise InscriptionStartError(message=dict_response["error_message"], code=response.status_code)

        return InscriptionStartResponse(**dict_response)

    @classmethod
    def finish(cls, token: str, options: Options = None) -> InscriptionFinishResponse:
        options = cls.build_options(options)
        endpoint = '{}/{}/{}'.format(cls.__base_url(options.integration_type), 'inscriptions', token)

        response = requests.put(url=endpoint, headers=HeadersBuilder.build(options))
        json_response = response.text
        dict_response = InscriptionFinishResponseSchema().loads(json_response).data
        if response.status_code not in range(200, 299):
            raise InscriptionFinishError(message=dict_response["error_message"], code=response.status_code)

        return InscriptionFinishResponse(**dict_response)

    @classmethod
    def delete(cls, tbk_user: str, user_name: str, options: Options = None):
        options = cls.build_options(options)
        endpoint = '{}/{}'.format(cls.__base_url(options.integration_type), 'inscriptions')

        request = InscriptionDeleteRequest(user_name, tbk_user)
        data = InscriptionDeleteRequestSchema().dumps(request).data

        response = requests.delete(url=endpoint, data=data,
                                   headers=HeadersBuilder.build(options))

        if response.status_code not in range(200, 299):
            raise InscriptionDeleteError(message="Delete could not be performed", code=response.status_code)
