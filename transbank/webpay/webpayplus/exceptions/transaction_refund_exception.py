from .transbank_exception import TransbankException


class TransactionRefundException(TransbankException):
    def __init__(self, error_code, original_exception, message=None):
        super(TransactionRefundException, self).__init__(error_code, original_exception, message)


