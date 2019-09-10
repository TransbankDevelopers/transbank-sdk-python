from transbank.error.transbank_error import TransbankError


class TransactionCommitError(TransbankError):
    def __init__(self, message = "Transaction could not be committed. Please verify given parameters", code=0):
        super().__init__(message, code)
