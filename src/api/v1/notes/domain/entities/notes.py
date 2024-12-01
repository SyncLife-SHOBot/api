from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.notes.domain.validators import NotesValidator


@dataclass()
class Notes:
    id: Uuid
    user_id: Uuid
    title: str
    content: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        NotesValidator.validate_all(
            title=self.title,
            content=self.content,
        )

    def __repr__(self) -> str:
        return (
            f"<title(={self.title},"
            f"content={self.content},"
            f"created_at={self.created_at})>"
        )

    def __str__(self) -> str:
        return (
            f"Note(Note title: {self.title},"
            f"Content: {self.content},"
            f"Created at: {self.created_at})"
        )
