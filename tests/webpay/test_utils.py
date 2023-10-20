import secrets
import string
from transbank.common.api_constants import ApiConstants


def get_invalid_length_param() -> str:
    valid_string = string.ascii_letters + string.digits + "-._~"
    invalid_length_param = ''.join(secrets.choice(valid_string) for _ in range(ApiConstants.RETURN_URL_LENGTH + 1))
    return invalid_length_param
