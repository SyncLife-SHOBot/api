from pydantic import BaseModel
from datetime import date
from src.api.v1.inventory.application.create.create_item_dto import CreateItemDto


class PydanticCreateItemRequestDto(BaseModel):
    user_id: str
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self) -> CreateItemDto:
        return CreateItemDto(
            user_id=self.user_id,
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
        )

    @classmethod
    def from_application(cls, app_dto: CreateItemDto) -> "PydanticCreateItemRequestDto":
        return cls(
            user_id=app_dto.user_id,
            product_name=app_dto.product_name,
            amount=app_dto.amount,
            expiration_date=app_dto.expiration_date,
        )
