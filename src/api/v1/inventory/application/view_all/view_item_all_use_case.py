from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.application.view_all.view_all_item_dto import (
    ViewAllInventoryItemsDTO,
)
from typing import List


class ViewAllInventoryItems:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: ViewAllInventoryItemsDTO) -> List[Inventory]:
        inventory_items = self.repository.find_all_by_user_id(dto.user_id)

        return inventory_items
