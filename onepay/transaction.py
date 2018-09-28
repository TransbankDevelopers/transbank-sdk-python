# encoding: utf-8
from __future__ import unicode_literals

class Options(object):
    def __init__(self, api_key: str, shared_secret: str):
        if not isinstance(api_key, str):
            raise ValueError('api_key must be a string')

        if not isinstance(shared_secret, str):
                raise ValueError('shared_secret must be a string')

        self.api_key = api_key
        self.shared_secret = shared_secret
