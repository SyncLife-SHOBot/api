from datetime import date
from src.api.v1.user.domain.errors import (
    UserValidationError,
    UserValidationTypeError,
)


class UserValidator:
    @staticmethod
    def validate_minimum_age(birth_date: date, minimum_age: int = 12) -> None:
        today = date.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

        if (age < minimum_age) or (birth_date > today):
            raise UserValidationError(UserValidationTypeError.INVALID_BIRTHDATE)
