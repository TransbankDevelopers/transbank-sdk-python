import json

from transbank.webpay.webpayplus.transaction_create_response import TransactionCreateResponse
from .exceptions.transaction_exception import TransactionHttpException, TransactionRequestException, \
    TransactionTimeoutException, TransactionConnectionException
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
        except requests.exceptions.HTTPError as http_error:
            raise TransactionHttpException(http_response.status_code, http_response.reason, http_error.args)
        except requests.exceptions.ConnectionError as conn_error:
            raise TransactionConnectionException(http_response.status_code, http_response.reason, conn_error.args)
        except requests.exceptions.Timeout as timeout_err:
            raise TransactionTimeoutException(http_response.status_code, http_response.reason, timeout_err.args)
        except requests.exceptions.RequestException as req_error:
            raise TransactionRequestException(http_response.status_code, http_response.reason, req_error.args)
        else:
            response_json = http_response.json()

        try:
            token = response_json["token"]
            url = response_json["url"]
        except KeyError:
            raise Exception(response_json["error_message"])

        return TransactionCreateResponse(response_json)
