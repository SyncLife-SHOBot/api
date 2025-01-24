from enum import Enum

from src.api.v1.reminder.domain.errors.reminder_error import ReminderError


class ReminderValidationTypeError(Enum):
    NOT_FOUND = "El recordatorio no fue encontrado."
    DELETE_FAILED = "No se pudo eliminar el recordatorio."
    SAVE_FAILED = "No se pudo crear el recordatorio."
    MODIFY_FAILED = "No se pudo modificar el recordatorio"
    TITLE_FAILED = "El nombre del recordatorio no puede ser nulo"
    NOT_OWNED = "Este recordatorio no pertenece al usuario"
    INVALID_DATE = "La fecha del recordatorio es invalida"


class ReminderValidationError(ReminderError):
    def __init__(self, error_type: ReminderValidationTypeError):
        super().__init__(error_type.value)
