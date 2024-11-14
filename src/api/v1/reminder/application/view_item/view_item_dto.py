from dataclasses import dataclass
from datetime import datetime


@dataclass
class ViewReminderItemDto:
    uuid: str
    title: str
    content: str
    creation_date: datetime
    remind_date: datetime

