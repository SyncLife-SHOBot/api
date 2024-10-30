import re
import bcrypt
from api.v1.user.domain.errors import PasswordError, PasswordTypeError


class PasswordValidator:
    @staticmethod
    def validate(password: str) -> str:
        """Valida la seguridad de una contraseña en texto plano."""
        if len(password) < 8:
            raise PasswordError(PasswordTypeError.TOO_SHORT)
        if not re.search(r"\d", password):
            raise PasswordError(PasswordTypeError.MISSING_NUMBER)
        if not re.search(r"[A-Z]", password):
            raise PasswordError(PasswordTypeError.MISSING_UPPERCASE)
        if not re.search(r"[a-z]", password):
            raise PasswordError(PasswordTypeError.MISSING_LOWERCASE)
        if not re.search(r"[\W_]", password):
            raise PasswordError(PasswordTypeError.MISSING_SPECIAL)
        return password

    @staticmethod
    def encrypt_password(password: str) -> str:
        """Encripta la contraseña si aún no está encriptada."""
        if PasswordValidator.is_encrypted(password):
            return password
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def is_encrypted(password: str) -> bool:
        """Determina si la contraseña ya está encriptada comprobando su
        formato `bcrypt`."""
        bcrypt_regex = r"^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$"
        return bool(re.match(bcrypt_regex, password))

    @staticmethod
    def check_password(plain_password: str, hashed_password: str) -> bool:
        """Verifica una contraseña en texto plano contra la encriptada."""
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
