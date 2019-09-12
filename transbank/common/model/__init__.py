class CardDetail(object):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def __repr__(self) -> str:
        return "CardDetail(card_number: {})".format(self.card_number)
