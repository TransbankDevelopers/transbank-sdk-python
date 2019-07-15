class TransactionCommitResponse:
    vci = None
    amount = None
    status = None
    buy_order = None
    session_id = None
    card_number = None
    accounting_date = None
    transaction_date = None
    authorization_code = None
    payment_type_code = None
    response_code = None
    installments_amount = None
    installments_number = None
    balance = None

    def __init_(self, json):
        self.vci = json.get('vci', None)
        self.amount = json.get('amount', None)
        self.status = json.get('status', None)
        self.buy_order = json.get('buy_order', None)
        self.session_id = json.get('session_id', None)
        self.card_number = json.get('card_details').get('card_number', None) \
            if json.get('card_details', None) is not None else None
        self.accounting_date = json.get('accounting_date', None)
        self.transaction_date = json.get('transaction_date', None)
        self.authorization_code = json.get('authorization_code', None)
        self.payment_type_code = json.get('payment_type_code', None)
        self.response_code = json.get('response_code', None)
        self.installments_amount = json.get('installments_amount', None)
        self.installments_number = json.get('installments_number', None)
        self.balance = json.get('balance', None)

    @property
    def vci(self):
        return self.vci

    @vci.setter
    def vci(self, vci):
        self.vci = vci

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self.amount = amount

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status

    @property
    def buy_order(self):
        return self.buy_order

    @buy_order.setter
    def buy_order(self, buy_order):
        self.buy_order = buy_order

    @property
    def session_id(self):
        return self.session_id

    @session_id.setter
    def session_id(self, session_id):
        self.session_id = session_id

    @property
    def card_number(self):
        return self.card_number

    @card_number.setter
    def card_number(self, card_number):
        self.card_number = card_number

    @property
    def accounting_date(self):
        return self.accounting_date

    @accounting_date.setter
    def accounting_date(self, accounting_date):
        self.accounting_date = accounting_date

    @property
    def transaction_date(self):
        return self.transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self.transaction_date = transaction_date

    @property
    def authorization_code(self):
        return self.authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        self.authorization_code = authorization_code

    @property
    def payment_type_code(self):
        return self.payment_type_code

    @payment_type_code.setter
    def payment_type_code(self, payment_type_code):
        self.payment_type_code = payment_type_code

    @property
    def response_code(self):
        return self.response_code

    @response_code.setter
    def response_code(self, response_code):
        self.response_code = response_code

    @property
    def installments_amount(self):
        return self.installments_amount

    @installments_amount.setter
    def installments_amount(self, installments_amount):
        self.installments_amount = installments_amount

    @property
    def installments_number(self):
        return self.installments_number

    @installments_number.setter
    def installments_number(self, installments_number):
        self.installments_number = installments_number

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, balance):
        self.balance = balance
