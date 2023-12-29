from marshmallow import Schema, fields

from transbank.common.schema import CardDetailSchema

class MallInscriptionStartRequestSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    response_url = fields.Str()

class MallInscriptionDeleteRequestSchema(Schema):
    username = fields.Str()
    tbk_user = fields.Str()


class MallDetailsSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    installments_number = fields.Int()
    amount = fields.Str()


class MallTransactionAuthorizeRequestSchema(Schema):
    username = fields.Str()
    tbk_user = fields.Str()
    buy_order = fields.Str()
    details = fields.Nested(MallDetailsSchema, many=True)

class MallTransactionCaptureRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()

class MallTransactionRefundRequestSchema(Schema):
    commerce_code = fields.Str()
    detail_buy_order = fields.Str()
    amount = fields.Str()
