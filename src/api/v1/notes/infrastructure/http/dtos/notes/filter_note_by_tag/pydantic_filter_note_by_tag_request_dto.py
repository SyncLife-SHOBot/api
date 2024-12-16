from pydantic import BaseModel

from src.api.v1.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)


class PydanticFilterNotesByTagRequestDto(BaseModel):
    tag_id: str

    def to_application(self) -> FilterNotesByTagDTO:
        return FilterNotesByTagDTO(tag_id=self.tag_id)

    @classmethod
    def from_application(
        cls, app_dto: FilterNotesByTagDTO
    ) -> "PydanticFilterNotesByTagRequestDto":
        return cls(tag_id=app_dto.tag_id)
