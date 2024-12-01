from pydantic import BaseModel
from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)


class PydanticCreateNoteResponseDto(BaseModel):
    note: SqlModelNotesModel
