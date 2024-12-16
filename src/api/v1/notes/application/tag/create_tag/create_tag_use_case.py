from src.api.v1.notes.application.tag.create_tag.create_tag_dto import CreateTagDto
from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateTagUseCase:
    def __init__(self, repository: TagsRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: CreateTagDto) -> Tags:

        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.user_repository.find_by_id(Uuid(dto.user_id))
        )

        # Valida que no haya otro tag con el mismo nombresillo
        TagsRepositoryValidator.tag_name_unique(
            self.repository, dto.name, Uuid(dto.user_id)
        )

        # Crear y guardar el tag
        tag = Tags(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            name=dto.name.strip(),
            is_deleted=False,
        )

        self.repository.save(tag)
        return tag
