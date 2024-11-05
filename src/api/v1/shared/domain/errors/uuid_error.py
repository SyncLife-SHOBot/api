from enum import Enum
from src.api.v1.shared.domain.errors.shared_error import SharedError


class UuidTypeError(Enum):
    INVALID_UUID = "La UUID no es válida."


class UuidError(SharedError):
    def __init__(self, error_type: UuidTypeError):
        super().__init__(f"Error de UUID: {error_type.value}")
