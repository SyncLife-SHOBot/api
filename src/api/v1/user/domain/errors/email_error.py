from enum import Enum

from src.api.v1.user.domain.errors.user_error import UserError


class EmailTypeError(Enum):
    INVALID_EMAIL = "El correo electrónico no es válido."


class EmailError(UserError):
    def __init__(self, error_type: EmailTypeError):
        super().__init__(f"Error de Email: {error_type.value}")
