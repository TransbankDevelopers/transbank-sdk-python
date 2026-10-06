import unittest
from unittest.mock import Mock
import json
from transbank.common.request_service import RequestService
from transbank.error.transbank_error import TransbankError
from tests.mocks.responses_api_mocks import responses


class RequestServiceTestCase(unittest.TestCase):

    def build_response(self, status_code, body=None):
        response = Mock()
        response.status_code = status_code
        response.text = json.dumps(body) if body is not None else ''
        return response

    def test_process_response_200_with_body(self):
        response = self.build_response(200, responses['commit_status_response'])

        self.assertEqual(RequestService.process_response(response), responses['commit_status_response'])

    def test_process_response_201_with_body(self):
        response = self.build_response(201, responses['create_response'])

        self.assertEqual(RequestService.process_response(response), responses['create_response'])

    def test_process_response_204_without_body(self):
        response = self.build_response(204)

        self.assertEqual(RequestService.process_response(response), 204)

    def test_process_response_422_with_error_message(self):
        response = self.build_response(422, responses['commit_error'])

        with self.assertRaises(TransbankError) as context:
            RequestService.process_response(response)

        self.assertEqual(context.exception.message, responses['commit_error']['error_message'])
        self.assertEqual(context.exception.code, 422)

    def test_process_response_500_with_description(self):
        response = self.build_response(500, responses['general_error'])

        with self.assertRaises(TransbankError) as context:
            RequestService.process_response(response)

        self.assertEqual(context.exception.message, responses['general_error']['description'])
        self.assertEqual(context.exception.code, 500)
