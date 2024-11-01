from enum import Enum


class UuidTypeError(Enum):
    INVALID_UUID = "La UUID no es válida."


class UuidError(Exception):
    def __init__(self, error_type: UuidTypeError):
        super().__init__(f"Error de UUID: {error_type.value}")
