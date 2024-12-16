from typing import List

from src.api.v1.notes.application.note.view_all_notes.view_all_dto import (
    ViewAllNotesDTO,
)
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository


class ViewAllNotesUseCase:
    def __init__(self, repository: NotesRepository):
        self.repository = repository

    def execute(self, dto: ViewAllNotesDTO) -> List[Notes]:
        note = self.repository.find_all_by_user_id(dto.user_id)

        return note
