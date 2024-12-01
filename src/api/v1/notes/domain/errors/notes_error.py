from enum import Enum
from src.api.v1.notes.domain.errors import NoteError


class NotesTypeError(Enum):
    INVALID_TITLE = "El titulo no puede estar vacio."
    DUPLICATED_TITLE = "Ya existe una nota con ese titulo."
    TITLE_MAX = "El titulo de la nota debe tener menos de 200 caracteres."
    INVALID_CONTENT = "La nota no puede estar vacia."
    CONTENT_MAX = "El contenido de la nota debe tener menos de 2500 caracteres."
    CONTENT_MIN = "El contenido de la nota debe tener al menos una palabra."
    NOTE_NOT_FOUND = "No se encontro esta nota."
    NOTE_NOT_OWNED = "Esta nota no pertenece al usuario."
    OPERATION_FAILED = "La operacion no pudo completarse. Intentalo nuevamente."


class NotesError(NoteError):
    def __init__(self, error_type: NotesTypeError):
        super().__init__(error_type.value)
