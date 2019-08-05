from .transbank_exception import TransbankException


class TransactionCreateException(TransbankException):
    def __init__(self, error_code, original_exception, message=None):
        super(TransactionCreateException, self).__init__(error_code, original_exception, message)

