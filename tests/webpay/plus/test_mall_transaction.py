import unittest
import random
from unittest.mock import Mock
from transbank.webpay.webpay_plus.mall_transaction import *
from transbank.webpay.webpay_plus.request import *
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes


class TransactionMallTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mall_buy_order_mock = 'mall_buy_order_mock_123'
        self.session_id_mock = 'session_id_mock_123456789'
        self.return_url_mock = "https://url_return.com"
        self.amount1_mock = 1000
        self.child1_commerce_code = IntegrationCommerceCodes.WEBPAY_PLUS_MALL_CHILD1
        self.child1_buy_order = 'child_buy_order1_mock_123'
        self.amount2_mock = 2000
        self.child2_commerce_code = IntegrationCommerceCodes.WEBPAY_PLUS_MALL_CHILD2
        self.child2_buy_order = 'child_buy_order2_mock_123'
        self.token_mock = '01abf2be20aad1da804aeae1ed3062fb8fba108ee0e07f4d37181f51c3f6714d'
        self.mock_response = Mock()
        self.transaction = MallTransaction()
        self.invalid_amount = -1000
        self.authorization_code_mock = '123456'

    def get_mall_transaction_details(self):
        commerce_code_child_1 = IntegrationCommerceCodes.WEBPAY_PLUS_MALL_CHILD1
        buy_order_child_1 = self.get_random_str()
        amount_child_1 = self.get_random_str()

        commerce_code_child_2 = IntegrationCommerceCodes.WEBPAY_PLUS_MALL_CHILD2
        buy_order_child_2 = self.get_random_str()
        amount_child_2 = self.get_random_str()

        details = MallTransactionCreateDetails(amount_child_1, commerce_code_child_1, buy_order_child_1) \
            .add(amount_child_2, commerce_code_child_2, buy_order_child_2)
        return details

    def test_when_transaction_create(self):
        response = MallTransaction().create(
            buy_order=self.get_random_str(),
            session_id=self.get_random_str(),
            return_url=self.return_url_mock,
            details=self.get_mall_transaction_details()
        )
        self.assertIsNotNone(response['url'])
        self.assertIsNotNone(response['token'])

    # These can't be tested until we have a mock URL
    # def test_when_transaction_commit(self):
    #     response = MallTransaction.commit(token=self.token_mock)
    #     self.assertIsNotNone(response.vci)
    #     self.assertIsNotNone(response.details[0].amount)
    #     self.assertIsNotNone(response.details[0].status)
    #     self.assertIsNotNone(response.details[0].authorization_code)
    #     self.assertIsNotNone(response.details[0].response_code)
    #     self.assertIsNotNone(response.details[0].installments_number)
    #     self.assertIsNotNone(response.details[0].commerce_code)
    #     self.assertIsNotNone(response.details[1].amount)
    #     self.assertIsNotNone(response.details[1].status)
    #     self.assertIsNotNone(response.details[1].authorization_code)
    #     self.assertIsNotNone(response.details[1].response_code)
    #     self.assertIsNotNone(response.details[1].installments_number)
    #     self.assertIsNotNone(response.details[1].commerce_code)

    # def test_when_transaction_refund(self):
    #     response = MallTransaction.refund(token=self.token_mock, amount=1, \
    #                                       child_commerce_code=mall_default_child_commerce_codes[0], \
    #                                       child_buy_order=self.buy_order_child_refund_mock)
    #     self.assertIsNotNone(response.type)
    #     self.assertIsNotNone(response.balance)
    #     self.assertIsNotNone(response.authorization_code)
    #     self.assertIsNotNone(response.response_code)
    #     self.assertIsNotNone(response.authorization_date)
    #     self.assertIsNotNone(response.nullified_amount)
    #     return response

    # def test_when_transaction_status(self):
    #     response = MallTransaction.status(token=self.token_mock)
    #     self.assertIsNotNone(response.vci)
    #     self.assertIsNotNone(response.details[0].amount)
    #     self.assertIsNotNone(response.details[0].status)
    #     self.assertIsNotNone(response.details[0].authorization_code)
    #     self.assertIsNotNone(response.details[0].response_code)
    #     self.assertIsNotNone(response.details[0].installments_number)
    #     self.assertIsNotNone(response.details[0].commerce_code)
    #     self.assertIsNotNone(response.details[1].amount)
    #     self.assertIsNotNone(response.details[1].status)
    #     self.assertIsNotNone(response.details[1].authorization_code)
    #     self.assertIsNotNone(response.details[1].response_code)
    #     self.assertIsNotNone(response.details[1].installments_number)
    #     self.assertIsNotNone(response.details[1].commerce_code)

