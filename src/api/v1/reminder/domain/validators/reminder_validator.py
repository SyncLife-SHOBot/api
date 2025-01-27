from datetime import datetime, timezone

from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


class ReminderValidator:
    @staticmethod
    def validate_title(title: str) -> str:
        if not title or not title.strip():
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_TITLE_INVALID
            )
        return title

    @staticmethod
    def validate_reminder_date(remind_date: datetime) -> None:
        # Convertir remind_date a aware si es naive
        if remind_date.tzinfo is None:
            remind_date = remind_date.replace(tzinfo=timezone.utc)

        creation_date = datetime.now(timezone.utc)

        if remind_date < creation_date:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_DATE_INVALID
            )

    @staticmethod
    def validate_all(title: str, remind_date: datetime) -> None:
        ReminderValidator.validate_title(title)
        ReminderValidator.validate_reminder_date(remind_date)
