from dataclasses import dataclass
from datetime import date
from src.api.v1.inventory.domain.validators.expiration_validator import ExpirationDateValidator

@dataclass(frozen=True)
class ExpirationDate:
    date: date

    def __post_init__(self) -> None:
        validated_date = ExpirationDateValidator.validate(self.date)
        object.__setattr__(self, "date", validated_date)
