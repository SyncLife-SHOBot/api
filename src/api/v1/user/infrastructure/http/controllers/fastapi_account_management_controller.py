from fastapi import HTTPException
from src.api.v1.shared.infrastructure.persistence import get_session
from src.api.v1.shared.domain.errors.shared_error import SharedError
from src.api.v1.user.domain.errors.user_error import UserError
from src.api.v1.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.v1.user.domain.value_objects import Email
from src.api.v1.user.infrastructure.http.dtos import (
    PydanticChangePasswordRequestDto,
    PydanticChangePasswordResponseDto,
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
    PydanticChangePersonalInformationRequestDto,
    PydanticChangePersonalInformationResponseDto,
)
from src.api.v1.user.infrastructure.persistence.models import (
    SqlModelUserModel,
)
from src.api.v1.user.infrastructure.persistence.repositories import (
    SQLModelUserRepository,
)
from src.api.v1.user.application import (
    ViewAccountUseCase,
    DeleteAccountUseCase,
    ChangePasswordUseCase,
    ChangePersonalInformationUseCase,
)


class FastApiAccountManagementController:
    @staticmethod
    async def view_account(
        request_dto: PydanticViewAccountRequestDto, user_request_id: str
    ) -> PydanticViewAccountResponseDto:
        with get_session() as session:
            repository = SQLModelUserRepository(session=session)
        try:
            if not user_request_id == request_dto.uuid:
                raise HTTPException(
                    status_code=403, detail="No tienes permisos para hacer esto."
                )

            use_case = ViewAccountUseCase(repository)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticViewAccountResponseDto(
                user=SqlModelUserModel.from_entity(user)
            )
        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )

    @staticmethod
    async def delete_account(
        request_dto: PydanticDeleteAccountRequestDto, user_request_id: str
    ) -> PydanticDeleteAccountResponseDto:
        with get_session() as session:
            repository = SQLModelUserRepository(session=session)
        try:
            if not user_request_id == request_dto.uuid:
                raise HTTPException(
                    status_code=403, detail="No tienes permisos para hacer esto."
                )

            use_case = DeleteAccountUseCase(repository)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticDeleteAccountResponseDto(
                user=SqlModelUserModel.from_entity(user)
            )
        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )

    @staticmethod
    async def change_password(
        request_dto: PydanticChangePasswordRequestDto, user_request_id: str
    ) -> PydanticChangePasswordResponseDto:
        with get_session() as session:
            repository = SQLModelUserRepository(session=session)
        try:
            validation_user = repository.find_by_email(Email(request_dto.email))

            if validation_user is None:
                raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)

            if not user_request_id == validation_user.uuid.id:
                raise HTTPException(
                    status_code=403, detail="No tienes permisos para hacer esto."
                )

            use_case = ChangePasswordUseCase(repository)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticChangePasswordResponseDto(
                user=SqlModelUserModel.from_entity(user)
            )
        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )

    @staticmethod
    async def change_personal_information(
        request_dto: PydanticChangePersonalInformationRequestDto, user_request_id: str
    ) -> PydanticChangePersonalInformationResponseDto:
        with get_session() as session:
            repository = SQLModelUserRepository(session=session)
        try:
            if not user_request_id == request_dto.uuid:
                raise HTTPException(
                    status_code=403, detail="No tienes permisos para hacer esto."
                )

            use_case = ChangePersonalInformationUseCase(repository)
            app_dto = request_dto.to_application()
            user = use_case.execute(app_dto)

            return PydanticChangePersonalInformationResponseDto(
                user=SqlModelUserModel.from_entity(user)
            )
        except (UserError, SharedError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error interno del servidor: {e}"
            )
