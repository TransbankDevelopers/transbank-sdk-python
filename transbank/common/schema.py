from marshmallow import Schema, fields


class CardDetailSchema(Schema):
    card_number = fields.Str()


class MallDetailsSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    installments_number = fields.Int()
    amount = fields.Float()
