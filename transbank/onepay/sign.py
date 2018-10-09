# encoding: utf-8
import hashlib, hmac, base64

from transbank import onepay

def str_with_len_prefix(param):
    return str(len(str(param).encode('utf-8'))) + str(param)

def concat_for_signing(*params):
    return ''.join(str_with_len_prefix(param) for param in params)

def sign_sha256(secret: str, data: str) -> str:
    digest = hmac.new(str.encode(secret), msg=str.encode(data), digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode()

def build_signature_for_transaction_create_request(signable, secret: str):
    data = concat_for_signing(*signable.get_signable_data(append_data=[onepay.callback_url]))
    return sign_sha256(secret, data)

def build_signature_for_transaction_commit_request_or_create_response(signable, secret: str):
    data = concat_for_signing(*signable.get_signable_data())
    return sign_sha256(secret, data)

def validate_create_response(signable, secret, response_signature):
    calculated_signature = build_signature_for_transaction_commit_request_or_create_response(signable, secret)
    return calculated_signature == response_signature
