from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.application.create.create_item_dto import CreateItemDto
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.errors import UserRepositoryError, UserRepositoryTypeError


class CreateItem:
    def __init__(
        self, repository: InventoryRepository, user_repository: UserRepository
    ):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: CreateItemDto) -> Inventory:

        # Valida si el usuario existe
        user_id = Uuid(dto.user_id)
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)

        # Crear y guardar el inventario
        inventory_item = Inventory(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            product_name=str(dto.product_name),
            amount=int(dto.amount),
            expiration_date=dto.expiration_date,
        )
        self.repository.save(inventory_item)
        return inventory_item
