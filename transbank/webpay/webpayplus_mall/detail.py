class Detail:

    def __init__(self, json_data):
        self._amount = json_data.get('amount', None)
        self._status = json_data.get('status', None)
        self._authorization_code = json_data.get('authorization_code', None)
        self._payment_type_code = json_data.get('payment_type_code', None)
        self._response_code = json_data.get('response_code', None)
        self._installments_number = json_data.get('installments_number', None)
        self._installments_amount = json_data.get('installments_amount', None)
        self._commerce_code = json_data.get('commerce_code', None)
        self._buy_order = json_data.get('buy_order', None)
