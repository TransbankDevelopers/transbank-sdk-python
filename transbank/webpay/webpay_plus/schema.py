from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema


class TransactionStatusResponseSchema(Schema):
    error_message = fields.Str()
    vci = fields.Str()
    amount = fields.Float()
    status = fields.Str()
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()
    authorization_code = fields.Str()
    payment_type_code = fields.Str()
    response_code = fields.Int()
    installments_number = fields.Int()
    installments_amount = fields.Float()
    balance = fields.Float()


class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    return_url = fields.Str()


class TransactionCreateResponseSchema(Schema):
    error_message = fields.Str()
    token = fields.Str()
    url = fields.Str()
