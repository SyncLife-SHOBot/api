from enum import Enum
from src.api.v1.user.domain.errors.user_error import UserError


class FullNameTypeError(Enum):
    INVALID_NAME = "El nombre o apellido no es válido."


class FullNameError(UserError):
    def __init__(self, error_type: FullNameTypeError):
        super().__init__(f"Error de nombre: {error_type.value}")
