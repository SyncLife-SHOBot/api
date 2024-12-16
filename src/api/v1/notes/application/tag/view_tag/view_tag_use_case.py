from src.api.v1.notes.application.tag.view_tag.view_tag_dto import ViewTagDto
from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ViewTagUseCase:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    def execute(self, dto: ViewTagDto, user_id: str) -> Tags:
        # Valida que el tag exista
        tag = TagsRepositoryValidator.tag_found(
            self.repository.find_by_id(Uuid(dto.tag_id))
        )
        # Valida que el usuario sea propietario del tagsillo
        TagsRepositoryValidator.user_owns_tag(
            self.repository, Uuid(user_id), Uuid(dto.tag_id)
        )

        return tag
