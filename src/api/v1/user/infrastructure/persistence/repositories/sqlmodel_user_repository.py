from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel


class SQLModelUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> List[User]:
        statement = select(SqlModelUserModel).where(not SqlModelUserModel.is_deleted)
        users = self.session.exec(statement).all()
        return [user.to_entity() for user in users]

    def find_by_id(self, id: str) -> Optional[User]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == id, not SqlModelUserModel.is_deleted
        )
        user = self.session.exec(statement).first()
        return user.to_entity() if user else None

    def find_by_email(self, email: Email) -> Optional[User]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.email == str(email), not SqlModelUserModel.is_deleted
        )
        user = self.session.exec(statement).first()
        return user.to_entity() if user else None

    def save(self, user: User) -> bool:
        user_model = SqlModelUserModel.from_entity(user)
        self.session.add(user_model)
        self.session.commit()
        return True

    def update(self, user: User) -> bool:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.id
        )
        db_user = self.session.exec(statement).first()
        if db_user:
            user_model = SqlModelUserModel.from_entity(user)
            user_model.updated_at = datetime.now()
            for key, value in user_model.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.session.add(db_user)
            self.session.commit()
            return True
        return False

    def delete(self, user: User) -> bool:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.id
        )
        db_user = self.session.exec(statement).first()

        if db_user:
            user_model = SqlModelUserModel.from_entity(user)
            user_model.is_deleted = True
            user_model.deleted_at = datetime.now()
            self.session.add(db_user)
            self.session.commit()
            return True
        return False
