from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema

class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    return_url = fields.Str()

class TransactionRefundRequestSchema(Schema):
    amount = fields.Float()

class MallTransactionRefundRequestSchema(Schema):
    amount = fields.Float()
    commerce_code = fields.Str()
    buy_order = fields.Str()

class MallDetailsSchema(Schema):
    amount = fields.Float()
    commerce_code = fields.Str()
    buy_order = fields.Str()
    status = fields.Str()
    authorization_code = fields.Str()
    payment_type_code = fields.Str()
    response_code = fields.Int()
    installments_number = fields.Int()

class MallTransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    return_url = fields.Str()
    details = fields.Nested(MallDetailsSchema, many=True)

class TransactionCaptureRequestSchema(Schema):
    buy_order = fields.Int()
    capture_amount = fields.Float()
    authorization_code = fields.Str()

class MallTransactionCaptureRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()

class MallDeferredTransactionRefundRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    amount = fields.Float()