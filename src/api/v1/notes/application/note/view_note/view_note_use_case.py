from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.application.note.view_note.view_note_dto import ViewNoteDTO
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ViewNoteUseCase:
    def __init__(self, repository: NotesRepository):
        self.repository = repository

    def execute(self, dto: ViewNoteDTO, user_id: str) -> Notes:
        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.repository.find_by_id(Uuid(dto.note_id))
        )
        # Valida que el usuario sea propietario de la notita
        NotesRepositoryValidator.user_owns_note(
            self.repository, Uuid(user_id), Uuid(dto.note_id)
        )
        return note
