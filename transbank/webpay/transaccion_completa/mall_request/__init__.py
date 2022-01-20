class TransactionCommitRequest(object):
    def __init__(self, details: list):
        self.details = self.commit_details(details)

    def commit_details(self, details: list) -> list:
        return [{
            "commerce_code": detail['commerce_code'],
            "buy_order": detail['buy_order'],
            "id_query_installments": detail['id_query_installments'],
            "deferred_period_index": detail['deferred_period_index'],
            "grace_period": detail['grace_period']
        } for detail in details]


class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, card_number: str, card_expiration_date: str, details: list, cvv: str):
        self.buy_order = buy_order
        self.session_id = session_id
        self.card_number = card_number
        self.card_expiration_date = card_expiration_date
        self.details = self.create_details(details)
        self.cvv = cvv

    def create_details(self, details: list) -> list:
        return [
            {
                "amount": detail["amount"],
                "commerce_code": detail["commerce_code"],
                "buy_order": detail["buy_order"]
            } for detail in details
        ]


class TransactionStatusRequest(object):
    def __init__(self, token: str):
        self.token = token


class TransactionRefundRequest(object):
    def __init__(self, commerce_code: str, buy_order: str, amount: float):
        self.buy_order = buy_order
        self.commerce_code = commerce_code
        self.amount = amount


class TransactionCaptureRequest(object):
    def __init__(self, commerce_code: str, buy_order: str, authorization_code: str, capture_amount: float):
        self.commerce_code = commerce_code
        self.buy_order= buy_order
        self.authorization_code = authorization_code
        self.capture_amount = capture_amount


class TransactionInstallmentsRequest(object):
    def __init__(self, installments_number: float, buy_order: str, commerce_code: str):
        self.installments_number = installments_number
        self.buy_order = buy_order
        self.commerce_code = commerce_code
