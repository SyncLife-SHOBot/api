from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators import UserValidator
from src.api.v1.user.domain.entities import User
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.value_objects import Email, FullName, Password, Phone
from src.api.v1.user.application.authentication.register import RegisterDto


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

        UserValidator.is_email_already_registered(self.repository, email)

        user = User(
            uuid=uuid,
            email=email,
            password=password,
            full_name=full_name,
            birth_date=dto.birth_date,
            phone=phone,
        )

        self.repository.save(user)

        return user
