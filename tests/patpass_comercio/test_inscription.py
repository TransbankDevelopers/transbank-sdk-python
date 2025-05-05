import unittest
import json
from unittest.mock import Mock
from tests.mocks.patpass_responses_api_mocks import responses
from unittest.mock import patch
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.patpass_comercio.inscription import Inscription

class OneclickMallInscriptionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_response = Mock()
        self.inscription = Inscription.build_for_integration(IntegrationCommerceCodes.PATPASS_COMERCIO, IntegrationApiKeys.PATPASS_COMERCIO)

    @patch('transbank.common.request_service.requests.post')
    def test_inscription_start_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['inscription_response'])
        mock_post.return_value = self.mock_response

        response = self.inscription.start(
            url="https://example.com",
            name="John",
            last_name="Doe",
            second_last_name="Smith",
            rut="12345678-9",
            service_id="service_001",
            final_url="https://example.com/final",
            max_amount=1000.0,
            phone="12345678",
            cell_phone="87654321",
            patpass_name="Patpass User",
            person_email="user@example.com",
            commerce_email="commerce@example.com",
            address="123 Street",
            city="Santiago"
        )
        self.assertEqual(response, responses['inscription_response'])

    @patch('transbank.common.request_service.requests.post')
    def test_status_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['status_response'])
        mock_post.return_value = self.mock_response

        response = self.inscription.status("dummy_token")

        self.assertIn("authorized", response)
        self.assertEqual(response, responses['status_response'])
