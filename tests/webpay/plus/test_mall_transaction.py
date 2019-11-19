import unittest
import random
from transbank.webpay.webpay_plus.mall_transaction import *
from transbank.webpay.webpay_plus import mall_default_child_commerce_codes
class TransactionTestCase(unittest.TestCase):

    buy_order_mock = str(random.randrange(1000000, 99999999))
    session_id_mock = str(random.randrange(1000000, 99999999))
    return_url_mock = "https://url_return.com"

    def get_random_str(self):
        return str(random.randrange(1000000, 99999999))

    def get_mall_transaction_details(self):
        commerce_code_child_1 = mall_default_child_commerce_codes[0]
        buy_order_child_1 = self.get_random_str()
        amount_child_1 = self.get_random_str()

        commerce_code_child_2 = mall_default_child_commerce_codes[1]
        buy_order_child_2 = self.get_random_str()
        amount_child_2 = self.get_random_str()

        details = MallTransactionCreateDetails(amount_child_1, commerce_code_child_1, buy_order_child_1) \
            .add(amount_child_2, commerce_code_child_2, buy_order_child_2)
        return details

    def test_when_transaction_create(self):
        response = MallTransaction.create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            return_url=self.return_url_mock,
            details=self.get_mall_transaction_details()
        )
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

