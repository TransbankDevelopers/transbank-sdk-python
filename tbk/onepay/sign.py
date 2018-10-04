# encoding: utf-8
from __future__ import unicode_literals

from tbk.onepay.onepay_base import Onepay
import hashlib, hmac, base64

def sign_sha256(secret: str, data: str) -> str:
    digest = hmac.new(str.encode(secret), msg=str.encode(data), digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode()

class SignUtil(object):

    @staticmethod
    def build_signature_transaction_create_request(signable, secret: str):
        external_unique_number_as_string = str(signable.external_unique_number)
        total_as_string = str(signable.total)
        items_quantity_as_string = str(signable.items_quantity)
        issued_at_as_string = str(signable.issued_at)

        data = str(len(external_unique_number_as_string.encode('utf-8'))) + external_unique_number_as_string
        data += str(len(total_as_string.encode('utf-8'))) + total_as_string
        data += str(len(items_quantity_as_string.encode('utf-8'))) + items_quantity_as_string
        data += str(len(issued_at_as_string.encode('utf-8'))) + issued_at_as_string
        data += str(len(Onepay.get_callback_url().encode('utf-8'))) + Onepay.get_callback_url()

        signature = sign_sha256(secret, data)

        return signature

    @staticmethod
    def build_signature_transaction_commit_request_or_create_response(signable, secret: str):
        external_unique_number_as_string = str(signable.external_unique_number)
        occ_as_string = str(signable.occ)
        issued_at_as_string = str(signable.issued_at)

        data = str(len(occ_as_string.encode('utf-8'))) + occ_as_string
        data += str(len(external_unique_number_as_string.encode('utf-8'))) + external_unique_number_as_string
        data += str(len(issued_at_as_string.encode('utf-8'))) + issued_at_as_string

        signature = sign_sha256(secret, data)

        return signature
