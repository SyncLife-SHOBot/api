from pydantic import BaseModel
from src.api.v1.notes.application.tag.update_tag.update_tag_dto import UpdateTagDto


class PydanticUpdateTagsRequestDto(BaseModel):
    tag_id: str
    name: str

    def to_application(self) -> UpdateTagDto:
        return UpdateTagDto(tag_id=self.tag_id, name=self.name)

    @classmethod
    def from_application(cls, app_dto: UpdateTagDto) -> "PydanticUpdateTagsRequestDto":
        return cls(tag_id=app_dto.tag_id, name=app_dto.name)
