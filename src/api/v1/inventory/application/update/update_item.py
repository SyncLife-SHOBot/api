from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import InventoryRepository
from src.api.v1.inventory.application.update.update_item_dto import UpdateItemDto
from src.api.v1.shared.domain.value_objects.uuid import Uuid
from src.api.v1.inventory.domain.value_objects.product_name import ProductName
from src.api.v1.inventory.domain.value_objects.amount import Amount
from src.api.v1.inventory.domain.value_objects.expiration_date import ExpirationDate

class UpdateItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: UpdateItemDto) -> None:
        inventory_item = self.repository.find_by_id(dto.inventory_id)
        if not inventory_item:
            raise ValueError("item not found")
        
        update_inventory_item = Inventory(
            id = inventory_item.id,
            user_id = inventory_item.user_id,
            product_name = ProductName(dto.product_name),
            amount = Amount(dto.amount),
            expiration_date = ExpirationDate(dto.expiration_date)
        )

        self.repository.update(update_inventory_item)