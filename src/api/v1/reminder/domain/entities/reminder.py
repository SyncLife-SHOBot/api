from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


@dataclass
class Reminder:
    uuid: Uuid
    title: str
    content: str
    creation_date: datetime
    remind_date: datetime
    updated_at: Optional[datetime]
    is_deleted: bool

    def __post_init__(self):
        '''Valida que la fecha de recordatorio no sea pasada la fecha actual'''
        if self.remind_date < self.creation_date:
            raise ReminderValidationError(
                ReminderValidationTypeError.INVALID_CREATION_DATE
            )

    def __repr__(self) -> str:
        return (
            f"<Reminder(uuid={self.uuid}, title={self.title}, "
            f"content={self.content}, creation_date={self.creation_date}, "
            f"remind_date={self.remind_date})>"
        )

    def __str__(self) -> str:
        return (
            f"Title({self.title}, "
            f"Content: {self.content}, UUID: {self.uuid}, "
            f"Creation Date: {self.creation_date}),"
            f"Remind Date: {self.remind_date}"
        )
