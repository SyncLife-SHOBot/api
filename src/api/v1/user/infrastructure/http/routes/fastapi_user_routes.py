from fastapi import APIRouter
from src.api.v1.user.infrastructure.http.controllers import FastApiUserController
from src.api.v1.user.infrastructure.http.dtos import PydanticRegisterDto
from src.api.v1.user.infrastructure.persistence.models import SqlModelUserModel

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=SqlModelUserModel)
async def register_user(user_data: PydanticRegisterDto) -> SqlModelUserModel:
    return await FastApiUserController.register(user_data)
