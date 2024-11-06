from fastapi import HTTPException
from src.api.v1.user.infrastructure.persistence.repositories import (
    SQLModelUserRepository,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel
from src.api.v1.user.application.authentication.register import RegisterUseCase
from src.api.v1.user.domain.errors.user_error import UserError
from src.api.v1.shared.domain.errors.shared_error import SharedError
from src.api.v1.shared.infrastructure.persistence import get_session
from src.api.v1.user.infrastructure.http.services import InMemorySessionService


class FastApiAuthenticationController:
    @staticmethod
    async def register(
        request_dto: PydanticRegisterRequestDto,
    ) -> PydanticRegisterResponseDto:
        with get_session() as session:
            user_repo = SQLModelUserRepository(session=session)
        try:
            use_case = RegisterUseCase(user_repo)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticRegisterResponseDto(
                user=SqlModelUserModel.from_entity(user),
                session_token=InMemorySessionService.create_session(str(user.uuid)),
            )

        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise HTTPException(status_code=500, detail="Error interno del servidor")

    @staticmethod
    async def get_authenticated_user(session_token: str) -> SqlModelUserModel:
        user_id = InMemorySessionService.get_user_from_session(session_token)
        if not user_id:
            raise HTTPException(status_code=401, detail="Sesión no válida")

        with get_session() as session:
            user_repo = SQLModelUserRepository(session=session)
            user = user_repo.find_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        return SqlModelUserModel.from_entity(user)
