from dataclasses import dataclass
from src.api.v1.inventory.domain.validators import (
    ProductNameValidator,
)


@dataclass(frozen=True)
class ProductName:
    name: str

    def __post_init__(self) -> None:
        validated_name = ProductNameValidator.validate(self.name)
        object.__setattr__(self, "name", validated_name)
