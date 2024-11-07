from fastapi import HTTPException
from src.api.v1.shared.domain.errors.shared_error import SharedError
from src.api.v1.shared.infrastructure.persistence import get_session
from src.api.v1.user.application.account_management.view_account import (
    ViewAccountUseCase,
)
from src.api.v1.user.domain.errors.user_error import UserError
from src.api.v1.user.infrastructure.http.dtos.view_account import (
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)
from src.api.v1.user.infrastructure.persistence.repositories import (
    SQLModelUserRepository,
)


class FastApiAccountManagementController:
    @staticmethod
    async def view_account(
        request_dto: PydanticViewAccountRequestDto,
    ) -> PydanticViewAccountResponseDto:
        with get_session() as session:
            repository = SQLModelUserRepository(session=session)
        try:
            use_case = ViewAccountUseCase(repository)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticViewAccountResponseDto(
                user=SqlModelUserModel.from_entity(user)
            )
        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception:
            raise HTTPException(status_code=500, detail="Error interno del servidor")
