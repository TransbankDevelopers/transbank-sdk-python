# encoding: utf-8

class TransbankError(Exception):
    def __init__(self, message = "An error has happened, verify given parameters and try again.", code = 0):
        self.message = message
        self.code = code

class TransactionCreateError(TransbankError):
    def __init__(self, message = "Transaction could not be created. Please verify given parameters", code = 0):
        self.message = message
        self.code = code

class TransactionCommitError(TransbankError):
    def __init__(self, message = "Transaction could not be commited. Please verify given parameters", code = 0):
        self.message = message
        self.code = code

class RefundCreateError(TransbankError):
    def __init__(self, message = "Refund could not be executed. Please verify given parameters", code = 0):
        self.message = message
        self.code = code

class SignError(TransbankError):
    def __init__(self, message = "Signature does not match", code = 0):
        self.message = message
        self.code = code
