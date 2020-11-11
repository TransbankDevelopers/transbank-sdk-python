from transbank.common.model import CardDetail


class InscriptionStartResponse(object):
    def __init__(self, token: str, url_webpay: str):
        self.token = token
        self.url_webpay = url_webpay

    def __repr__(self):
        return "token: {}, url_webpay: {}".format(self.token, self.url_webpay)


class InscriptionFinishResponse(object):
    def __init__(self, response_code: int, tbk_user: str = None, authorization_code: str = None,
                 card_type: str = None, card_number: str = None):
        self.response_code = response_code
        self.tbk_user = tbk_user
        self.authorization_code = authorization_code
        self.card_type = card_type
        self.card_number = card_number

    def __repr__(self):
        return "response_code: {}, tbk_user: {}, authorization_code: {}, card_type: {}, " \
               "card_number: " \
               "{}".format(self.response_code, self.tbk_user, self.authorization_code, self.card_type,
                           self.card_number)


class TransactionAuthorizeResponse(object):
    def __init__(self,
                 transaction_date: str,
                 accounting_date: str,
                 card_detail: CardDetail,
                 buy_order: str,
                 details: list
                 ):
        self.transaction_date = transaction_date
        self.accounting_date = accounting_date
        self.card_detail = card_detail
        self.buy_order = buy_order
        self.details = details

    def __repr__(self):
        return "transaction_date: {}, accounting_date: {}, card_detail: {}, buy_order: {}, " \
               "details: " \
               "{}".format(self.transaction_date, self.accounting_date, self.card_detail, self.buy_order,
                           self.details)


class TransactionRefundResponse(object):
    def __init__(self,
                 type: str,
                 balance: float = None,
                 response_code: int = None,
                 nullified_amount: float = None,
                 authorization_code: str = None,
                 authorization_date: str = None

                 ):
        self.type = type
        self.balance = balance
        self.authorization_code = authorization_code
        self.response_code = response_code
        self.authorization_date = authorization_date
        self.nullified_amount = nullified_amount

    def __repr__(self):
        return "type: {}, balance: {}, authorization_code: {}, response_code: {}, " \
               "authorization_date: {}, nullified_amount: {} " \
            .format(self.type, self.balance, self.authorization_code, self.response_code,
                    self.authorization_date, self.nullified_amount)


class TransactionStatusResponse(object):
    def __init__(self,
                 buy_order: str,
                 card_detail: CardDetail,
                 accounting_date: str,
                 transaction_date: str,
                 details: list
                 ):
        self.buy_order = buy_order
        self.card_detail = card_detail
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date
        self.details = details

    def __repr__(self):
        return "buy_order: {}, card_detail: {}, accounting_date: {}, transaction_date: {}, " \
               "details: " \
               "{}".format(self.buy_order, self.card_detail, self.accounting_date, self.transaction_date,
                           self.details)
