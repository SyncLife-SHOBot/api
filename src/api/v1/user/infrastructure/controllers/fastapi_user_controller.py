from fastapi import HTTPException
from src.api.v1.user.infrastructure.models import SqlModelUserModel
from src.api.v1.user.infrastructure.repositories import SQLModelUserRepository
from src.api.v1.user.application.authentication.register import (
    RegisterUseCase,
    RegisterDto,
)
from src.api.v1.user.domain.errors import UserError
from src.api.v1.shared.domain.errors import SharedError
from src.api.v1.shared.infrastructure.persistence import get_session


class FastApiUserController:
    @staticmethod
    async def register(user_data: SqlModelUserModel) -> SqlModelUserModel:
        with get_session() as session:
            user_repo = SQLModelUserRepository(session=session)
        try:
            use_case = RegisterUseCase(user_repo)

            dto = RegisterDto(
                email=user_data.email,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                phone=user_data.phone,
                password=user_data.password,
                birth_date=user_data.birth_date,
            )

            user = use_case.execute(dto)

            return SqlModelUserModel.from_entity(user)

        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise HTTPException(status_code=500, detail="Error interno del servidor")
