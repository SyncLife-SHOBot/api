from datetime import date
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.domain.errors import UserValidationError, UserValidationTypeError


class UserValidator:
    @staticmethod
    def is_email_already_registered(repository: UserRepository, email: Email) -> None:
        """
        Verifica si ya existe un usuario con el email proporcionado
        """
        existing_user = repository.find_by_email(email)
        if existing_user is not None:
            raise UserValidationError(UserValidationTypeError.USER_ALREADY_EXISTS)

    @staticmethod
    def validate_minimum_age(birth_date: date, minimum_age: int = 18) -> None:
        """
        Valida que el usuario tenga la edad mínima requerida

        Args:
            birth_date (date): Fecha de nacimiento del usuario
            minimum_age (int, optional): Edad mínima requerida. Defaults to 18.

        Raises:
            UserError: Si el usuario no cumple con la edad mínima
        """
        today = date.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

        if age < minimum_age:
            raise UserValidationError(UserValidationTypeError.INVALID_BIRTHDATE)
