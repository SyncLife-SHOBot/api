from dataclasses import dataclass
from src.api.v1.inventory.domain.validators import AmountValidator



@dataclass(frozen=True)
class Amount:
    value: int

    def __post_init__(self) -> None:
        validated_amount = AmountValidator.validate(self.value)
        object.__setattr__(self, "value", validated_amount)
