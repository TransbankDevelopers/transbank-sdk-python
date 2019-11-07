from transbank.error.transbank_error import TransbankError


class TransactionCaptureError(TransbankError):
    def __init__(self, message="Transaction could not be Captured. Please verify given parameters", code=0):
        super().__init__(message, code)
