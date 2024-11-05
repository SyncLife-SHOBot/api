from src.api.v1.user.domain.errors import FullNameError, FullNameTypeError
from typing import Tuple


class FullNameValidator:
    @staticmethod
    def validate(first_name: str, last_name: str) -> Tuple[str, str]:
        if not first_name or not last_name:
            raise FullNameError(FullNameTypeError.INVALID_NAME)
        return first_name, last_name
