from enum import Enum


class PasswordTypeError(Enum):
    TOO_SHORT = "La contraseña debe tener al menos 8 caracteres."
    MISSING_NUMBER = "La contraseña debe contener al menos un número."
    MISSING_UPPERCASE = "La contraseña debe contener al menos una letra mayúscula."
    MISSING_LOWERCASE = "La contraseña debe contener al menos una letra minúscula."
    MISSING_SPECIAL = "La contraseña debe contener al menos un carácter especial."


class PasswordError(Exception):
    def __init__(self, error_type: PasswordTypeError):
        super().__init__(f"Error de Password: {error_type.value}")
