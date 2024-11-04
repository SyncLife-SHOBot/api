from enum import Enum
from src.api.v1.user.domain.errors import UserError


class UserValidationTypeError(Enum):
    INVALID_BIRTHDATE = "La fecha de nacimiento no es válida."
    USER_ALREADY_EXISTS = "El usuario con este email ya existe."


class UserValidationError(UserError):
    def __init__(self, error_type: UserValidationTypeError):
        super().__init__(error_type.value)
