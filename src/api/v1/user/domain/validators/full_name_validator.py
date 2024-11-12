import re
from src.api.v1.user.domain.errors import FullNameError, FullNameTypeError
from typing import Tuple


class FullNameValidator:
    @staticmethod
    def validate(first_name: str, last_name: str) -> Tuple[str, str]:
        if not first_name or not last_name:
            raise FullNameError(FullNameTypeError.INVALID_NAME)

        name_regex = r"^[a-zA-Z]+(?:[-' ][a-zA-Z]+)*$"
        if not (re.match(name_regex, first_name) and re.match(name_regex, last_name)):
            raise FullNameError(FullNameTypeError.INVALID_NAME_FORMAT)

        max_name_length = 50
        if len(first_name) > max_name_length or len(last_name) > max_name_length:
            raise FullNameError(FullNameTypeError.NAME_TOO_LONG)

        first_name = first_name.title()
        last_name = last_name.title()

        return first_name, last_name
