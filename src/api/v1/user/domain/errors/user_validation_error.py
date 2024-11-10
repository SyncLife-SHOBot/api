from enum import Enum
from src.api.v1.user.domain.errors.user_error import UserError


class UserValidationTypeError(Enum):
    INVALID_BIRTHDATE = "La fecha de nacimiento no es válida."
    USER_ALREADY_EXISTS = "El usuario con este email ya existe."
    INVALID_CREDENTIALS = "El email o la contraseño son incorrectos."


class UserValidationError(UserError):
    def __init__(self, error_type: UserValidationTypeError):
        super().__init__(error_type.value)
