from src.api.v1.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.value_objects.email import Email
from src.api.v1.user.domain.value_objects.password import Password


class ChangePasswordUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: ChangePasswordDto) -> User:
        user = self.repository.find_by_email(Email(dto.email))

        if user is None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)

        user.password = Password(dto.new_password)

        is_updated, user_updated = self.repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated
