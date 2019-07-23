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

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def authorization_code(self):
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        self._authorization_code = authorization_code

    @property
    def payment_type_code(self):
        return self._payment_type_code

    @payment_type_code.setter
    def payment_type_code(self, payment_type_code):
        self._payment_type_code = payment_type_code

    @property
    def response_code(self):
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        self._response_code = response_code

    @property
    def installments_number(self):
        return self._installments_number

    @installments_number.setter
    def installments_number(self, installments_number):
        self._installments_number = installments_number

    @property
    def installments_amount(self):
        return self._installments_amount

    @installments_amount.setter
    def installments_amount(self, installments_amount):
        self._installments_amount = installments_amount

    @property
    def commerce_code(self):
        return self._commerce_code

    @commerce_code.setter
    def commerce_code(self, commerce_code):
        self._commerce_code = commerce_code

    @property
    def buy_order(self):
        return self._buy_order

    @buy_order.setter
    def buy_order(self, buy_order):
        self._buy_order = buy_order



