from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

class WebpayTransaction(object):
    def __init__(self, options: WebpayOptions = None):
        self.options = options

    def configure_for_integration(self, commerce_code, api_key):
        self.options = WebpayOptions(commerce_code, api_key, IntegrationType.TEST)
        return self

    def configure_for_production(self, commerce_code, api_key):
        self.options = WebpayOptions(commerce_code, api_key, IntegrationType.LIVE)
        return self