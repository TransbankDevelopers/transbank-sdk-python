from transbank.error.transbank_error import TransbankError


class TransactionStatusError(TransbankError):
    def __init__(self, message="Transaction status could not be performed. Please verify given parameters", code=0):
        super().__init__(message, code)
