from marshmallow import Schema, fields


class CardDetailSchema(Schema):
    card_number = fields.Str()
