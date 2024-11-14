from src.api.v1.inventory.domain.entities import Inventory
from src.api.v1.inventory.domain.repositories import (
    InventoryRepository,
)
from src.api.v1.inventory.application.create import CreateItemDto
from src.api.v1.shared.domain.value_objects import Uuid


class CreateItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: CreateItemDto) -> Inventory:
        inventory_item = Inventory(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
        )
        self.repository.save(inventory_item)
        return inventory_item
