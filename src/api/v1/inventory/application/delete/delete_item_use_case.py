__all__ = ["DeleteItem", "DeleteItemDTO"]

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.delete.delete_item_dto import DeleteItemDTO


class DeleteItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: DeleteItemDTO) -> bool:
        inventory_id = (
            Uuid(dto.inventory_id)
            if isinstance(dto.inventory_id, str)
            else dto.inventory_id
        )
        inventory_item = self.repository.find_by_id(inventory_id)
        if not inventory_item:
            return False

        self.repository.delete(inventory_item)
        return True
