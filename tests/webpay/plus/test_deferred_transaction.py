import unittest
import random
import requests_mock
from transbank.webpay.webpay_plus.deferred_transaction import *


class TransactionDeferredTestCase(unittest.TestCase):

    buy_order_mock = str(random.randrange(1000000, 99999999))
    session_id_mock = str(random.randrange(1000000, 99999999))
    amount_mock = random.randrange(1000000, 99999999)
    return_url_mock = "https://url_return.com"
    token_mock = 'e8dd746d0867aa0035bb9fa48c398b4824b74f26b167b924e08315baca967d6f'

    def test_when_deferred_transaction_create(self):
        response = DeferredTransaction.create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            amount=self.amount_mock,
            return_url=self.return_url_mock,
        )
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)


