import unittest
import unittest.mock

import requests_mock
import re

from transbank import onepay

from transbank.onepay.transaction import Options, Transaction, Channel, TransactionCreateRequest
from transbank.onepay.cart import ShoppingCart, Item
from transbank.onepay.error import TransactionCreateError, SignError

class TransactionTestCase(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        onepay.integration_type = onepay.IntegrationType.TEST
        onepay.callback_url = "http://localhost/callback"

    def test_get_signable_elements(self):
        request = TransactionCreateRequest(1, 1000, 1, 1, None, "http://localhost/callback", "WEB", None)
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
        onepay.api_key = "dKVhq1WGt_XapIYirTXNyUKoWTDFfxaEV63-O5jcsdw"
        onepay.shared_secret = "?XW#WOLG##FBAGEAYSNQ5APD#JF@$AYZ"

        with requests_mock.Mocker() as m:
            m.register_uri("POST", re.compile("/sendtransaction"), text="{\"response_code\": \"ERROR\", \"description\": \"ERROR\"}")
            
            with self.assertRaisesRegex(TransactionCreateError, "ERROR : ERROR"):
                response = Transaction.create(self.get_valid_cart(), Channel.WEB)

    def test_create_transaction(self):
        onepay.api_key = "dKVhq1WGt_XapIYirTXNyUKoWTDFfxaEV63-O5jcsdw"
        onepay.shared_secret = "?XW#WOLG##FBAGEAYSNQ5APD#JF@$AYZ"
        response = Transaction.create(self.get_valid_cart(), Channel.WEB)

        self.assertIsNotNone(response)

    def test_create_transaction_with_options(self):
        onepay.api_key = None
        onepay.shared_secret = None
        options = Options("dKVhq1WGt_XapIYirTXNyUKoWTDFfxaEV63-O5jcsdw", "?XW#WOLG##FBAGEAYSNQ5APD#JF@$AYZ")
        response = Transaction.create(self.get_valid_cart(), Channel.WEB, options=options)

        self.assertIsNotNone(response)
