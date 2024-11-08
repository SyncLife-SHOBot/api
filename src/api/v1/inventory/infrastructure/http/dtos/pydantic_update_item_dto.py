from pydantic import BaseModel
from datetime import date
from src.api.v1.inventory.application.update.update_item_dto import UpdateItemDto


class PydanticUpdateItemDto(BaseModel):
    inventory_id: str
    product_name: str
    amount: int
    expiration_date: date

    def to_aplication(self) -> UpdateItemDto:
        return UpdateItemDto(
            inventory_id=self.inventory_id,
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
        )
