from marshmallow import Schema, fields
from transbank.common.schema import CardDetailSchema


class CreateTransactionRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    card_number = fields.Str()
    card_expiration_date = fields.Str()
    details = fields.List(fields.Raw())


class CreateTransactionResponseSchema(Schema):
    error_message = fields.Str()
    token = fields.Str()


class CommitTransactionRequestSchema(Schema):
    details = fields.List(fields.Raw())


class CommitTransactionResponseSchema(Schema):
    error_message = fields.Str()
    amount = fields.Float()
    status = fields.Str()
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()
    authorization_code = fields.Str()
    payment_type_code = fields.Str()
    response_code = fields.Float()
    installments_number = fields.Float()
    expiration_date = fields.Str()
    details = fields.List(fields.Raw())


class InstallmentsTransactionRequestSchema(Schema):
    installments_number = fields.Float()
    buy_order = fields.Str()
    commerce_code = fields.Str()


class InstallmentsTransactionResponseSchema(Schema):
    error_message = fields.Str()
    installments_amount = fields.Float()
    id_query_installments = fields.Raw()
    deferred_periods = fields.Raw()


class StatusTransactionResponseSchema(Schema):
    error_message = fields.Str()
    amount = fields.Float()
    status = fields.Str()
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()
    authorization_code = fields.Str()
    payment_type_code = fields.Str()
    response_code = fields.Float()
    installments_number = fields.Float()
    expiration_date = fields.Str()
    details = fields.List(fields.Raw())


class RefundTransactionRequestSchema(Schema):
    amount = fields.Float()
    commerce_code = fields.Str()
    buy_order = fields.Str()


class RefundTransactionResponseSchema(Schema):
    error_message = fields.Str()
    type = fields.Str()
    authorization_code = fields.Str()
    authorization_date = fields.Str()
    nullified_amount = fields.Raw()
    balance = fields.Raw()
    response_code = fields.Raw()


class CaptureTransactionRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Float()


class CaptureTransactionResponseSchema(Schema):
    authorization_code = fields.Str()
    authorization_date = fields.Str()
    captured_amount = fields.Float()
    response_code = fields.Raw()
