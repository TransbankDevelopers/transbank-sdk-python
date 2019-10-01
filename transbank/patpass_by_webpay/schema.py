from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema


class WpmDetailSchema(Schema):
    service_id = fields.Str()
    card_holder_id = fields.Str()
    card_holder_name = fields.Str()
    card_holder_last_name1 = fields.Str()
    card_holder_last_name2 = fields.Str()
    card_holder_mail = fields.Str()
    cellphone_number = fields.Str()
    expiration_date = fields.Str()
    commerce_mail = fields.Str()
    uf_flag = fields.Bool()


class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    return_url = fields.Str()
    wpm_detail = fields.Nested(WpmDetailSchema, many=False)


class TransactionCreateResponseSchema(Schema):
    error_message = fields.Str()
    token = fields.Str()
    url = fields.Str()


class TransactionCommitResponseSchema(Schema):
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
