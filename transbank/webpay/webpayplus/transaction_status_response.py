class TransactionStatusResponse:

    def __init__(self, json_data):
        self._vci = json_data.get('vci', None)
        self._amount = json_data.get('amount', None)
        self._status = json_data.get('status', None)
        self._buy_order = json_data.get('buy_order', None)
        self._session_id = json_data.get('session_id', None)
        self._card_number = json_data.get('card_details').get('card_number', None) \
            if json_data.get('card_details', None) is not None else None
        self.accounting_date = json_data.get('accounting_date', None)
        self.transaction_date = json_data.get('transaction_date', None)
        self._authorization_code = json_data.get('authorization_code', None)
        self._payment_type_code = json_data.get('payment_type_code', None)
        self._response_code = json_data.get('response_code', None)
        self._installments_amount = json_data.get('installments_amount', None)
        self._installments_number = json_data.get('installments_number', None)
        self._balance = json_data.get('balance', None)

    @property
    def vci(self):
        return self._vci

    @vci.setter
    def vci(self, vci):
        self._vci = vci

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
    def buy_order(self):
        return self._buy_order

    @buy_order.setter
    def buy_order(self, buy_order):
        self._buy_order = buy_order

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number

    @property
    def accounting_date(self):
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, accounting_date):
        self._accounting_date = accounting_date

    @property
    def transaction_date(self):
        return self.transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self._transaction_date = transaction_date

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
    def installments_amount(self):
        return self._installments_amount

    @installments_amount.setter
    def installments_amount(self, installments_amount):
        self._installments_amount = installments_amount

    @property
    def installments_number(self):
        return self._installments_number

    @installments_number.setter
    def installments_number(self, installments_number):
        self._installments_number = installments_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance
