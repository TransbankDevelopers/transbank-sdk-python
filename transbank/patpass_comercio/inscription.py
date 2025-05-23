from transbank.common.options import PatpassComercioOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_type import IntegrationType
from transbank.patpass_comercio.request import InscriptionStartRequest, InscriptionStatusRequest
from transbank.patpass_comercio.schema import InscriptionStartRequestSchema, InscriptionStatusRequestSchema
from transbank.error.transbank_error import TransbankError
from transbank.error.inscription_start_error import InscriptionStartError
from transbank.error.inscription_status_error import InscriptionStatusError

class Inscription(object):

    START_ENDPOINT = ApiConstants.PATPASS_ENDPOINT + '/patInscription'
    STATUS_ENDPOINT = ApiConstants.PATPASS_ENDPOINT + '/status'

    def __init__(self, options: PatpassComercioOptions):
        self.options = options

    @classmethod
    def build_for_integration(cls, commerce_code, api_key):
        options = PatpassComercioOptions(commerce_code, api_key, IntegrationType.TEST)
        return cls(options)

    @classmethod
    def build_for_production(cls, commerce_code, api_key):
        options = PatpassComercioOptions(commerce_code, api_key, IntegrationType.LIVE)
        return cls(options)

    def start(self, url: str,
              name: str,
              last_name: str,
              second_last_name: str,
              rut: str,
              service_id: str,
              final_url: str,
              max_amount: float,
              phone: str,
              cell_phone: str,
              patpass_name: str,
              person_email: str,
              commerce_email: str,
              address: str,
              city: str):
        try:
            m_amount = max_amount
            if max_amount == 0:
                m_amount = ''
            endpoint = Inscription.START_ENDPOINT
            request = InscriptionStartRequest(url, name, last_name, second_last_name, rut,
                                          service_id, final_url, self.options.commerce_code, m_amount,
                                          phone, cell_phone, patpass_name, person_email,
                                          commerce_email, address, city)
            return RequestService.post(endpoint, InscriptionStartRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise InscriptionStartError(e.message, e.code)

    def status(self, token: str):
        try:
            endpoint = Inscription.STATUS_ENDPOINT
            request = InscriptionStatusRequest(token)
            return RequestService.post(endpoint, InscriptionStatusRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise InscriptionStatusError(e.message, e.code)


