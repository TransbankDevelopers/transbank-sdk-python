import json
import requests
from transbank.webpay.webpayplus.transaction_create_response import TransactionCreateResponse
from .exceptions.transaction_create_exception import TransactionCreateException
from .exceptions.transaction_commit_exception import TransactionCommitException
from transbank.webpay.webpayplus.transaction_commit_response import TransactionCommitResponse
from transbank.webpay.webpayplus.webpayplus import *


class Transaction:
    CREATE_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    COMMIT_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    REFUND_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}/refund'
    GET_TRANSACTION_STATUS_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}'

    def __init__(self):
        pass

    @classmethod
    def create(cls, buy_order, session_id, amount,
               return_url, options=None):

        commerce_code, api_key, base_url = Options.build_options(options)

        headers = {
            "Tbk-Api-Key-Id": commerce_code,
            "Tbk-Api-Key-Secret": api_key,
            "Content-Type": "application/json",
        }

        payload = json.dumps({
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": amount,
            "return_url": return_url,
        })

        final_url = base_url + cls.CREATE_TRANSACTION_ENDPOINT

        try:
            http_response = requests.post(final_url, data=payload, headers=headers)
            http_response.raise_for_status()
            response_json = http_response.json()
            return TransactionCreateResponse(response_json)
        except Exception as e:
            if 'http_response' in locals():
                raise TransactionCreateException(-1)
            raise TransactionCreateException(http_response.status_code, e.args)

    @classmethod
    def commit(cls, token_ws, options=None):

        commerce_code, api_key, base_url = Options.build_options(options)

        headers = {
            "Tbk-Api-Key-Id": commerce_code,
            "Tbk-Api-Key-Secret": api_key,
            "Content-Type": "application/json",
        }

        final_url = base_url + cls.COMMIT_TRANSACTION_ENDPOINT + "/" + token_ws

        try:
            http_response = requests.put(final_url, headers=headers)
            http_response.raise_for_status()
            response_json = http_response.json()
            return TransactionCommitResponse(response_json)
        except Exception as e:
            if 'http_response' in locals():
                raise TransactionCommitException(-1)
            raise TransactionCommitException(http_response.status_code, e.args)
