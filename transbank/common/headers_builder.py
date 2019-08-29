from transbank.common.options import Options


class HeadersBuilder(object):
    @staticmethod
    def build(options: Options):
        return {
            "Content-Type": "application/json",
            options.get_header_commerce_code_name(): options.commerce_code,
            options.get_header_api_key_name(): options.api_key
        }
