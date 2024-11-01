from dataclasses import dataclass
from datetime import date
from api.v1.user.domain.repositories import UserRepository
from api.v1.user.domain.validators import UserValidator
from api.v1.user.domain.entities import User
from api.v1.shared.domain.value_objects import Uuid
from api.v1.user.domain.value_objects import Email, FullName, Password, Phone
from api.v1.user.domain.errors import UserError, UserTypeError


@dataclass
class RegisterDto:
    email: str
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date


class RegisterUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: RegisterDto) -> User:
        uuid = Uuid()
        email = Email(dto.email)
        full_name = FullName(dto.first_name, dto.last_name)
        password = Password(dto.password)
        phone = Phone(dto.phone)

        UserValidator.validate_minimum_age(dto.birth_date)

        if UserValidator.is_email_already_registered(self.repository, email):
            raise UserError(UserTypeError.USER_ALREADY_EXISTS)

        user = User(
            uuid=uuid,
            email=email,
            password=password,
            full_name=full_name,
            birth_date=dto.birth_date,
            phone=phone.phone,
        )

        self.repository.save(user)

        return user
