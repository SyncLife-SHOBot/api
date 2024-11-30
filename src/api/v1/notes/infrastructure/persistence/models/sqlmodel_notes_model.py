from datetime import datetime
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class SqlModelNotesModel(SQLModel, table=True):
    __tablename__ = "notes"

    id: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    title: str
    content: str
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default=None)
    user: "SqlModelUserModel" = Relationship(back_populates="notes")

    @classmethod
    def from_entity(cls, entity: "Notes") -> "SqlModelNotesModel":
        return cls(
            id=str(entity.id),
            user_id=str(entity.user_id),
            title=entity.title.strip(),
            content=entity.content.strip(),
            is_deleted=False,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> "Notes":
        return Notes(
            id=Uuid(self.id),
            user_id=Uuid(self.user_id),
            title=self.title,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
