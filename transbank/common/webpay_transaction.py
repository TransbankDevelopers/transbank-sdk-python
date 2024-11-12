from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

class WebpayTransaction(object):
    def __init__(self, options: WebpayOptions):
        self.options = options

    @classmethod
    def build_for_integration(cls, commerce_code, api_key):
        options = WebpayOptions(commerce_code, api_key, IntegrationType.TEST)
        return cls(options)

    @classmethod
    def build_for_production(cls, commerce_code, api_key):
        options = WebpayOptions(commerce_code, api_key, IntegrationType.LIVE)
        return cls(options)
