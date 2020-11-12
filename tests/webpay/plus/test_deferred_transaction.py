import unittest
import random
import requests_mock
from transbank.webpay.webpay_plus.deferred_transaction import *


class TransactionDeferredTestCase(unittest.TestCase):

    buy_order_mock = str(random.randrange(1000000, 99999999))
    session_id_mock = str(random.randrange(1000000, 99999999))
    amount_mock = random.randrange(1000, 999999)
    return_url_mock = "https://url_return.com"
    token_mock = 'e547ea9ddf27ac6c9b9691ccc399921ddd67d4264467bc7e925a294dad16b244'

    def test_when_deferred_transaction_create(self):
        response = DeferredTransaction.create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            amount=self.amount_mock,
            return_url=self.return_url_mock,
        )
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

    # These can't be tested until we have a mock URL
    # def test_when_deferred_transaction_commit(self):
    #     response = DeferredTransaction.status(token=self.token_mock)
    #     self.assertIsNotNone(response.vci)
    #     self.assertIsNotNone(response.amount)
    #     self.assertIsNotNone(response.status)
    #     self.assertIsNotNone(response.buy_order)
    #     self.assertIsNotNone(response.session_id)
    #     self.assertIsNotNone(response.card_detail.card_number)
    #     self.assertIsNotNone(response.accounting_date)
    #     self.assertIsNotNone(response.transaction_date)
    #     self.assertIsNotNone(response.authorization_code)
    #     self.assertIsNotNone(response.payment_type_code)
    #     self.assertIsNotNone(response.response_code)
    #     self.assertIsNotNone(response.installments_number)

    #     return response

    # def test_when_deferred_transaction_status(self):
    #     response = DeferredTransaction.status(token=self.token_mock)
    #     self.assertIsNotNone(response.vci)
    #     self.assertIsNotNone(response.amount)
    #     self.assertIsNotNone(response.status)
    #     self.assertIsNotNone(response.buy_order)
    #     self.assertIsNotNone(response.session_id)
    #     self.assertIsNotNone(response.card_detail.card_number)
    #     self.assertIsNotNone(response.accounting_date)
    #     self.assertIsNotNone(response.transaction_date)
    #     self.assertIsNotNone(response.authorization_code)
    #     self.assertIsNotNone(response.payment_type_code)
    #     self.assertIsNotNone(response.response_code)
    #     self.assertIsNotNone(response.installments_number)
