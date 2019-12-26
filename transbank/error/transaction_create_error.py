from transbank.error.transbank_error import TransbankError


class TransactionCreateError(TransbankError):
    def __init__(self, message = "Transaction could not be created. Please verify given parameters", code = 0):
        super().__init__(message, code)
