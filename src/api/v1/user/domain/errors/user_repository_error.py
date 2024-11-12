from enum import Enum
from src.api.v1.user.domain.errors.user_error import UserError


class UserRepositoryTypeError(Enum):
    USER_ALREADY_EXISTS = "El usuario con este email ya existe."
    USER_NOT_FOUND = "El usuario no esta registrado."
    OPERATION_FAILED = "La operación fallo."


class UserRepositoryError(UserError):
    def __init__(self, error_type: UserRepositoryTypeError):
        super().__init__(error_type.value)
