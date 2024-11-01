from enum import Enum


class UserTypeError(Enum):
    INVALID_BIRTHDATE = "La fecha de nacimiento no es válida."
    USER_ALREADY_EXISTS = "El usuario con este email ya existe."


class UserError(Exception):
    def __init__(self, error_type: UserTypeError):
        super().__init__(f"Error de User: {error_type.value}")
