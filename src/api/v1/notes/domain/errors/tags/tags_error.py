from enum import Enum
from src.api.v1.notes.domain.errors.tags import TagError


class TagsTypeError(Enum):
    INVALID_NAME = "El nombre del tag no puede estar vacio."
    DUPLICATED_NAME = "El nombre del tag ya existe"
    NAME_MAX = "El nombre del tag debe tener menos de 200 caracteres"
    TAG_NOT_FOUND = "No se encontro este tag"
    TAG_NOT_OWNED = "Este tag no pertence al usuario"
    OPERATION_FAILED = "La operacion no pudo completarse. Intentalo nuevamente"


class TagsError(TagError):
    def __init__(self, error_type: TagsTypeError):
        super().__init__(error_type.value)
