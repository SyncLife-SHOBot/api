from typing import List

from src.api.v1.reminder.application.view_all_items.view_all_items_dto import (
    ViewAllReminderItemsDto,
)
from src.api.v1.reminder.domain.entities.reminder import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories.reminder_repository import (
    ReminderRepository,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ViewAllReminderItemsUseCase:
    def __init__(self, repository: ReminderRepository):
        self.repository = repository

    def execute(self, dto: ViewAllReminderItemsDto) -> List[Reminder]:
        # Validar que el user_id es un string si es necesario
        user_id = Uuid(dto.user_id) if isinstance(dto.user_id, str) else dto.user_id

        # Buscar todos los recordatorios del usuario
        reminders = self.repository.find_all_by_user_id(user_id)

        # Lanzar error si no hay recordatorios
        if not reminders:
            raise ReminderValidationError(
                ReminderValidationTypeError.NO_REMINDERS_FOUND
            )

        # Retornar los recordatorios
        return reminders
