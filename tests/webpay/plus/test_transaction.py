import unittest
from unittest.mock import Mock
from unittest.mock import patch
from tests.mocks.responses_api_mocks import responses
from transbank.webpay.webpay_plus.transaction import *
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys


class TransactionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.buy_order_mock = 'buy_order_mock_123456789'
        self.session_id_mock = 'session_ide_mock_123456789'
        self.amount_mock = 150000
        self.return_url_mock = "https://url_return.com"
        self.token_mock = '01abf2be20aad1da804aeae1ed3062fb8fba108ee0e07f4d37181f51c3f6714d'
        self.invalid_token_mock = '01ab47af75fbebedef5bf009efdc4a925e51c84677770ddc51b26283aac53f1a'
        self.mock_response = Mock()
        self.invalid_amount = -1000

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_create_transaction(self, mock_request_service):
        mock_request_service.post.return_value = self.mock_response
        self.mock_response.json.return_value = responses['create_response']

        transaction = Transaction()
        response = transaction.create(self.buy_order_mock, self.session_id_mock, self.amount_mock, self.return_url_mock)

        self.assertEqual(response.json(), responses['create_response'])

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_create_transaction_error(self, mock_request_service):
        mock_request_service.post.side_effect = TransactionCreateError(responses['create_error']['error_message'],
                                                                       responses['create_error']['code'])

        transaction = Transaction()
        with self.assertRaises(TransactionCreateError) as context:
            transaction.create(self.buy_order_mock, self.session_id_mock, self.amount_mock, self.return_url_mock)

        self.assertEqual(context.exception.args[0], responses['create_error']['error_message'])
        self.assertEqual(context.exception.code, responses['create_error']['code'])

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_commit_transaction(self, mock_request_service):
        mock_request_service.put.return_value = self.mock_response
        self.mock_response.json.return_value = responses['commit_status_response']

        transaction = Transaction()
        response = transaction.commit(self.token_mock)

        self.assertEqual(response.json(), responses['commit_status_response'])

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_commit_transaction_error(self, mock_request_service):
        mock_request_service.put.side_effect = TransactionCommitError(responses['commit_error']['error_message'],
                                                                      responses['commit_error']['code'])

        transaction = Transaction()
        with self.assertRaises(TransactionCommitError) as context:
            transaction.commit(self.token_mock)

        self.assertEqual(context.exception.args[0], responses['commit_error']['error_message'])
        self.assertEqual(context.exception.code, responses['commit_error']['code'])

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_status_transaction(self, mock_request_service):
        mock_request_service.get.return_value = self.mock_response
        self.mock_response.json.return_value = responses['commit_status_response']

        transaction = Transaction()
        response = transaction.status(self.token_mock)

        self.assertEqual(response.json(), responses['commit_status_response'])

    @patch('transbank.webpay.webpay_plus.transaction.RequestService')
    def test_status_transaction_error(self, mock_request_service):
        mock_request_service.get.side_effect = TransactionStatusError(responses['expired_token']['error_message'],
                                                                      responses['expired_token']['code'])

        transaction = Transaction()
        with self.assertRaises(TransactionStatusError) as context:
            transaction.status(self.token_mock)

        self.assertEqual(context.exception.args[0], responses['expired_token']['error_message'])
        self.assertEqual(context.exception.code, responses['expired_token']['code'])
