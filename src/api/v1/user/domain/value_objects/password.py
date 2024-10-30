from dataclasses import dataclass
from api.v1.user.domain.validators import PasswordValidator


@dataclass(frozen=True)
class Password:
    password: str

    def __post_init__(self) -> None:
        # Valida y encripta la contraseña si aún no está encriptada
        if not PasswordValidator.is_encrypted(self.password):
            PasswordValidator.validate(self.password)
            encrypted_password = PasswordValidator.encrypt_password(self.password)
            object.__setattr__(self, "password", encrypted_password)

    def __repr__(self) -> str:
        return "<Password(***)>"

    def __eq__(self, other: object) -> bool:
        return self.password == other.password if isinstance(other, Password) else False

    def __str__(self) -> str:
        return "********"

    def check_password(self, plain_password: str) -> bool:
        """Verifica una contraseña en texto plano contra la encriptada."""
        return PasswordValidator.check_password(plain_password, self.password)
