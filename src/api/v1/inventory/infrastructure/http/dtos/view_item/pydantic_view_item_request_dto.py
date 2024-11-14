from pydantic import BaseModel
from src.api.v1.inventory.application.view import ViewItemDTO


class PydanticViewItemRequestDto(BaseModel):
    inventory_id: str

    def to_application(self) -> ViewItemDTO:
        return ViewItemDTO(
            inventory_id=self.inventory_id,
        )

    @classmethod
    def from_application(cls, app_dto: ViewItemDTO) -> "PydanticViewItemRequestDto":
        return cls(
            inventory_id=app_dto.inventory_id,
        )
