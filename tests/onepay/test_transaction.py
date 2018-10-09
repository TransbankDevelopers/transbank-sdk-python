import unittest
import unittest.mock

import http.client
from tbk import onepay

from tbk.onepay.transaction import Options, Transaction, Channel
from tbk.onepay.cart import ShoppingCart, Item
from tbk.onepay.error import TransactionCreateError, SignError

class TransactionTestCase(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        onepay.integration_type = onepay.IntegrationType.TEST
        onepay.callback_url = "http://localhost/callback"

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

        http.client.HTTPSConnection = unittest.mock.Mock(spec=http.client.HTTPSConnection)
        http.client.HTTPResponse = unittest.mock.Mock(spec=http.client.HTTPResponse)

        connection = http.client.HTTPSConnection()
        response = http.client.HTTPResponse()

        response.read.return_value = b'{"response_code": "ERROR", "description": "ERROR"}'
        connection.getresponse.return_value = response

        with self.assertRaisesRegex(TransactionCreateError, "ERROR : ERROR"):
            Transaction.create(self.get_valid_cart(), Channel.WEB)

    def test_create_transaction(self):
        onepay.api_key = "dKVhq1WGt_XapIYirTXNyUKoWTDFfxaEV63-O5jcsdw"
        onepay.shared_secret = "?XW#WOLG##FBAGEAYSNQ5APD#JF@$AYZ"
        response = Transaction.create(self.get_valid_cart(), Channel.WEB)

        self.assertIsNotNone(response)
