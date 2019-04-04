import unittest
import unittest.mock

import requests_mock
import re
import json

from transbank import onepay

from transbank.onepay import Options
from transbank.onepay.transaction import Transaction, Channel, TransactionCreateRequest
from transbank.onepay.cart import ShoppingCart, Item
from transbank.onepay.error import TransactionCreateError, TransactionCommitError, SignError
from transbank.onepay.schema import TransactionCreateRequestSchema

class TransactionTestCase(unittest.TestCase):

    external_unique_number_test = "1532376544050"
    occ_commit_test = "1807829988419927"
    shared_secret_mock = "P4DCPS55QB2QLT56SQH6#W#LV76IAPYX"
    api_key_mock = "mUc0GxYGor6X8u-_oB3e-HWJulRG01WoC96-_tUA3Bg"

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        onepay.integration_type = onepay.IntegrationType.MOCK
        onepay.api_key = self.api_key_mock
        onepay.shared_secret = self.shared_secret_mock
        onepay.callback_url = None
        onepay.app_scheme = None

    def test_get_signable_elements(self):
        request = TransactionCreateRequest(1, 1000, 1, 1, None, "http://localhost/callback")
        self.assertEqual(request.signable_data(), [1, 1000, 1, 1, "http://localhost/callback"])

    def get_valid_cart(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add(Item("item", 1, 1000))
        return shopping_cart

    def test_create_options(self):
        options = Options("api_key", "shared_secret")
        self.assertEqual(options.api_key, "api_key")
        self.assertEqual(options.shared_secret, "shared_secret")

    def test_validate_create(self):
        with self.assertRaisesRegex(Exception, "Shopping cart must not be null or empty"):
            Transaction.create(None)

        with self.assertRaisesRegex(Exception, "Shopping cart must not be null or empty"):
            Transaction.create(self.shopping_cart)

        with self.assertRaisesRegex(TransactionCreateError, "You need to set an app_scheme if you want to use the APP channel"):
            Transaction.create(self.get_valid_cart(), Channel.APP)

        with self.assertRaisesRegex(TransactionCreateError, "You need to set valid callback if you want to use the MOBILE channel"):
            Transaction.create(self.get_valid_cart(), Channel.MOBILE)

    def test_raise_error_response_create_transaction(self):
        with requests_mock.Mocker() as m:
            m.register_uri("POST", re.compile("/sendtransaction"), text="{\"response_code\": \"ERROR\", \"description\": \"ERROR\"}")

            with self.assertRaisesRegex(TransactionCreateError, "ERROR : ERROR"):
                Transaction.create(self.get_valid_cart())

    def test_raise_error_response_commit_transaction(self):
        with requests_mock.Mocker() as m:
            m.register_uri("POST", re.compile("/gettransactionnumber"), text="{\"response_code\": \"ERROR\", \"description\": \"ERROR\"}")

            with self.assertRaisesRegex(TransactionCommitError, "ERROR : ERROR"):
                Transaction.commit("occ", "external_unique_number")

    def test_create_transaction_global_options(self):
        response = Transaction.create(self.get_valid_cart())

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.ott)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.external_unique_number)
        self.assertIsNotNone(response.qr_code_as_base64)

    def test_create_transaction_given_options(self):
        onepay.api_key = None
        onepay.shared_secret = None
        options = Options(self.api_key_mock, self.shared_secret_mock)
        response = Transaction.create(self.get_valid_cart(), options=options)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.ott)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.external_unique_number)
        self.assertIsNotNone(response.qr_code_as_base64)

    def test_create_transaction_skip_none_params(self):
        external_unique_number_req = 123
        options = Options()
        shopping_cart = self.get_valid_cart()

        req = TransactionCreateRequest(external_unique_number_req,
              shopping_cart.total, shopping_cart.item_quantity,
              5473782781, shopping_cart.items,
              onepay.callback_url, Channel.WEB.value , onepay.app_scheme, options)
        request_string = TransactionCreateRequestSchema().dumps(req).data
        request_json = json.loads(request_string)
        self.assertFalse('commerceLogoUrl' in request_json)
        self.assertFalse('widthHeight' in request_json)

    def test_commit_transaction_global_options(self):

        response = Transaction.commit(self.occ_commit_test, self.external_unique_number_test)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.authorization_code)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.transaction_desc)
        self.assertIsNotNone(response.buy_order)
        self.assertIsNotNone(response.issued_at)
        self.assertIsNotNone(response.amount)
        self.assertIsNotNone(response.installments_amount)
        self.assertIsNotNone(response.installments_number)

    def test_commit_transaction_given_options(self):
        onepay.api_key = None
        onepay.shared_secret = None

        options = Options(self.api_key_mock, self.shared_secret_mock)
        response = Transaction.commit(self.occ_commit_test, self.external_unique_number_test, options)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.authorization_code)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.transaction_desc)
        self.assertIsNotNone(response.buy_order)
        self.assertIsNotNone(response.issued_at)
        self.assertIsNotNone(response.amount)
        self.assertIsNotNone(response.installments_amount)
        self.assertIsNotNone(response.installments_number)
