from abc import ABC, abstractmethod

from transbank.common.integration_type import IntegrationType


class Options(ABC):
    def __init__(self, commerce_code: str = None, api_key: str = None, integration_type: IntegrationType = None):
        self.commerce_code = commerce_code
        self.api_key = api_key
        self.integration_type = integration_type

    @abstractmethod
    def header_commerce_code_name(self):
        pass

    @abstractmethod
    def header_api_key_name(self):
        pass

    def set_commerce_code(self, commerce_code: str) -> None:
        self._commerce_code = commerce_code

    def get_commerce_code(self) -> str:
        return self._commerce_code

    def set_api_key(self, api_key: str) -> None:
        self._api_key = api_key

    def get_api_key(self) -> str:
        return self._api_key

    def set_integration_type(self, integration_type: IntegrationType) -> None:
        self._integration_type = integration_type

    def get_integration_type(self) -> IntegrationType:
        return self._integration_type

    @staticmethod
    def is_empty(options: 'Options') -> bool:
        return options is None or not options.commerce_code and not options.api_key and not options.integration_type

    def __str__(self) -> str:
        return "Options(commerce_code: {}, api_key: {}, integration_type: {})".format(self.commerce_code, self.api_key, self.integration_type)

    commerce_code = property(get_commerce_code, set_commerce_code)
    api_key = property(get_api_key, set_api_key)
    integration_type = property(get_integration_type, set_integration_type)


class WebpayOptions(Options):
    def header_commerce_code_name(self):
        return "Tbk-Api-Key-Id"

    def header_api_key_name(self):
        return "Tbk-Api-Key-Secret"
