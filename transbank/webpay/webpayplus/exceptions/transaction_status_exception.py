from .transbank_exception import TransbankException


class TransactionStatusException(TransbankException):
    DEFAULT_MESSAGE = 'Transaction could not be created. Unidentified error.'

    def __init__(self, error_code, original_exception, message=DEFAULT_MESSAGE):
        self._error_code = error_code
        self._message = message
        self._original_exception = original_exception
        msg = "{0} - {1} - {2}".format(self._error_code, self._message, self._message)
        super(TransactionStatusException, self).__init__(msg)

    @property
    def error_code(self):
        return self._error_code

    @property
    def message(self):
        return self._message

    @property
    def previous(self):
        return self._previous

