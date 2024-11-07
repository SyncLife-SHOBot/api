from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors.user_validation_error import (
    UserValidationError,
    UserValidationTypeError,
)
from src.api.v1.user.domain.repositories import UserRepository


class ViewAccountUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: ViewAccountDto) -> User:
        uuid = Uuid(dto.uuid)

        user = self.repository.find_by_id(str(uuid))

        if user is None:
            raise UserValidationError(UserValidationTypeError.USER_NOT_FOUND)

        return user
