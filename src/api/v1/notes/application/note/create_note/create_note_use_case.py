from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories import NotesRepository
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.notes.application.note.create_note.create_note_dto import CreateNoteDto
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateNoteUseCase:
    def __init__(self, repository: NotesRepository, user_repository: UserRepository):
        self.repository = repository
        self.user_repository = user_repository

    def execute(self, dto: CreateNoteDto) -> Notes:

        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.user_repository.find_by_id(Uuid(dto.user_id))
        )

        # Valida que no haya otra nota con el mismo titulo
        NotesRepositoryValidator.note_title_unique(
            self.repository, dto.title, Uuid(dto.user_id)
        )

        # Crear y guadar notita
        note = Notes(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            title=dto.title.strip(),
            content=dto.content.strip(),
            is_deleted=False,
        )

        """
        El strip() elimina los espacios en blanco innecesarios, si al usuario
        le pinta poner " Mi     Titulo  " se corrige a "Mi Titulo" lo mismo para
        el content
        """

        self.repository.save(note)
        return note
