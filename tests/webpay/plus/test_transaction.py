import unittest
from unittest.mock import Mock
from unittest.mock import patch
import json
import secrets
import string
from transbank.webpay.webpay_plus.transaction import *
from transbank.error.transaction_create_error import TransactionCreateError
from tests.mocks.responses_api_mocks import responses
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys


class TransactionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.buy_order_mock = 'buy_order_mock_123456789'
        self.session_id_mock = 'session_ide_mock_123456789'
        self.amount_mock = 150000
        self.return_url_mock = "https://url_return.com"
        self.token_mock = '01abf2be20aad1da804aeae1ed3062fb8fba108ee0e07f4d37181f51c3f6714d'
        self.invalid_amount = -1000
        self.authorization_code_mock = '123456'
        self.capture_amount_mock = 150000
        self.mock_response = Mock()
        self.transaction = Transaction()

    @patch('transbank.common.request_service.requests.post')
    def test_create_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['create_response'])
        mock_post.return_value = self.mock_response

        response = self.transaction.create(self.buy_order_mock, self.session_id_mock, self.amount_mock,
                                           self.return_url_mock)

        self.assertEqual(response, responses['create_response'])

    @patch('transbank.common.request_service.requests.post')
    def test_create_exception_not_authorized(self, mock_post):
        self.mock_response.status_code = 401
        self.mock_response.text = json.dumps(responses['create_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(TransactionCreateError) as context:
            self.transaction.create(self.buy_order_mock, self.session_id_mock, self.amount_mock, self.return_url_mock)

        self.assertTrue('Not Authorized' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransactionCreateError)

    def test_create_exception_buy_order_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.token_mock, self.session_id_mock, self.amount_mock, self.return_url_mock)

        self.assertTrue('too long, the maximum length' in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_exception_session_id_max_length(self):
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.buy_order_mock, self.token_mock, self.amount_mock, self.return_url_mock)

        self.assertTrue("'session_id' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_create_exception_return_url_max_length(self):
        valid_string = string.ascii_letters + string.digits + "-._~"
        too_long_url = ''.join(secrets.choice(valid_string) for _ in range(ApiConstants.RETURN_URL_LENGTH + 1))
        with self.assertRaises(TransbankError) as context:
            self.transaction.create(self.buy_order_mock, self.session_id_mock, self.amount_mock, too_long_url)

        self.assertTrue("'return_url' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.put')
    def test_commit_transaction_successful(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['commit_status_response'])
        mock_put.return_value = self.mock_response

        response = self.transaction.commit(self.token_mock)

        self.assertEqual(response, responses['commit_status_response'])
        self.assertTrue(response['response_code'] == 0)

    @patch('transbank.common.request_service.requests.put')
    def test_commit_exception_when_authorized(self, mock_put):
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
    def test_status_transaction_successful(self, mock_get):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['commit_status_response'])
        mock_get.return_value = self.mock_response

        response = self.transaction.status(self.token_mock)

        self.assertEqual(response, responses['commit_status_response'])
        self.assertTrue(response['response_code'] == 0)

    def test_status_exception_token_max_length(self):
        invalid_token = self.token_mock + 'a'
        with self.assertRaises(TransbankError) as context:
            self.transaction.status(invalid_token)

        self.assertTrue("'token' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_when_transaction_status(self):
        response = Transaction().create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            amount=self.amount_mock,
            return_url=self.return_url_mock,
        )

        response = Transaction().status(token=response['token'])
        print(response)
        # self.assertIsNotNone(response.vci) # This is empty when asking status of Initialized tx
        self.assertIsNotNone(response['amount'])
        self.assertIsNotNone(response['status'])
        self.assertIsNotNone(response['buy_order'])
        self.assertIsNotNone(response['session_id'])
        # self.assertIsNotNone(response.card_detail.card_number) # This is empty when asking status of Initialized tx
        self.assertIsNotNone(response['accounting_date'])
        self.assertIsNotNone(response['transaction_date'])
        # self.assertIsNotNone(response.authorization_code) # This is empty when asking status of Initialized tx
        # self.assertIsNotNone(response.payment_type_code) # This is empty when asking status of Initialized tx
        # self.assertIsNotNone(response.response_code) # This is empty when asking status of Initialized tx
        self.assertIsNotNone(response['installments_number'])

    # def test_when_transaction_commit(self):
    #     response = Transaction.status(token=self.token_mock)
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

    # def test_when_transaction_refund(self):
    #     response = Transaction.refund(token=self.token_mock, amount=1)
    #     self.assertIsNotNone(response.type)
    #     self.assertIsNotNone(response.balance)
    #     self.assertIsNotNone(response.authorization_date)
    #     self.assertIsNotNone(response.response_code)
    #     self.assertIsNotNone(response.authorization_code)
    #     self.assertIsNotNone(response.nullified_amount)

