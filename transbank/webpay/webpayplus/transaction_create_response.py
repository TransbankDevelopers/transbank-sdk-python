class TransactionCreateResponse:
    _token = None
    _url = None

    def __init__(self, json):
        self._token = None
        self._url = None

    def from_json(self, json):
        self.url = json["url"]
        self.token = json["token"]

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url
