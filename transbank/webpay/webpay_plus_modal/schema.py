from marshmallow import Schema, fields

class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    return_url = fields.Str()

class TransactionRefundRequestSchema(Schema):
    amount = fields.Float()
