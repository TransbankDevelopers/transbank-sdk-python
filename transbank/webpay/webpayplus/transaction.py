import json
from transbank.webpay.webpayplus.webpayplus import WebpayPlus


class Transaction:
    CREATE_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    COMMIT_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions'
    REFUND_TRANSACTION_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}/refund'
    GET_TRANSACTION_STATUS_ENDPOINT = 'rswebpaytransaction/api/webpay/v1.0/transactions/{0}'

    @classmethod
    def create(cls, buy_order, session_id, amount,
               return_url, options=None):
        commerce_code = None
        api_key = None
        base_url = None
        if options is None:
            commerce_code = WebpayPlus.commerce_code
            api_key = WebpayPlus.api_key
            base_url = WebpayPlus.base_url
        else:
            commerce_code = options.commerce_code
            api_key = options.api_key
            WebpayPlus.integration_type_url = options.integration_type
            base_url = WebpayPlus.integration_type_url

        headers = dict({
            "Tbk-Api-Key-Id": commerce_code,
            "Tbk-Api-Key-Secret": api_key,
        })

        payload = json.dumps(dict({
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": amount,
            "return_url": return_url,
        }))

        http_client = WebpayPlus.http_client

        http_response = http_client.post(cls.CREATE_TRANSACTION_ENDPOINT, data=payload, headers=headers)
        if 200 > http_response.status_code > 300:
            raise Exception('Could not obtain a response from the service', -1)

        response_json = http_response.json()

        if response_json["token"] is None or response_json["url"] is None:
            raise Exception(response_json["error_message"])

        json_data = response_json
        transaction_create_reponse = None
        return transaction_create_reponse


