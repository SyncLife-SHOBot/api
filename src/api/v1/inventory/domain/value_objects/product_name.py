from dataclasses import dataclass
from src.api.v1.inventory.domain.validators.product_name_validator import (
    ProductNameValidator,
)


@dataclass(frozen=True)
class ProductName:
    name: str

    def __post_init__(self) -> None:
        validated_name = ProductNameValidator.validate(self.name)
        object.__setattr__(self, "name", validated_name)
