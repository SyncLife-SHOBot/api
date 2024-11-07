from dataclasses import dataclass, field
from typing import List
from datetime import date, datetime
from typing import Optional
from src.api.v1.user.domain.validators.user_validator import UserValidator
from src.api.v1.user.domain.value_objects import Email, FullName, Password
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.value_objects.phone import Phone


@dataclass
class User:
    uuid: Uuid
    email: Email
    password: Password
    full_name: FullName
    birth_date: date
    phone: Phone
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime]
    inventory: List[Inventory] = field(default_factory=list)
    def __post_init__(self) -> None:
        UserValidator.validate_minimum_age(self.birth_date)

    def __repr__(self) -> str:
        return f"<User(uuid={self.uuid}, email={self.email}, phone={self.phone})>"

    def __str__(self) -> str:
        return (
            f"User({self.full_name.get_full_name()}, "
            f"Email: {self.email}, UUID: {self.uuid}, "
            f"Birth Date: {self.birth_date}),"
            f"Phone: {self.phone},"
            f"Inventory Products: {len(self.inventory)}"
        )
