from transbank.common.model import CardDetail


class TransactionCreateResponse(object):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def __repr__(self):
        return "token: {}, url: {}".format(self.token, self.url)
