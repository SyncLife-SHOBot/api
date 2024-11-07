from fastapi import HTTPException
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import SqlModelInventoryModel
from src.api.v1.inventory.infrastructure.persistence.repositories.sqlmodel_inventory_repository import SQLModelInventoryRepository
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_create_item_dto import PydanticCreateItemDto
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_update_item_dto import PydanticUpdateItemDto
from src.api.v1.inventory.application.create.create_item import CreateItem
from src.api.v1.inventory.application.delete.delete_item import DeleteItem
from src.api.v1.inventory.application.update.update_item import UpdateItem
from src.api.v1.inventory.application.view.view_item import ViewItem
from src.api.v1.shared.infrastructure.persistence import get_session

class FastApiInventoryController:
    @staticmethod
    async def create(item_data: PydanticCreateItemDto) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = CreateItem(repo)
            dto = item_data.to_application()
            item = use_case.execute(dto)
            return SqlModelInventoryModel.from_entity(item)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    @staticmethod
    async def update(item_data: PydanticUpdateItemDto) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = UpdateItem(repo)
            dto = item_data.to_aplication()
            use_case.execute(dto)
            return SqlModelInventoryModel.from_entity(repo.find_by_id(dto.inventory_id))
        except Exception as e:
            raise HTTPException(status_code=400 , detail=str(e))
        
    @staticmethod
    async def delete(inventory_id: str) -> None:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = DeleteItem(repo)
            use_case.execute(inventory_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    @staticmethod
    async def view(inventory_id: str) -> SqlModelInventoryModel:
        with get_session() as session:
            repo = SQLModelInventoryRepository(session=session)
        try:
            use_case = ViewItem(repo)
            item = use_case.execute(inventory_id)
            return SqlModelInventoryModel.from_entity(item)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))