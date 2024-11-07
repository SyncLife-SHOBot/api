from dataclasses import dataclass
from datetime import date

@dataclass
class CreateItemDto:
    user_id: str
    product_name: str
    amount: int
    expiration_date: date