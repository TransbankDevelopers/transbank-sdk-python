import unittest
from unittest.mock import Mock
import random
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
        self.invalid_amount = -1000
        self.authorization_code_mock = '123456'
        self.capture_amount_mock = 150000
        self.mock_response = Mock()
        self.transaction = Transaction()

    def test_when_transaction_create(self):
        response = Transaction().create(
            buy_order=self.buy_order_mock,
            session_id=self.session_id_mock,
            amount=self.amount_mock,
            return_url=self.return_url_mock,
        )
        self.assertIsNotNone(response['url'])
        self.assertIsNotNone(response['token'])

    def test_when_transaction_create_using_invalid_credentials(self):
        with self.assertRaises(TransactionCreateError) as context:
            tx = Transaction().configure_for_integration('597012345678', 'FakeApiKeySecret')

            response = tx.create(
                buy_order=self.buy_order_mock,
                session_id=self.session_id_mock,
                amount=self.amount_mock,
                return_url=self.return_url_mock,
            )

        self.assertTrue('Not Authorized' in context.exception.message)

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

