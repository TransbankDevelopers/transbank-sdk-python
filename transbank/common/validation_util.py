from transbank.error.transbank_error import TransbankError

class ValidationUtil(object):

    @staticmethod
    def has_text(value: str, value_name: str):
        if not value or not value.strip():
            raise TransbankError("'{}' can't be null or white space".format(value_name))

    @staticmethod
    def has_text_with_max_length(value: str, value_max_length: int,  value_name: str):
        ValidationUtil.has_text(value, value_name)
        if len(value) > value_max_length:
            raise TransbankError("'{}' is too long, the maximum length is {}".format(value_name, value_max_length))
    
    @staticmethod
    def has_text_trim_with_max_length(value: str, value_max_length: int,  value_name: str):
        ValidationUtil.has_text_with_max_length(value, value_max_length, value_name)
        if len(value) > len(value.strip()):
            raise TransbankError("'{}' has spaces at the beginning or the end".format(value_name))
        
    @staticmethod
    def has_elements(value: any, value_name: str):
        if value == None or len(value) == 0:
            raise TransbankError("list '{}'" + " can't be null or empty".format(value_name))
    