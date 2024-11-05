import re
from src.api.v1.user.domain.errors import EmailError, EmailTypeError


class EmailValidator:
    @staticmethod
    def validate(email: str) -> str:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(email_regex, email):
            return email
        raise EmailError(EmailTypeError.INVALID_EMAIL)
