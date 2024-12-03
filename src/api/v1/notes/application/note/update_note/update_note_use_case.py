import datetime
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.validators.notes.notes_validator import NotesValidator
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.notes.application.note.update_note.update_note_dto import UpdateNoteDTO
from src.api.v1.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.v1.shared.domain.value_objects import Uuid


class UpdateNoteUseCase:
    def __init__(self, repository: NotesRepository) -> None:
        self.repository = repository

    # Valida que el inventario existe
    def execute(self, dto: UpdateNoteDTO) -> Notes:
        note = NotesRepositoryValidator.note_found(
            self.repository.find_by_id(Uuid(dto.note_id))
        )

        # Actualiza la nota

        note.title = NotesValidator.validate_title(dto.title)
        note.content = NotesValidator.validate_content(dto.title, dto.content)
        note.updated_at = datetime.datetime.now()

        is_updated, updated_note = self.repository.update(note)

        if not is_updated or updated_note is None:
            raise NotesError(NotesTypeError.OPERATION_FAILED)

        return updated_note
