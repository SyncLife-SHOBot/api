from enum import Enum


class FullNameTypeError(Enum):
    INVALID_NAME = "El nombre o apellido no es válido."


class FullNameError(Exception):
    def __init__(self, error_type: FullNameTypeError):
        super().__init__(f"Error de FullName: {error_type.value}")
