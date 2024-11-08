from src.api.v1.shared.domain.value_objects import Uuid
from fastapi import HTTPException
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)
from src.api.v1.inventory.infrastructure.persistence.repositories.sqlmodel_inventory_repository import (  # noqa: E501
    SQLModelInventoryRepository,
)
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_create_item_dto import (
    PydanticCreateItemDto,
)  # noqa: E501
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_update_item_dto import (
    PydanticUpdateItemDto,
)  # noqa: E501
from src.api.v1.inventory.application.create.create_item_use_case import CreateItem
from src.api.v1.inventory.application.delete.delete_item_use_case import DeleteItem
from src.api.v1.inventory.application.delete.delete_item_use_case import DeleteItemDTO
from src.api.v1.inventory.application.update.update_item_use_case import UpdateItem
from src.api.v1.inventory.application.view.view_item_use_case import ViewItem
from src.api.v1.inventory.application.view.view_item_use_case import ViewItemDTO
from src.api.v1.shared.infrastructure.persistence import get_session
import logging


class FastApiInventoryController:
    @staticmethod
    async def create(item_data: PydanticCreateItemDto) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = CreateItem(repo)
            dto = item_data.to_application()
            logging.debug("DEBUG - DTO passed to use case: %s", dto)
            item = use_case.execute(dto)
            logging.debug("DEBUG - Item created in use case: %s", item)
            return SqlModelInventoryModel.from_entity(item)
        except Exception as e:
            logging.error("Error in FastApiInventoryController.create: %s", e)
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def update(item_data: PydanticUpdateItemDto) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = UpdateItem(repo)
            dto = item_data.to_aplication()
            use_case.execute(dto)
            inventory_id = (
                Uuid(dto.inventory_id)
                if isinstance(dto.inventory_id, str)
                else dto.inventory_id
            )
            inventory_item = repo.find_by_id(inventory_id)
            if inventory_item is None:
                raise HTTPException(status_code=404, detail="Item not found")

            return SqlModelInventoryModel.from_entity(inventory_item)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def delete(inventory_id: str) -> bool:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = DeleteItem(repo)
            dto = DeleteItemDTO(inventory_id=inventory_id)
            success = use_case.execute(dto)
            if not success:
                raise HTTPException(status_code=404, detail="Item not found")
            return success
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def view(inventory_id: str) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = ViewItem(repo)
            dto = ViewItemDTO(inventory_id=inventory_id)
            item = use_case.execute(dto)
            return SqlModelInventoryModel.from_entity(item)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
