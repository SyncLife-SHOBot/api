from pydantic import BaseModel
from src.api.v1.notes.application.note.delete_note.delete_note_dto import DeleteNoteDTO


class PydanticDeleteNotesRequestDto(BaseModel):
    note_id: str

    def to_application(self) -> DeleteNoteDTO:
        return DeleteNoteDTO(
            note_id=self.note_id,
        )

    @classmethod
    def from_application(
        cls, app_dto: DeleteNoteDTO
    ) -> "PydanticDeleteNotesRequestDto":
        return cls(
            note_id=app_dto.note_id,
        )
