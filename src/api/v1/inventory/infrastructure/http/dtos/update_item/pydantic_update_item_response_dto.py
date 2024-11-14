from pydantic import BaseModel
from src.api.v1.inventory.infrastructure.persistence.models import (
    SqlModelInventoryModel,
)


class PydanticUpdateItemResponseDto(BaseModel):
    item: SqlModelInventoryModel
