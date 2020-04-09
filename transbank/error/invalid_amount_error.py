from transbank.error.transbank_error import TransbankError


class InvalidAmountError(TransbankError):
    DEFAULT_MESSAGE = 'Invalid amount given.'
    NOT_NUMERIC_MESSAGE = 'Given amount is not numeric.'
    HAS_DECIMALS_MESSAGE = 'Given amount has decimals. Webpay only accepts integer amounts. Please remove decimal places.'

    def __init__(self, message=DEFAULT_MESSAGE, code=0):
        super().__init__(message, code)

    @staticmethod
    def is_valid(amount, nullable=False):
        if nullable and amount is None:
            return
        try:
            float(amount)
        except ValueError:
            raise InvalidAmountError(InvalidAmountError.NOT_NUMERIC_MESSAGE)
        amount_str = str(amount)
        if amount_str.startswith("-"):  # ignore sign
            amount_str = amount_str[1:]
        if not str.isdigit(amount_str):
            raise InvalidAmountError(InvalidAmountError.HAS_DECIMALS_MESSAGE)
