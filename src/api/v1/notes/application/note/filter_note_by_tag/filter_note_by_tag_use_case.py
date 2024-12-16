from typing import List

from src.api.v1.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class FilterNotesByTagUseCase:
    def __init__(
        self, notes_repository: NotesRepository, tags_repository: TagsRepository
    ):
        self.notes_repository = notes_repository
        self.tags_repository = tags_repository

    def execute(self, dto: FilterNotesByTagDTO) -> List[Notes]:

        # Valida que el tag exista
        tag = self.tags_repository.find_by_id(Uuid(dto.tag_id))
        TagsRepositoryValidator.tag_found(tag)

        # Filtra las notas por el tagsillo
        notes = self.notes_repository.find_by_tag(Uuid(dto.tag_id))
        return notes
