import unittest

from onepay.onepay import Onepay, IntegrationType

class OnepayTestCase(unittest.TestCase):
    def test_set_global_keys(self):
        Onepay.set_api_key("api_key")
        Onepay.set_shared_secret("shared_secret")
        Onepay.set_callback_url("callback_url")
        Onepay.set_app_scheme("app_scheme")

        self.assertEqual(Onepay.get_api_key(), "api_key")
        self.assertEqual(Onepay.get_shared_secret(), "shared_secret")
        self.assertEqual(Onepay.get_callback_url(), "callback_url")
        self.assertEqual(Onepay.get_app_scheme(), "app_scheme")

        with self.assertRaisesRegex(ValueError, "api_key must be a string"):
            Onepay.set_api_key(0)
        with self.assertRaisesRegex(ValueError, "shared_secret must be a string"):
            Onepay.set_shared_secret(0)
        with self.assertRaisesRegex(ValueError, "callback_url must be a string"):
            Onepay.set_callback_url(0)
        with self.assertRaisesRegex(ValueError, "app_scheme must be a string"):
            Onepay.set_app_scheme(0)

    def test_integration_types(self):
        self.assertIsNotNone(IntegrationType.LIVE)
        self.assertIsNotNone(IntegrationType.TEST)
        self.assertIsNotNone(IntegrationType.MOCK)

        self.assertIsNotNone(IntegrationType.LIVE.value.get_api_base())
        self.assertIsNotNone(IntegrationType.LIVE.value.get_key())
        self.assertIsNotNone(IntegrationType.LIVE.value.get_app_key())

        Onepay.set_integration_type(IntegrationType.LIVE)
        self.assertEqual(Onepay.get_current_integration_type(), IntegrationType.LIVE)
