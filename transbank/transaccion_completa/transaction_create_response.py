class TransactionCreateResponse(object):
    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return "token: {}".format(self.token)
