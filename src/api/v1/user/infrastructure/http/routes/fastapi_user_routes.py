from fastapi import APIRouter
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


router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=PydanticRegisterResponseDto)
async def register_user(
    dto: PydanticRegisterRequestDto,
) -> PydanticRegisterResponseDto:
    return await FastApiAuthenticationController.register(dto)


@router.post("/login", response_model=PydanticLoginResponseDto)
async def login_user(dto: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
    return await FastApiAuthenticationController.login(dto)


@router.post("/view", response_model=PydanticViewAccountResponseDto)
async def view_account_user(
    dto: PydanticViewAccountRequestDto,
) -> PydanticViewAccountResponseDto:
    return await FastApiAccountManagementController.view_account(dto)
