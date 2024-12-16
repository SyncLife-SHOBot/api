from pydantic import BaseModel

from src.api.v1.notes.application.note.remove_tag.remove_tag_dto import RemoveTagDTO


class PydanticRemoveTagRequestDto(BaseModel):
    note_id: str
    tag_id: str

    def to_application(self) -> RemoveTagDTO:
        return RemoveTagDTO(
            note_id=self.note_id,
            tag_id=self.tag_id,
        )

    @classmethod
    def from_application(cls, app_dto: RemoveTagDTO) -> "PydanticRemoveTagRequestDto":
        return cls(
            note_id=app_dto.note_id,
            tag_id=app_dto.tag_id,
        )
