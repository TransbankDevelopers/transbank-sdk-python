import unittest

from onepay.transaction import Options, Transaction, Channel
from onepay.cart import ShoppingCart, Item

class TransactionTestCase(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart()

    def get_valid_cart(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add(Item("item", 1, 1000))
        return shopping_cart

    def test_create_options(self):
        options = Options("api_key", "shared_secret")
        self.assertEqual(options.api_key, "api_key")
        self.assertEqual(options.shared_secret, "shared_secret")

        with self.assertRaisesRegex(ValueError, "api_key must be a string"):
            Options(0, "")

        with self.assertRaisesRegex(ValueError, "shared_secret must be a string"):
            Options("", 0)

    def test_validate_create(self):
        with self.assertRaisesRegex(Exception, "Shopping cart is null or empty"):
            Transaction.create(None)

        with self.assertRaisesRegex(Exception, "Shopping cart is null or empty"):
            Transaction.create(self.shopping_cart)

        with self.assertRaisesRegex(Exception, "You need to set an app_scheme if you want to use the APP channel"):
            Transaction.create(self.get_valid_cart(), Channel.APP)

        with self.assertRaisesRegex(Exception, "You need to set valid callback if you want to use the MOBILE channel"):
            Transaction.create(self.get_valid_cart(), Channel.MOBILE)
