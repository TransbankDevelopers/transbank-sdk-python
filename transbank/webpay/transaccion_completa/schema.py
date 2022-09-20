from marshmallow import Schema, fields
from transbank.common.schema import CardDetailSchema

class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Str()
    card_number = fields.Str()
    cvv = fields.Str()
    card_expiration_date = fields.Str()

class TransactionCommitRequestSchema(Schema):
    id_query_installments = fields.Str()
    deferred_periods_index = fields.Str()
    grace_period = fields.Str()

class TransactionInstallmentsRequestSchema(Schema):
    installments_number = fields.Float()

class TransactionRefundRequestSchema(Schema):
    amount = fields.Str()

class TransactionCaptureRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()

class TransactionIncreaseAmountRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    amount = fields.Str()
    commerce_code = fields.Str()

class TransactionIncreaseAuthorizationDateRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    commerce_code = fields.Str()

class TransactionReversePreAuthorizedAmountRequestSchema(Schema):
    buy_order = fields.Str()
    authorization_code = fields.Str()
    amount = fields.Str()
    commerce_code = fields.Str()
