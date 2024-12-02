from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.application.tag.view_all_tags.view_all_tags_dto import (
    ViewAllTagsDto,
)
from typing import List


class ViewAllTagsUseCase:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    def execute(self, dto: ViewAllTagsDto) -> List[Tags]:
        tag = self.repository.find_all_by_user_id(dto.user_id)

        return tag
