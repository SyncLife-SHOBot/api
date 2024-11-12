from typing import Optional

from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.value_objects import Email


class UserRepositoryValidator:
    @staticmethod
    def is_email_already_registered(repository: UserRepository, email: Email) -> None:
        existing_user = repository.find_by_email(email, True)
        if existing_user is not None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_ALREADY_EXISTS)

    @staticmethod
    def user_found(user: Optional[User]) -> User:
        if user is None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)
        return user
