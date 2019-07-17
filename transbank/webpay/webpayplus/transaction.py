import json

from transbank.webpay.webpayplus.transaction_create_response import TransactionCreateResponse
from .exceptions.transaction_create_exception import TransactionCreateException
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
        commerce_code = None
        api_key = None
        base_url = None
        if options is None:
            commerce_code = WebpayPlus.commerce_code()
            api_key = WebpayPlus.api_key()
            base_url = WebpayPlus.integration_type_url()
        else:
            commerce_code = options.commerce_code
            api_key = options.api_key
            base_url = WebpayPlus.integration_type_url(options.integration_type)

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

        http_client = WebpayPlus.http_client
        final_url = base_url + cls.CREATE_TRANSACTION_ENDPOINT

        try:
            http_response = http_client.post(final_url, data=payload, headers=headers)
            http_response.raise_for_status()
            response_json = http_response.json()
            return TransactionCreateResponse(response_json)
        except Exception as e:
            if 'http_response' in locals():
                raise TransactionCreateException(-1)
            else:
                raise TransactionCreateException(http_response.status_code, e.args)

    @classmethod
    def commit(cls, token_ws, options=None):
        commerce_code = None
        api_key = None
        base_url = None
        if options is None:
            commerce_code = WebpayPlus.commerce_code()
            api_key = WebpayPlus.api_key()
            base_url = WebpayPlus.integration_type_url()
        else:
            commerce_code = options.commerce_code
            api_key = options.api_key
            WebpayPlus.integration_type_url = options.integration_type
            base_url = WebpayPlus.integration_type_url()

        headers = dict({
            "Tbk-Api-Key-Id": commerce_code,
            "Tbk-Api-Key-Secret": api_key,
            "Content-Type": "application/json",
        })

        http_client = WebpayPlus.http_client
        final_url = base_url + cls.COMMIT_TRANSACTION_ENDPOINT + "/" + token_ws
        http_response = http_client.put(final_url, headers=headers)

        response_json = http_response.json()

        if response_json.get('error_message') is not None:
            raise Exception(response_json["error_message"])

        json_data = response_json
        transaction_commit_response = TransactionCommitResponse(json_data)
        return transaction_commit_response
