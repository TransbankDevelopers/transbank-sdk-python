from transbank.common.response import CardDetail


class TransactionCreateResponse(object):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def __repr__(self):
        return "token: {}, url: {}".format(self.token, self.url)


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
