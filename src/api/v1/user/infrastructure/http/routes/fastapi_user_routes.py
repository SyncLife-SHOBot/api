from fastapi import APIRouter
from src.api.v1.user.infrastructure.http.controllers import (
    FastApiAuthenticationController,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)
from src.api.v1.user.infrastructure.http.dtos.login import (
    PydanticLoginRequestDto,
    PydanticLoginResponseDto,
)

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=PydanticRegisterResponseDto)
async def register_user(
    user_data: PydanticRegisterRequestDto,
) -> PydanticRegisterResponseDto:
    return await FastApiAuthenticationController.register(user_data)


@router.post("/login", response_model=PydanticLoginResponseDto)
async def login_user(user_data: PydanticLoginRequestDto) -> PydanticLoginResponseDto:
    return await FastApiAuthenticationController.login(user_data)
