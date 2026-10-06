import unittest
from unittest.mock import Mock
from unittest.mock import patch
import json
from transbank.common.transaction_status import TransactionStatus
from transbank.webpay.webpay_plus.transaction import Transaction
from tests.mocks.responses_api_mocks import responses
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys


class TransactionStatusTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.token_mock = '01abf2be20aad1da804aeae1ed3062fb8fba108ee0e07f4d37181f51c3f6714d'
        self.mock_response = Mock()
        self.transaction = Transaction.build_for_integration(
            IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY)

    def test_values_match_documented_statuses(self):
        documented_statuses = ['INITIALIZED', 'AUTHORIZED', 'REVERSED', 'FAILED', 'NULLIFIED',
                               'PARTIALLY_NULLIFIED', 'CAPTURED']

        self.assertEqual([status.value for status in TransactionStatus], documented_statuses)

    def test_members_are_equal_to_api_strings(self):
        for status in TransactionStatus:
            self.assertIsInstance(status, str)
            self.assertEqual(status, status.name)

    def test_str_and_json_return_plain_value(self):
        self.assertEqual(str(TransactionStatus.AUTHORIZED), 'AUTHORIZED')
        self.assertEqual(json.dumps({'status': TransactionStatus.FAILED}), '{"status": "FAILED"}')

    def test_build_from_api_value(self):
        status = TransactionStatus(responses['commit_status_response']['status'])

        self.assertIs(status, TransactionStatus.AUTHORIZED)

    def test_unknown_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            TransactionStatus('UNKNOWN_STATUS')

    @patch('transbank.common.request_service.requests.put')
    def test_commit_response_is_unchanged_and_comparable(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['commit_status_response'])
        mock_put.return_value = self.mock_response

        response = self.transaction.commit(self.token_mock)

        self.assertEqual(response, responses['commit_status_response'])
        self.assertIs(type(response['status']), str)
        self.assertEqual(response['status'], TransactionStatus.AUTHORIZED)
