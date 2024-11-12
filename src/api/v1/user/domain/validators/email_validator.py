import re
from src.api.v1.user.domain.errors import EmailError, EmailTypeError


class EmailValidator:
    @staticmethod
    def validate(email: str) -> str:
        email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"  # noqa: E501
        if re.match(email_regex, email):
            return email
        raise EmailError(EmailTypeError.INVALID_EMAIL)
