from transbank.error.transbank_error import TransbankError

class MallBinInfoQueryError(TransbankError):
    def __init__(self, message="Mall bin info query could not be performed. Please verify given parameters", code=0):
        super().__init__(message, code)
