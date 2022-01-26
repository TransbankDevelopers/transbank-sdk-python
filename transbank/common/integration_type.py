from enum import Enum, unique


@unique
class IntegrationType(Enum):
    LIVE = 1
    TEST = 2
    MOCK = 3

def webpay_host(integration_type: IntegrationType) -> str:
    if integration_type is IntegrationType.LIVE:
        return "https://webpay3g.transbank.cl"

    if integration_type is IntegrationType.TEST:
        return "https://webpay3gint.transbank.cl"

    if integration_type is IntegrationType.MOCK:
        return None

    return "https://webpay3gint.transbank.cl"


def patpass_comercio_host(integration_type: IntegrationType) -> str:
    if integration_type is IntegrationType.LIVE:
        return "https://www.pagoautomaticocontarjetas.cl"

    if integration_type is IntegrationType.TEST:
        return "https://pagoautomaticocontarjetasint.transbank.cl"

    if integration_type is IntegrationType.MOCK:
        return None

    return "https://pagoautomaticocontarjetasint.transbank.cl"
