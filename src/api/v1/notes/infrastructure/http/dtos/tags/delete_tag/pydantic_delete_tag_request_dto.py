from pydantic import BaseModel

from src.api.v1.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDto


class PydanticDeleteTagRequestDto(BaseModel):
    tag_id: str

    def to_application(self) -> DeleteTagDto:
        return DeleteTagDto(tag_id=self.tag_id)

    @classmethod
    def from_application(cls, app_dto: DeleteTagDto) -> "PydanticDeleteTagRequestDto":
        return cls(tag_id=app_dto.tag_id)
