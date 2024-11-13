from abc import ABC, abstractmethod
from typing import List, Optional
from src.api.v1.reminder.domain.entities import Reminder


class ReminderRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Reminder]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Reminder]:
        pass

    @abstractmethod
    def save(self, reminder: Reminder) -> bool:
        pass

    @abstractmethod
    def delete(self, reminder: Reminder) -> bool:
        pass

    @abstractmethod
    def update(self, reminder: Reminder) -> bool:
        pass
