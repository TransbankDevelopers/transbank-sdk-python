
class TransactionException(Exception):
    pass


class TransactionHttpException(TransactionException):

    def __init__(self, http_code, http_reason, http_message):
        self._http_code = http_code
        self._http_reason = http_reason
        self._http_message = http_message

    def __str__(self):
        return repr(self._http_message)


class TransactionTimeoutException(TransactionException):

    def __init__(self, http_code, http_reason, http_message):
        self._http_code = http_code
        self._http_reason = http_reason
        self._http_message = http_message

    def __str__(self):
        return repr(self._http_message)


class TransactionRequestException(TransactionException):

    def __init__(self, http_code, http_reason, http_message):
        self._http_code = http_code
        self._http_reason = http_reason
        self._http_message = http_message

    def __str__(self):
        return repr(self._http_message)


class TransactionConnectionException(TransactionException):

    def __init__(self, http_code, http_reason, http_message):
        self._http_code = http_code
        self._http_reason = http_reason
        self._http_message = http_message

    def __str__(self):
        return repr(self._http_message)
