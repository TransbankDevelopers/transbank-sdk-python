import unittest
import json
from unittest.mock import Mock
from transbank.webpay.oneclick.mall_inscription import *
from transbank.webpay.oneclick.request import *
from tests.mocks.responses_api_mocks import responses
from unittest.mock import patch


class MallInscriptionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.username_mock = 'test_user'
        self.email_mock = 'test@user.test'
        self.return_url_mock = 'https://url_return.com'
        self.tbk_token_mock = '01ab5218921c3ffe06a19835b3fa7b4fcffa75965c14c7bda69ac7eeeb7d4245'
        self.tbk_user_mock = '08ed03b1-8fa6-4d7b-b35c-b134e1c5e9ee'
        self.mock_response = Mock()
        self.inscription = MallInscription()

    @patch('transbank.common.request_service.requests.post')
    def test_inscription_start_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['inscription_start_response'])
        mock_post.return_value = self.mock_response

        response = self.inscription.start(self.username_mock, self.email_mock, self.return_url_mock)

        self.assertEqual(response, responses['inscription_start_response'])
