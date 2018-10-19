# encoding: utf-8
import hashlib, hmac, base64

def str_with_len_prefix(param):
    return str(len(str(param).encode('utf-8'))) + str(param)

def concat_for_signing(*params):
    return ''.join(str_with_len_prefix(param) for param in params)

def sign_sha256(secret: str, data: str) -> str:
    digest = hmac.new(str.encode(secret), msg=str.encode(data), digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode()

