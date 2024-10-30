import uuid
from typing import Optional


class Uuid:
    def __init__(self, id: Optional[str] = None) -> None:
        if id is None:
            self.__id = str(uuid.uuid4())
        else:
            self.__id = self.__validate_uuid(id)

    @property
    def id(self) -> str:
        return self.__id

    @staticmethod
    def __validate_uuid(id: str) -> str:
        try:
            return str(uuid.UUID(id))
        except ValueError:
            raise ValueError(f"{id} no es una UUID válida.")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Uuid):
            return self.id == other.id
        return False

    def __str__(self) -> str:
        return self.__id
