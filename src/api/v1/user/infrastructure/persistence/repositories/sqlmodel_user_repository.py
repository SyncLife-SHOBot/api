from typing import List, Optional, Tuple
from sqlmodel import Session, select, not_
from datetime import datetime
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel


class SQLModelUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> List[User]:
        statement = select(SqlModelUserModel).where(not_(SqlModelUserModel.is_deleted))
        users = self.session.exec(statement).all()
        return [user.to_entity() for user in users]

    def find_by_id(self, id: str, include_deleted: bool = False) -> Optional[User]:
        if include_deleted:
            statement = select(SqlModelUserModel).where(SqlModelUserModel.id == id)
        else:
            statement = (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.id == id)
                .where(not_(SqlModelUserModel.is_deleted))
            )
        user = self.session.exec(statement).first()
        return user.to_entity() if user else None

    def find_by_email(
        self, email: Email, include_deleted: bool = False
    ) -> Optional[User]:
        if include_deleted:
            statement = select(SqlModelUserModel).where(
                SqlModelUserModel.email == str(email)
            )
        else:
            statement = (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.email == str(email))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        user = self.session.exec(statement).first()

        return user.to_entity() if user else None

    def save(self, user: User) -> bool:
        user_model = SqlModelUserModel.from_entity(user)
        self.session.add(user_model)
        self.session.commit()
        return True

    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.id
        )
        db_user = self.session.exec(statement).first()
        if db_user:
            db_user.updated_at = datetime.now()
            if user.email.email != db_user.email:
                db_user.email = user.email.email
            if user.password.password != db_user.password:
                db_user.password = user.password.password
            if user.full_name.first_name != db_user.first_name:
                db_user.first_name = user.full_name.first_name
            if user.full_name.last_name != db_user.last_name:
                db_user.last_name = user.full_name.last_name
            if user.birth_date != db_user.birth_date:
                db_user.birth_date = user.birth_date
            if user.phone.phone != user.phone:
                db_user.phone = user.phone.phone

            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)
            user = db_user.to_entity()
            return (True, user)
        return (False, None)

    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.id
        )
        db_user = self.session.exec(statement).first()

        if db_user:
            db_user.is_deleted = True
            db_user.updated_at = datetime.now()
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)

            user_entity = db_user.to_entity()
            return (True, user_entity)
        return (False, None)
