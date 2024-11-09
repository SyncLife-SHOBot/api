from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.update.update_item_dto import UpdateItemDto
from src.api.v1.inventory.domain.errors.inventoryItem_error import (
    InventoryItemTypeError,
    InventoryItemError,
)


class UpdateItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: UpdateItemDto) -> None:
        inventory_id = (
            Uuid(dto.inventory_id)
            if isinstance(dto.inventory_id, str)
            else dto.inventory_id
        )
        inventory_item = self.repository.find_by_id(inventory_id)
        if not inventory_item:
            raise InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND)

        update_inventory_item = Inventory(
            id=inventory_item.id,
            user_id=inventory_item.user_id,
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
        )

        self.repository.update(update_inventory_item)
