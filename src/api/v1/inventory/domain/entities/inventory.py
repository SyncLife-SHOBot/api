from dataclasses import dataclass
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.validators.inventory_validator import (
    InventoryValidator,
)
from datetime import date


@dataclass()
class Inventory:
    id: Uuid
    user_id: Uuid
    product_name: str
    amount: int
    expiration_date: date

    def __post_init__(self) -> None:
        InventoryValidator.validate_all(
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
        )

    def __repr__(self) -> str:
        return (
            f"<InventoryItem(id={self.id},"
            f"product_name={self.product_name},"
            f"amount={self.amount})>"
        )

    def __str__(self) -> str:
        return (
            f"InventoryItem(Product name: {self.product_name}, "
            f"Amount: {self.amount}, Expiration date: {self.expiration_date})"
        )
