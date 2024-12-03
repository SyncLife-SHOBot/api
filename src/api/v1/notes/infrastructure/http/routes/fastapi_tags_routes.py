from src.api.v1.notes.infrastructure.http.controllers.tags.fastapi_tags_controller import (  # noqa: E501
    FastApiTagsController,
)
from src.api.v1.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDto,
    PydanticCreateTagResponseDto,
    PydanticUpdateTagsRequestDto,
    PydanticUpdateTagsResponseDto,
    PydanticViewTagsResponseDto,
    PydanticDeleteTagResponseDto,
)
from src.api.v1.user.infrastructure.http.services import InMemorySessionService
from typing import List
from fastapi import APIRouter, Depends

router: APIRouter = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/create", response_model=PydanticCreateTagResponseDto)
async def create_tag(
    dto: PydanticCreateTagRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticCreateTagResponseDto:
    return await FastApiTagsController.create(dto, user_id)


@router.get("/view/{tag_id}", response_model=PydanticViewTagsResponseDto)
async def view_tag(
    tag_id: str, user_id: str = Depends(InMemorySessionService.validate_session_token)
) -> PydanticViewTagsResponseDto:
    return await FastApiTagsController.view(tag_id, user_id)


@router.get("/view_all", response_model=List[PydanticViewTagsResponseDto])
async def view_all_tags(
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> List[PydanticViewTagsResponseDto]:
    return await FastApiTagsController.view_all(user_id)


@router.put("/update", response_model=PydanticUpdateTagsResponseDto)
async def update_tags(
    dto: PydanticUpdateTagsRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticUpdateTagsResponseDto:
    return await FastApiTagsController.update(dto, user_id)


@router.delete("/delete/{tag_id}", response_model=PydanticDeleteTagResponseDto)
async def delete_tag(
    tag_id: str, user_id: str = Depends(InMemorySessionService.validate_session_token)
) -> PydanticDeleteTagResponseDto:
    return await FastApiTagsController.delete(tag_id, user_id)
