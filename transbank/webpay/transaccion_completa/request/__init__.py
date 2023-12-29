from transbank.validators.amount_validator import AmountValidator

class TransactionCommitRequest(object):
    def __init__(self, id_query_installments: str, deferred_period_index: float, grace_period):
        self.id_query_installments = id_query_installments
        self.deferred_period_index = deferred_period_index
        if type(grace_period) == bool:
            grace_p = grace_period
        else:
            grace_p = grace_period == 'True'
        self.grace_period = str(grace_p).lower()


class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, card_number: str, cvv: str,
                 card_expiration_date: str):
        AmountValidator.validate(amount)
        self.buy_order = buy_order
        self.session_id = session_id
        self.amount = amount
        self.card_number = card_number
        self.cvv = cvv
        self.card_expiration_date = card_expiration_date

class TransactionRefundRequest(object):
    def __init__(self, amount: float):
        self.amount = amount

class TransactionCaptureRequest(object):
    def __init__(self, buy_order: str, authorization_code: str, capture_amount: float):
        self.buy_order = buy_order
        self.authorization_code = authorization_code
        self.capture_amount = capture_amount

class TransactionInstallmentsRequest(object):
    def __init__(self, installments_number: float):
        self.installments_number = installments_number
