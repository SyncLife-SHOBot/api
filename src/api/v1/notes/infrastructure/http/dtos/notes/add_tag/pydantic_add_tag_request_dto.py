from typing import List

from pydantic import BaseModel

from src.api.v1.notes.application.note.add_tag.add_tag_dto import AddTagsDTO


class PydanticAddTagToNoteRequestDto(BaseModel):
    note_id: str
    tags: List[str]

    def to_application(self) -> AddTagsDTO:
        return AddTagsDTO(note_id=self.note_id, tags=self.tags)

    @classmethod
    def from_application(cls, app_dto: AddTagsDTO) -> "PydanticAddTagToNoteRequestDto":
        return cls(note_id=app_dto.note_id, tags=app_dto.tags)
