class InscriptionStartResponse(object):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def __repr__(self):
        return "token: {}, url: {}".format(self.token, self.url)


class InscriptionStatusResponse(object):
    def __init__(self, authorized: bool, voucherUrl: str):
        self.authorized = authorized
        self.voucherUrl = voucherUrl

    def __repr__(self):
        return "authorized: {}, voucherUrl: {}".format(self.authorized, self.voucherUrl)
