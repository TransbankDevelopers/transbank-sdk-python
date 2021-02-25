from transbank.common.integration_type import IntegrationType

webpay_plus_default_commerce_code = "597055555532"
webpay_plus_mall_default_commerce_code = "597055555535"
mall_default_child_commerce_codes  = ['597055555536', '597055555537']
default_api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
default_integration_type = IntegrationType.TEST
webpay_plus_deferred_commerce_code = "597055555540"
webpay_plus_mall_deferred_default_commerce_code = "597055555544"
mall_deferred_default_child_commerce_codes  = ['597055555545', '597055555546']

class WebpayPlus:
    __commerce_code = webpay_plus_default_commerce_code
    __api_key = default_api_key
    __integration_type = default_integration_type

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
