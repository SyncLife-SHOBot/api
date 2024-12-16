from src.api.v1.notes.application.note.delete_note.delete_note_dto import DeleteNoteDTO
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteNoteUseCase:
    def __init__(self, repository: NotesRepository):
        self.repository = repository

    def execute(self, dto: DeleteNoteDTO) -> Notes:
        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.repository.find_by_id(Uuid(dto.note_id))
        )
        # Valida que el usuario sea dueño de la notita
        NotesRepositoryValidator.user_owns_note(
            self.repository, note.user_id, Uuid(dto.note_id)
        )
        # Elimina (logicamente) la nota
        is_deleted, deleted_note = self.repository.delete(note)

        if not is_deleted or deleted_note is None:
            raise NotesError(NotesTypeError.OPERATION_FAILED)

        return deleted_note
