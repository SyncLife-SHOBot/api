from pydantic import BaseModel, EmailStr

from src.api.v1.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)


class PydanticChangePasswordRequestDto(BaseModel):
    email: EmailStr
    new_password: str

    def to_application(self) -> ChangePasswordDto:
        return ChangePasswordDto(email=self.email, new_password=self.new_password)

    @classmethod
    def from_application(
        cls, app_dto: ChangePasswordDto
    ) -> "PydanticChangePasswordRequestDto":
        return cls(email=app_dto.email, new_password=app_dto.new_password)
