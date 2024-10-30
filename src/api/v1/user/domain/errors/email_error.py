from enum import Enum


class EmailTypeError(Enum):
    INVALID_EMAIL = "El correo electrónico no es válido."


class EmailError(Exception):
    def __init__(self, error_type: EmailTypeError):
        super().__init__(f"Error de Email: {error_type.value}")
