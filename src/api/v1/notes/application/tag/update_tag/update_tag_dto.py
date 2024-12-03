from dataclasses import dataclass


@dataclass
class UpdateTagDto:
    tag_id: str
    name: str
