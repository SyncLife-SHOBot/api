from enum import Enum
from src.api.v1.user.domain.errors.user_error import UserError


class PhoneTypeError(Enum):
    INVALID_PHONE = "El número de teléfono no es válido."


class PhoneError(UserError):
    def __init__(self, error_type: PhoneTypeError):
        super().__init__(f"Error de teléfono: {error_type.value}")
