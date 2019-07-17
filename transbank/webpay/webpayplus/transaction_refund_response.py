class TransactionRefundResponse:

    def __init__(self, json_data):
        self._type = json_data.get('type',None)
        self._authorization_code = json_data.get('authorization_code',None)
        self._authorization_date = json_data.get('authorization_date',None)
        self._nullified_amount = json_data.get('nullified_amount',None)
        self._balance = json_data.get('balance',None)
        self._response_code = json_data.get('response_code',None)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def authorization_code(self):
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, auth_code):
        self._authorization_code = auth_code

    @property
    def authorization_date(self):
        return self._authorization_date

    @authorization_date.setter
    def authorization_date(self, auth_date):
        self._authorization_date = auth_date

    @property
    def nullified_amount(self):
        return self.nullified_amount

    @nullified_amount.setter
    def nullified_amount(self, nullified_amount):
        self._nullified_amount = nullified_amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def response_code(self):
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        self._response_code = response_code
