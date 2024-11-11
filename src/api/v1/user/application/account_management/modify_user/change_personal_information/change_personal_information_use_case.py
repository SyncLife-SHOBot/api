from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDto,
)
from src.api.v1.user.domain.value_objects import Email, FullName, Phone


class ChangePersonalInformationUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: ChangePersonalInformationDto) -> User:
        user = self.repository.find_by_id(dto.uuid)

        if user is None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)

        user.email = Email(dto.email)
        user.full_name = FullName(dto.first_name, dto.last_name)
        user.birth_date = dto.birth_date
        user.phone = Phone(dto.phone)

        is_updated, user_updated = self.repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user
