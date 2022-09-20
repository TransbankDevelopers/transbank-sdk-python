from marshmallow import Schema, fields

class MallTransactionRefundRequestSchema(Schema):
    amount = fields.Str()
    commerce_code = fields.Str()
    buy_order = fields.Str()

class MallDetailsSchema(Schema):
    amount = fields.Str()
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

class MallTransactionCaptureRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()

class MallTransactionIncreaseAmountRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    amount = fields.Str()
    commerce_code = fields.Str()

class MallTransactionIncreaseAuthorizationDateRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    commerce_code = fields.Str()

class MallTransactionReversePreAuthorizedAmountRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    amount = fields.Str()
    commerce_code = fields.Str()

class MallTransacionDeferredCaptureHistoryRequestSchema(Schema):
    buy_order = fields.Str()
    commerce_code = fields.Str()
