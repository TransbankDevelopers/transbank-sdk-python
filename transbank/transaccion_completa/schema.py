from marshmallow import Schema, fields


class CreateTransactionRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    card_number = fields.Str()
    cvv = fields.Str()
    card_expiration_date = fields.Str()


class CreateTransactionResponseSchema(Schema):
    error_message = fields.Str()
    token = fields.Str()
