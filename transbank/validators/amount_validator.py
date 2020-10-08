from transbank.error.invalid_amount_error import InvalidAmountError


class AmountValidator:

    @staticmethod
    def validate(amount, nullable=False):
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
