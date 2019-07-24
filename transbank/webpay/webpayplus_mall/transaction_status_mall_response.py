from .detail import Detail


class TransactionStatusMallResponse:
    def __init__(self, json_data):
        self._buy_order = json_data.get('buy_order', None)
        self._vci = json_data.get('vci', None)
        self._card_detail = dict({'card_number': json_data.get('card_detail').get('card_number', None) if
        json_data.get('card_detail', None) is not None else None})
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
    def card_detail(self):
        return self._card_detail

    @card_detail.setter
    def card_detail(self, card_detail):
        self._card_detail = card_detail

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

    def as_dict(self):
        instance_as_dict = None
        if self._details is not None:
            instance_as_dict = {k[1:]: v for k, v in self.__dict__.items() if k[1:] != 'details'}
            instance_as_dict['details'] = [e.attributes_as_dict() for e in self._details]
        return instance_as_dict
