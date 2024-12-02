from pydantic import BaseModel
from src.api.v1.notes.application.tag.create_tag.create_tag_dto import CreateTagDto


class PydanticCreateTagRequestDto(BaseModel):
    user_id: str
    name: str

    def to_application(self) -> CreateTagDto:
        return CreateTagDto(user_id=self.user_id, name=self.name)

    @classmethod
    def from_application(cls, app_dto: CreateTagDto) -> "PydanticCreateTagRequestDto":
        return cls(user_id=app_dto.user_id, name=app_dto.name)
