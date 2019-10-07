from marshmallow import Schema, fields


class InscriptionStartRequestSchema(Schema):
    url = fields.Str()
    nombre = fields.Str()
    pApellido = fields.Str()
    sApellido = fields.Str()
    rut = fields.Str()
    serviceId = fields.Str()
    finalUrl = fields.Str()
    commerceCode = fields.Str()
    montoMaximo = fields.Float()
    telefonoFijo = fields.Str()
    telefonoCelular = fields.Str()
    nombrePatPass = fields.Str()
    correoPersona = fields.Str()
    correoComercio = fields.Str()
    direccion = fields.Str()
    ciudad = fields.Str()


class InscriptionStartResponseSchema(Schema):
    token = fields.Str()
    url = fields.Str()


class InscriptionStatusRequestSchema(Schema):
    token = fields.Str()


class InscriptionStatusResponseSchema(Schema):
    authorized = fields.Bool()
    voucherUrl = fields.Str()
