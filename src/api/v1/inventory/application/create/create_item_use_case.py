from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.create.create_item_dto import CreateItemDto
from src.api.v1.shared.domain.value_objects.uuid import Uuid
import logging


class CreateItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: CreateItemDto) -> Inventory:
        logging.debug("Executing use case with DTO: %s", dto)
        inventory_item = Inventory(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
        )
        self.repository.save(inventory_item)
        return inventory_item
