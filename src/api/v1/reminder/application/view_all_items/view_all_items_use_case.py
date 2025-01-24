from typing import List

from src.api.v1.reminder.application.view_all_items.view_all_items_dto import (
    ViewAllReminderItemsDto,
)
from src.api.v1.reminder.domain.entities.reminder import Reminder
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)


class ViewAllReminderItemsUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: ViewAllReminderItemsDto) -> List[Reminder]:
        reminders = self.repository.find_all_by_user_id(dto.user_id)

        return reminders
