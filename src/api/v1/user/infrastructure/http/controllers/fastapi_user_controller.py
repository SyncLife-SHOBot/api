from fastapi import HTTPException
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel
from src.api.v1.user.infrastructure.persistence.repositories import (
    SQLModelUserRepository,
)
from src.api.v1.user.infrastructure.http.dtos import PydanticRegisterDto
from src.api.v1.user.application.authentication.register import RegisterUseCase
from src.api.v1.user.domain.errors.user_error import UserError
from src.api.v1.shared.domain.errors.shared_error import SharedError
from src.api.v1.shared.infrastructure.persistence import get_session


class FastApiUserController:
    @staticmethod
    async def register(user_data: PydanticRegisterDto) -> SqlModelUserModel:
        with get_session() as session:
            user_repo = SQLModelUserRepository(session=session)
        try:
            use_case = RegisterUseCase(user_repo)

            dto = user_data.to_application()

            user = use_case.execute(dto)

            return SqlModelUserModel.from_entity(user)

        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise HTTPException(status_code=500, detail="Error interno del servidor")
