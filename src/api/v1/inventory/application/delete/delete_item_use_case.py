__all__ = ["DeleteItem", "DeleteItemDTO"]

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.repositories import (
    InventoryRepository,
)
from src.api.v1.inventory.domain.entities import Inventory
from src.api.v1.inventory.application.delete import DeleteItemDTO
from src.api.v1.inventory.domain.errors import (
    InventoryItemError,
    InventoryItemTypeError,
)


class DeleteItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: DeleteItemDTO) -> Inventory:
        inventory_id = (
            Uuid(dto.inventory_id)
            if isinstance(dto.inventory_id, str)
            else dto.inventory_id
        )
        inventory_item = self.repository.find_by_id(inventory_id)
        if not inventory_item:
            raise ValueError(InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND))

        self.repository.delete(inventory_item)
        return inventory_item
