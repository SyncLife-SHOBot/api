from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.view_item.view_item_dto import ViewItemDTO
from src.api.v1.inventory.domain.validators.inventory_repository_validator import (
    InventoryRepositoryValidator,
)


class ViewItemUseCase:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: ViewItemDTO) -> Inventory:
        # Valida que el inventario existe
        inventory_id = Uuid(dto.inventory_id)
        inventory_item = InventoryRepositoryValidator.inventory_found(
            self.repository.find_by_id(inventory_id)
        )
        return inventory_item
