import unittest

from transbank import onepay
from transbank.onepay.error import TransactionCreateError, TransactionCommitError, TransbankError, SignError

class ErrorTestCase(unittest.TestCase):

    def test_errors(self):
        transaction_create_error = TransactionCreateError("Transaction Error", 100)
        transaction_commit_error = TransactionCommitError("Transaction Commit Error", 150)
        transbank_error = TransbankError("Transbank Error", 200 )
        sign_error = SignError("Sign Error", 300)

        self.assertEqual(transaction_create_error.message, "Transaction Error")
        self.assertEqual(transaction_create_error.code, 100)

        self.assertEqual(transaction_commit_error.message, "Transaction Commit Error")
        self.assertEqual(transaction_commit_error.code, 150)

        self.assertEqual(transbank_error.message, "Transbank Error")
        self.assertEqual(transbank_error.code, 200)

        self.assertEqual(sign_error.message, "Sign Error")
        self.assertEqual(sign_error.code, 300)
