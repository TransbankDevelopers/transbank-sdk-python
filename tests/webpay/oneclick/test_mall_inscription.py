import unittest
import json
import string
import secrets
from unittest.mock import Mock
from transbank.webpay.oneclick.mall_inscription import *
from tests.mocks.responses_api_mocks import responses
from unittest.mock import patch
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys

class OneclickMallInscriptionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.username_mock = 'test_user'
        self.email_mock = 'test@user.test'
        self.return_url_mock = 'https://url_return.com'
        self.tbk_token_mock = '01ab5218921c3ffe06a19835b3fa7b4fcffa75965c14c7bda69ac7eeeb7d4245'
        self.tbk_user_mock = '08ed03b1-8fa6-4d7b-b35c-b134e1c5e9ee'
        self.mock_response = Mock()
        self.inscription = MallInscription.build_for_integration(IntegrationCommerceCodes.ONECLICK_MALL, IntegrationApiKeys.WEBPAY)

    @patch('transbank.common.request_service.requests.post')
    def test_inscription_start_transaction_successful(self, mock_post):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['inscription_start_response'])
        mock_post.return_value = self.mock_response

        response = self.inscription.start(self.username_mock, self.email_mock, self.return_url_mock)

        self.assertEqual(response, responses['inscription_start_response'])

    def get_invalid_length_param(self) -> str:
        valid_string = string.ascii_letters + string.digits + "-._~"
        invalid_length_param = ''.join(secrets.choice(valid_string) for _ in range(ApiConstants.RETURN_URL_LENGTH + 1))
        return invalid_length_param

    @patch('transbank.common.request_service.requests.post')
    def test_inscription_start_exception_not_authorized(self, mock_post):
        self.mock_response.status_code = 401
        self.mock_response.text = json.dumps(responses['create_error'])
        mock_post.return_value = self.mock_response

        with self.assertRaises(InscriptionStartError) as context:
            self.inscription.start(self.username_mock, self.email_mock, self.return_url_mock)

        self.assertTrue('Not Authorized' in context.exception.message)
        self.assertEqual(context.exception.__class__, InscriptionStartError)

    def test_inscription_start_exception_username_max_length(self):
        invalid_username = self.get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.inscription.start(invalid_username, self.email_mock, self.return_url_mock)

        self.assertTrue("'username' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_inscription_start_exception_email_max_length(self):
        invalid_email = self.get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.inscription.start(self.username_mock, invalid_email, self.return_url_mock)

        self.assertTrue("'email' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    def test_inscription_start_exception_response_url_max_length(self):
        invalid_url = self.get_invalid_length_param()

        with self.assertRaises(TransbankError) as context:
            self.inscription.start(self.username_mock, self.email_mock, invalid_url)

        print(context.exception.message)
        self.assertTrue("'response_url' is too long, the maximum length" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)

    @patch('transbank.common.request_service.requests.put')
    def test_inscription_finish_transaction_successful(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['inscription_finish_response'])
        mock_put.return_value = self.mock_response

        response = self.inscription.finish(self.tbk_token_mock)

        self.assertEqual(response, responses['inscription_finish_response'])

    @patch('transbank.common.request_service.requests.put')
    def test_inscription_finish_transaction_fail(self, mock_put):
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(responses['inscription_finish_fail'])
        mock_put.return_value = self.mock_response

        response = self.inscription.finish(self.tbk_token_mock)

        self.assertEqual(response, responses['inscription_finish_fail'])

    @patch('transbank.common.request_service.requests.put')
    def test_inscription_finish_exception(self, mock_put):
        self.mock_response.status_code = 500
        self.mock_response.text = json.dumps(responses['general_error'])
        mock_put.return_value = self.mock_response

        with self.assertRaises(InscriptionFinishError) as context:
            self.inscription.finish(self.tbk_token_mock)

        self.assertEqual(context.exception.__class__, InscriptionFinishError)

    def test_inscription_delete_exception_empty_tbk_user(self):
        empty_tbk_user = ''

        with self.assertRaises(TransbankError) as context:
            self.inscription.delete(empty_tbk_user, self.username_mock)

        self.assertTrue("'tbk_user' can't be null or white space" in context.exception.message)
        self.assertEqual(context.exception.__class__, TransbankError)
