from dataclasses import dataclass
from src.api.v1.user.domain.validators import FullNameValidator


@dataclass(frozen=True)
class FullName:
    first_name: str
    last_name: str

    def __post_init__(self) -> None:
        validated_first, validated_last = FullNameValidator.validate(
            self.first_name, self.last_name
        )
        object.__setattr__(self, "first_name", validated_first)
        object.__setattr__(self, "last_name", validated_last)

    def get_full_name(self, last_first: bool = False) -> str:
        return (
            f"{self.last_name}, {self.first_name}"
            if last_first
            else f"{self.first_name} {self.last_name}"
        )

    def __repr__(self) -> str:
        return f"<FullName({self.first_name} {self.last_name})>"

    def __eq__(self, other: object) -> bool:
        return (
            (self.first_name == other.first_name and self.last_name == other.last_name)
            if isinstance(other, FullName)
            else False
        )

    def __str__(self) -> str:
        return self.get_full_name()
