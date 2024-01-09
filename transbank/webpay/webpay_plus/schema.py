from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema

class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Str()
    return_url = fields.Str()

class TransactionRefundRequestSchema(Schema):
    amount = fields.Str()

class TransactionCaptureRequestSchema(Schema):
    buy_order = fields.Str()
    capture_amount = fields.Str()
    authorization_code = fields.Str()
