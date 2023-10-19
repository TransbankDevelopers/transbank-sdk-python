import unittest
import json
import string
import secrets
from unittest.mock import Mock
from transbank.webpay.oneclick.mall_transaction import *
from tests.mocks.responses_api_mocks import responses
from unittest.mock import patch


class OneclickMallTransactionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.username_mock = 'test_user'
        self.tbk_user_mock = '08ed03b1-8fa6-4d7b-b35c-b134e1c5e9ee'
        self.parent_buy_order_mock = 'parent_buy_order'
        self.installments_number_mock = 0
        self.child1_commerce_code = IntegrationCommerceCodes.ONECLICK_MALL_CHILD1
        self.amount1_mock = 1000
        self.child1_buy_order_mock = 'child_buy_order_1'
        self.child2_commerce_code = IntegrationCommerceCodes.ONECLICK_MALL_CHILD2
        self.amount2_mock = 2000
        self.child2_buy_order_mock = 'child_buy_order_2'
        self.return_url_mock = 'https://url_return.com'
        self.mock_response = Mock()
        self.inscription = MallTransaction()
