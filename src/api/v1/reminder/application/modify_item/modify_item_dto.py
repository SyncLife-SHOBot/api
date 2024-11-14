from dataclasses import dataclass
from datetime import datetime


@dataclass
class ModifyReminderItemDto:
    uuid: str
    title: str
    content: str
    remind_date: datetime
