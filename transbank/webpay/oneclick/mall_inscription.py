from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.webpay.oneclick.schema import MallInscriptionStartRequestSchema, MallInscriptionDeleteRequestSchema
from transbank.webpay.oneclick.request import MallInscriptionStartRequest, MallInscriptionDeleteRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.inscription_start_error import InscriptionStartError
from transbank.error.inscription_finish_error import InscriptionFinishError
from transbank.error.inscription_delete_error import InscriptionDeleteError


class MallInscription(object):
    START_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions'
    FINISH_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions/{}'
    DELETE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.options = WebpayOptions(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY, IntegrationType.TEST)
        else:
            self.options = options  

    def start(self, username: str, email: str, response_url: str):        
        try:
            endpoint = MallInscription.START_ENDPOINT
            request = MallInscriptionStartRequest(username, email, response_url)
            return RequestService.post(endpoint, MallInscriptionStartRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise InscriptionStartError(e.message, e.code)

    def finish(self, token: str):
        try:
            endpoint = MallInscription.FINISH_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise InscriptionFinishError(e.message, e.code)

    def delete(self, tbk_user: str, username: str):
        try:
            endpoint = MallInscription.DELETE_ENDPOINT
            request = MallInscriptionDeleteRequest(username, tbk_user)
            RequestService.delete(endpoint, MallInscriptionDeleteRequestSchema().dumps(request).data, self.options)
        except TransbankError as e:
            raise InscriptionDeleteError(e.message, e.code)


   

    


