from .transbank_exception import TransbankException


class TransactionCommitException(TransbankException):
    DEFAULT_MESSAGE = 'Transaction could not be created. Unidentified error.'

    def __init__(self, error_code, message=DEFAULT_MESSAGE, previous=None):
        self._error_code = error_code
        self._message = message
        self._previous = previous
        super(TransactionCommitException, self).__init__(self._message)

    @property
    def error_code(self):
        return self._error_code

    @property
    def message(self):
        return self._message

    @property
    def previous(self):
        return self._previous

