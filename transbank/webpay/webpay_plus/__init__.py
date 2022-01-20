from transbank.common.integration_type import IntegrationType
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys

class WebpayPlus:
    __commerce_code = IntegrationCommerceCodes.WEBPAY_PLUS
    __api_key = IntegrationApiKeys.WEBPAY
    __integration_type = IntegrationType.TEST

    @classmethod
    def configure_for_integration(cls, commerce_code, api_key):
        cls.__commerce_code = commerce_code
        cls.__api_key = api_key
        cls.__integration_type = IntegrationType.TEST

    @classmethod
    def configure_for_production(cls, commerce_code, api_key):
        cls.__commerce_code = commerce_code
        cls.__api_key = api_key
        cls.__integration_type = IntegrationType.LIVE

    @classmethod
    def get_commerce_code(cls):
        return cls.__commerce_code

    @classmethod
    def get_api_key(cls):
        return cls.__api_key

    @classmethod
    def get_integration_type(cls):
        return cls.__integration_type
