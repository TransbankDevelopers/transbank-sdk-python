from typing import List

from transbank.common.model import CardDetail


class TransactionStatusResponse(object):
    def __init__(self, amount: float, status: str, buy_order: str, session_id: str, 
                 accounting_date: str, transaction_date: str, installments_number: int, 
                 payment_type_code: str = None, card_detail: dict = None,
                 installments_amount: float = None, authorization_code: str = None,
                 balance: float = None, vci: str = None, response_code: int = None):
        self.vci = vci
        self.amount = amount
        self.status = status
        self.buy_order = buy_order
        self.session_id = session_id
        if card_detail is not None:
            self.card_detail = CardDetail(**card_detail)
        else:
            self.card_detail = {}
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
    def __init__(self, amount: float, status: str, buy_order: str, session_id: str, card_detail: dict,
                 accounting_date: str, transaction_date: str, authorization_code: str, payment_type_code: str,
                 response_code: int, installments_number: int, vci: str = None):
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


class MallTransactionCreateResponse(TransactionCreateResponse):
    def __repr__(self):
        return "MallTransactionCreateResponse(token: {}, url: {})".format(self.token, self.url)


class MallDetails(object):
    def __init__(self, amount: float, status: str, installments_number: int, commerce_code: str, buy_order: str,
                 authorization_code: str = None, payment_type_code: str  = None, response_code: int = None):
        self.amount = amount
        self.status = status
        self.authorization_code = authorization_code
        self.payment_type_code = payment_type_code
        self.response_code = response_code
        self.installments_number = installments_number
        self.commerce_code = commerce_code
        self.buy_order = buy_order

    def __repr__(self):
        return "MallDetails(amount: {}, status: {}, authorization_code: {}, payment_type_code: {}, response_code: {}," \
               " installments_number: {}, commerce_code: {}, buy_order: {})"\
            .format(self.amount, self.status, self.authorization_code, self.payment_type_code, self.response_code,
                    self.installments_number, self.commerce_code, self.buy_order)


class MallTransactionCommitResponse(object):
    details = list()

    def __init__(self, details: list, buy_order: str, session_id: str, 
                 accounting_date: str, transaction_date: str,
                 vci: str = None, card_detail: dict = None):
        self.vci = vci
        for item in details:
            self.details.append(MallDetails(**item))
        self.buy_order = buy_order
        self.session_id = session_id
        if card_detail is not None:
            self.card_detail = CardDetail(**card_detail)
        else:
            self.card_detail = {}
        self.accounting_date = accounting_date
        self.transaction_date = transaction_date

    def __repr__(self):
        return "MallTransactionCommitResponse(vci: {}, details: {}, buy_order: {}, self.session_id: {}, " \
               "card_detail: {}, accounting_date: {}, transaction_date: {})"\
            .format(self.vci, self.details, self.buy_order, self.session_id, self.card_detail, self.accounting_date,
                    self.transaction_date)


class DeferredTransactionResponse(object):
    def __init__(self, authorization_code: str, authorization_date: str, captured_amount: float, response_code: str ):
        self.authorization_code = authorization_code
        self.authorization_date = authorization_date
        self.captured_amount = captured_amount
        self.response_code = response_code

    def __repr__(self):
        return "DeferredTransactionResponse(authorization_code: {}, authorization_date: {}, captured_amount: {}, " \
                "response_code: {})" \
            .format(self.authorization_code, self.authorization_date, self.captured_amount, self.response_code )
