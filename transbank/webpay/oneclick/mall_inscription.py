from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.validation_util import ValidationUtil
from transbank.webpay.oneclick.schema import MallInscriptionStartRequestSchema, MallInscriptionDeleteRequestSchema
from transbank.webpay.oneclick.request import MallInscriptionStartRequest, MallInscriptionDeleteRequest
from transbank.error.transbank_error import TransbankError
from transbank.error.inscription_start_error import InscriptionStartError
from transbank.error.inscription_finish_error import InscriptionFinishError
from transbank.error.inscription_delete_error import InscriptionDeleteError


class MallInscription(WebpayTransaction):
    START_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions'
    FINISH_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions/{}'
    DELETE_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/inscriptions'

    def __init__(self, options: WebpayOptions = None):
        if options is None:
            self.configure_for_testing()
        else: 
            super().__init__(options) 

    def start(self, username: str, email: str, response_url: str):        
        ValidationUtil.has_text_trim_with_max_length(username, ApiConstants.USER_NAME_LENGTH, "username")
        ValidationUtil.has_text_trim_with_max_length(email, ApiConstants.EMAIL_LENGTH, "email")
        ValidationUtil.has_text_with_max_length(response_url, ApiConstants.RETURN_URL_LENGTH, "response_url")
        try:
            endpoint = MallInscription.START_ENDPOINT
            request = MallInscriptionStartRequest(username, email, response_url)
            return RequestService.post(endpoint, MallInscriptionStartRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise InscriptionStartError(e.message, e.code)

    def finish(self, token: str):
        ValidationUtil.has_text_with_max_length(token, ApiConstants.TOKEN_LENGTH, "token")
        try:
            endpoint = MallInscription.FINISH_ENDPOINT.format(token)
            return RequestService.put(endpoint, {}, self.options)
        except TransbankError as e:
            raise InscriptionFinishError(e.message, e.code)

    def delete(self, tbk_user: str, username: str):
        ValidationUtil.has_text_trim_with_max_length(username, ApiConstants.USER_NAME_LENGTH, "username")
        ValidationUtil.has_text_with_max_length(tbk_user, ApiConstants.TBK_USER_LENGTH, "tbk_user")
        try:
            endpoint = MallInscription.DELETE_ENDPOINT
            request = MallInscriptionDeleteRequest(username, tbk_user)
            RequestService.delete(endpoint, MallInscriptionDeleteRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise InscriptionDeleteError(e.message, e.code)

    def configure_for_testing(self):
        return self.configure_for_integration(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY)

    def configure_for_testing_deferred(self):
        return self.configure_for_integration(IntegrationCommerceCodes.ONECLICK_MALL_DEFERRED, IntegrationApiKeys.WEBPAY)
   

    


