from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema, MallDetailsSchema


class InscriptionStartRequestSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    response_url = fields.Str()


class InscriptionStartResponseSchema(Schema):
    token = fields.Str()
    url_webpay = fields.Str()


class InscriptionFinishResponseSchema(Schema):
    response_code = fields.Int()
    tbk_user = fields.Str()
    authorization_code = fields.Str()
    credit_card_type = fields.Str()
    last_four_card_digits = fields.Str()


class InscriptionDeleteRequestSchema(Schema):
    username = fields.Str()
    tbk_user = fields.Str()


class TransactionAuthorizeRequestSchema(Schema):
    username = fields.Str()
    tbk_user = fields.Str()
    buy_order = fields.Str()
    details = fields.Nested(MallDetailsSchema, many=True)


class TransactionAuthorizeResponseSchema(Schema):
    transaction_date = fields.Str()
    accounting_date = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    buy_order = fields.Str()
    details = fields.List(fields.Raw())


class TransactionRefundResponseSchema(Schema):
    type = fields.Str()
    balance = fields.Float()
    authorization_code = fields.Str()
    response_code = fields.Int()
    authorization_date = fields.Str()
    nullified_amount = fields.Float()


class TransactionRefundRequestSchema(Schema):
    commerce_code = fields.Str()
    detail_buy_order = fields.Str()
    amount = fields.Float()


class TransactionStatusResponseSchema(Schema):
    buy_order = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()
    details = fields.List(fields.Raw())
