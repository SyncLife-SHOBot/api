from datetime import datetime, timezone

from src.api.v1.reminder.application.modify_item.modify_item_dto import (
    ModifyReminderItemDto,
)
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.domain.validators.reminder_repository_validator import (
    ReminderRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class ModifyReminderItemUseCase:
    def __init__(self, repository: ReminderRepository) -> None:
        self.repository = repository

    def execute(self, dto: ModifyReminderItemDto) -> Reminder:
        # Buscar el recordatorio en el repositorio usando el UUID
        reminder = ReminderRepositoryValidator.reminder_found(
            self.repository.find_by_id(Uuid(dto.reminder_id))
        )

        creation_date = datetime.now(timezone.utc)

        if dto.remind_date < creation_date:
            raise ReminderValidationError(ReminderValidationTypeError.INVALID_DATE)

        # Actualizar los campos del recordatorio
        reminder.title = dto.title
        reminder.content = dto.content
        reminder.remind_date = dto.remind_date

        # Intentar guardar los cambios en el repositorio
        is_modified, reminder_modified = self.repository.update(reminder)

        # Si la operación de modificación falla, lanzar una excepción
        if not is_modified or reminder_modified is None:
            raise ReminderValidationError(ReminderValidationTypeError.MODIFY_FAILED)

        # Retornar el recordatorio modificado
        return reminder_modified
