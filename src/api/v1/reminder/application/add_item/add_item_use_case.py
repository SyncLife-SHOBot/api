from src.api.v1.shared.domain.value_objects import Uuid
from datetime import datetime
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.application.add_item.add_item_dto import (
    AddReminderItemDto
)
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


class AddReminderItemUseCase:
    def __init__(self, repository: ReminderRepository) -> None:
        self.repository = repository

    def execute(self, dto: AddReminderItemDto) -> Reminder:
        reminder = Reminder(
            uuid=Uuid(),
            is_deleted=False,
            title=dto.title,
            content=dto.content,
            creation_date=datetime.now(),
            remind_date=dto.remind_date,
            updated_at=None,
        )
        is_saved, reminder_saved = self.repository.save(reminder)
        if not is_saved or reminder_saved is None:
            raise ReminderValidationError(ReminderValidationTypeError.SAVE_FAILED)
        return reminder_saved
