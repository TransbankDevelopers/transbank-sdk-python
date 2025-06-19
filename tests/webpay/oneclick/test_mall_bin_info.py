import unittest
import json
from unittest.mock import Mock
from unittest.mock import patch
from transbank.error.transbank_error import TransbankError
from transbank.error.mall_bin_info_query_error import MallBinInfoQueryError
from transbank.webpay.oneclick.mall_bin_info import MallBinInfo


class MallBinInfoTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_response = Mock()

    @patch('transbank.common.request_service.requests.post')
    def test_query_bin(self, mock_post):
        response = {'bin_issuer': 'TEST COMMERCE BANK', 'bin_payment_type': 'Credito', 'bin_brand': 'Visa'}
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps(response)
        mock_post.return_value = self.mock_response

        mall_bin_info = MallBinInfo.build_for_integration('commerce_code', 'api_key')
        result = mall_bin_info.query_bin('tbkUser')

        _, kwargs = mock_post.call_args
        body = json.loads(kwargs['data'])

        self.assertEqual(result['bin_issuer'], 'TEST COMMERCE BANK')
        self.assertEqual(result['bin_payment_type'], 'Credito')
        self.assertEqual(result['bin_brand'], 'Visa')
        self.assertEqual(body['tbk_user'], 'tbkUser')
    
    def test_query_bin_invalid_tbk_user(self):
        mall_bin_info = MallBinInfo.build_for_integration('commerce_code', 'api_key')
        with self.assertRaises(TransbankError):
            mall_bin_info.query_bin('b134e1c5e9eeb134e1c5e9eeb134e1c5e9eeb134e1c5e9eeb134e1c5e9eeb134e1c5e9eeb134e1c5e9eeb134e1c5e9ee')
    
    @patch('transbank.common.request_service.requests.post')
    def test_query_bin_throws_api_exception(self, mock_post):
        self.mock_response.status_code = 400
        self.mock_response.text = '{"error": "Bad Request"}'
        mock_post.return_value = self.mock_response
        mall_bin_info = MallBinInfo.build_for_integration('commerce_code', 'api_key')

        with self.assertRaises(MallBinInfoQueryError):
            mall_bin_info.query_bin('tbkUser')
