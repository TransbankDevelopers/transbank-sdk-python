class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, card_number: str, cvv: str,
                 card_expiration_date: str):
        self.buy_order = buy_order
        self.session_id = session_id
        self.amount = amount
        self.card_number = card_number
        self.cvv = cvv
        self.card_expiration_date = card_expiration_date

