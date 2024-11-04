from abc import ABC, abstractmethod
from typing import List, Optional
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.value_objects import Email


class UserRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: Email) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, user: User) -> bool:
        pass

    @abstractmethod
    def update(self, user: User) -> bool:
        pass
