
class TransbankException(Exception):
    DEFAULT_MESSAGE = 'Transaction could not be created. Unidentified error.'

    def __init__(self, error_code, original_exception, message):
        if message is None:
            message = TransbankException.DEFAULT_MESSAGE
        msg = "{0} - {1} - {2}".format(error_code, message, original_exception)
        super(TransbankException, self).__init__(msg)


