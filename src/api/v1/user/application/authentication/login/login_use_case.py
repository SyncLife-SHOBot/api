from src.api.v1.user.application.authentication.login.login_dto import LoginDto
from src.api.v1.user.domain.entities.user import User
from src.api.v1.user.domain.errors import (
    UserValidationError,
    UserValidationTypeError,
)
from src.api.v1.user.domain.repositories.user_repository import UserRepository
from src.api.v1.user.domain.value_objects import Email, Password


class LoginUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: LoginDto) -> User:
        email = Email(dto.email)
        password = Password(dto.password)

        user = self.repository.find_by_email(email)

        if user is None:
            raise UserValidationError(UserValidationTypeError.USER_NOT_FOUND)

        if user.password.check_password(password.password):
            raise UserValidationError(UserValidationTypeError.INVALID_CREDENTIALS)

        return user
