from pydantic import BaseModel
from src.api.v1.inventory.application.delete_item.delete_item_dto import DeleteItemDTO


class PydanticDeleteItemRequestDto(BaseModel):
    inventory_id: str

    def to_application(self) -> DeleteItemDTO:
        return DeleteItemDTO(
            inventory_id=self.inventory_id,
        )

    @classmethod
    def from_application(cls, app_dto: DeleteItemDTO) -> "PydanticDeleteItemRequestDto":
        return cls(
            inventory_id=app_dto.inventory_id,
        )
