from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional
from src.api.v1.user.domain.entities import User
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.value_objects import Email, FullName, Password, Phone


class SqlModelUserModel(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    is_deleted: bool = Field(default=False)
    created_at: date = Field(default_factory=date.today)
    updated_at: Optional[date] = Field(default=None)

    @classmethod
    def from_entity(cls, entity: User) -> "SqlModelUserModel":
        return cls(
            id=str(entity.uuid.id),
            email=entity.email.email,
            password=entity.password.password,
            first_name=entity.full_name.first_name,
            last_name=entity.full_name.last_name,
            birth_date=entity.birth_date,
            phone=entity.phone.phone,
            is_deleted=False,
        )

    def to_entity(self) -> User:
        return User(
            uuid=Uuid(self.id),
            email=Email(self.email),
            password=Password(self.password),
            full_name=FullName(self.first_name, self.last_name),
            birth_date=self.birth_date,
            phone=Phone(self.phone),
        )
