from dataclasses import dataclass

from src.api.v1.shared.domain.value_objects import Uuid


@dataclass
class ViewAllTagsDto:
    user_id: Uuid
