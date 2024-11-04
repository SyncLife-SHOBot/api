from fastapi import APIRouter
from src.api.v1.user.infrastructure.controllers import FastApiUserController
from src.api.v1.user.infrastructure.models import SqlModelUserModel
from typing import Annotated

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=SqlModelUserModel)
async def register_user(
    user_data: Annotated[SqlModelUserModel, "User registration data"],
) -> SqlModelUserModel:
    return await FastApiUserController.register(user_data)
