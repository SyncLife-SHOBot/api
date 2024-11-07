from fastapi import APIRouter
from src.api.v1.inventory.infrastructure.http.controllers.fastapi_inventory_controller import FastApiInventoryController
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_create_item_dto import PydanticCreateItemDto
from src.api.v1.inventory.infrastructure.http.dtos.pydantic_update_item_dto import PydanticUpdateItemDto
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import SqlModelInventoryModel

router: APIRouter = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/create", response_model=SqlModelInventoryModel)
async def create_inventory_item(item_data: PydanticCreateItemDto) -> SqlModelInventoryModel:
    return await FastApiInventoryController.create(item_data)

@router.get("/view/{inventory_id}", response_model=SqlModelInventoryModel)
async def view_inventory_item(inventory_id: str) -> SqlModelInventoryModel:
    return await FastApiInventoryController.view(inventory_id)

@router.put("/update", response_model=SqlModelInventoryModel)
async def update_inventory_item(item_data: PydanticUpdateItemDto) -> SqlModelInventoryModel:
    return await FastApiInventoryController.update(item_data)

@router.delete("/delete/{inventory_id}", response_model= SqlModelInventoryModel)
async def delete_inventory_item(inventory_id: str) -> None:
    return await FastApiInventoryController.delete(inventory_id)