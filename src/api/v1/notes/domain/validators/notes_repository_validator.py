from typing import Optional

from src.api.v1.notes.domain.errors import (
    NotesError,
    NotesTypeError,
)

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories import NotesRepository


class NotesRepositoryValidator:
    @staticmethod
    def note_found(note: Optional[Notes]) -> Notes:
        if note is None:
            raise NotesError(NotesTypeError.NOTE_NOT_FOUND)
        return note

    @staticmethod
    def user_owns_note(
        repository: NotesRepository, user_id: Uuid, note_id: Uuid
    ) -> None:
        note = repository.find_by_id(note_id)
        if note is None or note.user_id != user_id:
            raise NotesError(NotesTypeError.NOTE_NOT_OWNED)

    @staticmethod
    def note_title_unique(
        repository: NotesRepository, title: str, user_id: Uuid
    ) -> None:
        if repository.find_by_title_and_user_id(title, user_id):
            raise NotesError(NotesTypeError.DUPLICATED_TITLE)
