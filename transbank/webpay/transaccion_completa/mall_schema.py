from marshmallow import Schema, fields

class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    card_number = fields.Str()
    card_expiration_date = fields.Str()
    details = fields.List(fields.Raw())
    cvv = fields.Str()

class TransactionCommitRequestSchema(Schema):
    details = fields.List(fields.Raw())

class TransactionInstallmentsRequestSchema(Schema):
    installments_number = fields.Float()
    buy_order = fields.Str()
    commerce_code = fields.Str()

class TransactionRefundRequestSchema(Schema):
    amount = fields.Str()
    commerce_code = fields.Str()
    buy_order = fields.Str()

class TransactionCaptureRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()
