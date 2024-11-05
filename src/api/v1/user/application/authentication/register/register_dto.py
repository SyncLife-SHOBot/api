from dataclasses import dataclass
from datetime import date


@dataclass
class RegisterDto:
    email: str
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date
