from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.entities import Inventory
from src.api.v1.inventory.domain.repositories import (
    InventoryRepository,
)
from src.api.v1.inventory.application.view import ViewItemDTO
from src.api.v1.inventory.domain.errors import (
    InventoryItemError,
    InventoryItemTypeError,
)


class ViewItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: ViewItemDTO) -> Inventory:
        inventory_id = (
            Uuid(dto.inventory_id)
            if isinstance(dto.inventory_id, str)
            else dto.inventory_id
        )
        inventory_item = self.repository.find_by_id(inventory_id)
        if not inventory_item:
            raise InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND)
        return inventory_item
