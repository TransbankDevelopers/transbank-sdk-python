from transbank.common.options import Options


class HeadersBuilder(object):
    @staticmethod
    def build(options: Options):
        return {
            "Content-Type": "application/json",
            options.header_commerce_code_name(): options.commerce_code,
            options.header_api_key_name(): options.api_key
        }
