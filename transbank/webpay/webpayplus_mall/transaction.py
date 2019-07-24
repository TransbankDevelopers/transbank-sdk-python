import json

from transbank.webpay.webpayplus_mall.transaction_create_mall_response import TransactionCreateMallResponse
from transbank.webpay.webpayplus_mall.transaction_commit_mall_response import TransactionCommitMallResponse
# from transbank.webpay.webpayplus.transaction_refund_response import TransactionRefundResponse
# from transbank.webpay.webpayplus.transaction_status_response import TransactionStatusResponse
from transbank.webpay.webpayplus.webpayplus import WebpayPlus


class Transaction:
    CREATE_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    COMMIT_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    REFUND_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}/refunds'
    GET_TRANSACTION_STATUS_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}'

    def __init__(self):
        pass

    @classmethod
    def create_mall(cls, buy_order, session_id, return_url, details, options=None):
        commerce_code = WebpayPlus.commerce_code()
        api_key = WebpayPlus.api_key()
        base_url = WebpayPlus.integration_type_url()

        if options is not None:
            commerce_code = options.commerce_code
            api_key = options.api_key()
            base_url = WebpayPlus.integration_type_url(options.integration_type)

        headers = dict({
            "Tbk-Api-Key-Id": commerce_code,
            "Tbk-Api-Key-Secret": api_key,
            "Content-Type": "application/json",
        })

        payload = json.dumps(dict({
            "buy_order": buy_order,
            "session_id": session_id,
            "return_url": return_url,
            "details": details
        }))

        http_client = WebpayPlus.http_client
        final_url = base_url + cls.CREATE_TRANSACTION_ENDPOINT

        http_response = http_client.post(final_url, data=payload, headers=headers)
        if (http_response.status_code < 200) or (http_response.status_code > 300):
            raise Exception('Could not obtain a response from the service', -1)

        response_json = http_response.json()
        try:
            token = response_json["token"]
            url = response_json["url"]
        except KeyError:
            raise Exception(response_json["error_message"])

        json_data = response_json
        transaction_create_response = TransactionCreateMallResponse(json_data)
        return transaction_create_response

    @classmethod
    def commit_mall(cls, token_ws, options=None):
        commerce_code = WebpayPlus.commerce_code()
        api_key = WebpayPlus.api_key()
        base_url = WebpayPlus.integration_type_url()

        if options is not None:
            commerce_code = options.commerce_code
            api_key = options.api_key()
            base_url = WebpayPlus.integration_type_url(options.integration_type)

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
        transaction_commit_response = TransactionCommitMallResponse(json_data)
        return transaction_commit_response
