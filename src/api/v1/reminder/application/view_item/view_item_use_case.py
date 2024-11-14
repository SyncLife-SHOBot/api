from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.application.modify_item.modify_item_dto import (
    ModifyReminderItemDto
)
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


class ViewReminderItemUseCase:
    def __init__(self, repository: ReminderRepository) -> None:
        self.repository = repository

    def execute(self, dto: ModifyReminderItemDto) -> Reminder:
        reminder = self.repository.find_by_id(Uuid(dto.uuid))
        if reminder is None:
            raise ReminderValidationError(ReminderValidationTypeError.NOT_FOUND)
        return reminder
