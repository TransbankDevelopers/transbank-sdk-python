class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, return_url: str):
        self.buy_order = buy_order
        self.session_id = session_id
        self.amount = amount
        self.return_url = return_url

    def __repr__(self):
        return "TransactionCreateRequest(buy_order: {}, session_id: {}, amount: {}, return_url: {})".format(
            self.buy_order, self.session_id, self.amount, self.return_url)


class TransactionRefundRequest(object):
    def __init__(self, amount: float):
        self.amount = amount

    def __repr__(self):
        return "TransactionRefundRequest(amount: {})".format(self.amount)

