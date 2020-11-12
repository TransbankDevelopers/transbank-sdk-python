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
