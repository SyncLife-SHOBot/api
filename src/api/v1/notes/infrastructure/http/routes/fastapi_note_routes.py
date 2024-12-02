from src.api.v1.notes.infrastructure.http.controllers.notes.fastapi_notes_controller import (  # noqa: E501
    FastApiNotesController,
)

from src.api.v1.notes.infrastructure.http.dtos.notes import (
    PydanticCreateNoteResponseDto,
    PydanticCreateNoteRequestDto,
    PydanticUpdateNotesRequestDto,
    PydanticUpdateNotesResponseDto,
    PydanticViewNotesResponseDto,
    PydanticDeleteNotesResponseDto,
    PydanticAddTagToNoteRequestDto,
    PydanticAddTagToNoteResponseDto,
    PydanticFilterNotesByTagResponseDto,
    PydanticRemoveTagResponseDto,
    PydanticRemoveTagRequestDto,
)
from src.api.v1.user.infrastructure.http.services import InMemorySessionService
from typing import List
from fastapi import APIRouter, Depends

router: APIRouter = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/create", response_model=PydanticCreateNoteResponseDto)
async def create_note(
    dto: PydanticCreateNoteRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticCreateNoteResponseDto:
    return await FastApiNotesController.create(dto, user_id)


@router.get("/view/{note_id}", response_model=PydanticViewNotesResponseDto)
async def view_note(
    note_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticViewNotesResponseDto:
    return await FastApiNotesController.view(note_id, user_id)


@router.get("/view_all", response_model=List[PydanticViewNotesResponseDto])
async def view_all_notes(
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> List[PydanticViewNotesResponseDto]:
    return await FastApiNotesController.view_all(user_id)


@router.put("/update", response_model=PydanticUpdateNotesResponseDto)
async def update_nots(
    dto: PydanticUpdateNotesRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticUpdateNotesResponseDto:
    return await FastApiNotesController.update(dto, user_id)


@router.delete("/delete/{inventory_id}", response_model=PydanticDeleteNotesResponseDto)
async def delete_note(
    note_id: str, user_id: str = Depends(InMemorySessionService.validate_session_token)
) -> PydanticDeleteNotesResponseDto:
    return await FastApiNotesController.delete(note_id, user_id)


@router.post("/add_tag", response_model=PydanticAddTagToNoteResponseDto)
async def add_tag_to_note(
    dto: PydanticAddTagToNoteRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticAddTagToNoteResponseDto:
    return await FastApiNotesController.add_tag_to_note(dto, user_id)


@router.get("/filter_by_tag", response_model=List[PydanticFilterNotesByTagResponseDto])
async def filter_notes_by_tag(
    tag_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> List[PydanticFilterNotesByTagResponseDto]:
    return await FastApiNotesController.filter_notes_by_tag(tag_id, user_id)


@router.delete("/remove_tag", response_model=PydanticRemoveTagResponseDto)
async def remove_tag_from_note(
    dto: PydanticRemoveTagRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticRemoveTagResponseDto:
    return await FastApiNotesController.remove_tag_from_note(dto, user_id)
