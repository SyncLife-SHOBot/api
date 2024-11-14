from enum import Enum
from src.api.v1.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    INVALID_CREATION_DATE = "La fecha de creación no es válida."
    NOT_FOUND = "El recordatorio no fue encontrado."
    DELETE_FAILED = "No se pudo eliminar el recordatorio."
    SAVE_FAILED = "No se pudo crear el recordatorio."
    MODIFY_FAILED = "No se pudo modificar el recordatorio"


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(error_type.value)
