from typing import List, Optional, Tuple
from sqlmodel import Session, select, not_
from datetime import datetime
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.v1.shared.infrastructure.persistence import get_db_connection


class SqlModelUserRepository(UserRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SqlModelUserRepository":
        with get_db_connection() as db_connection:
            return SqlModelUserRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[User]:
        query = (
            select(SqlModelUserModel)
            if include_deleted
            else select(SqlModelUserModel).where(not_(SqlModelUserModel.is_deleted))
        )
        users = self.db_connection.exec(query).all()
        return [user.to_entity() for user in users]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[User]:
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.id == id)
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.id == str(id))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.db_connection.exec(query).first()
        return user.to_entity() if user else None

    def find_by_email(
        self, email: Email, include_deleted: bool = False
    ) -> Optional[User]:
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.email == str(email))
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.email == str(email))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.db_connection.exec(query).first()

        return user.to_entity() if user else None

    def save(self, user: User) -> bool:
        user_model = SqlModelUserModel.from_entity(user)
        self.db_connection.add(user_model)
        self.db_connection.commit()
        return True

    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == str(user.uuid)
        )
        db_user = self.db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        updates = {
            "email": user.email.email,
            "password": user.password.password,
            "first_name": user.full_name.first_name,
            "last_name": user.full_name.last_name,
            "birth_date": user.birth_date,
            "phone": user.phone.phone,
        }
        for field, value in updates.items():
            if getattr(db_user, field) != value:
                setattr(db_user, field, value)

        db_user.updated_at = datetime.now()
        self.db_connection.add(db_user)
        self.db_connection.commit()
        self.db_connection.refresh(db_user)

        return (True, db_user.to_entity())

    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.id
        )
        db_user = self.db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        db_user.is_deleted = True
        db_user.updated_at = datetime.now()
        self.db_connection.add(db_user)
        self.db_connection.commit()
        self.db_connection.refresh(db_user)

        return (True, db_user.to_entity())
