from transbank.common.model import CardDetail


class TransactionCreateResponse(object):
    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return "token: {}".format(self.token)


class TransactionCommitResponse(object):
    def __init__(self,
                 buy_order: str,
                 session_id: str,
                 card_detail: CardDetail,
                 accounting_date: str,
                 transaction_date: str,
                 details: list,
                 expiration_date: str = None
                 ):
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.expiration_date = expiration_date
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.details = details


class TransactionStatusResponse(object):
    def __init__(self,
                 buy_order: str,
                 session_id: str,
                 card_detail: CardDetail,
                 accounting_date: str,
                 transaction_date: str,
                 details: list,
                 expiration_date: str = None
                 ):
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_detail = card_detail
        self.expiration_date = expiration_date
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.details = details

    def __repr__(self):
        return """
        buy_order: {},
        session_id: {},
        card_detail: {},
        expiration_date: {},
        accounting_date: {},
        transaction_date: {},
        details: {}
        """.format(self.buy_order,
                   self.session_id,
                   self.card_detail,
                   self.expiration_date,
                   self.accounting_date,
                   self.transaction_date,
                   self.details)


class TransactionRefundResponse(object):
    def __init__(self, type: str, authorization_code: str = None, authorization_date: str = None,
                 nullified_amount: float = None,
                 balance: float = None, response_code: str = None):
        self.type = type
        self.authorization_code = authorization_code
        self.authorization_date = authorization_date
        self.nullified_amount = nullified_amount
        self.balance = balance
        self.response_code = response_code

    def __repr__(self):
        return """
        type: {},
        authorization_code: {},
        authorization_date: {},
        nullified_amount: {},
        balance: {},
        response_code: {}
        """.format(self.type, self.authorization_code, self.authorization_date, self.nullified_amount, self.balance,
                   self.response_code)


class TransactionCaptureResponse(object):
    def __init__(self, authorization_code: str, authorization_date: str,
                 captured_amount: float, response_code: str):
        self.authorization_code = authorization_code
        self.authorization_date = authorization_date
        self.captured_amount = captured_amount
        self.response_code = response_code

    def __repr__(self):
        return """
        authorization_code: {},
        authorization_date: {},
        captured_amount: {},
        response_code: {}
        """.format(self.authorization_code, self.authorization_date, self.captured_amount, self.response_code)


class TransactionInstallmentsResponse(object):
    def __init__(self, installments_amount: float, id_query_installments: str, deferred_periods: str):
        self.installments_amount = installments_amount
        self.id_query_installments = id_query_installments
        self.deferred_periods = deferred_periods

    def __repr__(self):
        return """
        installments_amount: {},
        id_query_installments: {},
        deferred_periods: {}
        """.format(self.installments_amount, self.id_query_installments, self.deferred_periods)
