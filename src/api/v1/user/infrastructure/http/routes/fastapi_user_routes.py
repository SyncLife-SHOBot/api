from fastapi import APIRouter
from src.api.v1.user.infrastructure.http.controllers import (
    FastApiAuthenticationController,
)
from src.api.v1.user.infrastructure.http.dtos.register import (
    PydanticRegisterRequestDto,
    PydanticRegisterResponseDto,
)

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=PydanticRegisterResponseDto)
async def register_user(
    user_data: PydanticRegisterRequestDto,
) -> PydanticRegisterResponseDto:
    return await FastApiAuthenticationController.register(user_data)
