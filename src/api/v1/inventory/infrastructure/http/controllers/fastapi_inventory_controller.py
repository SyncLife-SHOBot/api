from src.api.v1.shared.domain.value_objects import Uuid
from fastapi import HTTPException
from src.api.v1.inventory.domain.errors import (
    InventoryItemTypeError,
    InventoryItemError,
)
from src.api.v1.shared.domain.value_objects.uuid import Uuid
from src.api.v1.inventory.infrastructure.persistence.models import (
    SqlModelInventoryModel,
)
from src.api.v1.inventory.infrastructure.persistence.repositories import (
    SQLModelInventoryRepository,
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
from src.api.v1.inventory.application.delete import DeleteItem, DeleteItemDTO
from src.api.v1.inventory.application.update import UpdateItem
from src.api.v1.inventory.application.view import ViewItem, ViewItemDTO
from src.api.v1.shared.infrastructure.persistence.sqlmodel_connection import get_session
from .exeption_handler import handle_exceptions


class FastApiInventoryController:
    @staticmethod
    @handle_exceptions
    async def create(
        item_data: PydanticCreateItemRequestDto, user_id: str
    ) -> PydanticCreateItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
            use_case = CreateItem(repo)
            dto = item_data.to_application()
            logging.debug("DEBUG - DTO passed to use case: %s", dto)
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
            use_case = UpdateItem(repo)
            dto = item_data.to_application()
            use_case.execute(dto)
            updated_item = repo.find_by_id(Uuid(dto.inventory_id))
            if not updated_item:
                raise HTTPException(
                    status_code=404,
                    detail=InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND),
                )
            return PydanticUpdateItemResponseDto(
                item=SqlModelInventoryModel.from_entity(updated_item)
            )

    @staticmethod
    @handle_exceptions
    async def delete(inventory_id: str, user_id: str) -> PydanticDeleteItemResponseDto:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
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
            use_case = ViewItem(repo)
            dto = ViewItemDTO(inventory_id=inventory_id)
            item = use_case.execute(dto)
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=InventoryItemError(InventoryItemTypeError.ITEM_NOT_FOUND),
                )
            return PydanticViewItemResponseDto(
                item=SqlModelInventoryModel.from_entity(item)
            )
