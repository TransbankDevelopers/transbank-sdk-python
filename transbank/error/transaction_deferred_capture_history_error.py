from transbank.error.transbank_error import TransbankError


class TransactionDeferredCaptureHistoryError(TransbankError):
    def __init__(self, message="Transaction deferred capture history could not be performed. Please verify given parameters", code=0):
        super().__init__(message, code)
