import re
from src.api.v1.user.domain.errors import PhoneError, PhoneTypeError


class PhoneValidator:
    @staticmethod
    def validate(phone: str) -> str:
        """
        Valida el formato del número de teléfono

        Args:
            phone (str): Número de teléfono a validar

        Returns:
            str: Número de teléfono validado

        Raises:
            PhoneError: Si el formato del teléfono no es válido
        """
        # Ejemplo de regex para validar teléfonos internacionales
        phone_regex = r"^\+?1?\d{9,15}$"
        if not re.match(phone_regex, phone):
            raise PhoneError(PhoneTypeError.INVALID_PHONE)
        return phone
