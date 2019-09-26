class TransactionCommitRequest(object):
    def __init__(self, id_query_installments: str, deferred_periods_index: str, grace_period: str):
        self.id_query_installments = id_query_installments
        self.deferred_periods_index = deferred_periods_index
        self.grace_period = grace_period


class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, card_number: str, cvv: str,
                 card_expiration_date: str):
        self.buy_order = buy_order
        self.session_id = session_id
        self.amount = amount
        self.card_number = card_number
        self.cvv = cvv
        self.card_expiration_date = card_expiration_date


class TransactionStatusRequest(object):
    def __init__(self, token: str):
        self.token = token


class TransactionRefundRequest(object):
    def __init__(self, amount: float):
        self.amount = amount
