import datetime
from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.notes.domain.validators.tags.tags_validator import TagsValidator
from src.api.v1.notes.application.tag.update_tag.update_tag_dto import UpdateTagDto
from src.api.v1.notes.domain.errors.tags import TagsError, TagsTypeError
from src.api.v1.shared.domain.value_objects import Uuid


class UpdateTagUseCase:
    def __init__(self, repository: TagsRepository) -> None:
        self.repository = repository

    # Valida que el tag exista
    def execute(self, dto: UpdateTagDto) -> Tags:
        tag = TagsRepositoryValidator.tag_found(
            self.repository.find_by_id(Uuid(dto.tag_id))
        )

        # Actualizar el tag

        tag.name = TagsValidator.validate_name(dto.name)
        tag.updated_at = datetime.datetime.now()

        is_updated, updated_tag = self.repository.update(tag)

        if not is_updated or updated_tag is None:
            raise TagsError(TagsTypeError.OPERATION_FAILED)

        return updated_tag
