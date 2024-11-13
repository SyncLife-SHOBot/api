from enum import Enum
from src.api.v1.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    INVALID_CREATION_DATE = "La fecha de creación no es válida."


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(error_type.value)
