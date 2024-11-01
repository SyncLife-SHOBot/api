from enum import Enum


class PhoneTypeError(Enum):
    INVALID_PHONE = "El número de teléfono no es válido."


class PhoneError(Exception):
    def __init__(self, error_type: PhoneTypeError):
        super().__init__(f"Error de Phone: {error_type.value}")
