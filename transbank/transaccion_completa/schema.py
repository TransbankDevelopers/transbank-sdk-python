from marshmallow import Schema, fields


class CreateTransactionRequestSchema(Schema):
    buy_order = fields.Str()
    session_id = fields.Str()
    amount = fields.Float()
    card_number = fields.Str()
    cvv = fields.Str()
    card_expiration_date = fields.Str()


class CreateTransactionResponseSchema(Schema):
    error_message = fields.Str()
    token = fields.Str()


class CommitTransactionRequestSchema(Schema):
    id_query_installments = fields.Str()
    deferred_periods_index = fields.Str()
    grace_period = fields.Str()


class CommitTransactionResponseSchema(Schema):
    vci = fields.Str()
    amount = fields.Str()
    status = fields.Str()
    buy_order = fields.Str()
    session_id = fields.Str()
    card_detail = fields.Str()
    accounting_date = fields.Str()
    transaction_date = fields.Str()
    authorization_code = fields.Str()
    payment_type_code = fields.Str()
    response_code = fields.Str()
    installments_number = fields.Str()
    installments_amount = fields.Str()
    balance = fields.Str()
