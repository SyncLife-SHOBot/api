from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import InventoryRepository
from src.api.v1.inventory.application.view.view_item_dto import ViewItemDTO


class ViewItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: ViewItemDTO) -> Inventory:
        inventory_item = self.repository.find_by_id(dto.inventory_id)
        if not inventory_item:
            raise ValueError("Item not found")
        return inventory_item