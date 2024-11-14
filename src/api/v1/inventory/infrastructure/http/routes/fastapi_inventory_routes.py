from fastapi import APIRouter, Depends

from src.api.v1.inventory.infrastructure.http.controllers import (
    FastApiInventoryController,
)

from src.api.v1.inventory.infrastructure.http.dtos import (
    PydanticUpdateItemResponseDto,
    PydanticUpdateItemRequestDto,
    PydanticCreateItemResponseDto,
    PydanticCreateItemRequestDto,
    PydanticViewItemResponseDto,
    PydanticDeleteItemResponseDto,
)

from src.api.v1.user.infrastructure.http.services import InMemorySessionService

router: APIRouter = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/create", response_model=PydanticCreateItemResponseDto)
async def create_inventory_item(
    dto: PydanticCreateItemRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticCreateItemResponseDto:
    return await FastApiInventoryController.create(dto, user_id)


@router.get("/view/{inventory_id}", response_model=PydanticViewItemResponseDto)
async def view_inventory_item(
    inventory_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticViewItemResponseDto:
    return await FastApiInventoryController.view(inventory_id, user_id)


@router.put("/update", response_model=PydanticUpdateItemResponseDto)
async def update_inventory_item(
    dto: PydanticUpdateItemRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticUpdateItemResponseDto:
    return await FastApiInventoryController.update(dto, user_id)


@router.delete("/delete/{inventory_id}", response_model=PydanticDeleteItemResponseDto)
async def delete_inventory_item(
    inventory_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticDeleteItemResponseDto:
    return await FastApiInventoryController.delete(inventory_id, user_id)
