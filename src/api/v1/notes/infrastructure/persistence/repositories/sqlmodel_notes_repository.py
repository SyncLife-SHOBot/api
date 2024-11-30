from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shared.infrastructure.persistence import get_db_connection
from datetime import datetime
from typing import List, Optional, Tuple
from sqlmodel import Session, select, not_


class SQLModelNotesRepository(NotesRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SQLModelNotesRepository":
        with get_db_connection() as db_connection:
            return SQLModelNotesRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Notes]:
        query = (
            select(SqlModelNotesModel)
            if include_deleted
            else select(SqlModelNotesModel).where(not_(SqlModelNotesModel.is_deleted))
        )
        notes = self.db_connection.exec(query).all()
        return [note.to_entity() for note in notes]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[Notes]:
        query = (
            select(SqlModelNotesModel).where(SqlModelNotesModel.id == str(id))
            if include_deleted
            else (
                select(SqlModelNotesModel)
                .where(SqlModelNotesModel.id == str(id))
                .where(not_(SqlModelNotesModel.is_deleted))
            )
        )
        note = self.db_connection.exec(query).first()
        return note.to_entity() if note else None

    def find_all_by_user_id(
        self, user_id: Uuid, include_deleted: bool = False
    ) -> List[Notes]:
        query = select(SqlModelNotesModel).where(
            SqlModelNotesModel.user_id == str(user_id)
        )

        if not include_deleted:
            query = query.where(not_(SqlModelNotesModel.is_deleted))

        notes = self.db_connection.exec(query).all()
        return [note.to_entity() for note in notes]

    def find_by_title_and_user_id(self, title: str, user_id: Uuid) -> Optional[Notes]:
        query = (
            select(SqlModelNotesModel)
            .where(SqlModelNotesModel.title == title)
            .where(SqlModelNotesModel.user_id == str(user_id))
            .where(not_(SqlModelNotesModel.is_deleted))
        )
        note = self.db_connection.exec(query).first()
        return note.to_entity() if note else None

    def save(self, note: Notes) -> bool:
        note_model = SqlModelNotesModel.from_entity(note)
        self.db_connection.add(note_model)
        self.db_connection.commit()
        return True

    def update(self, note: Notes) -> Tuple[bool, Optional[Notes]]:
        existing_note = self.db_connection.exec(
            select(SqlModelNotesModel)
            .where(SqlModelNotesModel.id == str(note.id))
            .where(not_(SqlModelNotesModel.is_deleted))
        ).first()

        if not existing_note:
            return (False, None)

        updates = {
            "title": note.title,
            "content": note.content,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_note, field) != value:
                setattr(existing_note, field, value)

        self.db_connection.add(existing_note)
        self.db_connection.commit()
        self.db_connection.refresh(existing_note)

        return (True, existing_note.to_entity())

    def delete(self, note: Notes) -> Tuple[bool, Optional[Notes]]:
        existing_note = self.db_connection.exec(
            select(SqlModelNotesModel)
            .where(SqlModelNotesModel.id == str(note.id))
            .where(not_(SqlModelNotesModel.is_deleted))
        ).first()

        if not existing_note:
            return (False, None)

        existing_note.is_deleted = True
        existing_note.updated_at = datetime.now()
        self.db_connection.add(existing_note)
        self.db_connection.commit()
        self.db_connection.refresh(existing_note)

        return (True, existing_note.to_entity())
