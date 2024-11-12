import unittest
import json
from unittest.mock import Mock
from transbank.webpay.oneclick.mall_transaction import *
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from tests.mocks.responses_api_mocks import responses
from unittest.mock import patch
from tests.webpay.test_utils import get_invalid_length_param


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
        self.transaction = MallTransaction.build_for_integration(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY)
        self.deferred_transaction = MallTransaction.build_for_integration(IntegrationCommerceCodes.ONECLICK_MALL_DEFERRED, IntegrationApiKeys.WEBPAY)
        self.deferred_child_commerce_code = IntegrationCommerceCodes.ONECLICK_MALL_DEFERRED_CHILD1
        self.capture_amount_mock = 2000
        self.authorization_code_mock = '123456'

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
    def test_deferred_authorize_transaction_successful(self, mock_post):
        details = MallTransactionAuthorizeDetails(
            self.deferred_child_commerce_code, self.child2_buy_order_mock, self.installments_number_mock,
            self.amount2_mock)
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['deferred_authorize_response'])
        mock_post.return_value = self.mock_response

        response = self.deferred_transaction.authorize(self.username_mock, self.tbk_user_mock,
                                                       self.parent_buy_order_mock, details)

        self.assertEqual(response, responses['deferred_authorize_response'])

    @patch('transbank.common.request_service.requests.post')
    def test_authorize_exception(self, mock_post):
        self.mock_response.status_code = 500
        self.mock_response.text = json.dumps(responses['general_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionAuthorizeError) as context:
            self.transaction.authorize(self.username_mock, self.tbk_user_mock, self.parent_buy_order_mock,
                                       self.get_mall_transaction_details())

        self.assertTrue('Internal server error' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionAuthorizeError)

    def test_authorize_exception_username_max_length(self):
        invalid_username = get_invalid_length_param()
        with self.assertRaises(TransbankError) as context:
            self.transaction.authorize(invalid_username, self.tbk_user_mock, self.parent_buy_order_mock,
                                       self.get_mall_transaction_details())

        self.assertTrue("'username' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_authorize_exception_tbk_user_max_length(self):
        invalid_tbk_user = get_invalid_length_param()
        with self.assertRaises(TransbankError) as context:
            self.transaction.authorize(self.username_mock, invalid_tbk_user, self.parent_buy_order_mock,
                                       self.get_mall_transaction_details())

        self.assertTrue("'tbk_user' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_authorize_exception_buy_order_max_length(self):
        invalid_parent_buy_order = get_invalid_length_param()
        with self.assertRaises(TransbankError) as context:
            self.transaction.authorize(self.username_mock, self.tbk_user_mock, invalid_parent_buy_order,
                                       self.get_mall_transaction_details())

        self.assertTrue("'parent_buy_order' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_authorize_exception_child_commerce_code_max_length(self):
        invalid_child_commerce_code = get_invalid_length_param()
        details = MallTransactionAuthorizeDetails(
            invalid_child_commerce_code, self.child1_buy_order_mock, self.installments_number_mock, self.amount1_mock)

        with self.assertRaises(TransbankError) as context:
            self.transaction.authorize(self.username_mock, self.tbk_user_mock, self.parent_buy_order_mock,
                                       details)

        self.assertTrue("'details.commerce_code' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_authorize_exception_child_buy_order_max_length(self):
        invalid_child_buy_order = get_invalid_length_param()
        details = MallTransactionAuthorizeDetails(
            self.child1_commerce_code, invalid_child_buy_order, self.installments_number_mock, self.amount1_mock)

        with self.assertRaises(TransbankError) as context:
            self.transaction.authorize(self.username_mock, self.tbk_user_mock, self.parent_buy_order_mock,
                                       details)

        self.assertTrue("'details.buy_order' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.put')
    def test_capture_transaction_successful(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['capture_response'])
        mock_put.return_value = self.mock_response

        response = self.deferred_transaction.capture(self.deferred_child_commerce_code, self.child2_buy_order_mock,
                                                     self.authorization_code_mock, self.capture_amount_mock)

        self.assertEqual(response, responses['capture_response'])

    @patch('transbank.common.request_service.requests.put')
    def test_capture_exception(self, mock_put):
        self.mock_response.status_code = 500
        self.mock_response.text = json.dumps(responses['general_error'])
        mock_put.return_value = self.mock_response

        with self.assertRaises(TransactionCaptureError) as context:
            self.deferred_transaction.capture(self.deferred_child_commerce_code, self.child2_buy_order_mock,
                                              self.authorization_code_mock, self.capture_amount_mock)

        self.assertTrue('Internal server error' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionCaptureError)

    def test_capture_exception_child_commerce_code_max_length(self):
        invalid_child_commerce_code = get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.deferred_transaction.capture(invalid_child_commerce_code, self.child2_buy_order_mock,
                                              self.authorization_code_mock, self.capture_amount_mock)

        self.assertTrue("'child_commerce_code' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_capture_exception_child_buy_order_max_length(self):
        invalid_child_buy_order = get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.deferred_transaction.capture(self.deferred_child_commerce_code, invalid_child_buy_order,
                                              self.authorization_code_mock, self.capture_amount_mock)

        self.assertTrue("'child_buy_order' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_capture_exception_authorizatioon_code_max_length(self):
        invalid_authorization_code = get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.deferred_transaction.capture(self.deferred_child_commerce_code, self.child2_buy_order_mock,
                                              invalid_authorization_code, self.capture_amount_mock)

        self.assertTrue("'authorization_code' is too long" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.get')
    def test_status_transaction_successful(self, mock_get):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['captured_status_response'])
        mock_get.return_value = self.mock_response

        response = self.deferred_transaction.status(self.child2_buy_order_mock)

        self.assertTrue(response['details'][0]['status'], 'CAPTURED')
        self.assertEqual(response, responses['captured_status_response'])

    @patch('transbank.common.request_service.requests.get')
    def test_status_exception(self, mock_get):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['buy_order_not_found'])
        mock_get.return_value = self.mock_response

        with self.assertRaises(TransactionStatusError) as context:
            self.deferred_transaction.status('FakeBuyOrder')

        self.assertTrue("buy order not found" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionStatusError)

    @patch('transbank.common.request_service.requests.post')
    def test_refund_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['reversed_response'])
        mock_post.return_value = self.mock_response

        response = self.deferred_transaction.refund(self.parent_buy_order_mock, self.deferred_child_commerce_code,
                                                    self.child2_buy_order_mock, self.amount2_mock)

        self.assertTrue(response['type'], 'REVERSED')

    @patch('transbank.common.request_service.requests.post')
    def test_refund_exception(self, mock_post):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['already_refunded_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionRefundError) as context:
            self.deferred_transaction.refund(self.parent_buy_order_mock, self.deferred_child_commerce_code,
                                             self.child2_buy_order_mock, self.amount2_mock)

        self.assertTrue("Transaction already fully refunded" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionRefundError)
