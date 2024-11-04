from dataclasses import dataclass
from typing import Optional
from src.api.v1.shared.domain.validators import UuidValidator
import uuid


@dataclass(frozen=True)
class Uuid:
    id: Optional[str] = None

    def __post_init__(self) -> None:
        validated_id = UuidValidator.validate(self.id) if self.id else str(uuid.uuid4())
        object.__setattr__(self, "id", validated_id)

    def __repr__(self) -> str:
        return f"<Uuid({self.id})>"

    def __eq__(self, other: object) -> bool:
        return self.id == other.id if isinstance(other, Uuid) else False

    def __str__(self) -> str:
        return self.id if self.id else ""
