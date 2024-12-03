from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.notes.application.note.remove_tag.remove_tag_dto import RemoveTagDTO
from src.api.v1.shared.domain.value_objects import Uuid


class RemoveTagUseCase:
    def __init__(
        self, notes_repository: NotesRepository, tags_repository: TagsRepository
    ):
        self.notes_repository = notes_repository
        self.tags_repository = tags_repository

    def execute(self, dto: RemoveTagDTO) -> Notes:

        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.notes_repository.find_by_id(Uuid(dto.note_id))
        )

        # Valida el tag
        tag = TagsRepositoryValidator.tag_found(
            self.tags_repository.find_by_id(Uuid(dto.tag_id))
        )
        TagsRepositoryValidator.user_owns_tag(
            self.tags_repository, note.user_id, Uuid(dto.tag_id)
        )

        # Remueve el tag de la nota
        note.remove_tag(tag)

        # Actualiza la nota
        self.notes_repository.update(note)
        return note
