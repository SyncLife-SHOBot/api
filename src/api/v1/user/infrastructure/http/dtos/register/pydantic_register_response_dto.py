from pydantic import BaseModel
from src.api.v1.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticRegisterResponseDto(BaseModel):
    user: SqlModelUserModel
    session_token: str
