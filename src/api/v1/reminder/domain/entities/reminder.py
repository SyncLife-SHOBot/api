from dataclasses import dataclass
from datetime import date
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


@dataclass(frozen=True)
class Reminder:
    uuid: Uuid
    tittle: str
    content: str
    creation_date: date
    remind_date: date

    def __post_init__(self):
        '''Valida que la fecha de recordatorio no sea pasada la fecha actual'''
        if self.remind_date < self.creation_date:
            raise ReminderValidationError(
                ReminderValidationTypeError.INVALID_CREATION_DATE
            )

    def __repr__(self) -> str:
        return (
            f"<Reminder(uuid={self.uuid}, tittle={self.tittle}, "
            f"content={self.content}, creation_date={self.creation_date}, "
            f"remind_date={self.remind_date})>"
        )

    def __str__(self) -> str:
        return (
            f"Tittle({self.tittle}, "
            f"Content: {self.content}, UUID: {self.uuid}, "
            f"Creation Date: {self.creation_date}),"
            f"Remind Date: {self.remind_date}"
        )
