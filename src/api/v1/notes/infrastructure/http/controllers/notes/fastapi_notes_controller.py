from typing import List

from fastapi import HTTPException

from src.api.v1.notes.application.note.add_tag import AddTagsUseCase
from src.api.v1.notes.application.note.create_note import CreateNoteUseCase
from src.api.v1.notes.application.note.delete_note import DeleteNoteUseCase
from src.api.v1.notes.application.note.delete_note.delete_note_dto import DeleteNoteDTO
from src.api.v1.notes.application.note.filter_note_by_tag import FilterNotesByTagUseCase
from src.api.v1.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)
from src.api.v1.notes.application.note.remove_tag import RemoveTagUseCase
from src.api.v1.notes.application.note.update_note import UpdateNoteUseCase
from src.api.v1.notes.application.note.view_all_notes import ViewAllNotesUseCase
from src.api.v1.notes.application.note.view_all_notes.view_all_dto import (
    ViewAllNotesDTO,
)
from src.api.v1.notes.application.note.view_note import ViewNoteUseCase
from src.api.v1.notes.application.note.view_note.view_note_dto import ViewNoteDTO
from src.api.v1.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.v1.notes.infrastructure.http.dtos.notes import (
    PydanticAddTagToNoteRequestDto,
    PydanticAddTagToNoteResponseDto,
    PydanticCreateNoteRequestDto,
    PydanticCreateNoteResponseDto,
    PydanticDeleteNotesResponseDto,
    PydanticFilterNotesByTagResponseDto,
    PydanticRemoveTagRequestDto,
    PydanticRemoveTagResponseDto,
    PydanticUpdateNotesRequestDto,
    PydanticUpdateNotesResponseDto,
    PydanticViewNotesResponseDto,
)
from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)
from src.api.v1.notes.infrastructure.persistence.repositories.sqlmodel_notes_repository import (  # noqa: E501
    SQLModelNotesRepository,
)
from src.api.v1.notes.infrastructure.persistence.repositories.sqlmodel_tags_repository import (  # noqa: E501
    SQLModelTagsRepository,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.infrastructure.http.services.in_memory_session_service import (
    InMemorySessionService,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)

from .exception_handler import handle_exceptions


class FastApiNotesController:
    @staticmethod
    @handle_exceptions
    async def create(
        note_data: PydanticCreateNoteRequestDto, user_id: str
    ) -> PydanticCreateNoteResponseDto:
        repo = SQLModelNotesRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        InMemorySessionService.validate_permission(
            Uuid(user_id), Uuid(note_data.user_id)
        )

        use_case = CreateNoteUseCase(repo, user_repo)
        dto = note_data.to_application()
        note = use_case.execute(dto)

        return PydanticCreateNoteResponseDto(note=SqlModelNotesModel.from_entity(note))

    @staticmethod
    @handle_exceptions
    async def update(
        note_data: PydanticUpdateNotesRequestDto, user_id: str
    ) -> PydanticUpdateNotesResponseDto:
        repo = SQLModelNotesRepository.get_repository()
        note = repo.find_by_id(Uuid(note_data.note_id))
        if not note:
            raise HTTPException(
                status_code=404, detail=NotesError(NotesTypeError.NOTE_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), note.user_id)

        use_case = UpdateNoteUseCase(repo)
        dto = note_data.to_application()
        use_case.execute(dto)
        updated_note = repo.find_by_id(Uuid(dto.note_id))
        if updated_note is None:
            raise HTTPException(
                status_code=404, detail=NotesError(NotesTypeError.NOTE_NOT_FOUND)
            )
        return PydanticUpdateNotesResponseDto(
            note=SqlModelNotesModel.from_entity(updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def delete(note_id: str, user_id: str) -> PydanticDeleteNotesResponseDto:
        repo = SQLModelNotesRepository.get_repository()
        note = repo.find_by_id(Uuid(note_id))
        if not note:
            raise HTTPException(
                status_code=404, detail=NotesError(NotesTypeError.NOTE_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), note.user_id)

        use_case = DeleteNoteUseCase(repo)
        dto = DeleteNoteDTO(note_id=note_id)
        deleted_note = use_case.execute(dto)
        return PydanticDeleteNotesResponseDto(
            note=SqlModelNotesModel.from_entity(deleted_note)
        )

    @staticmethod
    @handle_exceptions
    async def view(note_id: str, user_id: str) -> PydanticViewNotesResponseDto:
        repo = SQLModelNotesRepository.get_repository()
        note = repo.find_by_id(Uuid(note_id))
        if not note:
            raise HTTPException(
                status_code=404, detail=NotesError(NotesTypeError.NOTE_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), note.user_id)

        use_case = ViewNoteUseCase(repo)
        dto = ViewNoteDTO(note_id=note_id, user_id=user_id)
        note = use_case.execute(dto, user_id)
        return PydanticViewNotesResponseDto(note=SqlModelNotesModel.from_entity(note))

    @staticmethod
    @handle_exceptions
    async def view_all(user_id: str) -> List[PydanticViewNotesResponseDto]:
        repo = SQLModelNotesRepository.get_repository()
        use_case = ViewAllNotesUseCase(repo)

        dto = ViewAllNotesDTO(user_id=Uuid(user_id))
        notes = use_case.execute(dto)

        if not notes:
            raise HTTPException(status_code=404, detail="No notes found")

        return [
            PydanticViewNotesResponseDto(note=SqlModelNotesModel.from_entity(note))
            for note in notes
        ]

    @staticmethod
    @handle_exceptions
    async def add_tag_to_note(
        tag_data: PydanticAddTagToNoteRequestDto, user_id: str
    ) -> PydanticAddTagToNoteResponseDto:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()

        note = notes_repo.find_by_id(Uuid(tag_data.note_id))
        if not note:
            raise HTTPException(status_code=404, detail="Nota no encontrada.")

        # Validar permisos del usuario
        InMemorySessionService.validate_permission(Uuid(user_id), note.user_id)

        # Ejecutar el caso de uso para agregar tags
        use_case = AddTagsUseCase(notes_repo, tags_repo)
        dto = tag_data.to_application()
        note = use_case.execute(dto, Uuid(user_id))

        return PydanticAddTagToNoteResponseDto(
            note=SqlModelNotesModel.from_entity(note)
        )

    @staticmethod
    @handle_exceptions
    async def remove_tag_from_note(
        remove_data: PydanticRemoveTagRequestDto, user_id: str
    ) -> PydanticRemoveTagResponseDto:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()

        # Obtener la nota
        note = notes_repo.find_by_id(Uuid(remove_data.note_id))
        if not note:
            raise HTTPException(status_code=404, detail="Nota no encontrada.")

        # Validar permisos del usuario
        InMemorySessionService.validate_permission(Uuid(user_id), note.user_id)

        # Ejecutar el caso de uso para eliminar el tag
        use_case = RemoveTagUseCase(notes_repo, tags_repo)
        dto = remove_data.to_application()
        updated_note = use_case.execute(dto)

        return PydanticRemoveTagResponseDto(
            note=SqlModelNotesModel.from_entity(updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def filter_notes_by_tag(
        tag_id: str, user_id: str
    ) -> List[PydanticFilterNotesByTagResponseDto]:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()

        # Obtener el tag
        tag = tags_repo.find_by_id(Uuid(tag_id))
        if not tag:
            raise HTTPException(status_code=404, detail="Tag no encontrado.")

        # Validar permisos del usuario para el tag
        InMemorySessionService.validate_permission(Uuid(user_id), tag.user_id)

        # Ejecutar el caso de uso para filtrar notas por etiqueta
        use_case = FilterNotesByTagUseCase(notes_repo, tags_repo)
        dto = FilterNotesByTagDTO(tag_id=tag_id)
        notes = use_case.execute(dto)

        if not notes:
            raise HTTPException(status_code=404, detail="No notes found for the tag")

        return [
            PydanticFilterNotesByTagResponseDto(
                note=SqlModelNotesModel.from_entity(note)
            )
            for note in notes
        ]
