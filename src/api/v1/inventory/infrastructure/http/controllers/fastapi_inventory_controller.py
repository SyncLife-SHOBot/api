from typing import List
from src.api.v1.shared.domain.value_objects import Uuid
from fastapi import HTTPException
from src.api.v1.inventory.domain.errors import (
    InventoryItemTypeError,
    InventoryItemError,
)
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)
from src.api.v1.inventory.infrastructure.persistence.repositories import (
    SQLModelInventoryRepository,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)
from src.api.v1.inventory.infrastructure.http.dtos import (
    PydanticCreateItemRequestDto,
    PydanticCreateItemResponseDto,
    PydanticUpdateItemRequestDto,
    PydanticUpdateItemResponseDto,
    PydanticDeleteItemResponseDto,
    PydanticViewItemResponseDto,
)
from src.api.v1.inventory.application.create import CreateItem
from src.api.v1.inventory.application.delete import DeleteItem
from src.api.v1.inventory.application.delete.delete_item_dto import DeleteItemDTO
from src.api.v1.inventory.application.update import UpdateItem
from src.api.v1.inventory.application.view import ViewItem
from src.api.v1.inventory.application.view.view_item_dto import ViewItemDTO
from src.api.v1.inventory.application.view_all import ViewAllInventoryItems
from src.api.v1.inventory.application.view_all.view_all_item_dto import (
    ViewAllInventoryItemsDTO,
)
from src.api.v1.shared.infrastructure.persistence.sqlmodel_connection import get_session
from src.api.v1.user.infrastructure.http.services.in_memory_session_service import (
    InMemorySessionService,
)
from .exeption_handler import handle_exceptions


class FastApiInventoryController:
    @staticmethod
    @handle_exceptions
    async def create(
        item_data: PydanticCreateItemRequestDto, user_id: str
    ) -> PydanticCreateItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            user_repo = SqlModelUserRepository(db_connection=session)
            InMemorySessionService.validate_permission(
                Uuid(user_id), Uuid(item_data.user_id)
            )

            use_case = CreateItem(repo, user_repo)
            dto = item_data.to_application()
            item = use_case.execute(dto)
            return PydanticCreateItemResponseDto(
                item=SqlModelInventoryModel.from_entity(item)
            )

    @staticmethod
    @handle_exceptions
    async def update(
        item_data: PydanticUpdateItemRequestDto, user_id: str
    ) -> PydanticUpdateItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            inventory_item = repo.find_by_id(Uuid(item_data.inventory_id))
            if not inventory_item:
                raise HTTPException(
                    status_code=404,
                    detail=InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND),
                )
            InMemorySessionService.validate_permission(
                Uuid(user_id), inventory_item.user_id
            )

            use_case = UpdateItem(repo)
            dto = item_data.to_application()
            use_case.execute(dto)
            updated_item = repo.find_by_id(Uuid(dto.inventory_id))
            if updated_item is None:
                raise HTTPException(
                    status_code=404, detail="Updated inventory item not found"
                )

            return PydanticUpdateItemResponseDto(
                item=SqlModelInventoryModel.from_entity(updated_item)
            )

    @staticmethod
    @handle_exceptions
    async def delete(inventory_id: str, user_id: str) -> PydanticDeleteItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            inventory_item = repo.find_by_id(Uuid(inventory_id))
            if not inventory_item:
                raise HTTPException(
                    status_code=404,
                    detail=InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND),
                )
            InMemorySessionService.validate_permission(
                Uuid(user_id), inventory_item.user_id
            )

            use_case = DeleteItem(repo)
            dto = DeleteItemDTO(inventory_id=inventory_id)
            deleted_item = use_case.execute(dto)
            return PydanticDeleteItemResponseDto(
                item=SqlModelInventoryModel.from_entity(deleted_item)
            )

    @staticmethod
    @handle_exceptions
    async def view(inventory_id: str, user_id: str) -> PydanticViewItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            inventory_item = repo.find_by_id(Uuid(inventory_id))
            if not inventory_item:
                raise HTTPException(
                    status_code=404,
                    detail=InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND),
                )
            InMemorySessionService.validate_permission(
                Uuid(user_id), inventory_item.user_id
            )

            use_case = ViewItem(repo)
            dto = ViewItemDTO(inventory_id=inventory_id)
            item = use_case.execute(dto)
            return PydanticViewItemResponseDto(
                item=SqlModelInventoryModel.from_entity(item)
            )

    @staticmethod
    async def view_all(user_id: str) -> List[PydanticViewItemResponseDto]:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            use_case = ViewAllInventoryItems(repo)

            dto = ViewAllInventoryItemsDTO(user_id=Uuid(user_id))
            inventory_items = use_case.execute(dto)

            if not inventory_items:
                raise HTTPException(status_code=404, detail="No inventory items found")

            return [
                PydanticViewItemResponseDto(
                    item=SqlModelInventoryModel.from_entity(item)
                )
                for item in inventory_items
            ]
