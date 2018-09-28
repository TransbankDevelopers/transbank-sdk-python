import unittest

from onepay.transaction import Options

class TransactionTestCase(unittest.TestCase):
    def test_create_options(self):
        options = Options("api_key", "shared_secret")
        self.assertEqual(options.api_key, "api_key")
        self.assertEqual(options.shared_secret, "shared_secret")

        with self.assertRaises(ValueError):
            Options(0, "")

        with self.assertRaises(ValueError):
            Options("", 0)
