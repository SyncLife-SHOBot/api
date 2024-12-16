import re

from src.api.v1.user.domain.errors import PhoneError, PhoneTypeError


class PhoneValidator:
    @staticmethod
    def validate(phone: str) -> str:
        phone_regex = r"^\+?1?\d{9,15}$"
        if not re.match(phone_regex, phone):
            raise PhoneError(PhoneTypeError.INVALID_PHONE)
        return phone
