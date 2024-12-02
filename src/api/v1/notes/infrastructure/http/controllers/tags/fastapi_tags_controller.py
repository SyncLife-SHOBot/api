from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)
from src.api.v1.notes.infrastructure.persistence.repositories.sqlmodel_tags_repository import (  # noqa: E501
    SQLModelTagsRepository,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)
from src.api.v1.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDto,
    PydanticCreateTagResponseDto,
    PydanticDeleteTagResponseDto,
    PydanticUpdateTagsRequestDto,
    PydanticUpdateTagsResponseDto,
    PydanticViewTagsResponseDto,
)
from src.api.v1.notes.application.tag.create_tag import CreateTagUseCase
from src.api.v1.notes.application.tag.delete_tag import DeleteTagUseCase
from src.api.v1.notes.application.tag.update_tag import UpdateTagUseCase
from src.api.v1.notes.application.tag.view_tag import ViewTagUseCase
from src.api.v1.notes.application.tag.view_all_tags import ViewAllTagsUseCase
from src.api.v1.notes.application.tag.view_tag.view_tag_dto import ViewTagDto
from src.api.v1.notes.application.tag.view_all_tags.view_all_tags_dto import (
    ViewAllTagsDto,
)
from src.api.v1.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDto
from src.api.v1.notes.domain.errors.tags import TagsError, TagsTypeError
from src.api.v1.user.infrastructure.http.services.in_memory_session_service import (
    InMemorySessionService,
)
from src.api.v1.shared.domain.value_objects import Uuid
from .exception_handler import handle_exceptions
from fastapi import HTTPException
from typing import List


class FastApiTagsController:
    @staticmethod
    @handle_exceptions
    async def create(
        tag_data: PydanticCreateTagRequestDto, user_id: str
    ) -> PydanticCreateTagResponseDto:
        repo = SQLModelTagsRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        InMemorySessionService.validate_permission(
            Uuid(user_id), Uuid(tag_data.user_id)
        )

        use_case = CreateTagUseCase(repo, user_repo)
        dto = tag_data.to_application()
        tag = use_case.execute(dto)

        return PydanticCreateTagResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def update(
        tag_data: PydanticUpdateTagsRequestDto, user_id: str
    ) -> PydanticUpdateTagsResponseDto:
        repo = SQLModelTagsRepository.get_repository()
        tag = repo.find_by_id(Uuid(tag_data.tag_id))
        if not tag:
            raise HTTPException(
                status_code=404, detail=TagsError(TagsTypeError.TAG_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), tag.user_id)

        use_case = UpdateTagUseCase(repo)
        dto = tag_data.to_application()
        use_case.execute(dto)
        updated_tag = repo.find_by_id(Uuid(dto.tag_id))
        if updated_tag is None:
            raise HTTPException(
                status_code=404, detail=TagsError(TagsTypeError.TAG_NOT_FOUND)
            )
        return PydanticUpdateTagsResponseDto(
            tag=SqlModelTagsModel.from_entity(updated_tag)
        )

    @staticmethod
    @handle_exceptions
    async def delete(tag_id: str, user_id: str) -> PydanticDeleteTagResponseDto:
        repo = SQLModelTagsRepository.get_repository()
        tag = repo.find_by_id(Uuid(tag_id))
        if not tag:
            raise HTTPException(
                status_code=404, detail=TagsError(TagsTypeError.TAG_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), tag.user_id)

        use_case = DeleteTagUseCase(repo)
        dto = DeleteTagDto(tag_id=tag_id)
        deleted_tag = use_case.execute(dto)
        return PydanticDeleteTagResponseDto(
            tag=SqlModelTagsModel.from_entity(deleted_tag)
        )

    @staticmethod
    @handle_exceptions
    async def view(tag_id: str, user_id: str) -> PydanticViewTagsResponseDto:
        repo = SQLModelTagsRepository.get_repository()
        tag = repo.find_by_id(Uuid(tag_id))
        if not tag:
            raise HTTPException(
                status_code=404, detail=TagsError(TagsTypeError.TAG_NOT_FOUND)
            )
        InMemorySessionService.validate_permission(Uuid(user_id), tag.user_id)

        use_case = ViewTagUseCase(repo)
        dto = ViewTagDto(tag_id=tag_id, user_id=user_id)
        tag = use_case.execute(dto, user_id)
        return PydanticViewTagsResponseDto(tag=SqlModelTagsModel.from_entity(tag))

    @staticmethod
    @handle_exceptions
    async def view_all(user_id: str) -> List[PydanticViewTagsResponseDto]:
        repo = SQLModelTagsRepository.get_repository()
        use_case = ViewAllTagsUseCase(repo)

        dto = ViewAllTagsDto(user_id=Uuid(user_id))
        tags = use_case.execute(dto)

        if not tags:
            raise HTTPException(status_code=404, detail="Tags not found")

        return [
            PydanticViewTagsResponseDto(tag=SqlModelTagsModel.from_entity(tag))
            for tag in tags
        ]
