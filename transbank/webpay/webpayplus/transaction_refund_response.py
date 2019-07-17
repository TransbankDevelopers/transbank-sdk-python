class TransactionRefundResponse:

    def __init__(self, json_data):
        self._type = json_data.get('type',None)
        self._authorization_code = json_data.get('authorization_code',None)
        self._authorization_date = json_data.get('authorization_date',None)
        self._nullified_amount = json_data.get('nullified_amount',None)
        self._balance = json_data.get('balance',None)
        self._response_code = json_data.get('response_code',None)

