from pydantic import BaseModel
from src.api.v1.notes.application.tag.view_tag.view_tag_dto import ViewTagDto


class PydanticViewTagsRequestDto(BaseModel):
    tag_id: str
    user_id: str

    def to_application(self) -> ViewTagDto:
        return ViewTagDto(tag_id=self.tag_id, user_id=self.user_id)

    @classmethod
    def from_application(cls, app_dto: ViewTagDto) -> "PydanticViewTagsRequestDto":
        return cls(tag_id=app_dto.tag_id, user_id=app_dto.user_id)
