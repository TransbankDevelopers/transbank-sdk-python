from .transbank_exception import TransbankException


class TransactionStatusException(TransbankException):
    def __init__(self, error_code, original_exception, message=None):
        super(TransactionStatusException, self).__init__(error_code, original_exception, message)
