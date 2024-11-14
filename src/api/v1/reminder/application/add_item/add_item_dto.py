from dataclasses import dataclass
from datetime import datetime


@dataclass
class AddReminderItemDto:
    title: str
    content: str
    creation_date: datetime
    remind_date: datetime
