from pydantic import BaseModel
from src.api.v1.notes.application.note.view_note.view_note_dto import ViewNoteDTO


class PydanticViewNotesRequestDto(BaseModel):
    note_id: str
    user_id: str

    def to_application(self) -> ViewNoteDTO:
        return ViewNoteDTO(note_id=self.note_id, user_id=self.user_id)

    @classmethod
    def from_application(cls, app_dto: ViewNoteDTO) -> "PydanticViewNotesRequestDto":
        return cls(note_id=app_dto.note_id, user_id=app_dto.user_id)
