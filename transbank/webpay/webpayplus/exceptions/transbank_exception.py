
class TransbankException(Exception):
    DEFAULT_MESSAGE = 'Transaction could not be created. Unidentified error.'

    def __init__(self, error_code, message=DEFAULT_MESSAGE):
        self._error_code = error_code
        self._message = message
        super(TransbankException, self).__init__(self._message)


