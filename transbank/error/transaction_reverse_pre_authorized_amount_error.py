from transbank.error.transbank_error import TransbankError


class TransactionReversePreAuthorizedAmountError(TransbankError):
    def __init__(self, message="Transaction reverse pre authorized amount could not be performed. Please verify given parameters", code=0):
        super().__init__(message, code)
