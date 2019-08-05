from .transbank_exception import TransbankException


class TransactionCommitException(TransbankException):
    def __init__(self, error_code, original_exception, message=None):
        super(TransactionCommitException, self).__init__(error_code, original_exception, message)

