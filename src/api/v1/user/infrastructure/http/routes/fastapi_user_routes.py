from fastapi import APIRouter, Depends
from src.api.v1.user.infrastructure.http.controllers import (
    FastApiAuthenticationController,
    FastApiAccountManagementController,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.login import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.view_account import (
    PydanticViewAccountRequestDto,
    PydanticViewAccountResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.delete_account import (
    PydanticDeleteAccountRequestDto,
    PydanticDeleteAccountResponseDto,
)
from src.api.v1.user.infrastructure.http.services import InMemorySessionService


router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=PydanticRegisterResponseDto)
async def register_user(
    dto: PydanticRegisterRequestDto,
) -> PydanticRegisterResponseDto:
    return await FastApiAuthenticationController.register(dto)


@router.post("/login", response_model=PydanticLoginResponseDto)
async def login_user(dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
    return await FastApiAuthenticationController.login(dto)


@router.get("/", response_model=PydanticViewAccountResponseDto)
async def view_account_user(
    dto: PydanticViewAccountRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticViewAccountResponseDto:
    return await FastApiAccountManagementController.view_account(dto, user_id)


@router.delete("/", response_model=PydanticDeleteAccountResponseDto)
async def delete_account_user(
    dto: PydanticDeleteAccountRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticDeleteAccountResponseDto:
    return await FastApiAccountManagementController.delete_account(dto, user_id)
