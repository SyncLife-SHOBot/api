from dataclasses import dataclass
from api.v1.user.domain.validators import EmailValidator


@dataclass(frozen=True)
class Email:
    email: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "email", EmailValidator.validate(self.email))

    def __repr__(self) -> str:
        return f"<Email({self.email})>"

    def __eq__(self, other: object) -> bool:
        return self.email == other.email if isinstance(other, Email) else False

    def __str__(self) -> str:
        return self.email
