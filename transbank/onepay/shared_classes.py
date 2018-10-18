from transbank.onepay import sign

class Options(object):
    def __init__(self, api_key: str, shared_secret: str):
        self.api_key = api_key
        self.shared_secret = shared_secret

class Signable(object):
    signable_attributes = []

    def signable_data(self):
        signable_data = [getattr(self, item) for item in self.signable_attributes]
        return signable_data

    def sign(self, secret):
        data = sign.concat_for_signing(*self.signable_data())
        return sign.sign_sha256(secret, data)

    def is_valid_signature(self, secret, signature):
        return self.sign(secret) == signature
