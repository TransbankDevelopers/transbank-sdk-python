class TransactionCreateMallResponse:
    _token = None
    _url = None

    def __init__(self, json):
        self.from_json(json)

    def from_json(self, json):
        self._url = json["url"]
        self._token = json["token"]
        return self

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
