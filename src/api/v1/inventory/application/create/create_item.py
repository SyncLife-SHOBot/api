from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import InventoryRepository
from src.api.v1.inventory.application.create.create_item_dto import CreateItemDto
from src.api.v1.shared.domain.value_objects.uuid import Uuid
from src.api.v1.inventory.domain.value_objects.product_name import ProductName
from src.api.v1.inventory.domain.value_objects.amount import Amount
from src.api.v1.inventory.domain.value_objects.expiration_date import ExpirationDate

class CreateItem:
    def __init__(self,repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: CreateItemDto) -> Inventory:
        inventory_item = Inventory(
            id = Uuid.generate(),
            user_id = Uuid(dto.user_id),
            product_name = ProductName(dto.product_name),
            amount = Amount(dto.amount),
            expiration_date = ExpirationDate(dto.expiration_date)
        )
        self.repository.save(inventory_item)
        return inventory_item
    
    