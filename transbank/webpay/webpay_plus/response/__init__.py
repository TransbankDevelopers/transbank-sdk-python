from transbank.common.model import CardDetail


class TransactionStatusResponse(object):
    def __init__(self, vci: str, amount: float, status: str, buy_order: str, session_id: str, card_detail: dict,
                 accounting_date: str, transaction_date: str, authorization_code: str, payment_type_code: str,
                 response_code: int, installments_number: int, installments_amount: float = None,
                 balance: float = None):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = CardDetail(**card_detail)
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        self.installments_amount = installments_amount
        self.balance = balance

    def __repr__(self):
        return "TransactionStatusResponse(vci: {}, amount: {}, status: {}, buy_order: {}, session_id: {}, " \
               "card_detail: {}, accounting_date: {}, transaction_date: {}, authorization_code: {}, " \
               "payment_type_code: {}, response_code: {}, installments_number: {}, installments_amount: {}, " \
               "balance: {})" \
            .format(self.vci, self.amount, self.status, self.buy_order, self.session_id, self.card_detail,
                    self.accounting_date, self.transaction_date, self.authorization_code, self.payment_type_code,
                    self.response_code, self.installments_number, self.installments_amount, self.balance)


class TransactionCommitResponse(object):
    def __init__(self, vci: str, amount: float, status: str, buy_order: str, session_id: str, card_detail: dict,
                 accounting_date: str, transaction_date: str, authorization_code: str, payment_type_code: str,
                 response_code: int, installments_number: int):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = CardDetail(**card_detail)
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number

    def __repr__(self):
        return """
        vci: {},
        amount: {},
        status: {},
        buy_order: {},
        session_id: {}
        card_detail: {},
        accounting_date: {},
        transaction_date: {},
        authorization_code: {},
        payment_type_code: {},
        response_code: {},
        installments_nmumber: {}
        """.format(self.vci,
                   self.amount,
                   self.status,
                   self.buy_order,
                   self.session_id,
                   self.card_detail,
                   self.accounting_date,
                   self.transaction_date,
                   self.authorization_code,
                   self.payment_type_code,
                   self.response_code,
                   self.installments_number)


class TransactionCreateResponse(object):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def __repr__(self):
        return "TransactionCreateResponse(token: {}, url: {})".format(self.token, self.url)


class TransactionRefundResponse(object):
    def __init__(self, type: str, balance: float = None, authorization_code: str = None, response_code: int = None,
                 authorization_date: str = None, nullified_amount: float = None):
        self.type = type
        self.balance = balance
        self.authorization_code = authorization_code
        self.response_code = response_code
        self.authorization_date = authorization_date
        self.nullified_amount = nullified_amount

    def __repr__(self):
        return "TransactionRefundResponse(type: {}, balance: {}, authorization_code: {}, response_code: {}, " \
               "authorization_date: {}, nullified_amount: {})".format(self.type, self.balance, self.authorization_code,
                                                                      self.response_code, self.authorization_date,
                                                                      self.nullified_amount)
