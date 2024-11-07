from dataclasses import dataclass
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.value_objects.product_name import ProductName
from src.api.v1.inventory.domain.value_objects.expiration_date import ExpirationDate
from src.api.v1.inventory.domain.value_objects.amount import Amount

@dataclass(frozen=True)
class Inventory:
    id: Uuid
    user_id: Uuid
    product_name: ProductName
    amount: Amount
    expiration_date: ExpirationDate    

def __repr__(self) -> str:
    return f"<InventoryItem(id={self.id}, product_name={self.product_name}, amount={self.amount})>"

def __str__(self) -> str:
    return (
        f"InventoryItem(Product name: {self.product_name}, "
        f"Amount: {self.amount}, Expiration date: {self.expiration_date})"
        )