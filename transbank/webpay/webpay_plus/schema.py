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

class MallTransactionStatusResponseSchema(Schema):
    vci = fields.Str()
    details = fields.List(fields.Raw())
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()


class TransactionCreateRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    return_url = fields.Str()


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


class TransactionRefundRequestSchema(Schema):
    amount = fields.Float()

class MallTransactionRefundRequestSchema(Schema):
    amount = fields.Float()
    commerce_code = fields.Str()
    buy_order = fields.Str()

class TransactionRefundResponseSchema(Schema):
    error_message = fields.Str()
    amount = fields.Float()
    type = fields.Str()
    balance = fields.Float()
    authorization_code = fields.Str()
    response_code = fields.Int()
    authorization_date = fields.Str()
    nullified_amount = fields.Float()

class DeferredTransactionResponseSchema(Schema):
    authorization_code = fields.Str()
    authorization_date = fields.Str()
    captured_amount = fields.Float()
    response_code = fields.Int()

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


class MallTransactionCreateResponseSchema(TransactionCreateResponseSchema):
    pass


class MallTransactionCommitResponseSchema(Schema):
    error_message = fields.Str()
    vci = fields.Str()
    details = fields.Nested(MallDetailsSchema, many=True)
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Nested(CardDetailSchema, many=False)
    accounting_date = fields.Str()
    transaction_date = fields.Str()


class DeferredTransactionRequestSchema(Schema):
    buy_order = fields.Int()
    capture_amount = fields.Float()
    authorization_code = fields.Str()

class MallDeferredTransactionRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    authorization_code = fields.Str()
    capture_amount = fields.Str()

class MallDeferredTransactionRefundRequestSchema(Schema):
    commerce_code = fields.Str()
    buy_order = fields.Str()
    amount = fields.Float()