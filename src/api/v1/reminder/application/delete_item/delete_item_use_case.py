from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.application.delete_item.delete_item_dto import (
    DeleteReminderItemDto
)


class DeleteReminderItemUseCase:
    def __init__(self, repository: ReminderRepository) -> None:
        self.repository = repository

    def execute(self, dto: DeleteReminderItemDto) -> Reminder:
        # Buscar el recordatorio en el repositorio usando el UUID
        reminder = self.repository.find_by_id(Uuid(dto.uuid))

        # Verificar si el recordatorio existe
        if reminder is None:
            raise ReminderValidationError(ReminderValidationTypeError.NOT_FOUND)

        # Intentar eliminar el recordatorio
        is_deleted, reminder_deleted = self.repository.delete(reminder)

        # Si la eliminación falla, lanza un error
        if not is_deleted or reminder_deleted is None:
            raise ReminderValidationError(ReminderValidationTypeError.DELETE_FAILED)

        # Retornar el recordatorio eliminado
        return reminder_deleted
