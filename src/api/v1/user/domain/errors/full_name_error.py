from enum import Enum
from src.api.v1.user.domain.errors.user_error import UserError


class FullNameTypeError(Enum):
    INVALID_NAME = "El nombre o apellido no es válido."
    INVALID_NAME_FORMAT = "El nombre o apellido tiene caracteres inválidos."
    NAME_TOO_LONG = "El nombre o apellido es demasiado largo."


class FullNameError(UserError):
    def __init__(self, error_type: FullNameTypeError):
        super().__init__(f"Error de nombre: {error_type.value}")
