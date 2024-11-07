from sqlmodel import  SQLModel, Field
from datetime import date
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.value_objects.amount import Amount
from src.api.v1.inventory.domain.value_objects.expiration_date import ExpirationDate
from src.api.v1.inventory.domain.value_objects.product_name import ProductName


class SqlModelInventoryModel(SQLModel, table=True):
    __tablename__  = "inventory"

    id: str = Field(primary_key=True)
    user_id: str
    product_name: str
    amount: int
    expiration_date: date


    @classmethod
    def from_entity(cls, entity: Inventory) -> "SqlModelInventoryModel":
        return cls(
            id = str(entity.id),
            user_id = str(entity.user_id),
            product_name = str(entity.product_name.name),
            amount = int(entity.amount.value),
            expiration_date = date(entity.expiration_date.date)
        )
    
    def to_entity(self) -> Inventory:
        return Inventory(
            id = Uuid(self.id),
            user_id = Uuid(self.user_id),
            product_name = ProductName(self.product_name),
            amount = Amount(self.amount),
            expiration_date = ExpirationDate(self.expiration_date)
        )