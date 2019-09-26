from transbank.common.model import CardDetail


class TransactionCreateResponse(object):
    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return "token: {}".format(self.token)


class TransactionCommitResponse(object):
    def __init__(self, vci: str, amount: float, status: str, buy_order: str, session_id: str,
                 card_detail: CardDetail, accounting_date: str, transaction_date: str, authorization_code: str,
                 payment_type_code: str, response_code: str, installments_number: float, installments_amount: float,
                 balance: float):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        self.installments_amount = installments_amount
        self.balance = balance


class TransactionStatusResponse(object):
    def __init__(self, vci: str, amount: float, status: str, buy_order: str, session_id: str,
                 card_detail: CardDetail, accounting_date: str, transaction_date: str, authorization_code: str,
                 payment_type_code: str, response_code: str, installments_number: float, installments_amount: float,
                 balance: float):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        self.installments_amount = installments_amount
        self.balance = balance


class TransactionRefundResponse(object):
    def __init__(self, type: str, authorization_code: str, authorization_date: str, nullified_amount: float,
                 balance: float, response_code: str):
        self.type = type
        self.authorization_code = authorization_code
        self.authorization_date = authorization_date
        self.nullified_amount = nullified_amount
        self.balance = balance
        self.response_code = response_code
