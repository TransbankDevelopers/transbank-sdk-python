from transbank.error.transbank_error import TransbankError


class InscriptionDeleteError(TransbankError):
    def __init__(self, message="Inscription delete could not be performed. Please verify given parameters",
                 code=0):
        super().__init__(message, code)
