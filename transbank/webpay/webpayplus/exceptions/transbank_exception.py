
class TransbankException(Exception):
    DEFAULT_MESSAGE = 'Transaction could not be created. Unidentified error.'

    def __init__(self, error_code, original_exception, message=DEFAULT_MESSAGE):
        self._error_code = error_code
        self._message = message
        self._original_exception = original_exception
        msg = "{0} - {1} - {2}".format(self._error_code, self._message, self._message)
        super(TransbankException, self).__init__(msg)


