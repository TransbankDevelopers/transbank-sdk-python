from .detail import Detail


class TransactionCommitResponse:
    def __init__(self, json_data):
        self._buy_order = json_data.get('buy_order', None)
        self._vci = json_data.get('vci', None)
        self._amount = json_data.get('amount', None)
        self._card_number = json_data.get('card_details').get('card_number', None) \
            if json_data.get('card_details', None) is not None else None
        self._accounting_date = json_data.get('accounting_date', None)
        self._transaction_date = json_data.get('transaction_date', None)
        self._details = [Detail(i) for i in json_data.get('details')]

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
    def details(self):
        return self._details

    @details.setter
    def details(self, array_details):
        self._details = [Detail(i) for i in array_details]
