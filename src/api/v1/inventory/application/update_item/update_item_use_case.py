from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.update_item.update_item_dto import UpdateItemDto
from src.api.v1.inventory.domain.validators.inventory_repository_validator import (
    InventoryRepositoryValidator,
)
from src.api.v1.inventory.domain.errors import (
    InventoryItemError,
    InventoryItemTypeError,
)

from src.api.v1.inventory.domain.entities.inventory import Inventory


class UpdateItemUseCase:
    def __init__(self, repository: InventoryRepository) -> None:
        self.repository = repository

    # Valida que el inventario existe
    def execute(self, dto: UpdateItemDto) -> Inventory:
        inventory_item = InventoryRepositoryValidator.inventory_found(
            self.repository.find_by_id(Uuid(dto.inventory_id))
        )

        # Actualiza item

        inventory_item.product_name = str(dto.product_name)
        inventory_item.amount = int(dto.amount)
        inventory_item.expiration_date = dto.expiration_date

        is_updated, updated_item = self.repository.update(inventory_item)

        if not is_updated or updated_item is None:
            raise InventoryItemError(InventoryItemTypeError.OPERATION_FAILED)

        return updated_item
