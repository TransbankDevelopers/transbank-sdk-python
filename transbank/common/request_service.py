import requests
import json
from transbank.common.options import Options, WebpayOptions
from transbank.common.headers_builder import HeadersBuilder
from transbank.common.integration_type import webpay_host, patpass_comercio_host
from transbank.error.transbank_error import TransbankError

class RequestService(object):

    @classmethod
    def post(cls, endpoint: str, request: str, options: Options):
        endpoint = "{}{}".format(cls.host(options), endpoint)
        response = requests.post(url=endpoint, data=request, headers=HeadersBuilder.build(options))
        return cls.process_response(response)

    @classmethod
    def delete(cls, endpoint: str, request: str, options: Options):
        endpoint = "{}{}".format(cls.host(options), endpoint)
        response = requests.delete(url=endpoint, data=request, headers=HeadersBuilder.build(options))
        return cls.process_response(response)

    @classmethod
    def put(cls, endpoint: str, request: str, options: Options):
        endpoint = "{}{}".format(cls.host(options), endpoint)
        response = requests.put(url=endpoint, data=request, headers=HeadersBuilder.build(options))
        return cls.process_response(response)

    @classmethod
    def get(cls, endpoint: str, options: Options):
        endpoint = "{}{}".format(cls.host(options), endpoint)
        response = requests.get(url=endpoint, headers=HeadersBuilder.build(options))
        return cls.process_response(response)

    @classmethod
    def process_response(cls, response: any):
        if not response.text:
            return response.status_code
        dict_response = json.loads(response.text)
        if response.status_code not in (200, 299):
            if "error_message" in dict_response:
                raise TransbankError(message=dict_response["error_message"], code=response.status_code)
            if "description" in dict_response:
                raise TransbankError(message=dict_response["description"], code=response.status_code)
            raise TransbankError(message=response.text, code=response.status_code)
        return dict_response

    @classmethod
    def host(cls, options: Options):
        if isinstance(options, WebpayOptions):
            return webpay_host(options.integration_type)
        else:
            return patpass_comercio_host(options.integration_type)
