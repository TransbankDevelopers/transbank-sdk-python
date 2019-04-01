from marshmallow import Schema, fields

class ItemSchema(Schema):
    description = fields.Str()
    quantity = fields.Int()
    amount = fields.Int()
    additional_data = fields.Str(dump_to="additionalData")
    expire = fields.Int()

class TransactionCreateRequestSchema(Schema):
    external_unique_number = fields.Str(dump_to="externalUniqueNumber")
    total = fields.Int()
    items_quantity = fields.Int(dump_to = "itemsQuantity")
    issued_at = fields.Integer(dump_to = "issuedAt")
    items = fields.Nested(ItemSchema, many = True)
    callback_url = fields.Str(dump_to = "callbackUrl")
    channel = fields.Str()
    app_scheme = fields.Str(dump_to = "appScheme")
    app_key = fields.Str(dump_to = "appKey")
    api_key = fields.Str(dump_to = "apiKey")
    generate_ott_qr_code = fields.Bool(dump_to = "generateOttQrCode")
    signature = fields.Str()
    qr_width_height = fields.Str(dump_to = "widthHeight")
    commerce_logo_url = fields.Str(dump_to = "commerceLogoUrl")

class TransactionCreateResponseSchema(Schema):
    occ = fields.Str()
    ott = fields.Int()
    signature = fields.Str()
    external_unique_number = fields.Str(load_from="externalUniqueNumber", dump_to="externalUniqueNumber")
    issued_at = fields.Int(load_from="issuedAt", dump_to="issuedAt")
    qr_code_as_base64 = fields.Str(load_from="qrCodeAsBase64", dump_to="qrCodeAsBase64")

class TransactionCommitRequestSchema(Schema):
    occ = fields.Str()
    external_unique_number = fields.Str(dump_to="externalUniqueNumber")
    issued_at = fields.Int(dump_to="issuedAt")
    signature = fields.Str()
    app_key = fields.Str(dump_to = "appKey")
    api_key = fields.Str(dump_to = "apiKey")

class TransactionCommitResponseSchema(Schema):
    occ = fields.Str()
    authorization_code = fields.Str(load_from="authorizationCode")
    signature = fields.Str()
    transaction_desc = fields.Str(load_from="transactionDesc")
    buy_order = fields.Str(load_from="buyOrder")
    issued_at = fields.Int(load_from="issuedAt")
    amount = fields.Int()
    installments_amount = fields.Int(load_from="installmentsAmount")
    installments_number = fields.Int(load_from="installmentsNumber")

class SendTransactionResponseSchema(Schema):
    response_code = fields.Str(load_from="responseCode")
    description = fields.Str()
    result = fields.Nested(TransactionCreateResponseSchema)

class SendCommitResponseSchema(Schema):
    response_code = fields.Str(load_from="responseCode")
    description = fields.Str()
    result = fields.Nested(TransactionCommitResponseSchema)

class RefundCreateRequestSchema(Schema):
    occ = fields.Str()
    external_unique_number = fields.Str(dump_to="externalUniqueNumber")
    authorization_code = fields.Str(dump_to="authorizationCode")
    nullify_amount = fields.Int(dump_to = "nullifyAmount")
    issued_at = fields.Int(dump_to = "issuedAt")
    app_key = fields.Str(dump_to = "appKey")
    api_key = fields.Str(dump_to = "apiKey")
    signature = fields.Str()

class RefundCreateResponseSchema(Schema):
    occ = fields.Str()
    external_unique_number = fields.Str(load_from="externalUniqueNumber", dump_to="externalUniqueNumber")
    reverse_code = fields.Str(load_from="reverseCode", dump_to="reverseCode")
    issued_at = fields.Int(load_from="issuedAt", dump_to="issuedAt")
    signature = fields.Str()

class SendRefundResponseSchema(Schema):
    response_code = fields.Str(load_from="responseCode")
    description = fields.Str()
    result = fields.Nested(RefundCreateResponseSchema)
