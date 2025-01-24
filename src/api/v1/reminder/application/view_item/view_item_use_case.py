from src.api.v1.reminder.application.view_item.view_item_dto import ViewReminderItemDto
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)
from src.api.v1.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ViewReminderItemUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: ViewReminderItemDto) -> Reminder:
        # Valida que el inventario existe
        reminder_id = Uuid(dto.reminder_id)
        reminder_item = ReminderRepositoryValidator.reminder_found(
            self.repository.find_by_id(reminder_id)
        )
        return reminder_item
