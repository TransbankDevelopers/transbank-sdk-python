import unittest
import json
import secrets
import string
from unittest.mock import Mock
from unittest.mock import patch
from transbank.webpay.webpay_plus.mall_transaction import *
from transbank.webpay.webpay_plus.request import *
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from tests.mocks.responses_api_mocks import responses
from transbank.error.transaction_create_error import TransactionCreateError


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
        self.transaction = MallTransaction.build_for_integration(IntegrationCommerceCodes.WEBPAY_PLUS_MALL, IntegrationApiKeys.WEBPAY)
        self.invalid_amount = -1000
        self.authorization_code_mock = '123456'
        self.deferred_capture = MallTransaction.build_for_integration(IntegrationCommerceCodes.WEBPAY_PLUS_MALL_DEFERRED, IntegrationApiKeys.WEBPAY)

    def test_create_details(self):
        mall_details = MallDetails(self.amount1_mock, self.child1_commerce_code, self.child1_buy_order)

        details = MallTransactionCreateDetails(mall_details.amount, mall_details.commerce_code, mall_details.buy_order).\
            add(self.amount2_mock, self.child2_commerce_code, self.child2_buy_order)

        self.assertEqual(details.details[0].amount, self.amount1_mock)
        self.assertEqual(details.details[0].commerce_code, self.child1_commerce_code)
        self.assertEqual(details.details[0].buy_order, self.child1_buy_order)
        self.assertEqual(details.details[1].amount, self.amount2_mock)
        self.assertEqual(details.details[1].commerce_code, self.child2_commerce_code)
        self.assertEqual(details.details[1].buy_order, self.child2_buy_order)

    def get_mall_transaction_details(self):
        details = MallTransactionCreateDetails(self.amount1_mock, self.child1_commerce_code, self.child1_buy_order) \
            .add(self.amount2_mock, self.child2_commerce_code, self.child2_buy_order)
        return details

    @patch('transbank.common.request_service.requests.post')
    def test_create_mall_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['create_response'])
        mock_post.return_value = self.mock_response

        response = self.transaction.create(self.mall_buy_order_mock, self.session_id_mock, self.return_url_mock,
                                           self.get_mall_transaction_details())

        self.assertEqual(response, responses['create_response'])

    @patch('transbank.common.request_service.requests.post')
    def test_create_mall_exception_not_authorized(self, mock_post):
        self.mock_response.status_code = 401
        self.mock_response.text = json.dumps(responses['create_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionCreateError) as context:
            self.transaction.create(self.mall_buy_order_mock, self.session_id_mock, self.return_url_mock,
                                    self.get_mall_transaction_details())

        self.assertTrue('Not Authorized' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionCreateError)

    def test_create_mall_exception_buy_order_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.mall_buy_order_mock+'too_long', self.session_id_mock, self.return_url_mock,
                                    self.get_mall_transaction_details())

        self.assertTrue("'buy_order' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_mall_exception_session_id_max_length(self):
        valid_string = string.ascii_letters + string.digits + "-._~"
        too_long_session_id = ''.join(secrets.choice(valid_string) for _ in range(ApiConstants.SESSION_ID_LENGTH + 1))

        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.mall_buy_order_mock, too_long_session_id, self.return_url_mock,
                                    self.get_mall_transaction_details())

        self.assertTrue("'session_id' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_mall_exception_return_url_max_length(self):
        valid_string = string.ascii_letters + string.digits + "-._~"
        too_long_url = ''.join(secrets.choice(valid_string) for _ in range(ApiConstants.RETURN_URL_LENGTH + 1))
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.mall_buy_order_mock, self.session_id_mock, too_long_url,
                                    self.get_mall_transaction_details())

        self.assertTrue("'return_url' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_mall_exception_child_buy_order_max_length(self):
        valid_string = string.ascii_letters + string.digits + "-._~"
        invalid_child_buy_order = ''.join(secrets.choice(valid_string)
                                          for _ in range(ApiConstants.BUY_ORDER_LENGTH + 1))

        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.mall_buy_order_mock, self.session_id_mock, self.return_url_mock,
                                    MallTransactionCreateDetails(self.amount1_mock, self.child1_commerce_code,
                                                                 invalid_child_buy_order))

        self.assertTrue("'details.buy_order' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_mall_exception_commerce_code_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.mall_buy_order_mock, self.session_id_mock, self.return_url_mock,
                                    MallTransactionCreateDetails(self.amount1_mock, self.child1_commerce_code+'123',
                                                                 self.child1_buy_order))

        self.assertTrue("'details.commerce_code' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.put')
    def test_commit_mall_transaction_successful(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['commit_mall'])
        mock_put.return_value = self.mock_response

        response = self.transaction.commit(self.token_mock)

        self.assertIn('details', response)
        self.assertGreaterEqual(len(response['details']), 2)

        for detail in response['details']:
            self.assertEqual(detail['response_code'], 0)

    @patch('transbank.common.request_service.requests.put')
    def test_commit_mall_exception_when_authorized(self, mock_put):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['commit_error'])
        mock_put.return_value = self.mock_response

        with self.assertRaises(TransactionCommitError) as context:
            self.transaction.commit(self.token_mock)

        self.assertTrue('transaction while authorizing' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionCommitError)

    def test_commit_exception_token_max_length(self):
        invalid_token = self.token_mock + 'a'
        with self.assertRaises(TransbankError) as context:
            self.transaction.commit(invalid_token)

        self.assertTrue("'token' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.get')
    def test_status_mall_transaction_successful(self, mock_get):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['commit_mall'])
        mock_get.return_value = self.mock_response

        response = self.transaction.status(self.token_mock)

        self.assertEqual(response, responses['commit_mall'])

    def test_status_mall_exception_token_max_length(self):
        invalid_token = self.token_mock + 'a'
        with self.assertRaises(TransbankError) as context:
            self.transaction.status(invalid_token)

        self.assertTrue("'token' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.get')
    def test_status_mall_exception_expired_token(self, mock_get):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['expired_token'])
        mock_get.return_value = self.mock_response

        with self.assertRaises(TransactionStatusError) as context:
            self.transaction.status(self.token_mock)

        self.assertTrue('has passed max time (7 days)' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionStatusError)

    @patch('transbank.common.request_service.requests.post')
    def test_refund_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['nullified_response'])
        mock_post.return_value = self.mock_response

        response = self.transaction.refund(self.token_mock, self.child1_buy_order, self.child1_commerce_code,
                                           self.amount1_mock)

        self.assertTrue(response['type'] == 'NULLIFIED')

    @patch('transbank.common.request_service.requests.post')
    def test_refund_mall_exception(self, mock_post):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['bigger_amount_mall'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionRefundError) as context:
            self.transaction.refund(self.token_mock, self.child1_buy_order, self.child1_commerce_code,
                                    1000000)

        self.assertTrue('Amount to refund is bigger than' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionRefundError)

    def test_refund_mall_exception_token_max_length(self):
        invalid_token = self.token_mock + 'a'
        with self.assertRaises(TransbankError) as context:
            self.transaction.refund(invalid_token, self.child1_buy_order, self.child1_commerce_code, self.amount1_mock)

        self.assertTrue("'token' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_refund_mall_exception_child_commerce_code_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.refund(self.token_mock, self.child1_buy_order, self.child1_commerce_code+'123',
                                    self.amount1_mock)

        self.assertTrue("'child_commerce_code' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_refund_mall_exception_child_buy_order_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.refund(self.token_mock, self.child1_buy_order*2, self.child1_commerce_code,
                                    self.amount1_mock)

        self.assertTrue("'child_buy_order' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.get')
    def test_status_mall_deferred_transaction_successful(self, mock_get):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['status_mall_deferred'])
        mock_get.return_value = self.mock_response

        response = self.deferred_capture.status(self.token_mock)

        for detail in response['details']:
            self.assertIsNotNone(detail['capture_expiration_date'])

    @patch('transbank.common.request_service.requests.put')
    def test_capture_mall_transaction_successful(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['capture_response'])
        mock_put.return_value = self.mock_response

        response = self.deferred_capture.capture(self.child1_commerce_code, self.token_mock, self.child1_buy_order,
                                                 self.authorization_code_mock, self.amount1_mock)

        self.assertTrue(response['captured_amount'])
        self.assertTrue(response['response_code'] == 0)

    @patch('transbank.common.request_service.requests.put')
    def test_capture_mall_exception(self, mock_put):
        self.mock_response.status_code = 422
        self.mock_response.text = json.dumps(responses['invalid_parameter'])
        mock_put.return_value = self.mock_response

        with self.assertRaises(TransactionCaptureError) as context:
            self.deferred_capture.capture(self.child1_commerce_code, self.token_mock, self.child1_buy_order,
                                          self.authorization_code_mock, self.invalid_amount)

        self.assertTrue('Invalid value for parameter' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionCaptureError)
