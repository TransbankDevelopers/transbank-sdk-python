import unittest
from unittest.mock import Mock
from unittest.mock import patch
import json
from tests.mocks.transaccion_completa_responses_api_mocks import responses
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.webpay.transaccion_completa.transaction import Transaction

class TransactionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.buy_order_mock = 'buy_order_mock_123456789'
        self.session_id_mock = 'session_ide_mock_123456789'
        self.amount_mock = 150000
        self.token_mock = '01abf2be20aad1da804aeae1ed3062fb8fba108ee0e07f4d37181f51c3f6714d'
        self.invalid_amount = -1000
        self.authorization_code_mock = '123456'
        self.capture_amount_mock = 150000
        self.cvv = '123'
        self.card_number = 'XXXXXXXXXXXX6623'
        self.card_expiration_date = '12/28'
        self.mock_response = Mock()
        self.transaction = Transaction.build_for_integration(IntegrationCommerceCodes.TRANSACCION_COMPLETA, IntegrationApiKeys.WEBPAY)

    @patch('transbank.common.request_service.requests.post')
    def test_create_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['create_response'])
        mock_post.return_value = self.mock_response

        response = self.transaction.create(self.buy_order_mock,
                                           self.session_id_mock,
                                           self.amount_mock,
                                           self.cvv,
                                           self.card_number,
                                           self.card_expiration_date
                                           )

        self.assertEqual(response, responses['create_response'])

