from dataclasses import dataclass

from src.api.v1.user.domain.validators import PhoneValidator


@dataclass(frozen=True)
class Phone:
    phone: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "phone", PhoneValidator.validate(self.phone))

    def __repr__(self) -> str:
        return f"<Phone({self.phone})>"

    def __str__(self) -> str:
        return self.phone

    def __eq__(self, other: object) -> bool:
        return self.phone == other.phone if isinstance(other, Phone) else False
