class WpmDetail(object):
    def __init__(self, service_id: str, card_holder_id: str, card_holder_name: str, card_holder_last_name1: str,
                 card_holder_last_name2: str, card_holder_mail: str, cellphone_number: str,
                 expiration_date: str, commerce_mail: str, uf_flag: bool):
        self.service_id = service_id
        self.card_holder_id = card_holder_id
        self.card_holder_name = card_holder_name
        self.card_holder_last_name1 = card_holder_last_name1
        self.card_holder_last_name2 = card_holder_last_name2
        self.card_holder_mail = card_holder_mail
        self.cellphone_number = cellphone_number
        self.expiration_date = expiration_date
        self.commerce_mail = commerce_mail
        self.uf_flag = uf_flag


class TransactionCreateRequest(object):
    def __init__(self, buy_order: str, session_id: str, amount: float, return_url: str, service_id: str,
                 card_holder_id: str, card_holder_name: str, card_holder_last_name1: str, card_holder_last_name2: str,
                 card_holder_mail: str, cellphone_number: str, expiration_date: str, commerce_mail: str, uf_flag: bool):
        self.buy_order = buy_order
        self.session_id = session_id
        self.return_url = return_url
        self.amount = amount
        self.wpm_detail = WpmDetail(service_id, card_holder_id, card_holder_name, card_holder_last_name1,
                                    card_holder_last_name2, card_holder_mail, cellphone_number, expiration_date,
                                    commerce_mail, uf_flag)
