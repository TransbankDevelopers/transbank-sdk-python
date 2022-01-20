from typing import List, Iterator
from transbank.validators.amount_validator import AmountValidator


class MallInscriptionStartRequest(object):
    def __init__(self,
                 user_name: str,
                 email: str,
                 response_url: str):
        self.username = user_name
        self.email = email
        self.response_url = response_url


class MallInscriptionDeleteRequest(object):
    def __init__(self,
                 user_name: str,
                 tbk_user: str):
        self.username = user_name
        self.tbk_user = tbk_user


class MallDetails(object):
    def __init__(self, commerce_code: str, buy_order: str, installments_number: int, amount: float):
        AmountValidator.validate(amount)
        self.commerce_code = commerce_code
        self.buy_order = buy_order
        self.installments_number = installments_number
        self.amount = amount

    def __repr__(self):
        return "MallDetails(commerce_code: {}, buy_order: {}, installments_number: {}, amount: {})".format(
            self.commerce_code, self.buy_order, self.installments_number, self.amount)

    def __eq__(self, other) -> bool:
        if type(other) is not MallTransactionAuthorizeDetails:
            return False

        return self.commerce_code == other.commerce_code \
               and self.buy_order == other.buy_order \
               and self.installments_number == other.installments_number \
               and self.amount == other.amount

class MallTransactionAuthorizeDetails(object):
    def __init__(self, commerce_code: str, buy_order: str, installments_number: int, amount: float):
        self.__details = []
        self.add(commerce_code, buy_order, installments_number, amount)

    def add(self, commerce_code: str, buy_order: str, installments_number: int,
            amount: float) -> "MallTransactionAuthorizeDetails":
        mall_details = MallDetails(commerce_code, buy_order, installments_number, amount)
        self.__details.append(mall_details)
        return self

    def remove(self, commerce_code: str, buy_order: str, installments_number: int, amount: float) -> None:
        mall_details = MallDetails(commerce_code, buy_order, installments_number, amount)
        self.__details.remove(mall_details)

    @property
    def details(self) -> Iterator[MallDetails]:
        return tuple(self.__details)





class MallTransactionAuthorizeRequest(object):
    def __init__(self,
                 username: str,
                 tbk_user: str,
                 buy_order: str,
                 details: List[MallDetails]):
        self.username = username
        self.tbk_user = tbk_user
        self.buy_order = buy_order
        self.details = details


class MallTransactionCaptureRequest(object):
    def __init__(self, commerce_code: str, buy_order: str, authorization_code: str, capture_amount: float):
        self.commerce_code = commerce_code
        self.buy_order = buy_order
        self.authorization_code = authorization_code
        self.capture_amount = capture_amount

    def __repr__(self):
        return "MallTransactionCaptureRequest(commerce_code: {}, buy_order: {}, authorization_code: {}, capture_amount: {})".format(
            self.commerce_code, self.buy_order, self.authorization_code, self.capture_amount )


class MallTransactionRefundRequest(object):
    def __init__(self,
                 commerce_code: str,
                 detail_buy_order: str,
                 amount: float):
        AmountValidator.validate(amount)
        self.commerce_code = commerce_code
        self.detail_buy_order = detail_buy_order
        self.amount = amount









