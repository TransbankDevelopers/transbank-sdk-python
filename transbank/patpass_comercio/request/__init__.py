class InscriptionStartRequest(object):
    def __init__(self,
                 url: str,
                 name: str,
                 first_last_name: str,
                 second_last_name: str,
                 rut: str,
                 service_id: str,
                 final_url: str,
                 commerce_code: str,
                 max_amount: float,
                 phone_number: str,
                 mobile_number: str,
                 patpass_name: str,
                 person_email: str,
                 commerce_email: str,
                 address: str,
                 city: str):
        self.url = url
        self.nombre = name
        self.pApellido = first_last_name
        self.sApellido = second_last_name
        self.rut = rut
        self.serviceId = service_id
        self.finalUrl = final_url
        self.commerceCode = commerce_code;
        self.montoMaximo = max_amount
        self.telefonoFijo = phone_number
        self.telefonoCelular = mobile_number
        self.nombrePatPass = patpass_name
        self.correoPersona = person_email
        self.correoComercio = commerce_email
        self.direccion = address
        self.ciudad = city


class InscriptionStatusRequest(object):
    def __init__(self,
                 token: str):
        self.token = token
