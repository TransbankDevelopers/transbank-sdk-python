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

        print(context.exception.args[0])
        self.assertEqual(context.exception.args[0], responses['create_error']['error_message'])
        self.assertEqual(context.exception.code, responses['create_error']['code'])


    def test_when_transaction_create_using_invalid_credentials(self):

        response = Transaction().create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            amount=self.amount_mock,
            return_url=self.return_url_mock,
        )

        self.assertIsNotNone(response['url'])
        self.assertIsNotNone(response['token'])


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

