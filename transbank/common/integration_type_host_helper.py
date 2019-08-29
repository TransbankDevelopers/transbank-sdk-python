from transbank.common.integration_type import IntegrationType


class IntegrationTypeHostHelper(object):
    @classmethod
    def get_webpay_host(cls, integration_type: IntegrationType) -> str:
        if integration_type is IntegrationType.LIVE:
            return "https://webpay3g.transbank.cl"

        if integration_type is IntegrationType.TEST:
            return "https://webpay3gint.transbank.cl"

        if integration_type is IntegrationType.MOCK:
            return None

        return "https://webpay3gint.transbank.cl"
