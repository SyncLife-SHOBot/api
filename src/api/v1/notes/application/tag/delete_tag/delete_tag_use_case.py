from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.notes.domain.errors.tags import TagsError, TagsTypeError
from src.api.v1.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDto
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteTagUseCase:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    def execute(self, dto: DeleteTagDto) -> Tags:
        # Valida que el tag exista
        tag = TagsRepositoryValidator.tag_found(
            self.repository.find_by_id(Uuid(dto.tag_id))
        )
        # Valida que el usuario sea dueño del tag
        TagsRepositoryValidator.user_owns_tag(
            self.repository, tag.user_id, Uuid(dto.tag_id)
        )
        # Elimina (logicamente) el tag
        is_deleted, deleted_tag = self.repository.delete(tag)

        if not is_deleted or deleted_tag is None:
            raise TagsError(TagsTypeError.OPERATION_FAILED)

        return deleted_tag
