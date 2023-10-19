import unittest
import json
import string
import secrets
from unittest.mock import Mock
from transbank.webpay.oneclick.mall_transaction import *
from tests.mocks.responses_api_mocks import responses
from unittest.mock import patch


class OneclickMallTransactionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.username_mock = 'test_user'
        self.tbk_user_mock = '08ed03b1-8fa6-4d7b-b35c-b134e1c5e9ee'
        self.parent_buy_order_mock = 'parent_buy_order'
        self.installments_number_mock = 0
        self.child1_commerce_code = IntegrationCommerceCodes.ONECLICK_MALL_CHILD1
        self.amount1_mock = 1000
        self.child1_buy_order_mock = 'child_buy_order_1'
        self.child2_commerce_code = IntegrationCommerceCodes.ONECLICK_MALL_CHILD2
        self.amount2_mock = 2000
        self.child2_buy_order_mock = 'child_buy_order_2'
        self.return_url_mock = 'https://url_return.com'
        self.mock_response = Mock()
        self.transaction = MallTransaction()

    def test_authorize_details(self):
        mall_details = MallTransactionAuthorizeDetails(self.child1_commerce_code, self.child1_buy_order_mock,
                                                       self.installments_number_mock, self.amount1_mock)

        details = mall_details.add(self.child2_commerce_code, self.child2_buy_order_mock,
                                   self.installments_number_mock, self.amount2_mock)

        self.assertEqual(details.details[0].commerce_code, self.child1_commerce_code)
        self.assertEqual(details.details[0].buy_order, self.child1_buy_order_mock)
        self.assertEqual(details.details[0].installments_number, self.installments_number_mock)
        self.assertEqual(details.details[0].amount, self.amount1_mock)
        self.assertEqual(details.details[1].commerce_code, self.child2_commerce_code)
        self.assertEqual(details.details[1].buy_order, self.child2_buy_order_mock)
        self.assertEqual(details.details[1].installments_number, self.installments_number_mock)
        self.assertEqual(details.details[1].amount, self.amount2_mock)

    def get_mall_transaction_details(self):
        details = MallTransactionAuthorizeDetails(
            self.child1_commerce_code, self.child1_buy_order_mock, self.installments_number_mock, self.amount1_mock)
        return details

    @patch('transbank.common.request_service.requests.post')
    def test_authorize_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['authorize_response'])
        mock_post.return_value = self.mock_response

        response = self.transaction.authorize(self.username_mock, self.tbk_user_mock, self.parent_buy_order_mock,
                                              self.get_mall_transaction_details())

        self.assertEqual(response, responses['authorize_response'])

    @patch('transbank.common.request_service.requests.post')
    def test_create_mall_exception_not_authorized(self, mock_post):
        self.mock_response.status_code = 500
        self.mock_response.text = json.dumps(responses['general_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionAuthorizeError) as context:
            self.transaction.authorize(self.username_mock, self.tbk_user_mock, self.parent_buy_order_mock,
                                       self.get_mall_transaction_details())

        self.assertTrue('Internal server error' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionAuthorizeError)
