from src.api.v1.notes.application.note.add_tag.add_tag_dto import AddTagsDTO
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class AddTagsUseCase:
    def __init__(
        self, notes_repository: NotesRepository, tags_repository: TagsRepository
    ):
        self.notes_repository = notes_repository
        self.tags_repository = tags_repository

    def execute(self, dto: AddTagsDTO, user_id: Uuid) -> Notes:

        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.notes_repository.find_by_id(Uuid(dto.note_id))
        )

        if note.user_id != user_id:
            raise NotesError(NotesTypeError.NOTE_NOT_OWNED)

        # Valida los tags
        for tag_id in dto.tags:
            tag = TagsRepositoryValidator.tag_found(
                self.tags_repository.find_by_id(Uuid(tag_id))
            )

            if tag.user_id != user_id:
                raise NotesError(NotesTypeError.NOTE_NOT_OWNED)

            # Agrea el tagsillo a la notita
            note.add_tag(tag)

        # Actualiza la nota
        updated = self.notes_repository.update(note)
        if not updated:
            print("Error al actualizar la nota en el repositorio")

        return note
