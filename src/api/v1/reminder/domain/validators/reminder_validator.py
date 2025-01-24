from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


class ReminderValidator:
    @staticmethod
    def validate_title(title: str) -> str:
        if not title:
            raise ReminderValidationError(ReminderValidationTypeError.TITLE_FAILED)
        return title

    @staticmethod
    def validate_all(title: str) -> None:
        ReminderValidator.validate_title(title)
